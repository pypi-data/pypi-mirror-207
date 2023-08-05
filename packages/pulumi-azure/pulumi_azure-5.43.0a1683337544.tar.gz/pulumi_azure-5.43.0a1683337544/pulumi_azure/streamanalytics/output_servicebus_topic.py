# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OutputServicebusTopicArgs', 'OutputServicebusTopic']

@pulumi.input_type
class OutputServicebusTopicArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 serialization: pulumi.Input['OutputServicebusTopicSerializationArgs'],
                 servicebus_namespace: pulumi.Input[str],
                 stream_analytics_job_name: pulumi.Input[str],
                 topic_name: pulumi.Input[str],
                 authentication_mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 shared_access_policy_key: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_name: Optional[pulumi.Input[str]] = None,
                 system_property_columns: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a OutputServicebusTopic resource.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        :param pulumi.Input['OutputServicebusTopicSerializationArgs'] serialization: A `serialization` block as defined below.
        :param pulumi.Input[str] servicebus_namespace: The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[str] topic_name: The name of the Service Bus Topic.
        :param pulumi.Input[str] authentication_mode: The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        :param pulumi.Input[str] name: The name of the Stream Output. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] property_columns: A list of property columns to add to the Service Bus Topic output.
        :param pulumi.Input[str] shared_access_policy_key: The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] shared_access_policy_name: The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] system_property_columns: A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "serialization", serialization)
        pulumi.set(__self__, "servicebus_namespace", servicebus_namespace)
        pulumi.set(__self__, "stream_analytics_job_name", stream_analytics_job_name)
        pulumi.set(__self__, "topic_name", topic_name)
        if authentication_mode is not None:
            pulumi.set(__self__, "authentication_mode", authentication_mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if property_columns is not None:
            pulumi.set(__self__, "property_columns", property_columns)
        if shared_access_policy_key is not None:
            pulumi.set(__self__, "shared_access_policy_key", shared_access_policy_key)
        if shared_access_policy_name is not None:
            pulumi.set(__self__, "shared_access_policy_name", shared_access_policy_name)
        if system_property_columns is not None:
            pulumi.set(__self__, "system_property_columns", system_property_columns)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def serialization(self) -> pulumi.Input['OutputServicebusTopicSerializationArgs']:
        """
        A `serialization` block as defined below.
        """
        return pulumi.get(self, "serialization")

    @serialization.setter
    def serialization(self, value: pulumi.Input['OutputServicebusTopicSerializationArgs']):
        pulumi.set(self, "serialization", value)

    @property
    @pulumi.getter(name="servicebusNamespace")
    def servicebus_namespace(self) -> pulumi.Input[str]:
        """
        The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        """
        return pulumi.get(self, "servicebus_namespace")

    @servicebus_namespace.setter
    def servicebus_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "servicebus_namespace", value)

    @property
    @pulumi.getter(name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> pulumi.Input[str]:
        """
        The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_name")

    @stream_analytics_job_name.setter
    def stream_analytics_job_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "stream_analytics_job_name", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[str]:
        """
        The name of the Service Bus Topic.
        """
        return pulumi.get(self, "topic_name")

    @topic_name.setter
    def topic_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic_name", value)

    @property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        """
        return pulumi.get(self, "authentication_mode")

    @authentication_mode.setter
    def authentication_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Stream Output. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of property columns to add to the Service Bus Topic output.
        """
        return pulumi.get(self, "property_columns")

    @property_columns.setter
    def property_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "property_columns", value)

    @property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[pulumi.Input[str]]:
        """
        The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        """
        return pulumi.get(self, "shared_access_policy_key")

    @shared_access_policy_key.setter
    def shared_access_policy_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_access_policy_key", value)

    @property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        """
        return pulumi.get(self, "shared_access_policy_name")

    @shared_access_policy_name.setter
    def shared_access_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_access_policy_name", value)

    @property
    @pulumi.getter(name="systemPropertyColumns")
    def system_property_columns(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        """
        return pulumi.get(self, "system_property_columns")

    @system_property_columns.setter
    def system_property_columns(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "system_property_columns", value)


@pulumi.input_type
class _OutputServicebusTopicState:
    def __init__(__self__, *,
                 authentication_mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serialization: Optional[pulumi.Input['OutputServicebusTopicSerializationArgs']] = None,
                 servicebus_namespace: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_key: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_name: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
                 system_property_columns: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OutputServicebusTopic resources.
        :param pulumi.Input[str] authentication_mode: The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        :param pulumi.Input[str] name: The name of the Stream Output. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] property_columns: A list of property columns to add to the Service Bus Topic output.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        :param pulumi.Input['OutputServicebusTopicSerializationArgs'] serialization: A `serialization` block as defined below.
        :param pulumi.Input[str] servicebus_namespace: The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        :param pulumi.Input[str] shared_access_policy_key: The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] shared_access_policy_name: The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] system_property_columns: A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        :param pulumi.Input[str] topic_name: The name of the Service Bus Topic.
        """
        if authentication_mode is not None:
            pulumi.set(__self__, "authentication_mode", authentication_mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if property_columns is not None:
            pulumi.set(__self__, "property_columns", property_columns)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if serialization is not None:
            pulumi.set(__self__, "serialization", serialization)
        if servicebus_namespace is not None:
            pulumi.set(__self__, "servicebus_namespace", servicebus_namespace)
        if shared_access_policy_key is not None:
            pulumi.set(__self__, "shared_access_policy_key", shared_access_policy_key)
        if shared_access_policy_name is not None:
            pulumi.set(__self__, "shared_access_policy_name", shared_access_policy_name)
        if stream_analytics_job_name is not None:
            pulumi.set(__self__, "stream_analytics_job_name", stream_analytics_job_name)
        if system_property_columns is not None:
            pulumi.set(__self__, "system_property_columns", system_property_columns)
        if topic_name is not None:
            pulumi.set(__self__, "topic_name", topic_name)

    @property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        """
        return pulumi.get(self, "authentication_mode")

    @authentication_mode.setter
    def authentication_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Stream Output. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of property columns to add to the Service Bus Topic output.
        """
        return pulumi.get(self, "property_columns")

    @property_columns.setter
    def property_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "property_columns", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def serialization(self) -> Optional[pulumi.Input['OutputServicebusTopicSerializationArgs']]:
        """
        A `serialization` block as defined below.
        """
        return pulumi.get(self, "serialization")

    @serialization.setter
    def serialization(self, value: Optional[pulumi.Input['OutputServicebusTopicSerializationArgs']]):
        pulumi.set(self, "serialization", value)

    @property
    @pulumi.getter(name="servicebusNamespace")
    def servicebus_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        """
        return pulumi.get(self, "servicebus_namespace")

    @servicebus_namespace.setter
    def servicebus_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "servicebus_namespace", value)

    @property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[pulumi.Input[str]]:
        """
        The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        """
        return pulumi.get(self, "shared_access_policy_key")

    @shared_access_policy_key.setter
    def shared_access_policy_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_access_policy_key", value)

    @property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        """
        return pulumi.get(self, "shared_access_policy_name")

    @shared_access_policy_name.setter
    def shared_access_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_access_policy_name", value)

    @property
    @pulumi.getter(name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_name")

    @stream_analytics_job_name.setter
    def stream_analytics_job_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stream_analytics_job_name", value)

    @property
    @pulumi.getter(name="systemPropertyColumns")
    def system_property_columns(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        """
        return pulumi.get(self, "system_property_columns")

    @system_property_columns.setter
    def system_property_columns(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "system_property_columns", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Service Bus Topic.
        """
        return pulumi.get(self, "topic_name")

    @topic_name.setter
    def topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_name", value)


class OutputServicebusTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serialization: Optional[pulumi.Input[pulumi.InputType['OutputServicebusTopicSerializationArgs']]] = None,
                 servicebus_namespace: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_key: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_name: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
                 system_property_columns: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Stream Analytics Output to a ServiceBus Topic.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_job = azure.streamanalytics.get_job_output(name="example-job",
            resource_group_name=example_resource_group.name)
        example_namespace = azure.servicebus.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard")
        example_topic = azure.servicebus.Topic("exampleTopic",
            namespace_id=example_namespace.id,
            enable_partitioning=True)
        example_output_servicebus_topic = azure.streamanalytics.OutputServicebusTopic("exampleOutputServicebusTopic",
            stream_analytics_job_name=example_job.name,
            resource_group_name=example_job.resource_group_name,
            topic_name=example_topic.name,
            servicebus_namespace=example_namespace.name,
            shared_access_policy_key=example_namespace.default_primary_key,
            shared_access_policy_name="RootManageSharedAccessKey",
            property_columns=[
                "col1",
                "col2",
            ],
            serialization=azure.streamanalytics.OutputServicebusTopicSerializationArgs(
                type="Csv",
                format="Array",
            ))
        ```

        ## Import

        Stream Analytics Output ServiceBus Topic's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:streamanalytics/outputServicebusTopic:OutputServicebusTopic example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.StreamAnalytics/streamingJobs/job1/outputs/output1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_mode: The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        :param pulumi.Input[str] name: The name of the Stream Output. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] property_columns: A list of property columns to add to the Service Bus Topic output.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['OutputServicebusTopicSerializationArgs']] serialization: A `serialization` block as defined below.
        :param pulumi.Input[str] servicebus_namespace: The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        :param pulumi.Input[str] shared_access_policy_key: The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] shared_access_policy_name: The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] system_property_columns: A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        :param pulumi.Input[str] topic_name: The name of the Service Bus Topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OutputServicebusTopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Stream Analytics Output to a ServiceBus Topic.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_job = azure.streamanalytics.get_job_output(name="example-job",
            resource_group_name=example_resource_group.name)
        example_namespace = azure.servicebus.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard")
        example_topic = azure.servicebus.Topic("exampleTopic",
            namespace_id=example_namespace.id,
            enable_partitioning=True)
        example_output_servicebus_topic = azure.streamanalytics.OutputServicebusTopic("exampleOutputServicebusTopic",
            stream_analytics_job_name=example_job.name,
            resource_group_name=example_job.resource_group_name,
            topic_name=example_topic.name,
            servicebus_namespace=example_namespace.name,
            shared_access_policy_key=example_namespace.default_primary_key,
            shared_access_policy_name="RootManageSharedAccessKey",
            property_columns=[
                "col1",
                "col2",
            ],
            serialization=azure.streamanalytics.OutputServicebusTopicSerializationArgs(
                type="Csv",
                format="Array",
            ))
        ```

        ## Import

        Stream Analytics Output ServiceBus Topic's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:streamanalytics/outputServicebusTopic:OutputServicebusTopic example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.StreamAnalytics/streamingJobs/job1/outputs/output1
        ```

        :param str resource_name: The name of the resource.
        :param OutputServicebusTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OutputServicebusTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serialization: Optional[pulumi.Input[pulumi.InputType['OutputServicebusTopicSerializationArgs']]] = None,
                 servicebus_namespace: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_key: Optional[pulumi.Input[str]] = None,
                 shared_access_policy_name: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
                 system_property_columns: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OutputServicebusTopicArgs.__new__(OutputServicebusTopicArgs)

            __props__.__dict__["authentication_mode"] = authentication_mode
            __props__.__dict__["name"] = name
            __props__.__dict__["property_columns"] = property_columns
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if serialization is None and not opts.urn:
                raise TypeError("Missing required property 'serialization'")
            __props__.__dict__["serialization"] = serialization
            if servicebus_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'servicebus_namespace'")
            __props__.__dict__["servicebus_namespace"] = servicebus_namespace
            __props__.__dict__["shared_access_policy_key"] = None if shared_access_policy_key is None else pulumi.Output.secret(shared_access_policy_key)
            __props__.__dict__["shared_access_policy_name"] = shared_access_policy_name
            if stream_analytics_job_name is None and not opts.urn:
                raise TypeError("Missing required property 'stream_analytics_job_name'")
            __props__.__dict__["stream_analytics_job_name"] = stream_analytics_job_name
            __props__.__dict__["system_property_columns"] = system_property_columns
            if topic_name is None and not opts.urn:
                raise TypeError("Missing required property 'topic_name'")
            __props__.__dict__["topic_name"] = topic_name
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["sharedAccessPolicyKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(OutputServicebusTopic, __self__).__init__(
            'azure:streamanalytics/outputServicebusTopic:OutputServicebusTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication_mode: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            property_columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            serialization: Optional[pulumi.Input[pulumi.InputType['OutputServicebusTopicSerializationArgs']]] = None,
            servicebus_namespace: Optional[pulumi.Input[str]] = None,
            shared_access_policy_key: Optional[pulumi.Input[str]] = None,
            shared_access_policy_name: Optional[pulumi.Input[str]] = None,
            stream_analytics_job_name: Optional[pulumi.Input[str]] = None,
            system_property_columns: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            topic_name: Optional[pulumi.Input[str]] = None) -> 'OutputServicebusTopic':
        """
        Get an existing OutputServicebusTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_mode: The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        :param pulumi.Input[str] name: The name of the Stream Output. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] property_columns: A list of property columns to add to the Service Bus Topic output.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['OutputServicebusTopicSerializationArgs']] serialization: A `serialization` block as defined below.
        :param pulumi.Input[str] servicebus_namespace: The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        :param pulumi.Input[str] shared_access_policy_key: The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] shared_access_policy_name: The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        :param pulumi.Input[str] stream_analytics_job_name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] system_property_columns: A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        :param pulumi.Input[str] topic_name: The name of the Service Bus Topic.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OutputServicebusTopicState.__new__(_OutputServicebusTopicState)

        __props__.__dict__["authentication_mode"] = authentication_mode
        __props__.__dict__["name"] = name
        __props__.__dict__["property_columns"] = property_columns
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["serialization"] = serialization
        __props__.__dict__["servicebus_namespace"] = servicebus_namespace
        __props__.__dict__["shared_access_policy_key"] = shared_access_policy_key
        __props__.__dict__["shared_access_policy_name"] = shared_access_policy_name
        __props__.__dict__["stream_analytics_job_name"] = stream_analytics_job_name
        __props__.__dict__["system_property_columns"] = system_property_columns
        __props__.__dict__["topic_name"] = topic_name
        return OutputServicebusTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The authentication mode for the Stream Output. Possible values are `Msi` and `ConnectionString`. Defaults to `ConnectionString`.
        """
        return pulumi.get(self, "authentication_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Stream Output. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of property columns to add to the Service Bus Topic output.
        """
        return pulumi.get(self, "property_columns")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def serialization(self) -> pulumi.Output['outputs.OutputServicebusTopicSerialization']:
        """
        A `serialization` block as defined below.
        """
        return pulumi.get(self, "serialization")

    @property
    @pulumi.getter(name="servicebusNamespace")
    def servicebus_namespace(self) -> pulumi.Output[str]:
        """
        The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.
        """
        return pulumi.get(self, "servicebus_namespace")

    @property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> pulumi.Output[Optional[str]]:
        """
        The shared access policy key for the specified shared access policy. Required if `authentication_mode` is `ConnectionString`.
        """
        return pulumi.get(self, "shared_access_policy_key")

    @property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required if `authentication_mode` is `ConnectionString`.
        """
        return pulumi.get(self, "shared_access_policy_name")

    @property
    @pulumi.getter(name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> pulumi.Output[str]:
        """
        The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_name")

    @property
    @pulumi.getter(name="systemPropertyColumns")
    def system_property_columns(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A key-value pair of system property columns that will be attached to the outgoing messages for the Service Bus Topic Output.
        """
        return pulumi.get(self, "system_property_columns")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Output[str]:
        """
        The name of the Service Bus Topic.
        """
        return pulumi.get(self, "topic_name")

