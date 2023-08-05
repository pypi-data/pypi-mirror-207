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

__all__ = [
    'GetVirtualHubRouteTableResult',
    'AwaitableGetVirtualHubRouteTableResult',
    'get_virtual_hub_route_table',
    'get_virtual_hub_route_table_output',
]

@pulumi.output_type
class GetVirtualHubRouteTableResult:
    """
    A collection of values returned by getVirtualHubRouteTable.
    """
    def __init__(__self__, id=None, labels=None, name=None, resource_group_name=None, routes=None, virtual_hub_id=None, virtual_hub_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if routes and not isinstance(routes, list):
            raise TypeError("Expected argument 'routes' to be a list")
        pulumi.set(__self__, "routes", routes)
        if virtual_hub_id and not isinstance(virtual_hub_id, str):
            raise TypeError("Expected argument 'virtual_hub_id' to be a str")
        pulumi.set(__self__, "virtual_hub_id", virtual_hub_id)
        if virtual_hub_name and not isinstance(virtual_hub_name, str):
            raise TypeError("Expected argument 'virtual_hub_name' to be a str")
        pulumi.set(__self__, "virtual_hub_name", virtual_hub_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Sequence[str]:
        """
        List of labels associated with this route table.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name which is used for this route.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def routes(self) -> Sequence['outputs.GetVirtualHubRouteTableRouteResult']:
        """
        A `route` block as defined below.
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> str:
        """
        The ID of the Virtual Hub within which this route table is created
        """
        return pulumi.get(self, "virtual_hub_id")

    @property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> str:
        return pulumi.get(self, "virtual_hub_name")


class AwaitableGetVirtualHubRouteTableResult(GetVirtualHubRouteTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualHubRouteTableResult(
            id=self.id,
            labels=self.labels,
            name=self.name,
            resource_group_name=self.resource_group_name,
            routes=self.routes,
            virtual_hub_id=self.virtual_hub_id,
            virtual_hub_name=self.virtual_hub_name)


def get_virtual_hub_route_table(name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                virtual_hub_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualHubRouteTableResult:
    """
    Uses this data source to access information about an existing Virtual Hub Route Table.

    ## Virtual Hub Route Table Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_virtual_hub_route_table(name="example-hub-route-table",
        resource_group_name="example-resources",
        virtual_hub_name="example-hub-name")
    pulumi.export("virtualHubRouteTableId", example.id)
    ```


    :param str name: The name of the Virtual Hub Route Table.
    :param str resource_group_name: The Name of the Resource Group where the Virtual Hub Route Table exists.
    :param str virtual_hub_name: The name which should be used for Virtual Hub Route Table.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualHubName'] = virtual_hub_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:network/getVirtualHubRouteTable:getVirtualHubRouteTable', __args__, opts=opts, typ=GetVirtualHubRouteTableResult).value

    return AwaitableGetVirtualHubRouteTableResult(
        id=__ret__.id,
        labels=__ret__.labels,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        routes=__ret__.routes,
        virtual_hub_id=__ret__.virtual_hub_id,
        virtual_hub_name=__ret__.virtual_hub_name)


@_utilities.lift_output_func(get_virtual_hub_route_table)
def get_virtual_hub_route_table_output(name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       virtual_hub_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualHubRouteTableResult]:
    """
    Uses this data source to access information about an existing Virtual Hub Route Table.

    ## Virtual Hub Route Table Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_virtual_hub_route_table(name="example-hub-route-table",
        resource_group_name="example-resources",
        virtual_hub_name="example-hub-name")
    pulumi.export("virtualHubRouteTableId", example.id)
    ```


    :param str name: The name of the Virtual Hub Route Table.
    :param str resource_group_name: The Name of the Resource Group where the Virtual Hub Route Table exists.
    :param str virtual_hub_name: The name which should be used for Virtual Hub Route Table.
    """
    ...
