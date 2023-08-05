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

__all__ = [
    'GetComputeMachineAgentConfigurationResult',
    'GetComputeMachineAgentConfigurationExtensionsAllowListResult',
    'GetComputeMachineAgentConfigurationExtensionsBlockListResult',
    'GetComputeMachineCloudMetadataResult',
    'GetComputeMachineErrorDetailResult',
    'GetComputeMachineErrorDetailAdditionalInfoResult',
    'GetComputeMachineIdentityResult',
    'GetComputeMachineLocationDataResult',
    'GetComputeMachineOsProfileResult',
    'GetComputeMachineOsProfileLinuxConfigurationResult',
    'GetComputeMachineOsProfileLinuxConfigurationPatchSettingResult',
    'GetComputeMachineOsProfileWindowsConfigurationResult',
    'GetComputeMachineOsProfileWindowsConfigurationPatchSettingResult',
    'GetComputeMachineServiceStatusResult',
    'GetComputeMachineServiceStatusExtensionServiceResult',
    'GetComputeMachineServiceStatusGuestConfigurationServiceResult',
]

@pulumi.output_type
class GetComputeMachineAgentConfigurationResult(dict):
    def __init__(__self__, *,
                 extensions_allow_lists: Sequence['outputs.GetComputeMachineAgentConfigurationExtensionsAllowListResult'],
                 extensions_block_lists: Sequence['outputs.GetComputeMachineAgentConfigurationExtensionsBlockListResult'],
                 extensions_enabled: bool,
                 guest_configuration_enabled: bool,
                 incoming_connections_ports: Sequence[str],
                 proxy_bypasses: Sequence[str],
                 proxy_url: str):
        """
        :param Sequence['GetComputeMachineAgentConfigurationExtensionsAllowListArgs'] extensions_allow_lists: A `extensions_allow_list` block as defined below.
        :param Sequence['GetComputeMachineAgentConfigurationExtensionsBlockListArgs'] extensions_block_lists: A `extensions_block_list` block as defined below.
        :param bool extensions_enabled: Specifies whether the extension service is enabled or disabled.
        :param bool guest_configuration_enabled: Specified whether the guest configuration service is enabled or disabled.
        :param Sequence[str] incoming_connections_ports: Specifies the list of ports that the agent will be able to listen on.
        :param Sequence[str] proxy_bypasses: List of service names which should not use the specified proxy server.
        :param str proxy_url: Specifies the URL of the proxy to be used.
        """
        pulumi.set(__self__, "extensions_allow_lists", extensions_allow_lists)
        pulumi.set(__self__, "extensions_block_lists", extensions_block_lists)
        pulumi.set(__self__, "extensions_enabled", extensions_enabled)
        pulumi.set(__self__, "guest_configuration_enabled", guest_configuration_enabled)
        pulumi.set(__self__, "incoming_connections_ports", incoming_connections_ports)
        pulumi.set(__self__, "proxy_bypasses", proxy_bypasses)
        pulumi.set(__self__, "proxy_url", proxy_url)

    @property
    @pulumi.getter(name="extensionsAllowLists")
    def extensions_allow_lists(self) -> Sequence['outputs.GetComputeMachineAgentConfigurationExtensionsAllowListResult']:
        """
        A `extensions_allow_list` block as defined below.
        """
        return pulumi.get(self, "extensions_allow_lists")

    @property
    @pulumi.getter(name="extensionsBlockLists")
    def extensions_block_lists(self) -> Sequence['outputs.GetComputeMachineAgentConfigurationExtensionsBlockListResult']:
        """
        A `extensions_block_list` block as defined below.
        """
        return pulumi.get(self, "extensions_block_lists")

    @property
    @pulumi.getter(name="extensionsEnabled")
    def extensions_enabled(self) -> bool:
        """
        Specifies whether the extension service is enabled or disabled.
        """
        return pulumi.get(self, "extensions_enabled")

    @property
    @pulumi.getter(name="guestConfigurationEnabled")
    def guest_configuration_enabled(self) -> bool:
        """
        Specified whether the guest configuration service is enabled or disabled.
        """
        return pulumi.get(self, "guest_configuration_enabled")

    @property
    @pulumi.getter(name="incomingConnectionsPorts")
    def incoming_connections_ports(self) -> Sequence[str]:
        """
        Specifies the list of ports that the agent will be able to listen on.
        """
        return pulumi.get(self, "incoming_connections_ports")

    @property
    @pulumi.getter(name="proxyBypasses")
    def proxy_bypasses(self) -> Sequence[str]:
        """
        List of service names which should not use the specified proxy server.
        """
        return pulumi.get(self, "proxy_bypasses")

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> str:
        """
        Specifies the URL of the proxy to be used.
        """
        return pulumi.get(self, "proxy_url")


@pulumi.output_type
class GetComputeMachineAgentConfigurationExtensionsAllowListResult(dict):
    def __init__(__self__, *,
                 publisher: str,
                 type: str):
        """
        :param str publisher: Publisher of the extension.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "publisher", publisher)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        Publisher of the extension.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetComputeMachineAgentConfigurationExtensionsBlockListResult(dict):
    def __init__(__self__, *,
                 publisher: str,
                 type: str):
        """
        :param str publisher: Publisher of the extension.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "publisher", publisher)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        Publisher of the extension.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetComputeMachineCloudMetadataResult(dict):
    def __init__(__self__, *,
                 provider: str):
        """
        :param str provider: Specifies the cloud provider. For example `Azure`, `AWS` and `GCP`.
        """
        pulumi.set(__self__, "provider", provider)

    @property
    @pulumi.getter
    def provider(self) -> str:
        """
        Specifies the cloud provider. For example `Azure`, `AWS` and `GCP`.
        """
        return pulumi.get(self, "provider")


@pulumi.output_type
class GetComputeMachineErrorDetailResult(dict):
    def __init__(__self__, *,
                 additional_infos: Sequence['outputs.GetComputeMachineErrorDetailAdditionalInfoResult'],
                 code: str,
                 message: str,
                 target: str):
        """
        :param Sequence['GetComputeMachineErrorDetailAdditionalInfoArgs'] additional_infos: A `additional_info` block as defined above.
        :param str code: The error code.
        :param str message: The error message.
        :param str target: The error target.
        """
        pulumi.set(__self__, "additional_infos", additional_infos)
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="additionalInfos")
    def additional_infos(self) -> Sequence['outputs.GetComputeMachineErrorDetailAdditionalInfoResult']:
        """
        A `additional_info` block as defined above.
        """
        return pulumi.get(self, "additional_infos")

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        The error code.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The error message.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        The error target.
        """
        return pulumi.get(self, "target")


@pulumi.output_type
class GetComputeMachineErrorDetailAdditionalInfoResult(dict):
    def __init__(__self__, *,
                 info: str,
                 type: str):
        """
        :param str info: The additional information message.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "info", info)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def info(self) -> str:
        """
        The additional information message.
        """
        return pulumi.get(self, "info")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetComputeMachineIdentityResult(dict):
    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str):
        """
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetComputeMachineLocationDataResult(dict):
    def __init__(__self__, *,
                 city: str,
                 country_or_region: str,
                 district: str,
                 name: str):
        """
        :param str city: The city or locality where the resource is located.
        :param str country_or_region: The country or region where the resource is located.
        :param str district: The district, state, or province where the resource is located.
        :param str name: The name of this hybrid compute machine.
        """
        pulumi.set(__self__, "city", city)
        pulumi.set(__self__, "country_or_region", country_or_region)
        pulumi.set(__self__, "district", district)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def city(self) -> str:
        """
        The city or locality where the resource is located.
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> str:
        """
        The country or region where the resource is located.
        """
        return pulumi.get(self, "country_or_region")

    @property
    @pulumi.getter
    def district(self) -> str:
        """
        The district, state, or province where the resource is located.
        """
        return pulumi.get(self, "district")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this hybrid compute machine.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetComputeMachineOsProfileResult(dict):
    def __init__(__self__, *,
                 computer_name: str,
                 linux_configurations: Sequence['outputs.GetComputeMachineOsProfileLinuxConfigurationResult'],
                 windows_configurations: Sequence['outputs.GetComputeMachineOsProfileWindowsConfigurationResult']):
        """
        :param str computer_name: Specifies the host OS name of the hybrid machine.
        :param Sequence['GetComputeMachineOsProfileLinuxConfigurationArgs'] linux_configurations: A `linux_configuration` block as defined above.
        :param Sequence['GetComputeMachineOsProfileWindowsConfigurationArgs'] windows_configurations: A `windows_configuration` block as defined below.
        """
        pulumi.set(__self__, "computer_name", computer_name)
        pulumi.set(__self__, "linux_configurations", linux_configurations)
        pulumi.set(__self__, "windows_configurations", windows_configurations)

    @property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> str:
        """
        Specifies the host OS name of the hybrid machine.
        """
        return pulumi.get(self, "computer_name")

    @property
    @pulumi.getter(name="linuxConfigurations")
    def linux_configurations(self) -> Sequence['outputs.GetComputeMachineOsProfileLinuxConfigurationResult']:
        """
        A `linux_configuration` block as defined above.
        """
        return pulumi.get(self, "linux_configurations")

    @property
    @pulumi.getter(name="windowsConfigurations")
    def windows_configurations(self) -> Sequence['outputs.GetComputeMachineOsProfileWindowsConfigurationResult']:
        """
        A `windows_configuration` block as defined below.
        """
        return pulumi.get(self, "windows_configurations")


@pulumi.output_type
class GetComputeMachineOsProfileLinuxConfigurationResult(dict):
    def __init__(__self__, *,
                 patch_settings: Sequence['outputs.GetComputeMachineOsProfileLinuxConfigurationPatchSettingResult']):
        """
        :param Sequence['GetComputeMachineOsProfileLinuxConfigurationPatchSettingArgs'] patch_settings: A `patch_settings` block as defined above.
        """
        pulumi.set(__self__, "patch_settings", patch_settings)

    @property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Sequence['outputs.GetComputeMachineOsProfileLinuxConfigurationPatchSettingResult']:
        """
        A `patch_settings` block as defined above.
        """
        return pulumi.get(self, "patch_settings")


@pulumi.output_type
class GetComputeMachineOsProfileLinuxConfigurationPatchSettingResult(dict):
    def __init__(__self__, *,
                 assessment_mode: str,
                 patch_mode: str):
        """
        :param str assessment_mode: Specifies the assessment mode.
        :param str patch_mode: Specifies the patch mode.
        """
        pulumi.set(__self__, "assessment_mode", assessment_mode)
        pulumi.set(__self__, "patch_mode", patch_mode)

    @property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> str:
        """
        Specifies the assessment mode.
        """
        return pulumi.get(self, "assessment_mode")

    @property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> str:
        """
        Specifies the patch mode.
        """
        return pulumi.get(self, "patch_mode")


@pulumi.output_type
class GetComputeMachineOsProfileWindowsConfigurationResult(dict):
    def __init__(__self__, *,
                 patch_settings: Sequence['outputs.GetComputeMachineOsProfileWindowsConfigurationPatchSettingResult']):
        """
        :param Sequence['GetComputeMachineOsProfileWindowsConfigurationPatchSettingArgs'] patch_settings: A `patch_settings` block as defined above.
        """
        pulumi.set(__self__, "patch_settings", patch_settings)

    @property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Sequence['outputs.GetComputeMachineOsProfileWindowsConfigurationPatchSettingResult']:
        """
        A `patch_settings` block as defined above.
        """
        return pulumi.get(self, "patch_settings")


@pulumi.output_type
class GetComputeMachineOsProfileWindowsConfigurationPatchSettingResult(dict):
    def __init__(__self__, *,
                 assessment_mode: str,
                 patch_mode: str):
        """
        :param str assessment_mode: Specifies the assessment mode.
        :param str patch_mode: Specifies the patch mode.
        """
        pulumi.set(__self__, "assessment_mode", assessment_mode)
        pulumi.set(__self__, "patch_mode", patch_mode)

    @property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> str:
        """
        Specifies the assessment mode.
        """
        return pulumi.get(self, "assessment_mode")

    @property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> str:
        """
        Specifies the patch mode.
        """
        return pulumi.get(self, "patch_mode")


@pulumi.output_type
class GetComputeMachineServiceStatusResult(dict):
    def __init__(__self__, *,
                 extension_services: Sequence['outputs.GetComputeMachineServiceStatusExtensionServiceResult'],
                 guest_configuration_services: Sequence['outputs.GetComputeMachineServiceStatusGuestConfigurationServiceResult']):
        """
        :param Sequence['GetComputeMachineServiceStatusExtensionServiceArgs'] extension_services: A `extension_service` block as defined above.
        :param Sequence['GetComputeMachineServiceStatusGuestConfigurationServiceArgs'] guest_configuration_services: A `guest_configuration_service` block as defined above.
        """
        pulumi.set(__self__, "extension_services", extension_services)
        pulumi.set(__self__, "guest_configuration_services", guest_configuration_services)

    @property
    @pulumi.getter(name="extensionServices")
    def extension_services(self) -> Sequence['outputs.GetComputeMachineServiceStatusExtensionServiceResult']:
        """
        A `extension_service` block as defined above.
        """
        return pulumi.get(self, "extension_services")

    @property
    @pulumi.getter(name="guestConfigurationServices")
    def guest_configuration_services(self) -> Sequence['outputs.GetComputeMachineServiceStatusGuestConfigurationServiceResult']:
        """
        A `guest_configuration_service` block as defined above.
        """
        return pulumi.get(self, "guest_configuration_services")


@pulumi.output_type
class GetComputeMachineServiceStatusExtensionServiceResult(dict):
    def __init__(__self__, *,
                 startup_type: str,
                 status: str):
        """
        :param str startup_type: The behavior of the service when the Arc-enabled machine starts up.
        :param str status: The current status of the service.
        """
        pulumi.set(__self__, "startup_type", startup_type)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="startupType")
    def startup_type(self) -> str:
        """
        The behavior of the service when the Arc-enabled machine starts up.
        """
        return pulumi.get(self, "startup_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetComputeMachineServiceStatusGuestConfigurationServiceResult(dict):
    def __init__(__self__, *,
                 startup_type: str,
                 status: str):
        """
        :param str startup_type: The behavior of the service when the Arc-enabled machine starts up.
        :param str status: The current status of the service.
        """
        pulumi.set(__self__, "startup_type", startup_type)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="startupType")
    def startup_type(self) -> str:
        """
        The behavior of the service when the Arc-enabled machine starts up.
        """
        return pulumi.get(self, "startup_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the service.
        """
        return pulumi.get(self, "status")


