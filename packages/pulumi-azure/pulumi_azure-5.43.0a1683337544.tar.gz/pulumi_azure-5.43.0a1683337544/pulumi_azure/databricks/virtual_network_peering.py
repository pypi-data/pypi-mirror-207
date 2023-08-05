# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VirtualNetworkPeeringArgs', 'VirtualNetworkPeering']

@pulumi.input_type
class VirtualNetworkPeeringArgs:
    def __init__(__self__, *,
                 remote_address_space_prefixes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 remote_virtual_network_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a VirtualNetworkPeering resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_address_space_prefixes: A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        :param pulumi.Input[str] remote_virtual_network_id: The ID of the remote virtual network. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] allow_forwarded_traffic: Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_gateway_transit: Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_virtual_network_access: Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        :param pulumi.Input[str] name: Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] use_remote_gateways: Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        """
        pulumi.set(__self__, "remote_address_space_prefixes", remote_address_space_prefixes)
        pulumi.set(__self__, "remote_virtual_network_id", remote_virtual_network_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if allow_forwarded_traffic is not None:
            pulumi.set(__self__, "allow_forwarded_traffic", allow_forwarded_traffic)
        if allow_gateway_transit is not None:
            pulumi.set(__self__, "allow_gateway_transit", allow_gateway_transit)
        if allow_virtual_network_access is not None:
            pulumi.set(__self__, "allow_virtual_network_access", allow_virtual_network_access)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_remote_gateways is not None:
            pulumi.set(__self__, "use_remote_gateways", use_remote_gateways)

    @property
    @pulumi.getter(name="remoteAddressSpacePrefixes")
    def remote_address_space_prefixes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "remote_address_space_prefixes")

    @remote_address_space_prefixes.setter
    def remote_address_space_prefixes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "remote_address_space_prefixes", value)

    @property
    @pulumi.getter(name="remoteVirtualNetworkId")
    def remote_virtual_network_id(self) -> pulumi.Input[str]:
        """
        The ID of the remote virtual network. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "remote_virtual_network_id")

    @remote_virtual_network_id.setter
    def remote_virtual_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "remote_virtual_network_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @allow_forwarded_traffic.setter
    def allow_forwarded_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_forwarded_traffic", value)

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[pulumi.Input[bool]]:
        """
        Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @allow_gateway_transit.setter
    def allow_gateway_transit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_gateway_transit", value)

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @allow_virtual_network_access.setter
    def allow_virtual_network_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_virtual_network_access", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[pulumi.Input[bool]]:
        """
        Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "use_remote_gateways")

    @use_remote_gateways.setter
    def use_remote_gateways(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_remote_gateways", value)


@pulumi.input_type
class _VirtualNetworkPeeringState:
    def __init__(__self__, *,
                 address_space_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remote_address_space_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_virtual_network_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 virtual_network_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VirtualNetworkPeering resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_space_prefixes: A list of address blocks reserved for this virtual network in CIDR notation. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] allow_forwarded_traffic: Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_gateway_transit: Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_virtual_network_access: Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        :param pulumi.Input[str] name: Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_address_space_prefixes: A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        :param pulumi.Input[str] remote_virtual_network_id: The ID of the remote virtual network. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] use_remote_gateways: Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[str] virtual_network_id: The ID of the internal Virtual Network used by the DataBricks Workspace.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        """
        if address_space_prefixes is not None:
            pulumi.set(__self__, "address_space_prefixes", address_space_prefixes)
        if allow_forwarded_traffic is not None:
            pulumi.set(__self__, "allow_forwarded_traffic", allow_forwarded_traffic)
        if allow_gateway_transit is not None:
            pulumi.set(__self__, "allow_gateway_transit", allow_gateway_transit)
        if allow_virtual_network_access is not None:
            pulumi.set(__self__, "allow_virtual_network_access", allow_virtual_network_access)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if remote_address_space_prefixes is not None:
            pulumi.set(__self__, "remote_address_space_prefixes", remote_address_space_prefixes)
        if remote_virtual_network_id is not None:
            pulumi.set(__self__, "remote_virtual_network_id", remote_virtual_network_id)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if use_remote_gateways is not None:
            pulumi.set(__self__, "use_remote_gateways", use_remote_gateways)
        if virtual_network_id is not None:
            pulumi.set(__self__, "virtual_network_id", virtual_network_id)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="addressSpacePrefixes")
    def address_space_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of address blocks reserved for this virtual network in CIDR notation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "address_space_prefixes")

    @address_space_prefixes.setter
    def address_space_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "address_space_prefixes", value)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @allow_forwarded_traffic.setter
    def allow_forwarded_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_forwarded_traffic", value)

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[pulumi.Input[bool]]:
        """
        Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @allow_gateway_transit.setter
    def allow_gateway_transit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_gateway_transit", value)

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @allow_virtual_network_access.setter
    def allow_virtual_network_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_virtual_network_access", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="remoteAddressSpacePrefixes")
    def remote_address_space_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "remote_address_space_prefixes")

    @remote_address_space_prefixes.setter
    def remote_address_space_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "remote_address_space_prefixes", value)

    @property
    @pulumi.getter(name="remoteVirtualNetworkId")
    def remote_virtual_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the remote virtual network. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "remote_virtual_network_id")

    @remote_virtual_network_id.setter
    def remote_virtual_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_virtual_network_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[pulumi.Input[bool]]:
        """
        Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "use_remote_gateways")

    @use_remote_gateways.setter
    def use_remote_gateways(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_remote_gateways", value)

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the internal Virtual Network used by the DataBricks Workspace.
        """
        return pulumi.get(self, "virtual_network_id")

    @virtual_network_id.setter
    def virtual_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class VirtualNetworkPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remote_address_space_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_virtual_network_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Databricks Virtual Network Peering

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        remote_virtual_network = azure.network.VirtualNetwork("remoteVirtualNetwork",
            resource_group_name=example_resource_group.name,
            address_spaces=["10.0.1.0/24"],
            location=example_resource_group.location)
        example_workspace = azure.databricks.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku="standard")
        example_virtual_network_peering = azure.databricks.VirtualNetworkPeering("exampleVirtualNetworkPeering",
            resource_group_name=example_resource_group.name,
            workspace_id=example_workspace.id,
            remote_address_space_prefixes=remote_virtual_network.address_spaces,
            remote_virtual_network_id=remote_virtual_network.id,
            allow_virtual_network_access=True)
        remote_virtual_network_peering = azure.network.VirtualNetworkPeering("remoteVirtualNetworkPeering",
            resource_group_name=example_resource_group.name,
            virtual_network_name=remote_virtual_network.name,
            remote_virtual_network_id=example_virtual_network_peering.virtual_network_id,
            allow_virtual_network_access=True)
        ```

        ## Import

        Databrick Virtual Network Peerings can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:databricks/virtualNetworkPeering:VirtualNetworkPeering example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Databricks/workspaces/workspace1/virtualNetworkPeerings/peering1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_forwarded_traffic: Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_gateway_transit: Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_virtual_network_access: Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        :param pulumi.Input[str] name: Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_address_space_prefixes: A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        :param pulumi.Input[str] remote_virtual_network_id: The ID of the remote virtual network. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] use_remote_gateways: Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualNetworkPeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Databricks Virtual Network Peering

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        remote_virtual_network = azure.network.VirtualNetwork("remoteVirtualNetwork",
            resource_group_name=example_resource_group.name,
            address_spaces=["10.0.1.0/24"],
            location=example_resource_group.location)
        example_workspace = azure.databricks.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku="standard")
        example_virtual_network_peering = azure.databricks.VirtualNetworkPeering("exampleVirtualNetworkPeering",
            resource_group_name=example_resource_group.name,
            workspace_id=example_workspace.id,
            remote_address_space_prefixes=remote_virtual_network.address_spaces,
            remote_virtual_network_id=remote_virtual_network.id,
            allow_virtual_network_access=True)
        remote_virtual_network_peering = azure.network.VirtualNetworkPeering("remoteVirtualNetworkPeering",
            resource_group_name=example_resource_group.name,
            virtual_network_name=remote_virtual_network.name,
            remote_virtual_network_id=example_virtual_network_peering.virtual_network_id,
            allow_virtual_network_access=True)
        ```

        ## Import

        Databrick Virtual Network Peerings can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:databricks/virtualNetworkPeering:VirtualNetworkPeering example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Databricks/workspaces/workspace1/virtualNetworkPeerings/peering1
        ```

        :param str resource_name: The name of the resource.
        :param VirtualNetworkPeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualNetworkPeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remote_address_space_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_virtual_network_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualNetworkPeeringArgs.__new__(VirtualNetworkPeeringArgs)

            __props__.__dict__["allow_forwarded_traffic"] = allow_forwarded_traffic
            __props__.__dict__["allow_gateway_transit"] = allow_gateway_transit
            __props__.__dict__["allow_virtual_network_access"] = allow_virtual_network_access
            __props__.__dict__["name"] = name
            if remote_address_space_prefixes is None and not opts.urn:
                raise TypeError("Missing required property 'remote_address_space_prefixes'")
            __props__.__dict__["remote_address_space_prefixes"] = remote_address_space_prefixes
            if remote_virtual_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'remote_virtual_network_id'")
            __props__.__dict__["remote_virtual_network_id"] = remote_virtual_network_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["use_remote_gateways"] = use_remote_gateways
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["address_space_prefixes"] = None
            __props__.__dict__["virtual_network_id"] = None
        super(VirtualNetworkPeering, __self__).__init__(
            'azure:databricks/virtualNetworkPeering:VirtualNetworkPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_space_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
            allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
            allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            remote_address_space_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            remote_virtual_network_id: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            use_remote_gateways: Optional[pulumi.Input[bool]] = None,
            virtual_network_id: Optional[pulumi.Input[str]] = None,
            workspace_id: Optional[pulumi.Input[str]] = None) -> 'VirtualNetworkPeering':
        """
        Get an existing VirtualNetworkPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_space_prefixes: A list of address blocks reserved for this virtual network in CIDR notation. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] allow_forwarded_traffic: Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_gateway_transit: Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[bool] allow_virtual_network_access: Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        :param pulumi.Input[str] name: Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] remote_address_space_prefixes: A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        :param pulumi.Input[str] remote_virtual_network_id: The ID of the remote virtual network. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] use_remote_gateways: Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        :param pulumi.Input[str] virtual_network_id: The ID of the internal Virtual Network used by the DataBricks Workspace.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualNetworkPeeringState.__new__(_VirtualNetworkPeeringState)

        __props__.__dict__["address_space_prefixes"] = address_space_prefixes
        __props__.__dict__["allow_forwarded_traffic"] = allow_forwarded_traffic
        __props__.__dict__["allow_gateway_transit"] = allow_gateway_transit
        __props__.__dict__["allow_virtual_network_access"] = allow_virtual_network_access
        __props__.__dict__["name"] = name
        __props__.__dict__["remote_address_space_prefixes"] = remote_address_space_prefixes
        __props__.__dict__["remote_virtual_network_id"] = remote_virtual_network_id
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["use_remote_gateways"] = use_remote_gateways
        __props__.__dict__["virtual_network_id"] = virtual_network_id
        __props__.__dict__["workspace_id"] = workspace_id
        return VirtualNetworkPeering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressSpacePrefixes")
    def address_space_prefixes(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of address blocks reserved for this virtual network in CIDR notation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "address_space_prefixes")

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> pulumi.Output[Optional[bool]]:
        """
        Can the forwarded traffic from the VMs in the local virtual network be forwarded to the remote virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> pulumi.Output[Optional[bool]]:
        """
        Can the gateway links be used in the remote virtual network to link to the Databricks virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> pulumi.Output[Optional[bool]]:
        """
        Can the VMs in the local virtual network space access the VMs in the remote virtual network space? Defaults to `true`.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Databricks Virtual Network Peering resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="remoteAddressSpacePrefixes")
    def remote_address_space_prefixes(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of address blocks reserved for the remote virtual network in CIDR notation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "remote_address_space_prefixes")

    @property
    @pulumi.getter(name="remoteVirtualNetworkId")
    def remote_virtual_network_id(self) -> pulumi.Output[str]:
        """
        The ID of the remote virtual network. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "remote_virtual_network_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group in which the Databricks Virtual Network Peering should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> pulumi.Output[Optional[bool]]:
        """
        Can remote gateways be used on the Databricks virtual network? Defaults to `false`.
        """
        return pulumi.get(self, "use_remote_gateways")

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> pulumi.Output[str]:
        """
        The ID of the internal Virtual Network used by the DataBricks Workspace.
        """
        return pulumi.get(self, "virtual_network_id")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Databricks Workspace that this Databricks Virtual Network Peering is bound. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "workspace_id")

