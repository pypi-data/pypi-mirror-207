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
    'GetFunctionAppHostKeysResult',
    'AwaitableGetFunctionAppHostKeysResult',
    'get_function_app_host_keys',
    'get_function_app_host_keys_output',
]

@pulumi.output_type
class GetFunctionAppHostKeysResult:
    """
    A collection of values returned by getFunctionAppHostKeys.
    """
    def __init__(__self__, blobs_extension_key=None, default_function_key=None, durabletask_extension_key=None, event_grid_extension_config_key=None, id=None, name=None, primary_key=None, resource_group_name=None, signalr_extension_key=None, webpubsub_extension_key=None):
        if blobs_extension_key and not isinstance(blobs_extension_key, str):
            raise TypeError("Expected argument 'blobs_extension_key' to be a str")
        pulumi.set(__self__, "blobs_extension_key", blobs_extension_key)
        if default_function_key and not isinstance(default_function_key, str):
            raise TypeError("Expected argument 'default_function_key' to be a str")
        pulumi.set(__self__, "default_function_key", default_function_key)
        if durabletask_extension_key and not isinstance(durabletask_extension_key, str):
            raise TypeError("Expected argument 'durabletask_extension_key' to be a str")
        pulumi.set(__self__, "durabletask_extension_key", durabletask_extension_key)
        if event_grid_extension_config_key and not isinstance(event_grid_extension_config_key, str):
            raise TypeError("Expected argument 'event_grid_extension_config_key' to be a str")
        pulumi.set(__self__, "event_grid_extension_config_key", event_grid_extension_config_key)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if signalr_extension_key and not isinstance(signalr_extension_key, str):
            raise TypeError("Expected argument 'signalr_extension_key' to be a str")
        pulumi.set(__self__, "signalr_extension_key", signalr_extension_key)
        if webpubsub_extension_key and not isinstance(webpubsub_extension_key, str):
            raise TypeError("Expected argument 'webpubsub_extension_key' to be a str")
        pulumi.set(__self__, "webpubsub_extension_key", webpubsub_extension_key)

    @property
    @pulumi.getter(name="blobsExtensionKey")
    def blobs_extension_key(self) -> str:
        """
        Function App resource's Blobs Extension system key.
        """
        return pulumi.get(self, "blobs_extension_key")

    @property
    @pulumi.getter(name="defaultFunctionKey")
    def default_function_key(self) -> str:
        """
        Function App resource's default function key.
        """
        return pulumi.get(self, "default_function_key")

    @property
    @pulumi.getter(name="durabletaskExtensionKey")
    def durabletask_extension_key(self) -> str:
        """
        Function App resource's Durable Task Extension system key.
        """
        return pulumi.get(self, "durabletask_extension_key")

    @property
    @pulumi.getter(name="eventGridExtensionConfigKey")
    def event_grid_extension_config_key(self) -> str:
        """
        Function App resource's Event Grid Extension Config system key.
        """
        return pulumi.get(self, "event_grid_extension_config_key")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        Function App resource's secret key
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="signalrExtensionKey")
    def signalr_extension_key(self) -> str:
        """
        Function App resource's SignalR Extension system key.
        """
        return pulumi.get(self, "signalr_extension_key")

    @property
    @pulumi.getter(name="webpubsubExtensionKey")
    def webpubsub_extension_key(self) -> str:
        """
        Function App resource's Web PubSub Extension system key.
        """
        return pulumi.get(self, "webpubsub_extension_key")


class AwaitableGetFunctionAppHostKeysResult(GetFunctionAppHostKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionAppHostKeysResult(
            blobs_extension_key=self.blobs_extension_key,
            default_function_key=self.default_function_key,
            durabletask_extension_key=self.durabletask_extension_key,
            event_grid_extension_config_key=self.event_grid_extension_config_key,
            id=self.id,
            name=self.name,
            primary_key=self.primary_key,
            resource_group_name=self.resource_group_name,
            signalr_extension_key=self.signalr_extension_key,
            webpubsub_extension_key=self.webpubsub_extension_key)


def get_function_app_host_keys(name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionAppHostKeysResult:
    """
    Use this data source to fetch the Host Keys of an existing Function App

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_function_app_host_keys(name="example-function",
        resource_group_name=azurerm_resource_group["example"]["name"])
    ```


    :param str name: The name of the Function App.
    :param str resource_group_name: The name of the Resource Group where the Function App exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:appservice/getFunctionAppHostKeys:getFunctionAppHostKeys', __args__, opts=opts, typ=GetFunctionAppHostKeysResult).value

    return AwaitableGetFunctionAppHostKeysResult(
        blobs_extension_key=__ret__.blobs_extension_key,
        default_function_key=__ret__.default_function_key,
        durabletask_extension_key=__ret__.durabletask_extension_key,
        event_grid_extension_config_key=__ret__.event_grid_extension_config_key,
        id=__ret__.id,
        name=__ret__.name,
        primary_key=__ret__.primary_key,
        resource_group_name=__ret__.resource_group_name,
        signalr_extension_key=__ret__.signalr_extension_key,
        webpubsub_extension_key=__ret__.webpubsub_extension_key)


@_utilities.lift_output_func(get_function_app_host_keys)
def get_function_app_host_keys_output(name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionAppHostKeysResult]:
    """
    Use this data source to fetch the Host Keys of an existing Function App

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_function_app_host_keys(name="example-function",
        resource_group_name=azurerm_resource_group["example"]["name"])
    ```


    :param str name: The name of the Function App.
    :param str resource_group_name: The name of the Resource Group where the Function App exists.
    """
    ...
