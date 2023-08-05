# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ManagedStorageAccountArgs', 'ManagedStorageAccount']

@pulumi.input_type
class ManagedStorageAccountArgs:
    def __init__(__self__, *,
                 key_vault_id: pulumi.Input[str],
                 storage_account_id: pulumi.Input[str],
                 storage_account_key: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 regenerate_key_automatically: Optional[pulumi.Input[bool]] = None,
                 regeneration_period: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ManagedStorageAccount resource.
        :param pulumi.Input[str] key_vault_id: The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account.
        :param pulumi.Input[str] storage_account_key: Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        :param pulumi.Input[str] name: The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        :param pulumi.Input[bool] regenerate_key_automatically: Should Storage Account access key be regenerated periodically?
        :param pulumi.Input[str] regeneration_period: How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "key_vault_id", key_vault_id)
        pulumi.set(__self__, "storage_account_id", storage_account_id)
        pulumi.set(__self__, "storage_account_key", storage_account_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regenerate_key_automatically is not None:
            pulumi.set(__self__, "regenerate_key_automatically", regenerate_key_automatically)
        if regeneration_period is not None:
            pulumi.set(__self__, "regeneration_period", regeneration_period)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> pulumi.Input[str]:
        """
        The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "key_vault_id")

    @key_vault_id.setter
    def key_vault_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_id", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[str]:
        """
        The ID of the Storage Account.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> pulumi.Input[str]:
        """
        Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        """
        return pulumi.get(self, "storage_account_key")

    @storage_account_key.setter
    def storage_account_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regenerateKeyAutomatically")
    def regenerate_key_automatically(self) -> Optional[pulumi.Input[bool]]:
        """
        Should Storage Account access key be regenerated periodically?
        """
        return pulumi.get(self, "regenerate_key_automatically")

    @regenerate_key_automatically.setter
    def regenerate_key_automatically(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "regenerate_key_automatically", value)

    @property
    @pulumi.getter(name="regenerationPeriod")
    def regeneration_period(self) -> Optional[pulumi.Input[str]]:
        """
        How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        """
        return pulumi.get(self, "regeneration_period")

    @regeneration_period.setter
    def regeneration_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "regeneration_period", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ManagedStorageAccountState:
    def __init__(__self__, *,
                 key_vault_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regenerate_key_automatically: Optional[pulumi.Input[bool]] = None,
                 regeneration_period: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 storage_account_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ManagedStorageAccount resources.
        :param pulumi.Input[str] key_vault_id: The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        :param pulumi.Input[bool] regenerate_key_automatically: Should Storage Account access key be regenerated periodically?
        :param pulumi.Input[str] regeneration_period: How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account.
        :param pulumi.Input[str] storage_account_key: Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        if key_vault_id is not None:
            pulumi.set(__self__, "key_vault_id", key_vault_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regenerate_key_automatically is not None:
            pulumi.set(__self__, "regenerate_key_automatically", regenerate_key_automatically)
        if regeneration_period is not None:
            pulumi.set(__self__, "regeneration_period", regeneration_period)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)
        if storage_account_key is not None:
            pulumi.set(__self__, "storage_account_key", storage_account_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "key_vault_id")

    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regenerateKeyAutomatically")
    def regenerate_key_automatically(self) -> Optional[pulumi.Input[bool]]:
        """
        Should Storage Account access key be regenerated periodically?
        """
        return pulumi.get(self, "regenerate_key_automatically")

    @regenerate_key_automatically.setter
    def regenerate_key_automatically(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "regenerate_key_automatically", value)

    @property
    @pulumi.getter(name="regenerationPeriod")
    def regeneration_period(self) -> Optional[pulumi.Input[str]]:
        """
        How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        """
        return pulumi.get(self, "regeneration_period")

    @regeneration_period.setter
    def regeneration_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "regeneration_period", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Storage Account.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[pulumi.Input[str]]:
        """
        Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        """
        return pulumi.get(self, "storage_account_key")

    @storage_account_key.setter
    def storage_account_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ManagedStorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_vault_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regenerate_key_automatically: Optional[pulumi.Input[bool]] = None,
                 regeneration_period: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 storage_account_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Key Vault Managed Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            tenant_id=current.tenant_id,
            sku_name="standard",
            access_policies=[azure.keyvault.KeyVaultAccessPolicyArgs(
                tenant_id=current.tenant_id,
                object_id=current.object_id,
                secret_permissions=[
                    "Get",
                    "Delete",
                ],
                storage_permissions=[
                    "Get",
                    "List",
                    "Set",
                    "SetSAS",
                    "GetSAS",
                    "DeleteSAS",
                    "Update",
                    "RegenerateKey",
                ],
            )])
        example_managed_storage_account = azure.keyvault.ManagedStorageAccount("exampleManagedStorageAccount",
            key_vault_id=example_key_vault.id,
            storage_account_id=example_account.id,
            storage_account_key="key1",
            regenerate_key_automatically=False,
            regeneration_period="P1D")
        ```
        ### Automatically Regenerate Storage Account Access Key)

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        current = azure.core.get_client_config()
        test = azuread.get_service_principal(application_id="cfa8b339-82a2-471a-a3c9-0fc0be7a4093")
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            tenant_id=current.tenant_id,
            sku_name="standard",
            access_policies=[azure.keyvault.KeyVaultAccessPolicyArgs(
                tenant_id=current.tenant_id,
                object_id=current.object_id,
                secret_permissions=[
                    "Get",
                    "Delete",
                ],
                storage_permissions=[
                    "Get",
                    "List",
                    "Set",
                    "SetSAS",
                    "GetSAS",
                    "DeleteSAS",
                    "Update",
                    "RegenerateKey",
                ],
            )])
        example_assignment = azure.authorization.Assignment("exampleAssignment",
            scope=example_account.id,
            role_definition_name="Storage Account Key Operator Service Role",
            principal_id=test.id)
        example_managed_storage_account = azure.keyvault.ManagedStorageAccount("exampleManagedStorageAccount",
            key_vault_id=example_key_vault.id,
            storage_account_id=example_account.id,
            storage_account_key="key1",
            regenerate_key_automatically=True,
            regeneration_period="P1D",
            opts=pulumi.ResourceOptions(depends_on=[example_assignment]))
        ```

        ## Import

        Key Vault Managed Storage Accounts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:keyvault/managedStorageAccount:ManagedStorageAccount example https://example-keyvault.vault.azure.net/storage/exampleStorageAcc01
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_vault_id: The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        :param pulumi.Input[bool] regenerate_key_automatically: Should Storage Account access key be regenerated periodically?
        :param pulumi.Input[str] regeneration_period: How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account.
        :param pulumi.Input[str] storage_account_key: Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedStorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Key Vault Managed Storage Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            tenant_id=current.tenant_id,
            sku_name="standard",
            access_policies=[azure.keyvault.KeyVaultAccessPolicyArgs(
                tenant_id=current.tenant_id,
                object_id=current.object_id,
                secret_permissions=[
                    "Get",
                    "Delete",
                ],
                storage_permissions=[
                    "Get",
                    "List",
                    "Set",
                    "SetSAS",
                    "GetSAS",
                    "DeleteSAS",
                    "Update",
                    "RegenerateKey",
                ],
            )])
        example_managed_storage_account = azure.keyvault.ManagedStorageAccount("exampleManagedStorageAccount",
            key_vault_id=example_key_vault.id,
            storage_account_id=example_account.id,
            storage_account_key="key1",
            regenerate_key_automatically=False,
            regeneration_period="P1D")
        ```
        ### Automatically Regenerate Storage Account Access Key)

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        current = azure.core.get_client_config()
        test = azuread.get_service_principal(application_id="cfa8b339-82a2-471a-a3c9-0fc0be7a4093")
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            tenant_id=current.tenant_id,
            sku_name="standard",
            access_policies=[azure.keyvault.KeyVaultAccessPolicyArgs(
                tenant_id=current.tenant_id,
                object_id=current.object_id,
                secret_permissions=[
                    "Get",
                    "Delete",
                ],
                storage_permissions=[
                    "Get",
                    "List",
                    "Set",
                    "SetSAS",
                    "GetSAS",
                    "DeleteSAS",
                    "Update",
                    "RegenerateKey",
                ],
            )])
        example_assignment = azure.authorization.Assignment("exampleAssignment",
            scope=example_account.id,
            role_definition_name="Storage Account Key Operator Service Role",
            principal_id=test.id)
        example_managed_storage_account = azure.keyvault.ManagedStorageAccount("exampleManagedStorageAccount",
            key_vault_id=example_key_vault.id,
            storage_account_id=example_account.id,
            storage_account_key="key1",
            regenerate_key_automatically=True,
            regeneration_period="P1D",
            opts=pulumi.ResourceOptions(depends_on=[example_assignment]))
        ```

        ## Import

        Key Vault Managed Storage Accounts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:keyvault/managedStorageAccount:ManagedStorageAccount example https://example-keyvault.vault.azure.net/storage/exampleStorageAcc01
        ```

        :param str resource_name: The name of the resource.
        :param ManagedStorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedStorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_vault_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regenerate_key_automatically: Optional[pulumi.Input[bool]] = None,
                 regeneration_period: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 storage_account_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedStorageAccountArgs.__new__(ManagedStorageAccountArgs)

            if key_vault_id is None and not opts.urn:
                raise TypeError("Missing required property 'key_vault_id'")
            __props__.__dict__["key_vault_id"] = key_vault_id
            __props__.__dict__["name"] = name
            __props__.__dict__["regenerate_key_automatically"] = regenerate_key_automatically
            __props__.__dict__["regeneration_period"] = regeneration_period
            if storage_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__.__dict__["storage_account_id"] = storage_account_id
            if storage_account_key is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_key'")
            __props__.__dict__["storage_account_key"] = storage_account_key
            __props__.__dict__["tags"] = tags
        super(ManagedStorageAccount, __self__).__init__(
            'azure:keyvault/managedStorageAccount:ManagedStorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key_vault_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            regenerate_key_automatically: Optional[pulumi.Input[bool]] = None,
            regeneration_period: Optional[pulumi.Input[str]] = None,
            storage_account_id: Optional[pulumi.Input[str]] = None,
            storage_account_key: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ManagedStorageAccount':
        """
        Get an existing ManagedStorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_vault_id: The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        :param pulumi.Input[bool] regenerate_key_automatically: Should Storage Account access key be regenerated periodically?
        :param pulumi.Input[str] regeneration_period: How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account.
        :param pulumi.Input[str] storage_account_key: Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagedStorageAccountState.__new__(_ManagedStorageAccountState)

        __props__.__dict__["key_vault_id"] = key_vault_id
        __props__.__dict__["name"] = name
        __props__.__dict__["regenerate_key_automatically"] = regenerate_key_automatically
        __props__.__dict__["regeneration_period"] = regeneration_period
        __props__.__dict__["storage_account_id"] = storage_account_id
        __props__.__dict__["storage_account_key"] = storage_account_key
        __props__.__dict__["tags"] = tags
        return ManagedStorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> pulumi.Output[str]:
        """
        The ID of the Key Vault where the Managed Storage Account should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "key_vault_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Key Vault Managed Storage Account. Changing this forces a new Key Vault Managed Storage Account to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regenerateKeyAutomatically")
    def regenerate_key_automatically(self) -> pulumi.Output[Optional[bool]]:
        """
        Should Storage Account access key be regenerated periodically?
        """
        return pulumi.get(self, "regenerate_key_automatically")

    @property
    @pulumi.getter(name="regenerationPeriod")
    def regeneration_period(self) -> pulumi.Output[Optional[str]]:
        """
        How often Storage Account access key should be regenerated. Value needs to be in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations).
        """
        return pulumi.get(self, "regeneration_period")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the Storage Account.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> pulumi.Output[str]:
        """
        Which Storage Account access key that is managed by Key Vault. Possible values are `key1` and `key2`.
        """
        return pulumi.get(self, "storage_account_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Key Vault Managed Storage Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "tags")

