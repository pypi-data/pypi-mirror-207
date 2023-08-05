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
    'AccountIdentity',
    'DatasetBlobStorageStorageAccount',
    'ShareSnapshotSchedule',
    'GetAccountIdentityResult',
    'GetDatasetBlobStorageStorageAccountResult',
    'GetShareSnapshotScheduleResult',
]

@pulumi.output_type
class AccountIdentity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccountIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccountIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccountIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        :param str type: Specifies the type of Managed Service Identity that should be configured on this Data Share Account. The only possible value is `SystemAssigned`. Changing this forces a new resource to be created.
        :param str principal_id: The Principal ID for the Service Principal associated with the Identity of this Data Share Account.
        :param str tenant_id: The Tenant ID for the Service Principal associated with the Identity of this Data Share Account.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the type of Managed Service Identity that should be configured on this Data Share Account. The only possible value is `SystemAssigned`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The Principal ID for the Service Principal associated with the Identity of this Data Share Account.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant ID for the Service Principal associated with the Identity of this Data Share Account.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class DatasetBlobStorageStorageAccount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceGroupName":
            suggest = "resource_group_name"
        elif key == "subscriptionId":
            suggest = "subscription_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DatasetBlobStorageStorageAccount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DatasetBlobStorageStorageAccount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DatasetBlobStorageStorageAccount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 resource_group_name: str,
                 subscription_id: str):
        """
        :param str name: The name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.
        :param str resource_group_name: The resource group name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.
        :param str subscription_id: The subscription id of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        """
        The resource group name of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        The subscription id of the storage account to be shared with the receiver. Changing this forces a new Data Share Blob Storage Dataset to be created.
        """
        return pulumi.get(self, "subscription_id")


@pulumi.output_type
class ShareSnapshotSchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ShareSnapshotSchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ShareSnapshotSchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ShareSnapshotSchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 recurrence: str,
                 start_time: str):
        """
        :param str name: The name of the snapshot schedule.
        :param str recurrence: The interval of the synchronization with the source data. Possible values are `Hour` and `Day`.
        :param str start_time: The synchronization with the source data's start time.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "recurrence", recurrence)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the snapshot schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def recurrence(self) -> str:
        """
        The interval of the synchronization with the source data. Possible values are `Hour` and `Day`.
        """
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The synchronization with the source data's start time.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class GetAccountIdentityResult(dict):
    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str):
        """
        :param str principal_id: The Principal ID associated with this Managed Service Identity.
        :param str tenant_id: The Tenant ID associated with this Managed Service Identity.
        :param str type: The identity type of this Managed Service Identity.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The Principal ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Tenant ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type of this Managed Service Identity.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetDatasetBlobStorageStorageAccountResult(dict):
    def __init__(__self__, *,
                 name: str,
                 resource_group_name: str,
                 subscription_id: str):
        """
        :param str name: The name of this Data Share Blob Storage Dataset.
        :param str resource_group_name: The resource group name of the storage account to be shared with the receiver.
        :param str subscription_id: The subscription id of the storage account to be shared with the receiver.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this Data Share Blob Storage Dataset.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        """
        The resource group name of the storage account to be shared with the receiver.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        The subscription id of the storage account to be shared with the receiver.
        """
        return pulumi.get(self, "subscription_id")


@pulumi.output_type
class GetShareSnapshotScheduleResult(dict):
    def __init__(__self__, *,
                 name: str,
                 recurrence: str,
                 start_time: str):
        """
        :param str name: The name of this Data Share.
        :param str recurrence: The interval of the synchronization with the source data.
        :param str start_time: The synchronization with the source data's start time.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "recurrence", recurrence)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this Data Share.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def recurrence(self) -> str:
        """
        The interval of the synchronization with the source data.
        """
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The synchronization with the source data's start time.
        """
        return pulumi.get(self, "start_time")


