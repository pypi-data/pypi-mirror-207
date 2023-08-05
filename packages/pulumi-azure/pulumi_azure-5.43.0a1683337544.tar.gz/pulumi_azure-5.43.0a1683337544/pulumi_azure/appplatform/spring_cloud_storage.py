# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SpringCloudStorageArgs', 'SpringCloudStorage']

@pulumi.input_type
class SpringCloudStorageArgs:
    def __init__(__self__, *,
                 spring_cloud_service_id: pulumi.Input[str],
                 storage_account_key: pulumi.Input[str],
                 storage_account_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SpringCloudStorage resource.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] storage_account_key: The access key of the Azure Storage Account.
        :param pulumi.Input[str] storage_account_name: The account name of the Azure Storage Account.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        """
        pulumi.set(__self__, "spring_cloud_service_id", spring_cloud_service_id)
        pulumi.set(__self__, "storage_account_key", storage_account_key)
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="springCloudServiceId")
    def spring_cloud_service_id(self) -> pulumi.Input[str]:
        """
        The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        """
        return pulumi.get(self, "spring_cloud_service_id")

    @spring_cloud_service_id.setter
    def spring_cloud_service_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "spring_cloud_service_id", value)

    @property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> pulumi.Input[str]:
        """
        The access key of the Azure Storage Account.
        """
        return pulumi.get(self, "storage_account_key")

    @storage_account_key.setter
    def storage_account_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_key", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[str]:
        """
        The account name of the Azure Storage Account.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SpringCloudStorageState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
                 storage_account_key: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SpringCloudStorage resources.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] storage_account_key: The access key of the Azure Storage Account.
        :param pulumi.Input[str] storage_account_name: The account name of the Azure Storage Account.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if spring_cloud_service_id is not None:
            pulumi.set(__self__, "spring_cloud_service_id", spring_cloud_service_id)
        if storage_account_key is not None:
            pulumi.set(__self__, "storage_account_key", storage_account_key)
        if storage_account_name is not None:
            pulumi.set(__self__, "storage_account_name", storage_account_name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="springCloudServiceId")
    def spring_cloud_service_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        """
        return pulumi.get(self, "spring_cloud_service_id")

    @spring_cloud_service_id.setter
    def spring_cloud_service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_service_id", value)

    @property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[pulumi.Input[str]]:
        """
        The access key of the Azure Storage Account.
        """
        return pulumi.get(self, "storage_account_key")

    @storage_account_key.setter
    def storage_account_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_key", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The account name of the Azure Storage Account.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_name", value)


class SpringCloudStorage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
                 storage_account_key: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Spring Cloud Storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_spring_cloud_storage = azure.appplatform.SpringCloudStorage("exampleSpringCloudStorage",
            spring_cloud_service_id=example_spring_cloud_service.id,
            storage_account_name=example_account.name,
            storage_account_key=example_account.primary_access_key)
        ```

        ## Import

        Spring Cloud Storages can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudStorage:SpringCloudStorage example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resourceGroup1/providers/Microsoft.AppPlatform/spring/service1/storages/storage1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] storage_account_key: The access key of the Azure Storage Account.
        :param pulumi.Input[str] storage_account_name: The account name of the Azure Storage Account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpringCloudStorageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Spring Cloud Storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_spring_cloud_storage = azure.appplatform.SpringCloudStorage("exampleSpringCloudStorage",
            spring_cloud_service_id=example_spring_cloud_service.id,
            storage_account_name=example_account.name,
            storage_account_key=example_account.primary_access_key)
        ```

        ## Import

        Spring Cloud Storages can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudStorage:SpringCloudStorage example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resourceGroup1/providers/Microsoft.AppPlatform/spring/service1/storages/storage1
        ```

        :param str resource_name: The name of the resource.
        :param SpringCloudStorageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpringCloudStorageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
                 storage_account_key: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SpringCloudStorageArgs.__new__(SpringCloudStorageArgs)

            __props__.__dict__["name"] = name
            if spring_cloud_service_id is None and not opts.urn:
                raise TypeError("Missing required property 'spring_cloud_service_id'")
            __props__.__dict__["spring_cloud_service_id"] = spring_cloud_service_id
            if storage_account_key is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_key'")
            __props__.__dict__["storage_account_key"] = storage_account_key
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__.__dict__["storage_account_name"] = storage_account_name
        super(SpringCloudStorage, __self__).__init__(
            'azure:appplatform/springCloudStorage:SpringCloudStorage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            spring_cloud_service_id: Optional[pulumi.Input[str]] = None,
            storage_account_key: Optional[pulumi.Input[str]] = None,
            storage_account_name: Optional[pulumi.Input[str]] = None) -> 'SpringCloudStorage':
        """
        Get an existing SpringCloudStorage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] spring_cloud_service_id: The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        :param pulumi.Input[str] storage_account_key: The access key of the Azure Storage Account.
        :param pulumi.Input[str] storage_account_name: The account name of the Azure Storage Account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SpringCloudStorageState.__new__(_SpringCloudStorageState)

        __props__.__dict__["name"] = name
        __props__.__dict__["spring_cloud_service_id"] = spring_cloud_service_id
        __props__.__dict__["storage_account_key"] = storage_account_key
        __props__.__dict__["storage_account_name"] = storage_account_name
        return SpringCloudStorage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Spring Cloud Storage. Changing this forces a new Spring Cloud Storage to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="springCloudServiceId")
    def spring_cloud_service_id(self) -> pulumi.Output[str]:
        """
        The ID of the Spring Cloud Service where the Spring Cloud Storage should exist. Changing this forces a new Spring Cloud Storage to be created.
        """
        return pulumi.get(self, "spring_cloud_service_id")

    @property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> pulumi.Output[str]:
        """
        The access key of the Azure Storage Account.
        """
        return pulumi.get(self, "storage_account_key")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[str]:
        """
        The account name of the Azure Storage Account.
        """
        return pulumi.get(self, "storage_account_name")

