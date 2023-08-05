# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TimeSeriesDatabaseConnectionArgs', 'TimeSeriesDatabaseConnection']

@pulumi.input_type
class TimeSeriesDatabaseConnectionArgs:
    def __init__(__self__, *,
                 digital_twins_id: pulumi.Input[str],
                 eventhub_name: pulumi.Input[str],
                 eventhub_namespace_endpoint_uri: pulumi.Input[str],
                 eventhub_namespace_id: pulumi.Input[str],
                 kusto_cluster_id: pulumi.Input[str],
                 kusto_cluster_uri: pulumi.Input[str],
                 kusto_database_name: pulumi.Input[str],
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 kusto_table_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TimeSeriesDatabaseConnection resource.
        :param pulumi.Input[str] digital_twins_id: The ID of the Digital Twins. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_name: Name of the Event Hub. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_endpoint_uri: URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_id: The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_id: The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_uri: URI of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_database_name: Name of the Kusto Database. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_consumer_group_name: Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        :param pulumi.Input[str] kusto_table_name: Name of the Kusto Table. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "digital_twins_id", digital_twins_id)
        pulumi.set(__self__, "eventhub_name", eventhub_name)
        pulumi.set(__self__, "eventhub_namespace_endpoint_uri", eventhub_namespace_endpoint_uri)
        pulumi.set(__self__, "eventhub_namespace_id", eventhub_namespace_id)
        pulumi.set(__self__, "kusto_cluster_id", kusto_cluster_id)
        pulumi.set(__self__, "kusto_cluster_uri", kusto_cluster_uri)
        pulumi.set(__self__, "kusto_database_name", kusto_database_name)
        if eventhub_consumer_group_name is not None:
            pulumi.set(__self__, "eventhub_consumer_group_name", eventhub_consumer_group_name)
        if kusto_table_name is not None:
            pulumi.set(__self__, "kusto_table_name", kusto_table_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="digitalTwinsId")
    def digital_twins_id(self) -> pulumi.Input[str]:
        """
        The ID of the Digital Twins. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "digital_twins_id")

    @digital_twins_id.setter
    def digital_twins_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "digital_twins_id", value)

    @property
    @pulumi.getter(name="eventhubName")
    def eventhub_name(self) -> pulumi.Input[str]:
        """
        Name of the Event Hub. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_name")

    @eventhub_name.setter
    def eventhub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "eventhub_name", value)

    @property
    @pulumi.getter(name="eventhubNamespaceEndpointUri")
    def eventhub_namespace_endpoint_uri(self) -> pulumi.Input[str]:
        """
        URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_namespace_endpoint_uri")

    @eventhub_namespace_endpoint_uri.setter
    def eventhub_namespace_endpoint_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "eventhub_namespace_endpoint_uri", value)

    @property
    @pulumi.getter(name="eventhubNamespaceId")
    def eventhub_namespace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_namespace_id")

    @eventhub_namespace_id.setter
    def eventhub_namespace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "eventhub_namespace_id", value)

    @property
    @pulumi.getter(name="kustoClusterId")
    def kusto_cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_cluster_id")

    @kusto_cluster_id.setter
    def kusto_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_cluster_id", value)

    @property
    @pulumi.getter(name="kustoClusterUri")
    def kusto_cluster_uri(self) -> pulumi.Input[str]:
        """
        URI of the Kusto Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_cluster_uri")

    @kusto_cluster_uri.setter
    def kusto_cluster_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_cluster_uri", value)

    @property
    @pulumi.getter(name="kustoDatabaseName")
    def kusto_database_name(self) -> pulumi.Input[str]:
        """
        Name of the Kusto Database. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_database_name")

    @kusto_database_name.setter
    def kusto_database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_database_name", value)

    @property
    @pulumi.getter(name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        """
        return pulumi.get(self, "eventhub_consumer_group_name")

    @eventhub_consumer_group_name.setter
    def eventhub_consumer_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_consumer_group_name", value)

    @property
    @pulumi.getter(name="kustoTableName")
    def kusto_table_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Kusto Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_table_name")

    @kusto_table_name.setter
    def kusto_table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_table_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TimeSeriesDatabaseConnectionState:
    def __init__(__self__, *,
                 digital_twins_id: Optional[pulumi.Input[str]] = None,
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 eventhub_name: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_endpoint_uri: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_uri: Optional[pulumi.Input[str]] = None,
                 kusto_database_name: Optional[pulumi.Input[str]] = None,
                 kusto_table_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TimeSeriesDatabaseConnection resources.
        :param pulumi.Input[str] digital_twins_id: The ID of the Digital Twins. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_consumer_group_name: Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        :param pulumi.Input[str] eventhub_name: Name of the Event Hub. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_endpoint_uri: URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_id: The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_id: The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_uri: URI of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_database_name: Name of the Kusto Database. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_table_name: Name of the Kusto Table. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        if digital_twins_id is not None:
            pulumi.set(__self__, "digital_twins_id", digital_twins_id)
        if eventhub_consumer_group_name is not None:
            pulumi.set(__self__, "eventhub_consumer_group_name", eventhub_consumer_group_name)
        if eventhub_name is not None:
            pulumi.set(__self__, "eventhub_name", eventhub_name)
        if eventhub_namespace_endpoint_uri is not None:
            pulumi.set(__self__, "eventhub_namespace_endpoint_uri", eventhub_namespace_endpoint_uri)
        if eventhub_namespace_id is not None:
            pulumi.set(__self__, "eventhub_namespace_id", eventhub_namespace_id)
        if kusto_cluster_id is not None:
            pulumi.set(__self__, "kusto_cluster_id", kusto_cluster_id)
        if kusto_cluster_uri is not None:
            pulumi.set(__self__, "kusto_cluster_uri", kusto_cluster_uri)
        if kusto_database_name is not None:
            pulumi.set(__self__, "kusto_database_name", kusto_database_name)
        if kusto_table_name is not None:
            pulumi.set(__self__, "kusto_table_name", kusto_table_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="digitalTwinsId")
    def digital_twins_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Digital Twins. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "digital_twins_id")

    @digital_twins_id.setter
    def digital_twins_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "digital_twins_id", value)

    @property
    @pulumi.getter(name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        """
        return pulumi.get(self, "eventhub_consumer_group_name")

    @eventhub_consumer_group_name.setter
    def eventhub_consumer_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_consumer_group_name", value)

    @property
    @pulumi.getter(name="eventhubName")
    def eventhub_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Event Hub. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_name")

    @eventhub_name.setter
    def eventhub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_name", value)

    @property
    @pulumi.getter(name="eventhubNamespaceEndpointUri")
    def eventhub_namespace_endpoint_uri(self) -> Optional[pulumi.Input[str]]:
        """
        URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_namespace_endpoint_uri")

    @eventhub_namespace_endpoint_uri.setter
    def eventhub_namespace_endpoint_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_namespace_endpoint_uri", value)

    @property
    @pulumi.getter(name="eventhubNamespaceId")
    def eventhub_namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_namespace_id")

    @eventhub_namespace_id.setter
    def eventhub_namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventhub_namespace_id", value)

    @property
    @pulumi.getter(name="kustoClusterId")
    def kusto_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_cluster_id")

    @kusto_cluster_id.setter
    def kusto_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_cluster_id", value)

    @property
    @pulumi.getter(name="kustoClusterUri")
    def kusto_cluster_uri(self) -> Optional[pulumi.Input[str]]:
        """
        URI of the Kusto Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_cluster_uri")

    @kusto_cluster_uri.setter
    def kusto_cluster_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_cluster_uri", value)

    @property
    @pulumi.getter(name="kustoDatabaseName")
    def kusto_database_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Kusto Database. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_database_name")

    @kusto_database_name.setter
    def kusto_database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_database_name", value)

    @property
    @pulumi.getter(name="kustoTableName")
    def kusto_table_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Kusto Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_table_name")

    @kusto_table_name.setter
    def kusto_table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_table_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class TimeSeriesDatabaseConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 digital_twins_id: Optional[pulumi.Input[str]] = None,
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 eventhub_name: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_endpoint_uri: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_uri: Optional[pulumi.Input[str]] = None,
                 kusto_database_name: Optional[pulumi.Input[str]] = None,
                 kusto_table_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Digital Twins Time Series Database Connection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_instance = azure.digitaltwins.Instance("exampleInstance",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            identity=azure.digitaltwins.InstanceIdentityArgs(
                type="SystemAssigned",
            ))
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard")
        example_event_hub = azure.eventhub.EventHub("exampleEventHub",
            namespace_name=example_event_hub_namespace.name,
            resource_group_name=example_resource_group.name,
            partition_count=2,
            message_retention=7)
        example_consumer_group = azure.eventhub.ConsumerGroup("exampleConsumerGroup",
            namespace_name=example_event_hub_namespace.name,
            eventhub_name=example_event_hub.name,
            resource_group_name=example_resource_group.name)
        example_cluster = azure.kusto.Cluster("exampleCluster",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Dev(No SLA)_Standard_D11_v2",
                capacity=1,
            ))
        example_database = azure.kusto.Database("exampleDatabase",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            cluster_name=example_cluster.name)
        database_contributor = azure.authorization.Assignment("databaseContributor",
            scope=example_database.id,
            principal_id=example_instance.identity.principal_id,
            role_definition_name="Contributor")
        eventhub_data_owner = azure.authorization.Assignment("eventhubDataOwner",
            scope=example_event_hub.id,
            principal_id=example_instance.identity.principal_id,
            role_definition_name="Azure Event Hubs Data Owner")
        example_database_principal_assignment = azure.kusto.DatabasePrincipalAssignment("exampleDatabasePrincipalAssignment",
            resource_group_name=example_resource_group.name,
            cluster_name=example_cluster.name,
            database_name=example_database.name,
            tenant_id=example_instance.identity.tenant_id,
            principal_id=example_instance.identity.principal_id,
            principal_type="App",
            role="Admin")
        example_time_series_database_connection = azure.digitaltwins.TimeSeriesDatabaseConnection("exampleTimeSeriesDatabaseConnection",
            digital_twins_id=example_instance.id,
            eventhub_name=example_event_hub.name,
            eventhub_namespace_id=example_event_hub_namespace.id,
            eventhub_namespace_endpoint_uri=example_event_hub_namespace.name.apply(lambda name: f"sb://{name}.servicebus.windows.net"),
            eventhub_consumer_group_name=example_consumer_group.name,
            kusto_cluster_id=example_cluster.id,
            kusto_cluster_uri=example_cluster.uri,
            kusto_database_name=example_database.name,
            kusto_table_name="exampleTable",
            opts=pulumi.ResourceOptions(depends_on=[
                    database_contributor,
                    eventhub_data_owner,
                    example_database_principal_assignment,
                ]))
        ```

        ## Import

        Digital Twins Time Series Database Connections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:digitaltwins/timeSeriesDatabaseConnection:TimeSeriesDatabaseConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DigitalTwins/digitalTwinsInstances/dt1/timeSeriesDatabaseConnections/connection1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] digital_twins_id: The ID of the Digital Twins. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_consumer_group_name: Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        :param pulumi.Input[str] eventhub_name: Name of the Event Hub. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_endpoint_uri: URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_id: The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_id: The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_uri: URI of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_database_name: Name of the Kusto Database. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_table_name: Name of the Kusto Table. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TimeSeriesDatabaseConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Digital Twins Time Series Database Connection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_instance = azure.digitaltwins.Instance("exampleInstance",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            identity=azure.digitaltwins.InstanceIdentityArgs(
                type="SystemAssigned",
            ))
        example_event_hub_namespace = azure.eventhub.EventHubNamespace("exampleEventHubNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard")
        example_event_hub = azure.eventhub.EventHub("exampleEventHub",
            namespace_name=example_event_hub_namespace.name,
            resource_group_name=example_resource_group.name,
            partition_count=2,
            message_retention=7)
        example_consumer_group = azure.eventhub.ConsumerGroup("exampleConsumerGroup",
            namespace_name=example_event_hub_namespace.name,
            eventhub_name=example_event_hub.name,
            resource_group_name=example_resource_group.name)
        example_cluster = azure.kusto.Cluster("exampleCluster",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Dev(No SLA)_Standard_D11_v2",
                capacity=1,
            ))
        example_database = azure.kusto.Database("exampleDatabase",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            cluster_name=example_cluster.name)
        database_contributor = azure.authorization.Assignment("databaseContributor",
            scope=example_database.id,
            principal_id=example_instance.identity.principal_id,
            role_definition_name="Contributor")
        eventhub_data_owner = azure.authorization.Assignment("eventhubDataOwner",
            scope=example_event_hub.id,
            principal_id=example_instance.identity.principal_id,
            role_definition_name="Azure Event Hubs Data Owner")
        example_database_principal_assignment = azure.kusto.DatabasePrincipalAssignment("exampleDatabasePrincipalAssignment",
            resource_group_name=example_resource_group.name,
            cluster_name=example_cluster.name,
            database_name=example_database.name,
            tenant_id=example_instance.identity.tenant_id,
            principal_id=example_instance.identity.principal_id,
            principal_type="App",
            role="Admin")
        example_time_series_database_connection = azure.digitaltwins.TimeSeriesDatabaseConnection("exampleTimeSeriesDatabaseConnection",
            digital_twins_id=example_instance.id,
            eventhub_name=example_event_hub.name,
            eventhub_namespace_id=example_event_hub_namespace.id,
            eventhub_namespace_endpoint_uri=example_event_hub_namespace.name.apply(lambda name: f"sb://{name}.servicebus.windows.net"),
            eventhub_consumer_group_name=example_consumer_group.name,
            kusto_cluster_id=example_cluster.id,
            kusto_cluster_uri=example_cluster.uri,
            kusto_database_name=example_database.name,
            kusto_table_name="exampleTable",
            opts=pulumi.ResourceOptions(depends_on=[
                    database_contributor,
                    eventhub_data_owner,
                    example_database_principal_assignment,
                ]))
        ```

        ## Import

        Digital Twins Time Series Database Connections can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:digitaltwins/timeSeriesDatabaseConnection:TimeSeriesDatabaseConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DigitalTwins/digitalTwinsInstances/dt1/timeSeriesDatabaseConnections/connection1
        ```

        :param str resource_name: The name of the resource.
        :param TimeSeriesDatabaseConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TimeSeriesDatabaseConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 digital_twins_id: Optional[pulumi.Input[str]] = None,
                 eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
                 eventhub_name: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_endpoint_uri: Optional[pulumi.Input[str]] = None,
                 eventhub_namespace_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_uri: Optional[pulumi.Input[str]] = None,
                 kusto_database_name: Optional[pulumi.Input[str]] = None,
                 kusto_table_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TimeSeriesDatabaseConnectionArgs.__new__(TimeSeriesDatabaseConnectionArgs)

            if digital_twins_id is None and not opts.urn:
                raise TypeError("Missing required property 'digital_twins_id'")
            __props__.__dict__["digital_twins_id"] = digital_twins_id
            __props__.__dict__["eventhub_consumer_group_name"] = eventhub_consumer_group_name
            if eventhub_name is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_name'")
            __props__.__dict__["eventhub_name"] = eventhub_name
            if eventhub_namespace_endpoint_uri is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_namespace_endpoint_uri'")
            __props__.__dict__["eventhub_namespace_endpoint_uri"] = eventhub_namespace_endpoint_uri
            if eventhub_namespace_id is None and not opts.urn:
                raise TypeError("Missing required property 'eventhub_namespace_id'")
            __props__.__dict__["eventhub_namespace_id"] = eventhub_namespace_id
            if kusto_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_cluster_id'")
            __props__.__dict__["kusto_cluster_id"] = kusto_cluster_id
            if kusto_cluster_uri is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_cluster_uri'")
            __props__.__dict__["kusto_cluster_uri"] = kusto_cluster_uri
            if kusto_database_name is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_database_name'")
            __props__.__dict__["kusto_database_name"] = kusto_database_name
            __props__.__dict__["kusto_table_name"] = kusto_table_name
            __props__.__dict__["name"] = name
        super(TimeSeriesDatabaseConnection, __self__).__init__(
            'azure:digitaltwins/timeSeriesDatabaseConnection:TimeSeriesDatabaseConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            digital_twins_id: Optional[pulumi.Input[str]] = None,
            eventhub_consumer_group_name: Optional[pulumi.Input[str]] = None,
            eventhub_name: Optional[pulumi.Input[str]] = None,
            eventhub_namespace_endpoint_uri: Optional[pulumi.Input[str]] = None,
            eventhub_namespace_id: Optional[pulumi.Input[str]] = None,
            kusto_cluster_id: Optional[pulumi.Input[str]] = None,
            kusto_cluster_uri: Optional[pulumi.Input[str]] = None,
            kusto_database_name: Optional[pulumi.Input[str]] = None,
            kusto_table_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'TimeSeriesDatabaseConnection':
        """
        Get an existing TimeSeriesDatabaseConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] digital_twins_id: The ID of the Digital Twins. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_consumer_group_name: Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        :param pulumi.Input[str] eventhub_name: Name of the Event Hub. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_endpoint_uri: URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] eventhub_namespace_id: The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_id: The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_cluster_uri: URI of the Kusto Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_database_name: Name of the Kusto Database. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kusto_table_name: Name of the Kusto Table. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TimeSeriesDatabaseConnectionState.__new__(_TimeSeriesDatabaseConnectionState)

        __props__.__dict__["digital_twins_id"] = digital_twins_id
        __props__.__dict__["eventhub_consumer_group_name"] = eventhub_consumer_group_name
        __props__.__dict__["eventhub_name"] = eventhub_name
        __props__.__dict__["eventhub_namespace_endpoint_uri"] = eventhub_namespace_endpoint_uri
        __props__.__dict__["eventhub_namespace_id"] = eventhub_namespace_id
        __props__.__dict__["kusto_cluster_id"] = kusto_cluster_id
        __props__.__dict__["kusto_cluster_uri"] = kusto_cluster_uri
        __props__.__dict__["kusto_database_name"] = kusto_database_name
        __props__.__dict__["kusto_table_name"] = kusto_table_name
        __props__.__dict__["name"] = name
        return TimeSeriesDatabaseConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="digitalTwinsId")
    def digital_twins_id(self) -> pulumi.Output[str]:
        """
        The ID of the Digital Twins. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "digital_twins_id")

    @property
    @pulumi.getter(name="eventhubConsumerGroupName")
    def eventhub_consumer_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the Event Hub Consumer Group. Changing this forces a new resource to be created. Defaults to `$Default`.
        """
        return pulumi.get(self, "eventhub_consumer_group_name")

    @property
    @pulumi.getter(name="eventhubName")
    def eventhub_name(self) -> pulumi.Output[str]:
        """
        Name of the Event Hub. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_name")

    @property
    @pulumi.getter(name="eventhubNamespaceEndpointUri")
    def eventhub_namespace_endpoint_uri(self) -> pulumi.Output[str]:
        """
        URI of the Event Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_namespace_endpoint_uri")

    @property
    @pulumi.getter(name="eventhubNamespaceId")
    def eventhub_namespace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Event Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "eventhub_namespace_id")

    @property
    @pulumi.getter(name="kustoClusterId")
    def kusto_cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Kusto Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_cluster_id")

    @property
    @pulumi.getter(name="kustoClusterUri")
    def kusto_cluster_uri(self) -> pulumi.Output[str]:
        """
        URI of the Kusto Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_cluster_uri")

    @property
    @pulumi.getter(name="kustoDatabaseName")
    def kusto_database_name(self) -> pulumi.Output[str]:
        """
        Name of the Kusto Database. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_database_name")

    @property
    @pulumi.getter(name="kustoTableName")
    def kusto_table_name(self) -> pulumi.Output[str]:
        """
        Name of the Kusto Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "kusto_table_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Digital Twins Time Series Database Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

