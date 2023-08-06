# netunicorn-connector-kubernetes
This is a Kubernetes connector for netunicorn platform.  

This connector allows you to attach **existing** Kubernetes cluster
to netunicorn platform and use it as a target for deployments.  

It does not configure or modify the cluster besides optional namespace creation.
All cluster configuration should be done by infrastructure administrators.


## How to use
This connector is supposed to be installed as a part of netunicorn-director-infrastructure package or container.

Install the package:
```bash
pip install netunicorn-connector-kubernetes
```

Then, add the connector to the netunicorn-director-infrastructure configuration:
```yaml
  k8s-1:  # unique name
    enabled: true
    module: "netunicorn.director.infrastructure.connectors.k8sconnector"  # where to import from
    class: "KubernetesConnector"  # class name
    config: "configuration-example.yaml"     # path to configuration file
```

Modify the configuration file to provide needed parameters (see [example](configuration-example.yaml)), such as
configuration file location, namespace, etc.