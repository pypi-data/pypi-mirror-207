# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ProviderFeaturesArgs',
    'ProviderFeaturesApiManagementArgs',
    'ProviderFeaturesAppConfigurationArgs',
    'ProviderFeaturesApplicationInsightsArgs',
    'ProviderFeaturesCognitiveAccountArgs',
    'ProviderFeaturesKeyVaultArgs',
    'ProviderFeaturesLogAnalyticsWorkspaceArgs',
    'ProviderFeaturesManagedDiskArgs',
    'ProviderFeaturesNetworkArgs',
    'ProviderFeaturesResourceGroupArgs',
    'ProviderFeaturesTemplateDeploymentArgs',
    'ProviderFeaturesVirtualMachineArgs',
    'ProviderFeaturesVirtualMachineScaleSetArgs',
]

@pulumi.input_type
class ProviderFeaturesArgs:
    def __init__(__self__, *,
                 api_management: Optional[pulumi.Input['ProviderFeaturesApiManagementArgs']] = None,
                 app_configuration: Optional[pulumi.Input['ProviderFeaturesAppConfigurationArgs']] = None,
                 application_insights: Optional[pulumi.Input['ProviderFeaturesApplicationInsightsArgs']] = None,
                 cognitive_account: Optional[pulumi.Input['ProviderFeaturesCognitiveAccountArgs']] = None,
                 key_vault: Optional[pulumi.Input['ProviderFeaturesKeyVaultArgs']] = None,
                 log_analytics_workspace: Optional[pulumi.Input['ProviderFeaturesLogAnalyticsWorkspaceArgs']] = None,
                 managed_disk: Optional[pulumi.Input['ProviderFeaturesManagedDiskArgs']] = None,
                 network: Optional[pulumi.Input['ProviderFeaturesNetworkArgs']] = None,
                 resource_group: Optional[pulumi.Input['ProviderFeaturesResourceGroupArgs']] = None,
                 template_deployment: Optional[pulumi.Input['ProviderFeaturesTemplateDeploymentArgs']] = None,
                 virtual_machine: Optional[pulumi.Input['ProviderFeaturesVirtualMachineArgs']] = None,
                 virtual_machine_scale_set: Optional[pulumi.Input['ProviderFeaturesVirtualMachineScaleSetArgs']] = None):
        if api_management is not None:
            pulumi.set(__self__, "api_management", api_management)
        if app_configuration is not None:
            pulumi.set(__self__, "app_configuration", app_configuration)
        if application_insights is not None:
            pulumi.set(__self__, "application_insights", application_insights)
        if cognitive_account is not None:
            pulumi.set(__self__, "cognitive_account", cognitive_account)
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if log_analytics_workspace is not None:
            pulumi.set(__self__, "log_analytics_workspace", log_analytics_workspace)
        if managed_disk is not None:
            pulumi.set(__self__, "managed_disk", managed_disk)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)
        if template_deployment is not None:
            pulumi.set(__self__, "template_deployment", template_deployment)
        if virtual_machine is not None:
            pulumi.set(__self__, "virtual_machine", virtual_machine)
        if virtual_machine_scale_set is not None:
            pulumi.set(__self__, "virtual_machine_scale_set", virtual_machine_scale_set)

    @property
    @pulumi.getter(name="apiManagement")
    def api_management(self) -> Optional[pulumi.Input['ProviderFeaturesApiManagementArgs']]:
        return pulumi.get(self, "api_management")

    @api_management.setter
    def api_management(self, value: Optional[pulumi.Input['ProviderFeaturesApiManagementArgs']]):
        pulumi.set(self, "api_management", value)

    @property
    @pulumi.getter(name="appConfiguration")
    def app_configuration(self) -> Optional[pulumi.Input['ProviderFeaturesAppConfigurationArgs']]:
        return pulumi.get(self, "app_configuration")

    @app_configuration.setter
    def app_configuration(self, value: Optional[pulumi.Input['ProviderFeaturesAppConfigurationArgs']]):
        pulumi.set(self, "app_configuration", value)

    @property
    @pulumi.getter(name="applicationInsights")
    def application_insights(self) -> Optional[pulumi.Input['ProviderFeaturesApplicationInsightsArgs']]:
        return pulumi.get(self, "application_insights")

    @application_insights.setter
    def application_insights(self, value: Optional[pulumi.Input['ProviderFeaturesApplicationInsightsArgs']]):
        pulumi.set(self, "application_insights", value)

    @property
    @pulumi.getter(name="cognitiveAccount")
    def cognitive_account(self) -> Optional[pulumi.Input['ProviderFeaturesCognitiveAccountArgs']]:
        return pulumi.get(self, "cognitive_account")

    @cognitive_account.setter
    def cognitive_account(self, value: Optional[pulumi.Input['ProviderFeaturesCognitiveAccountArgs']]):
        pulumi.set(self, "cognitive_account", value)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input['ProviderFeaturesKeyVaultArgs']]:
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input['ProviderFeaturesKeyVaultArgs']]):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspace")
    def log_analytics_workspace(self) -> Optional[pulumi.Input['ProviderFeaturesLogAnalyticsWorkspaceArgs']]:
        return pulumi.get(self, "log_analytics_workspace")

    @log_analytics_workspace.setter
    def log_analytics_workspace(self, value: Optional[pulumi.Input['ProviderFeaturesLogAnalyticsWorkspaceArgs']]):
        pulumi.set(self, "log_analytics_workspace", value)

    @property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input['ProviderFeaturesManagedDiskArgs']]:
        return pulumi.get(self, "managed_disk")

    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input['ProviderFeaturesManagedDiskArgs']]):
        pulumi.set(self, "managed_disk", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input['ProviderFeaturesNetworkArgs']]:
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input['ProviderFeaturesNetworkArgs']]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input['ProviderFeaturesResourceGroupArgs']]:
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input['ProviderFeaturesResourceGroupArgs']]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="templateDeployment")
    def template_deployment(self) -> Optional[pulumi.Input['ProviderFeaturesTemplateDeploymentArgs']]:
        return pulumi.get(self, "template_deployment")

    @template_deployment.setter
    def template_deployment(self, value: Optional[pulumi.Input['ProviderFeaturesTemplateDeploymentArgs']]):
        pulumi.set(self, "template_deployment", value)

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional[pulumi.Input['ProviderFeaturesVirtualMachineArgs']]:
        return pulumi.get(self, "virtual_machine")

    @virtual_machine.setter
    def virtual_machine(self, value: Optional[pulumi.Input['ProviderFeaturesVirtualMachineArgs']]):
        pulumi.set(self, "virtual_machine", value)

    @property
    @pulumi.getter(name="virtualMachineScaleSet")
    def virtual_machine_scale_set(self) -> Optional[pulumi.Input['ProviderFeaturesVirtualMachineScaleSetArgs']]:
        return pulumi.get(self, "virtual_machine_scale_set")

    @virtual_machine_scale_set.setter
    def virtual_machine_scale_set(self, value: Optional[pulumi.Input['ProviderFeaturesVirtualMachineScaleSetArgs']]):
        pulumi.set(self, "virtual_machine_scale_set", value)


@pulumi.input_type
class ProviderFeaturesApiManagementArgs:
    def __init__(__self__, *,
                 purge_soft_delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted: Optional[pulumi.Input[bool]] = None):
        if purge_soft_delete_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_delete_on_destroy", purge_soft_delete_on_destroy)
        if recover_soft_deleted is not None:
            pulumi.set(__self__, "recover_soft_deleted", recover_soft_deleted)

    @property
    @pulumi.getter(name="purgeSoftDeleteOnDestroy")
    def purge_soft_delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_delete_on_destroy")

    @purge_soft_delete_on_destroy.setter
    def purge_soft_delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_delete_on_destroy", value)

    @property
    @pulumi.getter(name="recoverSoftDeleted")
    def recover_soft_deleted(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted")

    @recover_soft_deleted.setter
    def recover_soft_deleted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted", value)


@pulumi.input_type
class ProviderFeaturesAppConfigurationArgs:
    def __init__(__self__, *,
                 purge_soft_delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted: Optional[pulumi.Input[bool]] = None):
        if purge_soft_delete_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_delete_on_destroy", purge_soft_delete_on_destroy)
        if recover_soft_deleted is not None:
            pulumi.set(__self__, "recover_soft_deleted", recover_soft_deleted)

    @property
    @pulumi.getter(name="purgeSoftDeleteOnDestroy")
    def purge_soft_delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_delete_on_destroy")

    @purge_soft_delete_on_destroy.setter
    def purge_soft_delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_delete_on_destroy", value)

    @property
    @pulumi.getter(name="recoverSoftDeleted")
    def recover_soft_deleted(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted")

    @recover_soft_deleted.setter
    def recover_soft_deleted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted", value)


@pulumi.input_type
class ProviderFeaturesApplicationInsightsArgs:
    def __init__(__self__, *,
                 disable_generated_rule: Optional[pulumi.Input[bool]] = None):
        if disable_generated_rule is not None:
            pulumi.set(__self__, "disable_generated_rule", disable_generated_rule)

    @property
    @pulumi.getter(name="disableGeneratedRule")
    def disable_generated_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "disable_generated_rule")

    @disable_generated_rule.setter
    def disable_generated_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_generated_rule", value)


@pulumi.input_type
class ProviderFeaturesCognitiveAccountArgs:
    def __init__(__self__, *,
                 purge_soft_delete_on_destroy: Optional[pulumi.Input[bool]] = None):
        if purge_soft_delete_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_delete_on_destroy", purge_soft_delete_on_destroy)

    @property
    @pulumi.getter(name="purgeSoftDeleteOnDestroy")
    def purge_soft_delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_delete_on_destroy")

    @purge_soft_delete_on_destroy.setter
    def purge_soft_delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_delete_on_destroy", value)


@pulumi.input_type
class ProviderFeaturesKeyVaultArgs:
    def __init__(__self__, *,
                 purge_soft_delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 purge_soft_deleted_certificates_on_destroy: Optional[pulumi.Input[bool]] = None,
                 purge_soft_deleted_hardware_security_modules_on_destroy: Optional[pulumi.Input[bool]] = None,
                 purge_soft_deleted_keys_on_destroy: Optional[pulumi.Input[bool]] = None,
                 purge_soft_deleted_secrets_on_destroy: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted_certificates: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted_key_vaults: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted_keys: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted_secrets: Optional[pulumi.Input[bool]] = None):
        if purge_soft_delete_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_delete_on_destroy", purge_soft_delete_on_destroy)
        if purge_soft_deleted_certificates_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_deleted_certificates_on_destroy", purge_soft_deleted_certificates_on_destroy)
        if purge_soft_deleted_hardware_security_modules_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_deleted_hardware_security_modules_on_destroy", purge_soft_deleted_hardware_security_modules_on_destroy)
        if purge_soft_deleted_keys_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_deleted_keys_on_destroy", purge_soft_deleted_keys_on_destroy)
        if purge_soft_deleted_secrets_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_deleted_secrets_on_destroy", purge_soft_deleted_secrets_on_destroy)
        if recover_soft_deleted_certificates is not None:
            pulumi.set(__self__, "recover_soft_deleted_certificates", recover_soft_deleted_certificates)
        if recover_soft_deleted_key_vaults is not None:
            pulumi.set(__self__, "recover_soft_deleted_key_vaults", recover_soft_deleted_key_vaults)
        if recover_soft_deleted_keys is not None:
            pulumi.set(__self__, "recover_soft_deleted_keys", recover_soft_deleted_keys)
        if recover_soft_deleted_secrets is not None:
            pulumi.set(__self__, "recover_soft_deleted_secrets", recover_soft_deleted_secrets)

    @property
    @pulumi.getter(name="purgeSoftDeleteOnDestroy")
    def purge_soft_delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_delete_on_destroy")

    @purge_soft_delete_on_destroy.setter
    def purge_soft_delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_delete_on_destroy", value)

    @property
    @pulumi.getter(name="purgeSoftDeletedCertificatesOnDestroy")
    def purge_soft_deleted_certificates_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_deleted_certificates_on_destroy")

    @purge_soft_deleted_certificates_on_destroy.setter
    def purge_soft_deleted_certificates_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_deleted_certificates_on_destroy", value)

    @property
    @pulumi.getter(name="purgeSoftDeletedHardwareSecurityModulesOnDestroy")
    def purge_soft_deleted_hardware_security_modules_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_deleted_hardware_security_modules_on_destroy")

    @purge_soft_deleted_hardware_security_modules_on_destroy.setter
    def purge_soft_deleted_hardware_security_modules_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_deleted_hardware_security_modules_on_destroy", value)

    @property
    @pulumi.getter(name="purgeSoftDeletedKeysOnDestroy")
    def purge_soft_deleted_keys_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_deleted_keys_on_destroy")

    @purge_soft_deleted_keys_on_destroy.setter
    def purge_soft_deleted_keys_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_deleted_keys_on_destroy", value)

    @property
    @pulumi.getter(name="purgeSoftDeletedSecretsOnDestroy")
    def purge_soft_deleted_secrets_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_deleted_secrets_on_destroy")

    @purge_soft_deleted_secrets_on_destroy.setter
    def purge_soft_deleted_secrets_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_deleted_secrets_on_destroy", value)

    @property
    @pulumi.getter(name="recoverSoftDeletedCertificates")
    def recover_soft_deleted_certificates(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted_certificates")

    @recover_soft_deleted_certificates.setter
    def recover_soft_deleted_certificates(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted_certificates", value)

    @property
    @pulumi.getter(name="recoverSoftDeletedKeyVaults")
    def recover_soft_deleted_key_vaults(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted_key_vaults")

    @recover_soft_deleted_key_vaults.setter
    def recover_soft_deleted_key_vaults(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted_key_vaults", value)

    @property
    @pulumi.getter(name="recoverSoftDeletedKeys")
    def recover_soft_deleted_keys(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted_keys")

    @recover_soft_deleted_keys.setter
    def recover_soft_deleted_keys(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted_keys", value)

    @property
    @pulumi.getter(name="recoverSoftDeletedSecrets")
    def recover_soft_deleted_secrets(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted_secrets")

    @recover_soft_deleted_secrets.setter
    def recover_soft_deleted_secrets(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted_secrets", value)


@pulumi.input_type
class ProviderFeaturesLogAnalyticsWorkspaceArgs:
    def __init__(__self__, *,
                 permanently_delete_on_destroy: Optional[pulumi.Input[bool]] = None):
        if permanently_delete_on_destroy is not None:
            pulumi.set(__self__, "permanently_delete_on_destroy", permanently_delete_on_destroy)

    @property
    @pulumi.getter(name="permanentlyDeleteOnDestroy")
    def permanently_delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "permanently_delete_on_destroy")

    @permanently_delete_on_destroy.setter
    def permanently_delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "permanently_delete_on_destroy", value)


@pulumi.input_type
class ProviderFeaturesManagedDiskArgs:
    def __init__(__self__, *,
                 expand_without_downtime: Optional[pulumi.Input[bool]] = None):
        if expand_without_downtime is not None:
            pulumi.set(__self__, "expand_without_downtime", expand_without_downtime)

    @property
    @pulumi.getter(name="expandWithoutDowntime")
    def expand_without_downtime(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "expand_without_downtime")

    @expand_without_downtime.setter
    def expand_without_downtime(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "expand_without_downtime", value)


@pulumi.input_type
class ProviderFeaturesNetworkArgs:
    def __init__(__self__, *,
                 relaxed_locking: pulumi.Input[bool]):
        pulumi.set(__self__, "relaxed_locking", relaxed_locking)

    @property
    @pulumi.getter(name="relaxedLocking")
    def relaxed_locking(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "relaxed_locking")

    @relaxed_locking.setter
    def relaxed_locking(self, value: pulumi.Input[bool]):
        pulumi.set(self, "relaxed_locking", value)


@pulumi.input_type
class ProviderFeaturesResourceGroupArgs:
    def __init__(__self__, *,
                 prevent_deletion_if_contains_resources: Optional[pulumi.Input[bool]] = None):
        if prevent_deletion_if_contains_resources is not None:
            pulumi.set(__self__, "prevent_deletion_if_contains_resources", prevent_deletion_if_contains_resources)

    @property
    @pulumi.getter(name="preventDeletionIfContainsResources")
    def prevent_deletion_if_contains_resources(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "prevent_deletion_if_contains_resources")

    @prevent_deletion_if_contains_resources.setter
    def prevent_deletion_if_contains_resources(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "prevent_deletion_if_contains_resources", value)


@pulumi.input_type
class ProviderFeaturesTemplateDeploymentArgs:
    def __init__(__self__, *,
                 delete_nested_items_during_deletion: pulumi.Input[bool]):
        pulumi.set(__self__, "delete_nested_items_during_deletion", delete_nested_items_during_deletion)

    @property
    @pulumi.getter(name="deleteNestedItemsDuringDeletion")
    def delete_nested_items_during_deletion(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "delete_nested_items_during_deletion")

    @delete_nested_items_during_deletion.setter
    def delete_nested_items_during_deletion(self, value: pulumi.Input[bool]):
        pulumi.set(self, "delete_nested_items_during_deletion", value)


@pulumi.input_type
class ProviderFeaturesVirtualMachineArgs:
    def __init__(__self__, *,
                 delete_os_disk_on_deletion: Optional[pulumi.Input[bool]] = None,
                 graceful_shutdown: Optional[pulumi.Input[bool]] = None,
                 skip_shutdown_and_force_delete: Optional[pulumi.Input[bool]] = None):
        if delete_os_disk_on_deletion is not None:
            pulumi.set(__self__, "delete_os_disk_on_deletion", delete_os_disk_on_deletion)
        if graceful_shutdown is not None:
            pulumi.set(__self__, "graceful_shutdown", graceful_shutdown)
        if skip_shutdown_and_force_delete is not None:
            pulumi.set(__self__, "skip_shutdown_and_force_delete", skip_shutdown_and_force_delete)

    @property
    @pulumi.getter(name="deleteOsDiskOnDeletion")
    def delete_os_disk_on_deletion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_os_disk_on_deletion")

    @delete_os_disk_on_deletion.setter
    def delete_os_disk_on_deletion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_os_disk_on_deletion", value)

    @property
    @pulumi.getter(name="gracefulShutdown")
    def graceful_shutdown(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "graceful_shutdown")

    @graceful_shutdown.setter
    def graceful_shutdown(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "graceful_shutdown", value)

    @property
    @pulumi.getter(name="skipShutdownAndForceDelete")
    def skip_shutdown_and_force_delete(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_shutdown_and_force_delete")

    @skip_shutdown_and_force_delete.setter
    def skip_shutdown_and_force_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_shutdown_and_force_delete", value)


@pulumi.input_type
class ProviderFeaturesVirtualMachineScaleSetArgs:
    def __init__(__self__, *,
                 roll_instances_when_required: pulumi.Input[bool],
                 force_delete: Optional[pulumi.Input[bool]] = None,
                 scale_to_zero_before_deletion: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "roll_instances_when_required", roll_instances_when_required)
        if force_delete is not None:
            pulumi.set(__self__, "force_delete", force_delete)
        if scale_to_zero_before_deletion is not None:
            pulumi.set(__self__, "scale_to_zero_before_deletion", scale_to_zero_before_deletion)

    @property
    @pulumi.getter(name="rollInstancesWhenRequired")
    def roll_instances_when_required(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "roll_instances_when_required")

    @roll_instances_when_required.setter
    def roll_instances_when_required(self, value: pulumi.Input[bool]):
        pulumi.set(self, "roll_instances_when_required", value)

    @property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force_delete")

    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_delete", value)

    @property
    @pulumi.getter(name="scaleToZeroBeforeDeletion")
    def scale_to_zero_before_deletion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "scale_to_zero_before_deletion")

    @scale_to_zero_before_deletion.setter
    def scale_to_zero_before_deletion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scale_to_zero_before_deletion", value)


