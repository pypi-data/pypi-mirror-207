# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FunctionAppHybridConnectionArgs', 'FunctionAppHybridConnection']

@pulumi.input_type
class FunctionAppHybridConnectionArgs:
    def __init__(__self__, *,
                 function_app_id: pulumi.Input[str],
                 hostname: pulumi.Input[str],
                 port: pulumi.Input[int],
                 relay_id: pulumi.Input[str],
                 send_key_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FunctionAppHybridConnection resource.
        :param pulumi.Input[str] function_app_id: The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: The hostname of the endpoint.
        :param pulumi.Input[int] port: The port to use for the endpoint
        :param pulumi.Input[str] relay_id: The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        :param pulumi.Input[str] send_key_name: The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        """
        pulumi.set(__self__, "function_app_id", function_app_id)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "relay_id", relay_id)
        if send_key_name is not None:
            pulumi.set(__self__, "send_key_name", send_key_name)

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> pulumi.Input[str]:
        """
        The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "function_app_id")

    @function_app_id.setter
    def function_app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_app_id", value)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        The hostname of the endpoint.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        The port to use for the endpoint
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="relayId")
    def relay_id(self) -> pulumi.Input[str]:
        """
        The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "relay_id")

    @relay_id.setter
    def relay_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "relay_id", value)

    @property
    @pulumi.getter(name="sendKeyName")
    def send_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        """
        return pulumi.get(self, "send_key_name")

    @send_key_name.setter
    def send_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "send_key_name", value)


@pulumi.input_type
class _FunctionAppHybridConnectionState:
    def __init__(__self__, *,
                 function_app_id: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 relay_id: Optional[pulumi.Input[str]] = None,
                 relay_name: Optional[pulumi.Input[str]] = None,
                 send_key_name: Optional[pulumi.Input[str]] = None,
                 send_key_value: Optional[pulumi.Input[str]] = None,
                 service_bus_namespace: Optional[pulumi.Input[str]] = None,
                 service_bus_suffix: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FunctionAppHybridConnection resources.
        :param pulumi.Input[str] function_app_id: The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: The hostname of the endpoint.
        :param pulumi.Input[str] namespace_name: The name of the Relay Namespace.
        :param pulumi.Input[int] port: The port to use for the endpoint
        :param pulumi.Input[str] relay_id: The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        :param pulumi.Input[str] relay_name: The name of the Relay in use.
        :param pulumi.Input[str] send_key_name: The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        :param pulumi.Input[str] send_key_value: The Primary Access Key for the `send_key_name`
        :param pulumi.Input[str] service_bus_namespace: The Service Bus Namespace.
        :param pulumi.Input[str] service_bus_suffix: The suffix for the endpoint.
        """
        if function_app_id is not None:
            pulumi.set(__self__, "function_app_id", function_app_id)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if relay_id is not None:
            pulumi.set(__self__, "relay_id", relay_id)
        if relay_name is not None:
            pulumi.set(__self__, "relay_name", relay_name)
        if send_key_name is not None:
            pulumi.set(__self__, "send_key_name", send_key_name)
        if send_key_value is not None:
            pulumi.set(__self__, "send_key_value", send_key_value)
        if service_bus_namespace is not None:
            pulumi.set(__self__, "service_bus_namespace", service_bus_namespace)
        if service_bus_suffix is not None:
            pulumi.set(__self__, "service_bus_suffix", service_bus_suffix)

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "function_app_id")

    @function_app_id.setter
    def function_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_app_id", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The hostname of the endpoint.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Relay Namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port to use for the endpoint
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="relayId")
    def relay_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "relay_id")

    @relay_id.setter
    def relay_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relay_id", value)

    @property
    @pulumi.getter(name="relayName")
    def relay_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Relay in use.
        """
        return pulumi.get(self, "relay_name")

    @relay_name.setter
    def relay_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relay_name", value)

    @property
    @pulumi.getter(name="sendKeyName")
    def send_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        """
        return pulumi.get(self, "send_key_name")

    @send_key_name.setter
    def send_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "send_key_name", value)

    @property
    @pulumi.getter(name="sendKeyValue")
    def send_key_value(self) -> Optional[pulumi.Input[str]]:
        """
        The Primary Access Key for the `send_key_name`
        """
        return pulumi.get(self, "send_key_value")

    @send_key_value.setter
    def send_key_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "send_key_value", value)

    @property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The Service Bus Namespace.
        """
        return pulumi.get(self, "service_bus_namespace")

    @service_bus_namespace.setter
    def service_bus_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_bus_namespace", value)

    @property
    @pulumi.getter(name="serviceBusSuffix")
    def service_bus_suffix(self) -> Optional[pulumi.Input[str]]:
        """
        The suffix for the endpoint.
        """
        return pulumi.get(self, "service_bus_suffix")

    @service_bus_suffix.setter
    def service_bus_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_bus_suffix", value)


class FunctionAppHybridConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 function_app_id: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 relay_id: Optional[pulumi.Input[str]] = None,
                 send_key_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Function App Hybrid Connection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service_plan = azure.appservice.ServicePlan("exampleServicePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            os_type="Windows",
            sku_name="S1")
        example_namespace = azure.relay.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Standard")
        example_hybrid_connection = azure.relay.HybridConnection("exampleHybridConnection",
            resource_group_name=example_resource_group.name,
            relay_namespace_name=example_namespace.name)
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_windows_web_app = azure.appservice.WindowsWebApp("exampleWindowsWebApp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            service_plan_id=example_service_plan.id,
            site_config=azure.appservice.WindowsWebAppSiteConfigArgs())
        example_windows_function_app = azure.appservice.WindowsFunctionApp("exampleWindowsFunctionApp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            service_plan_id=example_service_plan.id,
            storage_account_name=example_account.name,
            storage_account_access_key=example_account.primary_access_key,
            site_config=azure.appservice.WindowsFunctionAppSiteConfigArgs())
        example_function_app_hybrid_connection = azure.appservice.FunctionAppHybridConnection("exampleFunctionAppHybridConnection",
            function_app_id=example_windows_web_app.id,
            relay_id=example_hybrid_connection.id,
            hostname="myhostname.example",
            port=8081)
        ```

        ## Import

        a Function App Hybrid Connection can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/functionAppHybridConnection:FunctionAppHybridConnection example "/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Web/sites/site1/hybridConnectionNamespaces/hybridConnectionNamespace1/relays/relay1"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] function_app_id: The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: The hostname of the endpoint.
        :param pulumi.Input[int] port: The port to use for the endpoint
        :param pulumi.Input[str] relay_id: The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        :param pulumi.Input[str] send_key_name: The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FunctionAppHybridConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Function App Hybrid Connection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service_plan = azure.appservice.ServicePlan("exampleServicePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            os_type="Windows",
            sku_name="S1")
        example_namespace = azure.relay.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="Standard")
        example_hybrid_connection = azure.relay.HybridConnection("exampleHybridConnection",
            resource_group_name=example_resource_group.name,
            relay_namespace_name=example_namespace.name)
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_windows_web_app = azure.appservice.WindowsWebApp("exampleWindowsWebApp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            service_plan_id=example_service_plan.id,
            site_config=azure.appservice.WindowsWebAppSiteConfigArgs())
        example_windows_function_app = azure.appservice.WindowsFunctionApp("exampleWindowsFunctionApp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            service_plan_id=example_service_plan.id,
            storage_account_name=example_account.name,
            storage_account_access_key=example_account.primary_access_key,
            site_config=azure.appservice.WindowsFunctionAppSiteConfigArgs())
        example_function_app_hybrid_connection = azure.appservice.FunctionAppHybridConnection("exampleFunctionAppHybridConnection",
            function_app_id=example_windows_web_app.id,
            relay_id=example_hybrid_connection.id,
            hostname="myhostname.example",
            port=8081)
        ```

        ## Import

        a Function App Hybrid Connection can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/functionAppHybridConnection:FunctionAppHybridConnection example "/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Web/sites/site1/hybridConnectionNamespaces/hybridConnectionNamespace1/relays/relay1"
        ```

        :param str resource_name: The name of the resource.
        :param FunctionAppHybridConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FunctionAppHybridConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 function_app_id: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 relay_id: Optional[pulumi.Input[str]] = None,
                 send_key_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FunctionAppHybridConnectionArgs.__new__(FunctionAppHybridConnectionArgs)

            if function_app_id is None and not opts.urn:
                raise TypeError("Missing required property 'function_app_id'")
            __props__.__dict__["function_app_id"] = function_app_id
            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__.__dict__["hostname"] = hostname
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if relay_id is None and not opts.urn:
                raise TypeError("Missing required property 'relay_id'")
            __props__.__dict__["relay_id"] = relay_id
            __props__.__dict__["send_key_name"] = send_key_name
            __props__.__dict__["namespace_name"] = None
            __props__.__dict__["relay_name"] = None
            __props__.__dict__["send_key_value"] = None
            __props__.__dict__["service_bus_namespace"] = None
            __props__.__dict__["service_bus_suffix"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["sendKeyValue"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(FunctionAppHybridConnection, __self__).__init__(
            'azure:appservice/functionAppHybridConnection:FunctionAppHybridConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            function_app_id: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            namespace_name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            relay_id: Optional[pulumi.Input[str]] = None,
            relay_name: Optional[pulumi.Input[str]] = None,
            send_key_name: Optional[pulumi.Input[str]] = None,
            send_key_value: Optional[pulumi.Input[str]] = None,
            service_bus_namespace: Optional[pulumi.Input[str]] = None,
            service_bus_suffix: Optional[pulumi.Input[str]] = None) -> 'FunctionAppHybridConnection':
        """
        Get an existing FunctionAppHybridConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] function_app_id: The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: The hostname of the endpoint.
        :param pulumi.Input[str] namespace_name: The name of the Relay Namespace.
        :param pulumi.Input[int] port: The port to use for the endpoint
        :param pulumi.Input[str] relay_id: The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        :param pulumi.Input[str] relay_name: The name of the Relay in use.
        :param pulumi.Input[str] send_key_name: The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        :param pulumi.Input[str] send_key_value: The Primary Access Key for the `send_key_name`
        :param pulumi.Input[str] service_bus_namespace: The Service Bus Namespace.
        :param pulumi.Input[str] service_bus_suffix: The suffix for the endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FunctionAppHybridConnectionState.__new__(_FunctionAppHybridConnectionState)

        __props__.__dict__["function_app_id"] = function_app_id
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["namespace_name"] = namespace_name
        __props__.__dict__["port"] = port
        __props__.__dict__["relay_id"] = relay_id
        __props__.__dict__["relay_name"] = relay_name
        __props__.__dict__["send_key_name"] = send_key_name
        __props__.__dict__["send_key_value"] = send_key_value
        __props__.__dict__["service_bus_namespace"] = service_bus_namespace
        __props__.__dict__["service_bus_suffix"] = service_bus_suffix
        return FunctionAppHybridConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> pulumi.Output[str]:
        """
        The ID of the Function App for this Hybrid Connection. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "function_app_id")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The hostname of the endpoint.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[str]:
        """
        The name of the Relay Namespace.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        The port to use for the endpoint
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="relayId")
    def relay_id(self) -> pulumi.Output[str]:
        """
        The ID of the Relay Hybrid Connection to use. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "relay_id")

    @property
    @pulumi.getter(name="relayName")
    def relay_name(self) -> pulumi.Output[str]:
        """
        The name of the Relay in use.
        """
        return pulumi.get(self, "relay_name")

    @property
    @pulumi.getter(name="sendKeyName")
    def send_key_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Relay key with `Send` permission to use. Defaults to `RootManageSharedAccessKey`
        """
        return pulumi.get(self, "send_key_name")

    @property
    @pulumi.getter(name="sendKeyValue")
    def send_key_value(self) -> pulumi.Output[str]:
        """
        The Primary Access Key for the `send_key_name`
        """
        return pulumi.get(self, "send_key_value")

    @property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> pulumi.Output[str]:
        """
        The Service Bus Namespace.
        """
        return pulumi.get(self, "service_bus_namespace")

    @property
    @pulumi.getter(name="serviceBusSuffix")
    def service_bus_suffix(self) -> pulumi.Output[str]:
        """
        The suffix for the endpoint.
        """
        return pulumi.get(self, "service_bus_suffix")

