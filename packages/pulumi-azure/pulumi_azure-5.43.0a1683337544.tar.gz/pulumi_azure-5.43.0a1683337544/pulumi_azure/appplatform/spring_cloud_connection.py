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

__all__ = ['SpringCloudConnectionArgs', 'SpringCloudConnection']

@pulumi.input_type
class SpringCloudConnectionArgs:
    def __init__(__self__, *,
                 authentication: pulumi.Input['SpringCloudConnectionAuthenticationArgs'],
                 spring_cloud_id: pulumi.Input[str],
                 target_resource_id: pulumi.Input[str],
                 client_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input['SpringCloudConnectionSecretStoreArgs']] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SpringCloudConnection resource.
        :param pulumi.Input['SpringCloudConnectionAuthenticationArgs'] authentication: The authentication info. An `authentication` block as defined below.
        :param pulumi.Input[str] spring_cloud_id: The ID of the data source spring cloud. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input['SpringCloudConnectionSecretStoreArgs'] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        pulumi.set(__self__, "authentication", authentication)
        pulumi.set(__self__, "spring_cloud_id", spring_cloud_id)
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        if client_type is not None:
            pulumi.set(__self__, "client_type", client_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secret_store is not None:
            pulumi.set(__self__, "secret_store", secret_store)
        if vnet_solution is not None:
            pulumi.set(__self__, "vnet_solution", vnet_solution)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Input['SpringCloudConnectionAuthenticationArgs']:
        """
        The authentication info. An `authentication` block as defined below.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: pulumi.Input['SpringCloudConnectionAuthenticationArgs']):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="springCloudId")
    def spring_cloud_id(self) -> pulumi.Input[str]:
        """
        The ID of the data source spring cloud. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "spring_cloud_id")

    @spring_cloud_id.setter
    def spring_cloud_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "spring_cloud_id", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Input[str]:
        """
        The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[str]]:
        """
        The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        """
        return pulumi.get(self, "client_type")

    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input['SpringCloudConnectionSecretStoreArgs']]:
        """
        An option to store secret value in secure place. An `secret_store` block as defined below.
        """
        return pulumi.get(self, "secret_store")

    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input['SpringCloudConnectionSecretStoreArgs']]):
        pulumi.set(self, "secret_store", value)

    @property
    @pulumi.getter(name="vnetSolution")
    def vnet_solution(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        return pulumi.get(self, "vnet_solution")

    @vnet_solution.setter
    def vnet_solution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_solution", value)


@pulumi.input_type
class _SpringCloudConnectionState:
    def __init__(__self__, *,
                 authentication: Optional[pulumi.Input['SpringCloudConnectionAuthenticationArgs']] = None,
                 client_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input['SpringCloudConnectionSecretStoreArgs']] = None,
                 spring_cloud_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SpringCloudConnection resources.
        :param pulumi.Input['SpringCloudConnectionAuthenticationArgs'] authentication: The authentication info. An `authentication` block as defined below.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input['SpringCloudConnectionSecretStoreArgs'] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] spring_cloud_id: The ID of the data source spring cloud. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if client_type is not None:
            pulumi.set(__self__, "client_type", client_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secret_store is not None:
            pulumi.set(__self__, "secret_store", secret_store)
        if spring_cloud_id is not None:
            pulumi.set(__self__, "spring_cloud_id", spring_cloud_id)
        if target_resource_id is not None:
            pulumi.set(__self__, "target_resource_id", target_resource_id)
        if vnet_solution is not None:
            pulumi.set(__self__, "vnet_solution", vnet_solution)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input['SpringCloudConnectionAuthenticationArgs']]:
        """
        The authentication info. An `authentication` block as defined below.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input['SpringCloudConnectionAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[str]]:
        """
        The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        """
        return pulumi.get(self, "client_type")

    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input['SpringCloudConnectionSecretStoreArgs']]:
        """
        An option to store secret value in secure place. An `secret_store` block as defined below.
        """
        return pulumi.get(self, "secret_store")

    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input['SpringCloudConnectionSecretStoreArgs']]):
        pulumi.set(self, "secret_store", value)

    @property
    @pulumi.getter(name="springCloudId")
    def spring_cloud_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the data source spring cloud. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "spring_cloud_id")

    @spring_cloud_id.setter
    def spring_cloud_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_id", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="vnetSolution")
    def vnet_solution(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        return pulumi.get(self, "vnet_solution")

    @vnet_solution.setter
    def vnet_solution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_solution", value)


class SpringCloudConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['SpringCloudConnectionAuthenticationArgs']]] = None,
                 client_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[pulumi.InputType['SpringCloudConnectionSecretStoreArgs']]] = None,
                 spring_cloud_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a service connector for spring cloud app.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cosmosdb.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            offer_type="Standard",
            kind="GlobalDocumentDB",
            consistency_policy=azure.cosmosdb.AccountConsistencyPolicyArgs(
                consistency_level="BoundedStaleness",
                max_interval_in_seconds=10,
                max_staleness_prefix=200,
            ),
            geo_locations=[azure.cosmosdb.AccountGeoLocationArgs(
                location=example_resource_group.location,
                failover_priority=0,
            )])
        example_sql_database = azure.cosmosdb.SqlDatabase("exampleSqlDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_sql_container = azure.cosmosdb.SqlContainer("exampleSqlContainer",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            database_name=example_sql_database.name,
            partition_key_path="/definition")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_spring_cloud_app = azure.appplatform.SpringCloudApp("exampleSpringCloudApp",
            resource_group_name=example_resource_group.name,
            service_name=example_spring_cloud_service.name,
            identity=azure.appplatform.SpringCloudAppIdentityArgs(
                type="SystemAssigned",
            ))
        example_spring_cloud_java_deployment = azure.appplatform.SpringCloudJavaDeployment("exampleSpringCloudJavaDeployment", spring_cloud_app_id=example_spring_cloud_app.id)
        example_spring_cloud_connection = azure.appplatform.SpringCloudConnection("exampleSpringCloudConnection",
            spring_cloud_id=example_spring_cloud_java_deployment.id,
            target_resource_id=example_sql_database.id,
            authentication=azure.appplatform.SpringCloudConnectionAuthenticationArgs(
                type="systemAssignedIdentity",
            ))
        ```

        ## Import

        Service Connector for spring cloud can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudConnection:SpringCloudConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.AppPlatform/Spring/springcloud/apps/springcloudapp/deployments/deployment/providers/Microsoft.ServiceLinker/linkers/serviceconnector1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SpringCloudConnectionAuthenticationArgs']] authentication: The authentication info. An `authentication` block as defined below.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SpringCloudConnectionSecretStoreArgs']] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] spring_cloud_id: The ID of the data source spring cloud. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpringCloudConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a service connector for spring cloud app.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cosmosdb.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            offer_type="Standard",
            kind="GlobalDocumentDB",
            consistency_policy=azure.cosmosdb.AccountConsistencyPolicyArgs(
                consistency_level="BoundedStaleness",
                max_interval_in_seconds=10,
                max_staleness_prefix=200,
            ),
            geo_locations=[azure.cosmosdb.AccountGeoLocationArgs(
                location=example_resource_group.location,
                failover_priority=0,
            )])
        example_sql_database = azure.cosmosdb.SqlDatabase("exampleSqlDatabase",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_sql_container = azure.cosmosdb.SqlContainer("exampleSqlContainer",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            database_name=example_sql_database.name,
            partition_key_path="/definition")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_spring_cloud_app = azure.appplatform.SpringCloudApp("exampleSpringCloudApp",
            resource_group_name=example_resource_group.name,
            service_name=example_spring_cloud_service.name,
            identity=azure.appplatform.SpringCloudAppIdentityArgs(
                type="SystemAssigned",
            ))
        example_spring_cloud_java_deployment = azure.appplatform.SpringCloudJavaDeployment("exampleSpringCloudJavaDeployment", spring_cloud_app_id=example_spring_cloud_app.id)
        example_spring_cloud_connection = azure.appplatform.SpringCloudConnection("exampleSpringCloudConnection",
            spring_cloud_id=example_spring_cloud_java_deployment.id,
            target_resource_id=example_sql_database.id,
            authentication=azure.appplatform.SpringCloudConnectionAuthenticationArgs(
                type="systemAssignedIdentity",
            ))
        ```

        ## Import

        Service Connector for spring cloud can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudConnection:SpringCloudConnection example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.AppPlatform/Spring/springcloud/apps/springcloudapp/deployments/deployment/providers/Microsoft.ServiceLinker/linkers/serviceconnector1
        ```

        :param str resource_name: The name of the resource.
        :param SpringCloudConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpringCloudConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['SpringCloudConnectionAuthenticationArgs']]] = None,
                 client_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[pulumi.InputType['SpringCloudConnectionSecretStoreArgs']]] = None,
                 spring_cloud_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 vnet_solution: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SpringCloudConnectionArgs.__new__(SpringCloudConnectionArgs)

            if authentication is None and not opts.urn:
                raise TypeError("Missing required property 'authentication'")
            __props__.__dict__["authentication"] = authentication
            __props__.__dict__["client_type"] = client_type
            __props__.__dict__["name"] = name
            __props__.__dict__["secret_store"] = secret_store
            if spring_cloud_id is None and not opts.urn:
                raise TypeError("Missing required property 'spring_cloud_id'")
            __props__.__dict__["spring_cloud_id"] = spring_cloud_id
            if target_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__.__dict__["target_resource_id"] = target_resource_id
            __props__.__dict__["vnet_solution"] = vnet_solution
        super(SpringCloudConnection, __self__).__init__(
            'azure:appplatform/springCloudConnection:SpringCloudConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication: Optional[pulumi.Input[pulumi.InputType['SpringCloudConnectionAuthenticationArgs']]] = None,
            client_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            secret_store: Optional[pulumi.Input[pulumi.InputType['SpringCloudConnectionSecretStoreArgs']]] = None,
            spring_cloud_id: Optional[pulumi.Input[str]] = None,
            target_resource_id: Optional[pulumi.Input[str]] = None,
            vnet_solution: Optional[pulumi.Input[str]] = None) -> 'SpringCloudConnection':
        """
        Get an existing SpringCloudConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SpringCloudConnectionAuthenticationArgs']] authentication: The authentication info. An `authentication` block as defined below.
        :param pulumi.Input[str] client_type: The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        :param pulumi.Input[str] name: The name of the service connection. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SpringCloudConnectionSecretStoreArgs']] secret_store: An option to store secret value in secure place. An `secret_store` block as defined below.
        :param pulumi.Input[str] spring_cloud_id: The ID of the data source spring cloud. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        :param pulumi.Input[str] vnet_solution: The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SpringCloudConnectionState.__new__(_SpringCloudConnectionState)

        __props__.__dict__["authentication"] = authentication
        __props__.__dict__["client_type"] = client_type
        __props__.__dict__["name"] = name
        __props__.__dict__["secret_store"] = secret_store
        __props__.__dict__["spring_cloud_id"] = spring_cloud_id
        __props__.__dict__["target_resource_id"] = target_resource_id
        __props__.__dict__["vnet_solution"] = vnet_solution
        return SpringCloudConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output['outputs.SpringCloudConnectionAuthentication']:
        """
        The authentication info. An `authentication` block as defined below.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> pulumi.Output[Optional[str]]:
        """
        The application client type. Possible values are `none`, `dotnet`, `java`, `python`, `go`, `php`, `ruby`, `django`, `nodejs` and `springBoot`.
        """
        return pulumi.get(self, "client_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the service connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> pulumi.Output[Optional['outputs.SpringCloudConnectionSecretStore']]:
        """
        An option to store secret value in secure place. An `secret_store` block as defined below.
        """
        return pulumi.get(self, "secret_store")

    @property
    @pulumi.getter(name="springCloudId")
    def spring_cloud_id(self) -> pulumi.Output[str]:
        """
        The ID of the data source spring cloud. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "spring_cloud_id")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the target resource. Changing this forces a new resource to be created. Possible values are `Postgres`, `PostgresFlexible`, `Mysql`, `Sql`, `Redis`, `RedisEnterprise`, `CosmosCassandra`, `CosmosGremlin`, `CosmosMongo`, `CosmosSql`, `CosmosTable`, `StorageBlob`, `StorageQueue`, `StorageFile`, `StorageTable`, `AppConfig`, `EventHub`, `ServiceBus`, `SignalR`, `WebPubSub`, `ConfluentKafka`.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="vnetSolution")
    def vnet_solution(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the VNet solution. Possible values are `serviceEndpoint`, `privateLink`.
        """
        return pulumi.get(self, "vnet_solution")

