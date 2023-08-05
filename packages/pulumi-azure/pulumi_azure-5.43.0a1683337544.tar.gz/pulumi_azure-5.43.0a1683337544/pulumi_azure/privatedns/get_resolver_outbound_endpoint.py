# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetResolverOutboundEndpointResult',
    'AwaitableGetResolverOutboundEndpointResult',
    'get_resolver_outbound_endpoint',
    'get_resolver_outbound_endpoint_output',
]

@pulumi.output_type
class GetResolverOutboundEndpointResult:
    """
    A collection of values returned by getResolverOutboundEndpoint.
    """
    def __init__(__self__, id=None, location=None, name=None, private_dns_resolver_id=None, subnet_id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_dns_resolver_id and not isinstance(private_dns_resolver_id, str):
            raise TypeError("Expected argument 'private_dns_resolver_id' to be a str")
        pulumi.set(__self__, "private_dns_resolver_id", private_dns_resolver_id)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the Private DNS Resolver Outbound Endpoint exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateDnsResolverId")
    def private_dns_resolver_id(self) -> str:
        return pulumi.get(self, "private_dns_resolver_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the Subnet that is linked to the Private DNS Resolver Outbound Endpoint.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The tags assigned to the Private DNS Resolver Outbound Endpoint.
        """
        return pulumi.get(self, "tags")


class AwaitableGetResolverOutboundEndpointResult(GetResolverOutboundEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResolverOutboundEndpointResult(
            id=self.id,
            location=self.location,
            name=self.name,
            private_dns_resolver_id=self.private_dns_resolver_id,
            subnet_id=self.subnet_id,
            tags=self.tags)


def get_resolver_outbound_endpoint(name: Optional[str] = None,
                                   private_dns_resolver_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResolverOutboundEndpointResult:
    """
    Gets information about an existing Private DNS Resolver Outbound Endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.privatedns.get_resolver_outbound_endpoint(name="example-endpoint",
        private_dns_resolver_id="example-private-dns-resolver-id")
    ```


    :param str name: Name of the Private DNS Resolver Outbound Endpoint.
    :param str private_dns_resolver_id: ID of the Private DNS Resolver Outbound Endpoint.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['privateDnsResolverId'] = private_dns_resolver_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:privatedns/getResolverOutboundEndpoint:getResolverOutboundEndpoint', __args__, opts=opts, typ=GetResolverOutboundEndpointResult).value

    return AwaitableGetResolverOutboundEndpointResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        private_dns_resolver_id=__ret__.private_dns_resolver_id,
        subnet_id=__ret__.subnet_id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_resolver_outbound_endpoint)
def get_resolver_outbound_endpoint_output(name: Optional[pulumi.Input[str]] = None,
                                          private_dns_resolver_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResolverOutboundEndpointResult]:
    """
    Gets information about an existing Private DNS Resolver Outbound Endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.privatedns.get_resolver_outbound_endpoint(name="example-endpoint",
        private_dns_resolver_id="example-private-dns-resolver-id")
    ```


    :param str name: Name of the Private DNS Resolver Outbound Endpoint.
    :param str private_dns_resolver_id: ID of the Private DNS Resolver Outbound Endpoint.
    """
    ...
