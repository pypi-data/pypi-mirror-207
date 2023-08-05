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

__all__ = [
    'GetShareResult',
    'AwaitableGetShareResult',
    'get_share',
    'get_share_output',
]

@pulumi.output_type
class GetShareResult:
    """
    A collection of values returned by getShare.
    """
    def __init__(__self__, acls=None, id=None, metadata=None, name=None, quota=None, resource_manager_id=None, storage_account_name=None):
        if acls and not isinstance(acls, list):
            raise TypeError("Expected argument 'acls' to be a list")
        pulumi.set(__self__, "acls", acls)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if quota and not isinstance(quota, int):
            raise TypeError("Expected argument 'quota' to be a int")
        pulumi.set(__self__, "quota", quota)
        if resource_manager_id and not isinstance(resource_manager_id, str):
            raise TypeError("Expected argument 'resource_manager_id' to be a str")
        pulumi.set(__self__, "resource_manager_id", resource_manager_id)
        if storage_account_name and not isinstance(storage_account_name, str):
            raise TypeError("Expected argument 'storage_account_name' to be a str")
        pulumi.set(__self__, "storage_account_name", storage_account_name)

    @property
    @pulumi.getter
    def acls(self) -> Optional[Sequence['outputs.GetShareAclResult']]:
        """
        One or more acl blocks as defined below.
        """
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, str]:
        """
        A map of custom file share metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def quota(self) -> int:
        """
        The quota of the File Share in GB.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter(name="resourceManagerId")
    def resource_manager_id(self) -> str:
        return pulumi.get(self, "resource_manager_id")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> str:
        return pulumi.get(self, "storage_account_name")


class AwaitableGetShareResult(GetShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShareResult(
            acls=self.acls,
            id=self.id,
            metadata=self.metadata,
            name=self.name,
            quota=self.quota,
            resource_manager_id=self.resource_manager_id,
            storage_account_name=self.storage_account_name)


def get_share(acls: Optional[Sequence[pulumi.InputType['GetShareAclArgs']]] = None,
              metadata: Optional[Mapping[str, str]] = None,
              name: Optional[str] = None,
              storage_account_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShareResult:
    """
    Use this data source to access information about an existing File Share.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.storage.get_share(name="existing",
        storage_account_name="existing")
    pulumi.export("id", example.id)
    ```


    :param Sequence[pulumi.InputType['GetShareAclArgs']] acls: One or more acl blocks as defined below.
    :param Mapping[str, str] metadata: A map of custom file share metadata.
    :param str name: The name of the share.
    :param str storage_account_name: The name of the storage account.
    """
    __args__ = dict()
    __args__['acls'] = acls
    __args__['metadata'] = metadata
    __args__['name'] = name
    __args__['storageAccountName'] = storage_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:storage/getShare:getShare', __args__, opts=opts, typ=GetShareResult).value

    return AwaitableGetShareResult(
        acls=__ret__.acls,
        id=__ret__.id,
        metadata=__ret__.metadata,
        name=__ret__.name,
        quota=__ret__.quota,
        resource_manager_id=__ret__.resource_manager_id,
        storage_account_name=__ret__.storage_account_name)


@_utilities.lift_output_func(get_share)
def get_share_output(acls: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetShareAclArgs']]]]] = None,
                     metadata: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                     name: Optional[pulumi.Input[str]] = None,
                     storage_account_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetShareResult]:
    """
    Use this data source to access information about an existing File Share.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.storage.get_share(name="existing",
        storage_account_name="existing")
    pulumi.export("id", example.id)
    ```


    :param Sequence[pulumi.InputType['GetShareAclArgs']] acls: One or more acl blocks as defined below.
    :param Mapping[str, str] metadata: A map of custom file share metadata.
    :param str name: The name of the share.
    :param str storage_account_name: The name of the storage account.
    """
    ...
