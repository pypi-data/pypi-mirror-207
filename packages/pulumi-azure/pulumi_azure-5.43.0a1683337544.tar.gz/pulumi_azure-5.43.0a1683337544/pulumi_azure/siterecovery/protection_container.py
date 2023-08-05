# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProtectionContainerArgs', 'ProtectionContainer']

@pulumi.input_type
class ProtectionContainerArgs:
    def __init__(__self__, *,
                 recovery_fabric_name: pulumi.Input[str],
                 recovery_vault_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProtectionContainer resource.
        :param pulumi.Input[str] recovery_fabric_name: Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the protection container. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "recovery_fabric_name", recovery_fabric_name)
        pulumi.set(__self__, "recovery_vault_name", recovery_vault_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="recoveryFabricName")
    def recovery_fabric_name(self) -> pulumi.Input[str]:
        """
        Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_fabric_name")

    @recovery_fabric_name.setter
    def recovery_fabric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "recovery_fabric_name", value)

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> pulumi.Input[str]:
        """
        The name of the vault that should be updated. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_vault_name")

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "recovery_vault_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the protection container. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ProtectionContainerState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_fabric_name: Optional[pulumi.Input[str]] = None,
                 recovery_vault_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProtectionContainer resources.
        :param pulumi.Input[str] name: The name of the protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_fabric_name: Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if recovery_fabric_name is not None:
            pulumi.set(__self__, "recovery_fabric_name", recovery_fabric_name)
        if recovery_vault_name is not None:
            pulumi.set(__self__, "recovery_vault_name", recovery_vault_name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the protection container. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recoveryFabricName")
    def recovery_fabric_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_fabric_name")

    @recovery_fabric_name.setter
    def recovery_fabric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_fabric_name", value)

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the vault that should be updated. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_vault_name")

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_vault_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class ProtectionContainer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_fabric_name: Optional[pulumi.Input[str]] = None,
                 recovery_vault_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Azure Site Recovery protection container. Protection containers serve as containers for replicated VMs and belong to a single region / recovery fabric. Protection containers can contain more than one replicated VM. To replicate a VM, a container must exist in both the source and target Azure regions.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        primary = azure.core.ResourceGroup("primary", location="West US")
        secondary = azure.core.ResourceGroup("secondary", location="East US")
        vault = azure.recoveryservices.Vault("vault",
            location=secondary.location,
            resource_group_name=secondary.name,
            sku="Standard")
        fabric = azure.siterecovery.Fabric("fabric",
            resource_group_name=secondary.name,
            recovery_vault_name=vault.name,
            location=primary.location)
        protection_container = azure.siterecovery.ProtectionContainer("protection-container",
            resource_group_name=secondary.name,
            recovery_vault_name=vault.name,
            recovery_fabric_name=fabric.name)
        ```

        ## Import

        Site Recovery Protection Containers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:siterecovery/protectionContainer:ProtectionContainer mycontainer /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-name/providers/Microsoft.RecoveryServices/vaults/recovery-vault-name/replicationFabrics/fabric-name/replicationProtectionContainers/protection-container-name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_fabric_name: Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProtectionContainerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Azure Site Recovery protection container. Protection containers serve as containers for replicated VMs and belong to a single region / recovery fabric. Protection containers can contain more than one replicated VM. To replicate a VM, a container must exist in both the source and target Azure regions.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        primary = azure.core.ResourceGroup("primary", location="West US")
        secondary = azure.core.ResourceGroup("secondary", location="East US")
        vault = azure.recoveryservices.Vault("vault",
            location=secondary.location,
            resource_group_name=secondary.name,
            sku="Standard")
        fabric = azure.siterecovery.Fabric("fabric",
            resource_group_name=secondary.name,
            recovery_vault_name=vault.name,
            location=primary.location)
        protection_container = azure.siterecovery.ProtectionContainer("protection-container",
            resource_group_name=secondary.name,
            recovery_vault_name=vault.name,
            recovery_fabric_name=fabric.name)
        ```

        ## Import

        Site Recovery Protection Containers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:siterecovery/protectionContainer:ProtectionContainer mycontainer /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-name/providers/Microsoft.RecoveryServices/vaults/recovery-vault-name/replicationFabrics/fabric-name/replicationProtectionContainers/protection-container-name
        ```

        :param str resource_name: The name of the resource.
        :param ProtectionContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProtectionContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_fabric_name: Optional[pulumi.Input[str]] = None,
                 recovery_vault_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProtectionContainerArgs.__new__(ProtectionContainerArgs)

            __props__.__dict__["name"] = name
            if recovery_fabric_name is None and not opts.urn:
                raise TypeError("Missing required property 'recovery_fabric_name'")
            __props__.__dict__["recovery_fabric_name"] = recovery_fabric_name
            if recovery_vault_name is None and not opts.urn:
                raise TypeError("Missing required property 'recovery_vault_name'")
            __props__.__dict__["recovery_vault_name"] = recovery_vault_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(ProtectionContainer, __self__).__init__(
            'azure:siterecovery/protectionContainer:ProtectionContainer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            recovery_fabric_name: Optional[pulumi.Input[str]] = None,
            recovery_vault_name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'ProtectionContainer':
        """
        Get an existing ProtectionContainer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_fabric_name: Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        :param pulumi.Input[str] recovery_vault_name: The name of the vault that should be updated. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProtectionContainerState.__new__(_ProtectionContainerState)

        __props__.__dict__["name"] = name
        __props__.__dict__["recovery_fabric_name"] = recovery_fabric_name
        __props__.__dict__["recovery_vault_name"] = recovery_vault_name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return ProtectionContainer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the protection container. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recoveryFabricName")
    def recovery_fabric_name(self) -> pulumi.Output[str]:
        """
        Name of fabric that should contain this protection container. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_fabric_name")

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> pulumi.Output[str]:
        """
        The name of the vault that should be updated. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "recovery_vault_name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Name of the resource group where the vault that should be updated is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

