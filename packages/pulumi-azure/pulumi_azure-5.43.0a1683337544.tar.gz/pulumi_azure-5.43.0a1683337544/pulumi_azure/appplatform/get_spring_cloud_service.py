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
    'GetSpringCloudServiceResult',
    'AwaitableGetSpringCloudServiceResult',
    'get_spring_cloud_service',
    'get_spring_cloud_service_output',
]

@pulumi.output_type
class GetSpringCloudServiceResult:
    """
    A collection of values returned by getSpringCloudService.
    """
    def __init__(__self__, config_server_git_settings=None, id=None, location=None, name=None, outbound_public_ip_addresses=None, required_network_traffic_rules=None, resource_group_name=None, tags=None):
        if config_server_git_settings and not isinstance(config_server_git_settings, list):
            raise TypeError("Expected argument 'config_server_git_settings' to be a list")
        pulumi.set(__self__, "config_server_git_settings", config_server_git_settings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outbound_public_ip_addresses and not isinstance(outbound_public_ip_addresses, list):
            raise TypeError("Expected argument 'outbound_public_ip_addresses' to be a list")
        pulumi.set(__self__, "outbound_public_ip_addresses", outbound_public_ip_addresses)
        if required_network_traffic_rules and not isinstance(required_network_traffic_rules, list):
            raise TypeError("Expected argument 'required_network_traffic_rules' to be a list")
        pulumi.set(__self__, "required_network_traffic_rules", required_network_traffic_rules)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="configServerGitSettings")
    def config_server_git_settings(self) -> Sequence['outputs.GetSpringCloudServiceConfigServerGitSettingResult']:
        """
        A `config_server_git_setting` block as defined below.
        """
        return pulumi.get(self, "config_server_git_settings")

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
        The location of Spring Cloud Service.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name to identify on the Git repository.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundPublicIpAddresses")
    def outbound_public_ip_addresses(self) -> Sequence[str]:
        """
        A list of the outbound Public IP Addresses used by this Spring Cloud Service.
        """
        return pulumi.get(self, "outbound_public_ip_addresses")

    @property
    @pulumi.getter(name="requiredNetworkTrafficRules")
    def required_network_traffic_rules(self) -> Sequence['outputs.GetSpringCloudServiceRequiredNetworkTrafficRuleResult']:
        """
        A list of `required_network_traffic_rules` blocks as defined below.
        """
        return pulumi.get(self, "required_network_traffic_rules")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to Spring Cloud Service.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSpringCloudServiceResult(GetSpringCloudServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpringCloudServiceResult(
            config_server_git_settings=self.config_server_git_settings,
            id=self.id,
            location=self.location,
            name=self.name,
            outbound_public_ip_addresses=self.outbound_public_ip_addresses,
            required_network_traffic_rules=self.required_network_traffic_rules,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def get_spring_cloud_service(name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpringCloudServiceResult:
    """
    Use this data source to access information about an existing Spring Cloud Service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appplatform.get_spring_cloud_service(name=azurerm_spring_cloud_service["example"]["name"],
        resource_group_name=azurerm_spring_cloud_service["example"]["resource_group_name"])
    pulumi.export("springCloudServiceId", example.id)
    ```


    :param str name: Specifies The name of the Spring Cloud Service resource.
    :param str resource_group_name: Specifies the name of the Resource Group where the Spring Cloud Service exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:appplatform/getSpringCloudService:getSpringCloudService', __args__, opts=opts, typ=GetSpringCloudServiceResult).value

    return AwaitableGetSpringCloudServiceResult(
        config_server_git_settings=__ret__.config_server_git_settings,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        outbound_public_ip_addresses=__ret__.outbound_public_ip_addresses,
        required_network_traffic_rules=__ret__.required_network_traffic_rules,
        resource_group_name=__ret__.resource_group_name,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_spring_cloud_service)
def get_spring_cloud_service_output(name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSpringCloudServiceResult]:
    """
    Use this data source to access information about an existing Spring Cloud Service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appplatform.get_spring_cloud_service(name=azurerm_spring_cloud_service["example"]["name"],
        resource_group_name=azurerm_spring_cloud_service["example"]["resource_group_name"])
    pulumi.export("springCloudServiceId", example.id)
    ```


    :param str name: Specifies The name of the Spring Cloud Service resource.
    :param str resource_group_name: Specifies the name of the Resource Group where the Spring Cloud Service exists.
    """
    ...
