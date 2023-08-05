# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkspaceExtendedAuditingPolicyArgs', 'WorkspaceExtendedAuditingPolicy']

@pulumi.input_type
class WorkspaceExtendedAuditingPolicyArgs:
    def __init__(__self__, *,
                 synapse_workspace_id: pulumi.Input[str],
                 log_monitoring_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key_is_secondary: Optional[pulumi.Input[bool]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceExtendedAuditingPolicy resource.
        :param pulumi.Input[str] synapse_workspace_id: The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] log_monitoring_enabled: Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        :param pulumi.Input[int] retention_in_days: The number of days to retain logs for in the storage account. Defaults to `0`.
        :param pulumi.Input[str] storage_account_access_key: The access key to use for the auditing storage account.
        :param pulumi.Input[bool] storage_account_access_key_is_secondary: Is `storage_account_access_key` value the storage's secondary key?
        :param pulumi.Input[str] storage_endpoint: The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        """
        pulumi.set(__self__, "synapse_workspace_id", synapse_workspace_id)
        if log_monitoring_enabled is not None:
            pulumi.set(__self__, "log_monitoring_enabled", log_monitoring_enabled)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if storage_account_access_key is not None:
            pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_account_access_key_is_secondary is not None:
            pulumi.set(__self__, "storage_account_access_key_is_secondary", storage_account_access_key_is_secondary)
        if storage_endpoint is not None:
            pulumi.set(__self__, "storage_endpoint", storage_endpoint)

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "synapse_workspace_id")

    @synapse_workspace_id.setter
    def synapse_workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "synapse_workspace_id", value)

    @property
    @pulumi.getter(name="logMonitoringEnabled")
    def log_monitoring_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        """
        return pulumi.get(self, "log_monitoring_enabled")

    @log_monitoring_enabled.setter
    def log_monitoring_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_monitoring_enabled", value)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days to retain logs for in the storage account. Defaults to `0`.
        """
        return pulumi.get(self, "retention_in_days")

    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_days", value)

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The access key to use for the auditing storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_access_key", value)

    @property
    @pulumi.getter(name="storageAccountAccessKeyIsSecondary")
    def storage_account_access_key_is_secondary(self) -> Optional[pulumi.Input[bool]]:
        """
        Is `storage_account_access_key` value the storage's secondary key?
        """
        return pulumi.get(self, "storage_account_access_key_is_secondary")

    @storage_account_access_key_is_secondary.setter
    def storage_account_access_key_is_secondary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "storage_account_access_key_is_secondary", value)

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_endpoint", value)


@pulumi.input_type
class _WorkspaceExtendedAuditingPolicyState:
    def __init__(__self__, *,
                 log_monitoring_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key_is_secondary: Optional[pulumi.Input[bool]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceExtendedAuditingPolicy resources.
        :param pulumi.Input[bool] log_monitoring_enabled: Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        :param pulumi.Input[int] retention_in_days: The number of days to retain logs for in the storage account. Defaults to `0`.
        :param pulumi.Input[str] storage_account_access_key: The access key to use for the auditing storage account.
        :param pulumi.Input[bool] storage_account_access_key_is_secondary: Is `storage_account_access_key` value the storage's secondary key?
        :param pulumi.Input[str] storage_endpoint: The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        :param pulumi.Input[str] synapse_workspace_id: The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        """
        if log_monitoring_enabled is not None:
            pulumi.set(__self__, "log_monitoring_enabled", log_monitoring_enabled)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if storage_account_access_key is not None:
            pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_account_access_key_is_secondary is not None:
            pulumi.set(__self__, "storage_account_access_key_is_secondary", storage_account_access_key_is_secondary)
        if storage_endpoint is not None:
            pulumi.set(__self__, "storage_endpoint", storage_endpoint)
        if synapse_workspace_id is not None:
            pulumi.set(__self__, "synapse_workspace_id", synapse_workspace_id)

    @property
    @pulumi.getter(name="logMonitoringEnabled")
    def log_monitoring_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        """
        return pulumi.get(self, "log_monitoring_enabled")

    @log_monitoring_enabled.setter
    def log_monitoring_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_monitoring_enabled", value)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days to retain logs for in the storage account. Defaults to `0`.
        """
        return pulumi.get(self, "retention_in_days")

    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_days", value)

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The access key to use for the auditing storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_access_key", value)

    @property
    @pulumi.getter(name="storageAccountAccessKeyIsSecondary")
    def storage_account_access_key_is_secondary(self) -> Optional[pulumi.Input[bool]]:
        """
        Is `storage_account_access_key` value the storage's secondary key?
        """
        return pulumi.get(self, "storage_account_access_key_is_secondary")

    @storage_account_access_key_is_secondary.setter
    def storage_account_access_key_is_secondary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "storage_account_access_key_is_secondary", value)

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_endpoint", value)

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "synapse_workspace_id")

    @synapse_workspace_id.setter
    def synapse_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "synapse_workspace_id", value)


class WorkspaceExtendedAuditingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_monitoring_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key_is_secondary: Optional[pulumi.Input[bool]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Synapse Workspace Extended Auditing Policy.

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
            account_kind="BlobStorage")
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            identity=azure.synapse.WorkspaceIdentityArgs(
                type="SystemAssigned",
            ))
        audit_logs = azure.storage.Account("auditLogs",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_workspace_extended_auditing_policy = azure.synapse.WorkspaceExtendedAuditingPolicy("exampleWorkspaceExtendedAuditingPolicy",
            synapse_workspace_id=example_workspace.id,
            storage_endpoint=audit_logs.primary_blob_endpoint,
            storage_account_access_key=audit_logs.primary_access_key,
            storage_account_access_key_is_secondary=False,
            retention_in_days=6)
        ```

        ## Import

        Synapse Workspace Extended Auditing Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/workspaceExtendedAuditingPolicy:WorkspaceExtendedAuditingPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Synapse/workspaces/workspace1/extendedAuditingSettings/default
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] log_monitoring_enabled: Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        :param pulumi.Input[int] retention_in_days: The number of days to retain logs for in the storage account. Defaults to `0`.
        :param pulumi.Input[str] storage_account_access_key: The access key to use for the auditing storage account.
        :param pulumi.Input[bool] storage_account_access_key_is_secondary: Is `storage_account_access_key` value the storage's secondary key?
        :param pulumi.Input[str] storage_endpoint: The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        :param pulumi.Input[str] synapse_workspace_id: The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceExtendedAuditingPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Synapse Workspace Extended Auditing Policy.

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
            account_kind="BlobStorage")
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            identity=azure.synapse.WorkspaceIdentityArgs(
                type="SystemAssigned",
            ))
        audit_logs = azure.storage.Account("auditLogs",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_workspace_extended_auditing_policy = azure.synapse.WorkspaceExtendedAuditingPolicy("exampleWorkspaceExtendedAuditingPolicy",
            synapse_workspace_id=example_workspace.id,
            storage_endpoint=audit_logs.primary_blob_endpoint,
            storage_account_access_key=audit_logs.primary_access_key,
            storage_account_access_key_is_secondary=False,
            retention_in_days=6)
        ```

        ## Import

        Synapse Workspace Extended Auditing Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/workspaceExtendedAuditingPolicy:WorkspaceExtendedAuditingPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Synapse/workspaces/workspace1/extendedAuditingSettings/default
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceExtendedAuditingPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceExtendedAuditingPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_monitoring_enabled: Optional[pulumi.Input[bool]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key_is_secondary: Optional[pulumi.Input[bool]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceExtendedAuditingPolicyArgs.__new__(WorkspaceExtendedAuditingPolicyArgs)

            __props__.__dict__["log_monitoring_enabled"] = log_monitoring_enabled
            __props__.__dict__["retention_in_days"] = retention_in_days
            __props__.__dict__["storage_account_access_key"] = None if storage_account_access_key is None else pulumi.Output.secret(storage_account_access_key)
            __props__.__dict__["storage_account_access_key_is_secondary"] = storage_account_access_key_is_secondary
            __props__.__dict__["storage_endpoint"] = storage_endpoint
            if synapse_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'synapse_workspace_id'")
            __props__.__dict__["synapse_workspace_id"] = synapse_workspace_id
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["storageAccountAccessKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(WorkspaceExtendedAuditingPolicy, __self__).__init__(
            'azure:synapse/workspaceExtendedAuditingPolicy:WorkspaceExtendedAuditingPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            log_monitoring_enabled: Optional[pulumi.Input[bool]] = None,
            retention_in_days: Optional[pulumi.Input[int]] = None,
            storage_account_access_key: Optional[pulumi.Input[str]] = None,
            storage_account_access_key_is_secondary: Optional[pulumi.Input[bool]] = None,
            storage_endpoint: Optional[pulumi.Input[str]] = None,
            synapse_workspace_id: Optional[pulumi.Input[str]] = None) -> 'WorkspaceExtendedAuditingPolicy':
        """
        Get an existing WorkspaceExtendedAuditingPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] log_monitoring_enabled: Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        :param pulumi.Input[int] retention_in_days: The number of days to retain logs for in the storage account. Defaults to `0`.
        :param pulumi.Input[str] storage_account_access_key: The access key to use for the auditing storage account.
        :param pulumi.Input[bool] storage_account_access_key_is_secondary: Is `storage_account_access_key` value the storage's secondary key?
        :param pulumi.Input[str] storage_endpoint: The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        :param pulumi.Input[str] synapse_workspace_id: The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceExtendedAuditingPolicyState.__new__(_WorkspaceExtendedAuditingPolicyState)

        __props__.__dict__["log_monitoring_enabled"] = log_monitoring_enabled
        __props__.__dict__["retention_in_days"] = retention_in_days
        __props__.__dict__["storage_account_access_key"] = storage_account_access_key
        __props__.__dict__["storage_account_access_key_is_secondary"] = storage_account_access_key_is_secondary
        __props__.__dict__["storage_endpoint"] = storage_endpoint
        __props__.__dict__["synapse_workspace_id"] = synapse_workspace_id
        return WorkspaceExtendedAuditingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="logMonitoringEnabled")
    def log_monitoring_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor. Defaults to `true`.
        """
        return pulumi.get(self, "log_monitoring_enabled")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        The number of days to retain logs for in the storage account. Defaults to `0`.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        The access key to use for the auditing storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageAccountAccessKeyIsSecondary")
    def storage_account_access_key_is_secondary(self) -> pulumi.Output[Optional[bool]]:
        """
        Is `storage_account_access_key` value the storage's secondary key?
        """
        return pulumi.get(self, "storage_account_access_key_is_secondary")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        The blob storage endpoint (e.g. <https://example.blob.core.windows.net>). This blob storage will hold all extended auditing logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Synapse workspace to set the extended auditing policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "synapse_workspace_id")

