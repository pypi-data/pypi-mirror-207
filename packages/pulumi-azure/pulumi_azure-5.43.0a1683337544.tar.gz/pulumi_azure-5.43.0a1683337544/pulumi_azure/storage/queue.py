# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['QueueArgs', 'Queue']

@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *,
                 storage_account_name: pulumi.Input[str],
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Queue resource.
        :param pulumi.Input[str] storage_account_name: Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A mapping of MetaData which should be assigned to this Storage Queue.
        :param pulumi.Input[str] name: The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[str]:
        """
        Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of MetaData which should be assigned to this Storage Queue.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _QueueState:
    def __init__(__self__, *,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_manager_id: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Queue resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A mapping of MetaData which should be assigned to this Storage Queue.
        :param pulumi.Input[str] name: The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_manager_id: The Resource Manager ID of this Storage Queue.
        :param pulumi.Input[str] storage_account_name: Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        """
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_manager_id is not None:
            pulumi.set(__self__, "resource_manager_id", resource_manager_id)
        if storage_account_name is not None:
            pulumi.set(__self__, "storage_account_name", storage_account_name)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of MetaData which should be assigned to this Storage Queue.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceManagerId")
    def resource_manager_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Resource Manager ID of this Storage Queue.
        """
        return pulumi.get(self, "resource_manager_id")

    @resource_manager_id.setter
    def resource_manager_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_manager_id", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_name", value)


class Queue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Queue within an Azure Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_queue = azure.storage.Queue("exampleQueue", storage_account_name=example_account.name)
        ```

        ## Import

        Storage Queue's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/queue:Queue queue1 https://example.queue.core.windows.net/queue1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A mapping of MetaData which should be assigned to this Storage Queue.
        :param pulumi.Input[str] name: The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_account_name: Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Queue within an Azure Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_queue = azure.storage.Queue("exampleQueue", storage_account_name=example_account.name)
        ```

        ## Import

        Storage Queue's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/queue:Queue queue1 https://example.queue.core.windows.net/queue1
        ```

        :param str resource_name: The name of the resource.
        :param QueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QueueArgs.__new__(QueueArgs)

            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__.__dict__["storage_account_name"] = storage_account_name
            __props__.__dict__["resource_manager_id"] = None
        super(Queue, __self__).__init__(
            'azure:storage/queue:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_manager_id: Optional[pulumi.Input[str]] = None,
            storage_account_name: Optional[pulumi.Input[str]] = None) -> 'Queue':
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A mapping of MetaData which should be assigned to this Storage Queue.
        :param pulumi.Input[str] name: The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_manager_id: The Resource Manager ID of this Storage Queue.
        :param pulumi.Input[str] storage_account_name: Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QueueState.__new__(_QueueState)

        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_manager_id"] = resource_manager_id
        __props__.__dict__["storage_account_name"] = storage_account_name
        return Queue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of MetaData which should be assigned to this Storage Queue.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceManagerId")
    def resource_manager_id(self) -> pulumi.Output[str]:
        """
        The Resource Manager ID of this Storage Queue.
        """
        return pulumi.get(self, "resource_manager_id")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[str]:
        """
        Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_name")

