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

__all__ = ['NetworkManagerArgs', 'NetworkManager']

@pulumi.input_type
class NetworkManagerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 scope: pulumi.Input['NetworkManagerScopeArgs'],
                 scope_accesses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkManager resource.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        :param pulumi.Input['NetworkManagerScopeArgs'] scope: A `scope` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_accesses: A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        :param pulumi.Input[str] description: A description of the network manager.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Network Managers.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "scope_accesses", scope_accesses)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input['NetworkManagerScopeArgs']:
        """
        A `scope` block as defined below.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input['NetworkManagerScopeArgs']):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="scopeAccesses")
    def scope_accesses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        """
        return pulumi.get(self, "scope_accesses")

    @scope_accesses.setter
    def scope_accesses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scope_accesses", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the network manager.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Network Managers.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _NetworkManagerState:
    def __init__(__self__, *,
                 cross_tenant_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkManagerCrossTenantScopeArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['NetworkManagerScopeArgs']] = None,
                 scope_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering NetworkManager resources.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkManagerCrossTenantScopeArgs']]] cross_tenant_scopes: A `cross_tenant_scopes` block as defined below.
        :param pulumi.Input[str] description: A description of the network manager.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        :param pulumi.Input['NetworkManagerScopeArgs'] scope: A `scope` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_accesses: A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Network Managers.
        """
        if cross_tenant_scopes is not None:
            pulumi.set(__self__, "cross_tenant_scopes", cross_tenant_scopes)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if scope_accesses is not None:
            pulumi.set(__self__, "scope_accesses", scope_accesses)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="crossTenantScopes")
    def cross_tenant_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkManagerCrossTenantScopeArgs']]]]:
        """
        A `cross_tenant_scopes` block as defined below.
        """
        return pulumi.get(self, "cross_tenant_scopes")

    @cross_tenant_scopes.setter
    def cross_tenant_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkManagerCrossTenantScopeArgs']]]]):
        pulumi.set(self, "cross_tenant_scopes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the network manager.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input['NetworkManagerScopeArgs']]:
        """
        A `scope` block as defined below.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input['NetworkManagerScopeArgs']]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="scopeAccesses")
    def scope_accesses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        """
        return pulumi.get(self, "scope_accesses")

    @scope_accesses.setter
    def scope_accesses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scope_accesses", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Network Managers.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class NetworkManager(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['NetworkManagerScopeArgs']]] = None,
                 scope_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Network Managers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        current = azure.core.get_subscription()
        example_network_manager = azure.network.NetworkManager("exampleNetworkManager",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            scope=azure.network.NetworkManagerScopeArgs(
                subscription_ids=[current.id],
            ),
            scope_accesses=[
                "Connectivity",
                "SecurityAdmin",
            ],
            description="example network manager",
            tags={
                "foo": "bar",
            })
        ```

        ## Import

        Network Managers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/networkManager:NetworkManager example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.Network/networkManagers/networkManager1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the network manager.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        :param pulumi.Input[pulumi.InputType['NetworkManagerScopeArgs']] scope: A `scope` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_accesses: A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Network Managers.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkManagerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Network Managers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        current = azure.core.get_subscription()
        example_network_manager = azure.network.NetworkManager("exampleNetworkManager",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            scope=azure.network.NetworkManagerScopeArgs(
                subscription_ids=[current.id],
            ),
            scope_accesses=[
                "Connectivity",
                "SecurityAdmin",
            ],
            description="example network manager",
            tags={
                "foo": "bar",
            })
        ```

        ## Import

        Network Managers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/networkManager:NetworkManager example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.Network/networkManagers/networkManager1
        ```

        :param str resource_name: The name of the resource.
        :param NetworkManagerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkManagerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['NetworkManagerScopeArgs']]] = None,
                 scope_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkManagerArgs.__new__(NetworkManagerArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            if scope_accesses is None and not opts.urn:
                raise TypeError("Missing required property 'scope_accesses'")
            __props__.__dict__["scope_accesses"] = scope_accesses
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cross_tenant_scopes"] = None
        super(NetworkManager, __self__).__init__(
            'azure:network/networkManager:NetworkManager',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cross_tenant_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkManagerCrossTenantScopeArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[pulumi.InputType['NetworkManagerScopeArgs']]] = None,
            scope_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NetworkManager':
        """
        Get an existing NetworkManager resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkManagerCrossTenantScopeArgs']]]] cross_tenant_scopes: A `cross_tenant_scopes` block as defined below.
        :param pulumi.Input[str] description: A description of the network manager.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        :param pulumi.Input[pulumi.InputType['NetworkManagerScopeArgs']] scope: A `scope` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_accesses: A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Network Managers.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkManagerState.__new__(_NetworkManagerState)

        __props__.__dict__["cross_tenant_scopes"] = cross_tenant_scopes
        __props__.__dict__["description"] = description
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["scope"] = scope
        __props__.__dict__["scope_accesses"] = scope_accesses
        __props__.__dict__["tags"] = tags
        return NetworkManager(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="crossTenantScopes")
    def cross_tenant_scopes(self) -> pulumi.Output[Sequence['outputs.NetworkManagerCrossTenantScope']]:
        """
        A `cross_tenant_scopes` block as defined below.
        """
        return pulumi.get(self, "cross_tenant_scopes")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the network manager.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Network Managers should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name which should be used for this Network Managers. Changing this forces a new Network Managers to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group where the Network Managers should exist. Changing this forces a new Network Managers to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output['outputs.NetworkManagerScope']:
        """
        A `scope` block as defined below.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="scopeAccesses")
    def scope_accesses(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of configuration deployment type. Possible values are `Connectivity` and `SecurityAdmin`, corresponds to if Connectivity Configuration and Security Admin Configuration is allowed for the Network Manager.
        """
        return pulumi.get(self, "scope_accesses")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Network Managers.
        """
        return pulumi.get(self, "tags")

