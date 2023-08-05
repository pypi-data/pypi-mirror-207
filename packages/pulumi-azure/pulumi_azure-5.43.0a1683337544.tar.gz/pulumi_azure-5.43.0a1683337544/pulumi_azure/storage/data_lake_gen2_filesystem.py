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

__all__ = ['DataLakeGen2FilesystemArgs', 'DataLakeGen2Filesystem']

@pulumi.input_type
class DataLakeGen2FilesystemArgs:
    def __init__(__self__, *,
                 storage_account_id: pulumi.Input[str],
                 aces: Optional[pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DataLakeGen2Filesystem resource.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]] aces: One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        :param pulumi.Input[str] group: Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[str] name: The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] owner: Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        """
        pulumi.set(__self__, "storage_account_id", storage_account_id)
        if aces is not None:
            pulumi.set(__self__, "aces", aces)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter
    def aces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]]]:
        """
        One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        """
        return pulumi.get(self, "aces")

    @aces.setter
    def aces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]]]):
        pulumi.set(self, "aces", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)


@pulumi.input_type
class _DataLakeGen2FilesystemState:
    def __init__(__self__, *,
                 aces: Optional[pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DataLakeGen2Filesystem resources.
        :param pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]] aces: One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        :param pulumi.Input[str] group: Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[str] name: The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] owner: Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        if aces is not None:
            pulumi.set(__self__, "aces", aces)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)

    @property
    @pulumi.getter
    def aces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]]]:
        """
        One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        """
        return pulumi.get(self, "aces")

    @aces.setter
    def aces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLakeGen2FilesystemAceArgs']]]]):
        pulumi.set(self, "aces", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)


class DataLakeGen2Filesystem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2FilesystemAceArgs']]]]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Data Lake Gen2 File System within an Azure Storage Account.

        > **NOTE:** This resource requires some `Storage` specific roles which are not granted by default. Some of the built-ins roles that can be attributed are [`Storage Account Contributor`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-account-contributor), [`Storage Blob Data Owner`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-owner), [`Storage Blob Data Contributor`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor), [`Storage Blob Data Reader`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-reader).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            account_kind="StorageV2",
            is_hns_enabled=True)
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem",
            storage_account_id=example_account.id,
            properties={
                "hello": "aGVsbG8=",
            })
        ```

        ## Import

        Data Lake Gen2 File System's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/dataLakeGen2Filesystem:DataLakeGen2Filesystem queue1 https://account1.dfs.core.windows.net/fileSystem1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2FilesystemAceArgs']]]] aces: One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        :param pulumi.Input[str] group: Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[str] name: The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] owner: Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataLakeGen2FilesystemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Data Lake Gen2 File System within an Azure Storage Account.

        > **NOTE:** This resource requires some `Storage` specific roles which are not granted by default. Some of the built-ins roles that can be attributed are [`Storage Account Contributor`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-account-contributor), [`Storage Blob Data Owner`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-owner), [`Storage Blob Data Contributor`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor), [`Storage Blob Data Reader`](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-reader).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            account_kind="StorageV2",
            is_hns_enabled=True)
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem",
            storage_account_id=example_account.id,
            properties={
                "hello": "aGVsbG8=",
            })
        ```

        ## Import

        Data Lake Gen2 File System's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/dataLakeGen2Filesystem:DataLakeGen2Filesystem queue1 https://account1.dfs.core.windows.net/fileSystem1
        ```

        :param str resource_name: The name of the resource.
        :param DataLakeGen2FilesystemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataLakeGen2FilesystemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2FilesystemAceArgs']]]]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataLakeGen2FilesystemArgs.__new__(DataLakeGen2FilesystemArgs)

            __props__.__dict__["aces"] = aces
            __props__.__dict__["group"] = group
            __props__.__dict__["name"] = name
            __props__.__dict__["owner"] = owner
            __props__.__dict__["properties"] = properties
            if storage_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__.__dict__["storage_account_id"] = storage_account_id
        super(DataLakeGen2Filesystem, __self__).__init__(
            'azure:storage/dataLakeGen2Filesystem:DataLakeGen2Filesystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2FilesystemAceArgs']]]]] = None,
            group: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            storage_account_id: Optional[pulumi.Input[str]] = None) -> 'DataLakeGen2Filesystem':
        """
        Get an existing DataLakeGen2Filesystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2FilesystemAceArgs']]]] aces: One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        :param pulumi.Input[str] group: Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[str] name: The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] owner: Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataLakeGen2FilesystemState.__new__(_DataLakeGen2FilesystemState)

        __props__.__dict__["aces"] = aces
        __props__.__dict__["group"] = group
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["properties"] = properties
        __props__.__dict__["storage_account_id"] = storage_account_id
        return DataLakeGen2Filesystem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aces(self) -> pulumi.Output[Sequence['outputs.DataLakeGen2FilesystemAce']]:
        """
        One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        """
        return pulumi.get(self, "aces")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[str]:
        """
        Specifies the Object ID of the Azure Active Directory Group to make the owning group of the root path (i.e. `/`). Possible values also include `$superuser`.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Specifies the Object ID of the Azure Active Directory User to make the owning user of the root path (i.e. `/`). Possible values also include `$superuser`.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

