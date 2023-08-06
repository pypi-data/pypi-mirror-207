# netunicorn-connector-ssh
This is an SSH connector for netunicorn platform.  

This connector allows you to specify a list of hosts and use them as a target for deployments.
Access to the hosts is done via SSH and requires **passwordless** SSH certificate to be configured and preinstalled.

## How to use
This connector is supposed to be installed as a part of netunicorn-director-infrastructure package or container.

Install the package:
```bash
pip install netunicorn-connector-ssh
```

Then, add the connector to the netunicorn-director-infrastructure configuration:
```yaml
  ssh-connector-1:  # unique name
    enabled: true
    module: "netunicorn.director.infrastructure.connectors.ssh_connector"  # where to import from
    class: "SSHConnector"  # class name
    config: "configuration-example.yaml"     # path to configuration file
```

Then, modify the configuration file to provide needed parameters (see [example](configuration-example.yaml)), such as
list of hosts, SSH certificate location, etc.