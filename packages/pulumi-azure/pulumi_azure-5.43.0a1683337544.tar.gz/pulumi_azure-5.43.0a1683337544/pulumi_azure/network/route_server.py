# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RouteServerArgs', 'RouteServer']

@pulumi.input_type
class RouteServerArgs:
    def __init__(__self__, *,
                 public_ip_address_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input[str],
                 subnet_id: pulumi.Input[str],
                 branch_to_branch_traffic_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RouteServer resource.
        :param pulumi.Input[str] public_ip_address_id: The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] branch_to_branch_traffic_enabled: Whether to enable route exchange between Azure Route Server and the gateway(s)
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Route Server. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "public_ip_address_id", public_ip_address_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "subnet_id", subnet_id)
        if branch_to_branch_traffic_enabled is not None:
            pulumi.set(__self__, "branch_to_branch_traffic_enabled", branch_to_branch_traffic_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> pulumi.Input[str]:
        """
        The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "public_ip_address_id")

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_ip_address_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input[str]:
        """
        The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input[str]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="branchToBranchTrafficEnabled")
    def branch_to_branch_traffic_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable route exchange between Azure Route Server and the gateway(s)
        """
        return pulumi.get(self, "branch_to_branch_traffic_enabled")

    @branch_to_branch_traffic_enabled.setter
    def branch_to_branch_traffic_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "branch_to_branch_traffic_enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Route Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _RouteServerState:
    def __init__(__self__, *,
                 branch_to_branch_traffic_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ip_address_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_state: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_router_asn: Optional[pulumi.Input[int]] = None,
                 virtual_router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering RouteServer resources.
        :param pulumi.Input[bool] branch_to_branch_traffic_enabled: Whether to enable route exchange between Azure Route Server and the gateway(s)
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Route Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] public_ip_address_id: The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        if branch_to_branch_traffic_enabled is not None:
            pulumi.set(__self__, "branch_to_branch_traffic_enabled", branch_to_branch_traffic_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_ip_address_id is not None:
            pulumi.set(__self__, "public_ip_address_id", public_ip_address_id)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if routing_state is not None:
            pulumi.set(__self__, "routing_state", routing_state)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_router_asn is not None:
            pulumi.set(__self__, "virtual_router_asn", virtual_router_asn)
        if virtual_router_ips is not None:
            pulumi.set(__self__, "virtual_router_ips", virtual_router_ips)

    @property
    @pulumi.getter(name="branchToBranchTrafficEnabled")
    def branch_to_branch_traffic_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable route exchange between Azure Route Server and the gateway(s)
        """
        return pulumi.get(self, "branch_to_branch_traffic_enabled")

    @branch_to_branch_traffic_enabled.setter
    def branch_to_branch_traffic_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "branch_to_branch_traffic_enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Route Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "public_ip_address_id")

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_address_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="routingState")
    def routing_state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "routing_state")

    @routing_state.setter
    def routing_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_state", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[str]]:
        """
        The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "virtual_router_asn")

    @virtual_router_asn.setter
    def virtual_router_asn(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "virtual_router_asn", value)

    @property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "virtual_router_ips")

    @virtual_router_ips.setter
    def virtual_router_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "virtual_router_ips", value)


class RouteServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch_to_branch_traffic_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ip_address_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an Azure Route Server

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            tags={
                "environment": "Production",
            })
        example_subnet = azure.network.Subnet("exampleSubnet",
            virtual_network_name=example_virtual_network.name,
            resource_group_name=example_resource_group.name,
            address_prefixes=["10.0.1.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            allocation_method="Static",
            sku="Standard")
        example_route_server = azure.network.RouteServer("exampleRouteServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku="Standard",
            public_ip_address_id=example_public_ip.id,
            subnet_id=example_subnet.id,
            branch_to_branch_traffic_enabled=True)
        ```

        ## Import

        Route Server can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/routeServer:RouteServer example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/virtualHubs/routeServer1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] branch_to_branch_traffic_enabled: Whether to enable route exchange between Azure Route Server and the gateway(s)
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Route Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] public_ip_address_id: The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure Route Server

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            tags={
                "environment": "Production",
            })
        example_subnet = azure.network.Subnet("exampleSubnet",
            virtual_network_name=example_virtual_network.name,
            resource_group_name=example_resource_group.name,
            address_prefixes=["10.0.1.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            allocation_method="Static",
            sku="Standard")
        example_route_server = azure.network.RouteServer("exampleRouteServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku="Standard",
            public_ip_address_id=example_public_ip.id,
            subnet_id=example_subnet.id,
            branch_to_branch_traffic_enabled=True)
        ```

        ## Import

        Route Server can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/routeServer:RouteServer example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/virtualHubs/routeServer1
        ```

        :param str resource_name: The name of the resource.
        :param RouteServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch_to_branch_traffic_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ip_address_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteServerArgs.__new__(RouteServerArgs)

            __props__.__dict__["branch_to_branch_traffic_enabled"] = branch_to_branch_traffic_enabled
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if public_ip_address_id is None and not opts.urn:
                raise TypeError("Missing required property 'public_ip_address_id'")
            __props__.__dict__["public_ip_address_id"] = public_ip_address_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["routing_state"] = None
            __props__.__dict__["virtual_router_asn"] = None
            __props__.__dict__["virtual_router_ips"] = None
        super(RouteServer, __self__).__init__(
            'azure:network/routeServer:RouteServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            branch_to_branch_traffic_enabled: Optional[pulumi.Input[bool]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_ip_address_id: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            routing_state: Optional[pulumi.Input[str]] = None,
            sku: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtual_router_asn: Optional[pulumi.Input[int]] = None,
            virtual_router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'RouteServer':
        """
        Get an existing RouteServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] branch_to_branch_traffic_enabled: Whether to enable route exchange between Azure Route Server and the gateway(s)
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Route Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] public_ip_address_id: The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RouteServerState.__new__(_RouteServerState)

        __props__.__dict__["branch_to_branch_traffic_enabled"] = branch_to_branch_traffic_enabled
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["public_ip_address_id"] = public_ip_address_id
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["routing_state"] = routing_state
        __props__.__dict__["sku"] = sku
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["virtual_router_asn"] = virtual_router_asn
        __props__.__dict__["virtual_router_ips"] = virtual_router_ips
        return RouteServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="branchToBranchTrafficEnabled")
    def branch_to_branch_traffic_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable route exchange between Azure Route Server and the gateway(s)
        """
        return pulumi.get(self, "branch_to_branch_traffic_enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the Route Server should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Route Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> pulumi.Output[str]:
        """
        The ID of the Public IP Address. This option is required since September 1st 2021. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "public_ip_address_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group where the Route Server should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="routingState")
    def routing_state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "routing_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[str]:
        """
        The SKU of the Route Server. The only possible value is `Standard`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the Subnet that the Route Server will reside. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> pulumi.Output[int]:
        return pulumi.get(self, "virtual_router_asn")

    @property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "virtual_router_ips")

