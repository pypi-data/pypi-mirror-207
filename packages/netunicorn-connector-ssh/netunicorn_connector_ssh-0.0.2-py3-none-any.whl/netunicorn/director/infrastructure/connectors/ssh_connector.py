from __future__ import annotations

import asyncio
import asyncssh
import logging
from logging import Logger
from typing import Optional, Tuple, Any

import yaml
from netunicorn.base.architecture import Architecture
from netunicorn.base.deployment import Deployment
from netunicorn.base.environment_definitions import DockerImage, ShellExecution
from netunicorn.base.nodes import CountableNodePool, Node, Nodes
from returns.result import Failure, Result, Success

from netunicorn.director.base.connectors.protocol import (
    NetunicornConnectorProtocol,
)
from netunicorn.director.base.connectors.types import StopExecutorRequest


class SSHConnector(NetunicornConnectorProtocol):
    """
    During the development, you can read the documentation for each method
    from the Protocol class itself.
    """

    def __init__(
            self,
            connector_name: str,
            configuration: str | None,
            netunicorn_gateway: str,
            logger: Optional[Logger] = None,
    ):
        self.connector_name = connector_name
        self.configuration = configuration
        with open(self.configuration) as f:
            self.configuration = yaml.safe_load(f)

        self.netunicorn_gateway = netunicorn_gateway
        self.logger = logger or logging.getLogger(__name__)

        self.private_key = self.configuration.get('netunicorn.ssh.private_key_location', '~/.ssh/id_rsa')
        self.logger.info(f"Using private key located at {self.private_key}")
        self._parse_hosts()
        self.logger.info(f"Started SSH connector {self.connector_name}")

    def _parse_hosts(self):
        self.hosts = self.configuration.get('netunicorn.ssh.hosts', {})

        pool = []
        for hostname, host_info in self.hosts.items():
            if 'address' not in host_info:
                raise ValueError(f"Missing address for host {hostname}")
            if 'username' not in host_info:
                raise ValueError(f"Missing username for host {hostname}")
            if 'port' not in host_info:
                host_info['port'] = 22

            os = host_info.get('properties', {}).get('os', 'linux')
            arch = host_info.get('properties', {}).get('architecture', 'amd64')
            host_arch = Architecture.UNKNOWN
            if os == 'linux':
                match arch:
                    case 'amd64':
                        host_arch = Architecture.LINUX_AMD64
                    case 'arm64':
                        host_arch = Architecture.LINUX_ARM64

            pool.append(
                Node(
                    name=hostname,
                    properties=host_info.get('properties', {}),
                    architecture=host_arch,
                )
            )
        self.public_host_pool = CountableNodePool(pool)

    async def initialize(self, *args: Any, **kwargs: Any) -> None:
        pass

    async def health(self, *args: Any, **kwargs: Any) -> Tuple[bool, str]:
        return True, ""

    async def shutdown(self, *args: Any, **kwargs: Any) -> None:
        pass

    async def get_nodes(
            self,
            username: str,
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> Nodes:
        return self.public_host_pool

    async def _deploy_single(self, experiment_id: str, deployment: Deployment) -> Result[Optional[str], str]:
        if not deployment.prepared:
            message = f"Skipping deployment {deployment.executor_id} because it is not prepared"
            self.logger.debug(message)
            return Failure(message)

        if deployment.node.name not in self.hosts:
            message = f"Unknown node {deployment.node.name} for deployment {deployment.executor_id}"
            self.logger.warning(message)
            return Failure(message)

        if isinstance(deployment.environment_definition, DockerImage):
            self.logger.debug(
                f"Pulling image {deployment.environment_definition.image} on node {deployment.node.name}"
            )
            try:
                host = self.hosts[deployment.node.name]
                async with asyncssh.connect(
                        host=host['address'],
                        port=host['port'],
                        username=host['username'],
                        client_keys=[self.private_key],
                        known_hosts=None,
                ) as conn:
                    await conn.run(f'docker pull {deployment.environment_definition.image}', check=True)
                    return Success(
                        f"Successfully pulled image {deployment.environment_definition.image} "
                        f"on node {deployment.node.name}"
                    )
            except Exception as e:
                self.logger.exception(e)
                return Failure(
                    f"Failed to pull image {deployment.environment_definition.image} on"
                    f" node {deployment.node.name}: {e}\n"
                    f"{e.stderr}" if hasattr(e, 'stderr') else ""
                )
        elif isinstance(deployment.environment_definition, ShellExecution):
            try:
                host = self.hosts[deployment.node.name]
                async with asyncssh.connect(
                        host=host['address'],
                        port=host['port'],
                        username=host['username'],
                        client_keys=[self.private_key],
                        known_hosts=None,
                ) as conn:
                    for command in deployment.environment_definition.commands:
                        self.logger.debug(
                            f"Executing deployment command {command} on node {deployment.node.name}"
                        )
                        await conn.run(command, check=True)
                    return Success(
                        f"Successfully executed deployment commands on node {deployment.node.name}"
                    )
            except Exception as e:
                self.logger.exception(e)
                return Failure(
                    f"Failed to execute deployment commands on node {deployment.node.name}: {e}\n"
                    f"{e.stderr}" if hasattr(e, 'stderr') else ""
                )
        else:
            return Failure(f"Unknown environment definition: {deployment.environment_definition}")

    async def deploy(
            self,
            username: str,
            experiment_id: str,
            deployments: list[Deployment],
            deployment_context: Optional[dict[str, str]],
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> dict[str, Result[Optional[str], str]]:
        return {
            deployment.executor_id: await self._deploy_single(experiment_id, deployment)
            for deployment in deployments
        }

    @staticmethod
    def __shell_runcommand(deployment: Deployment) -> str:
        env_vars = " ".join(
            f" {k}={v}"
            for k, v in deployment.environment_definition.runtime_context.environment_variables.items()
        )
        runcommand = f"{env_vars} python3 -m netunicorn.executor"
        return runcommand

    @staticmethod
    def __docker_runcommand(deployment: Deployment) -> str:
        env_vars = " ".join(
            f"-e {k}={v}"
            for k, v in deployment.environment_definition.runtime_context.environment_variables.items()
        )

        additional_arguments = " ".join(
            deployment.environment_definition.runtime_context.additional_arguments
        )

        ports = ""
        if deployment.environment_definition.runtime_context.ports_mapping:
            ports = " ".join(
                f"-p {k}:{v}"
                for k, v in deployment.environment_definition.runtime_context.ports_mapping.items()
            )

        runcommand = (
            f"docker run -d {env_vars} {ports} --name {deployment.executor_id} "
            f"{additional_arguments} {deployment.environment_definition.image}"
        )
        return runcommand

    async def _execute_single(self, experiment_id: str, deployment: Deployment) -> tuple[
        str, Result[Optional[str], str]]:
        if not deployment.prepared:
            return (deployment.executor_id, Failure(
                f"Skipping execution {deployment.executor_id} because it is not prepared"
            ))

        if deployment.node.name not in self.hosts:
            return (deployment.executor_id, Failure(
                f"Unknown node {deployment.node.name} for execution {deployment.executor_id}"
            ))

        deployment.environment_definition.runtime_context.environment_variables.update({
            "NETUNICORN_EXPERIMENT_ID": experiment_id,
            "NETUNICORN_EXECUTOR_ID": deployment.executor_id,
            "NETUNICORN_GATEWAY_ENDPOINT": self.netunicorn_gateway
        })

        if isinstance(deployment.environment_definition, DockerImage):
            runcommand = self.__docker_runcommand(deployment)
        elif isinstance(deployment.environment_definition, ShellExecution):
            runcommand = self.__shell_runcommand(deployment)
        else:
            return (
                deployment.executor_id,
                Failure(f"Unknown environment definition: {deployment.environment_definition}")
            )

        try:
            host = self.hosts[deployment.node.name]
            async with asyncssh.connect(
                    host=host['address'],
                    port=host['port'],
                    username=host['username'],
                    client_keys=[self.private_key],
                    known_hosts=None,
            ) as conn:
                self.logger.debug(
                    f"Starting {deployment.executor_id} on node {deployment.node.name} "
                    f"with command:\n{runcommand}"
                )
                await conn.run(runcommand, check=True)
                return (
                    deployment.executor_id,
                    Success(
                        f"Successfully started {deployment.executor_id} "
                        f"on node {deployment.node.name}"
                    )
                )
        except Exception as e:
            self.logger.exception(e)
            return (
                deployment.executor_id,
                Failure(
                    f"Failure during starting {deployment.executor_id} on"
                    f" node {deployment.node.name}: {e}"
                )
            )

    async def execute(
            self,
            username: str,
            experiment_id: str,
            deployments: list[Deployment],
            execution_context: Optional[dict[str, str]],
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> dict[str, Result[Optional[str], str]]:

        result = {}
        ids_results: list[tuple[str, Result]] = await asyncio.gather(*[
            self._execute_single(experiment_id, deployment)
            for deployment in deployments
        ])
        result.update({executor_id: res for executor_id, res in ids_results})
        return result

    async def _stop_single_executor(
            self,
            request: StopExecutorRequest
    ) -> Result[None, str]:
        if request['node_name'] not in self.hosts:
            return Failure(f"Unknown node {request['node_name']} for executor {request['executor_id']}")

        try:
            host = self.hosts[request['node_name']]
            async with asyncssh.connect(
                    host=host['address'],
                    port=host['port'],
                    username=host['username'],
                    client_keys=[self.private_key],
                    known_hosts=None,
            ) as conn:

                self.logger.debug(
                    f"Stopping {request['executor_id']} on node {request['node_name']}"
                )
                await conn.run(f"docker rm -f {request['executor_id']}", check=True)
                return Success(
                    f"Successfully stopped {request['executor_id']} "
                    f"on node {request['node_name']}"
                )
        except Exception as e:
            self.logger.exception(e)
            return Failure(
                f"Failure during stopping {request['executor_id']} on"
                f" node {request['node_name']}: {e}"
            )

    async def stop_executors(
            self,
            username: str,
            requests_list: list[StopExecutorRequest],
            cancellation_context: Optional[dict[str, str]],
            authentication_context: Optional[dict[str, str]] = None,
            *args: Any,
            **kwargs: Any,
    ) -> dict[str, Result[Optional[str], str]]:
        return {
            request['executor_id']: await self._stop_single_executor(request)
            for request in requests_list
        }

    async def cleanup(
            self,
            experiment_id: str,
            deployments: list[Deployment],
            *args: Any,
            **kwargs: Any,
    ) -> None:
        # cleanup infrastructure after experiment is finished
        # example for docker infrastructure
        for deployment in deployments:
            if deployment.node.name not in self.hosts:
                continue
            if isinstance(deployment.environment_definition, DockerImage):
                try:
                    host = self.hosts[deployment.node.name]
                    async with asyncssh.connect(
                            host=host['address'],
                            port=host['port'],
                            username=host['username'],
                            client_keys=[self.private_key],
                            known_hosts=None,
                    ) as conn:
                        self.logger.debug(
                            f"Removing container {deployment.executor_id} and "
                            f"image {deployment.environment_definition.image} "
                            f"from node {deployment.node.name}"
                        )
                        await conn.run(f"docker rm {deployment.executor_id}", check=False)
                        await conn.run(f"docker rmi {deployment.environment_definition.image}", check=False)
                except Exception as e:
                    self.logger.exception(e)
                    self.logger.error(
                        f"Failure during cleanup of {deployment.executor_id} on"
                        f" node {deployment.node.name}: {e}"
                    )


async def test():
    from uuid import uuid4
    import cloudpickle  # you'll need it for tests
    from netunicorn.base import Pipeline

    connector = SSHConnector(
        connector_name="ssh-test-connector",
        configuration="configuration-example.yaml",
        netunicorn_gateway="http://localhost:8000",
    )
    await connector.initialize()
    print(await connector.health())
    nodes = await connector.get_nodes("test")
    print(nodes)

    # create dummy pipeline
    pipeline = Pipeline()
    pipeline.environment_definition.image = "ubuntu:latest"
    pipeline.environment_definition.runtime_context.ports_mapping = {30001: 80}
    deployment = Deployment(node=nodes.take(1)[0], pipeline=pipeline)
    deployment.prepared = True
    deployment.executor_id = str(uuid4())
    deployment_result = await connector.deploy(
        username="test",
        experiment_id="test",
        deployments=[deployment],
        deployment_context={},
    )
    print(deployment_result)
    execution_result = await connector.execute(
        username="test",
        experiment_id="test",
        deployments=[deployment],
        execution_context={},
    )
    print(execution_result)

    await connector.cleanup(
        experiment_id="test",
        deployments=[deployment],
    )


if __name__ == '__main__':
    asyncio.run(test())
