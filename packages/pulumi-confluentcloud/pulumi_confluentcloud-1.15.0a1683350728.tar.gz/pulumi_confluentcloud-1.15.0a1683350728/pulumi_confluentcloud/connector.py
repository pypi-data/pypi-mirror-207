# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ConnectorArgs', 'Connector']

@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *,
                 config_nonsensitive: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 environment: pulumi.Input['ConnectorEnvironmentArgs'],
                 kafka_cluster: pulumi.Input['ConnectorKafkaClusterArgs'],
                 config_sensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connector resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_nonsensitive: Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input['ConnectorEnvironmentArgs'] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_sensitive: Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input[str] status: The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        pulumi.set(__self__, "config_nonsensitive", config_nonsensitive)
        pulumi.set(__self__, "environment", environment)
        pulumi.set(__self__, "kafka_cluster", kafka_cluster)
        if config_sensitive is not None:
            pulumi.set(__self__, "config_sensitive", config_sensitive)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="configNonsensitive")
    def config_nonsensitive(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        """
        return pulumi.get(self, "config_nonsensitive")

    @config_nonsensitive.setter
    def config_nonsensitive(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "config_nonsensitive", value)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Input['ConnectorEnvironmentArgs']:
        """
        Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: pulumi.Input['ConnectorEnvironmentArgs']):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> pulumi.Input['ConnectorKafkaClusterArgs']:
        return pulumi.get(self, "kafka_cluster")

    @kafka_cluster.setter
    def kafka_cluster(self, value: pulumi.Input['ConnectorKafkaClusterArgs']):
        pulumi.set(self, "kafka_cluster", value)

    @property
    @pulumi.getter(name="configSensitive")
    def config_sensitive(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        """
        return pulumi.get(self, "config_sensitive")

    @config_sensitive.setter
    def config_sensitive(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "config_sensitive", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _ConnectorState:
    def __init__(__self__, *,
                 config_nonsensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_sensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 environment: Optional[pulumi.Input['ConnectorEnvironmentArgs']] = None,
                 kafka_cluster: Optional[pulumi.Input['ConnectorKafkaClusterArgs']] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Connector resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_nonsensitive: Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_sensitive: Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input['ConnectorEnvironmentArgs'] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[str] status: The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        if config_nonsensitive is not None:
            pulumi.set(__self__, "config_nonsensitive", config_nonsensitive)
        if config_sensitive is not None:
            pulumi.set(__self__, "config_sensitive", config_sensitive)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if kafka_cluster is not None:
            pulumi.set(__self__, "kafka_cluster", kafka_cluster)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="configNonsensitive")
    def config_nonsensitive(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        """
        return pulumi.get(self, "config_nonsensitive")

    @config_nonsensitive.setter
    def config_nonsensitive(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "config_nonsensitive", value)

    @property
    @pulumi.getter(name="configSensitive")
    def config_sensitive(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        """
        return pulumi.get(self, "config_sensitive")

    @config_sensitive.setter
    def config_sensitive(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "config_sensitive", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input['ConnectorEnvironmentArgs']]:
        """
        Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input['ConnectorEnvironmentArgs']]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> Optional[pulumi.Input['ConnectorKafkaClusterArgs']]:
        return pulumi.get(self, "kafka_cluster")

    @kafka_cluster.setter
    def kafka_cluster(self, value: Optional[pulumi.Input['ConnectorKafkaClusterArgs']]):
        pulumi.set(self, "kafka_cluster", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_nonsensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_sensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['ConnectorEnvironmentArgs']]] = None,
                 kafka_cluster: Optional[pulumi.Input[pulumi.InputType['ConnectorKafkaClusterArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        You can import a connector by using Environment ID, Kafka cluster ID, and connector's name, in the format `<Environment ID>/<Kafka cluster ID>/<Connector name>`, for example$ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>" $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
         $ pulumi import confluentcloud:index/connector:Connector my_connector "env-abc123/lkc-abc123/S3_SINKConnector_0"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_nonsensitive: Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_sensitive: Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input[pulumi.InputType['ConnectorEnvironmentArgs']] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[str] status: The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        You can import a connector by using Environment ID, Kafka cluster ID, and connector's name, in the format `<Environment ID>/<Kafka cluster ID>/<Connector name>`, for example$ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>" $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
         $ pulumi import confluentcloud:index/connector:Connector my_connector "env-abc123/lkc-abc123/S3_SINKConnector_0"
        ```

        :param str resource_name: The name of the resource.
        :param ConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_nonsensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_sensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['ConnectorEnvironmentArgs']]] = None,
                 kafka_cluster: Optional[pulumi.Input[pulumi.InputType['ConnectorKafkaClusterArgs']]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorArgs.__new__(ConnectorArgs)

            if config_nonsensitive is None and not opts.urn:
                raise TypeError("Missing required property 'config_nonsensitive'")
            __props__.__dict__["config_nonsensitive"] = config_nonsensitive
            __props__.__dict__["config_sensitive"] = None if config_sensitive is None else pulumi.Output.secret(config_sensitive)
            if environment is None and not opts.urn:
                raise TypeError("Missing required property 'environment'")
            __props__.__dict__["environment"] = environment
            if kafka_cluster is None and not opts.urn:
                raise TypeError("Missing required property 'kafka_cluster'")
            __props__.__dict__["kafka_cluster"] = kafka_cluster
            __props__.__dict__["status"] = status
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["configSensitive"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Connector, __self__).__init__(
            'confluentcloud:index/connector:Connector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config_nonsensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            config_sensitive: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            environment: Optional[pulumi.Input[pulumi.InputType['ConnectorEnvironmentArgs']]] = None,
            kafka_cluster: Optional[pulumi.Input[pulumi.InputType['ConnectorKafkaClusterArgs']]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'Connector':
        """
        Get an existing Connector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_nonsensitive: Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config_sensitive: Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        :param pulumi.Input[pulumi.InputType['ConnectorEnvironmentArgs']] environment: Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        :param pulumi.Input[str] status: The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectorState.__new__(_ConnectorState)

        __props__.__dict__["config_nonsensitive"] = config_nonsensitive
        __props__.__dict__["config_sensitive"] = config_sensitive
        __props__.__dict__["environment"] = environment
        __props__.__dict__["kafka_cluster"] = kafka_cluster
        __props__.__dict__["status"] = status
        return Connector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configNonsensitive")
    def config_nonsensitive(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Block for custom *nonsensitive* configuration properties that are *not* labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        """
        return pulumi.get(self, "config_nonsensitive")

    @property
    @pulumi.getter(name="configSensitive")
    def config_sensitive(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Block for custom *sensitive* configuration properties that are labelled with "Type: password" under "Configuration Properties" section in [the docs](https://docs.confluent.io/cloud/current/connectors/index.html):
        """
        return pulumi.get(self, "config_sensitive")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output['outputs.ConnectorEnvironment']:
        """
        Environment objects represent an isolated namespace for your Confluent resources for organizational purposes.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> pulumi.Output['outputs.ConnectorKafkaCluster']:
        return pulumi.get(self, "kafka_cluster")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the connector (one of `"NONE"`, `"PROVISIONING"`, `"RUNNING"`, `"DEGRADED"`, `"FAILED"`, `"PAUSED"`, `"DELETED"`). Pausing (`"RUNNING" > "PAUSED"`) and resuming (`"PAUSED" > "RUNNING"`) a connector is supported via an update operation.
        """
        return pulumi.get(self, "status")

