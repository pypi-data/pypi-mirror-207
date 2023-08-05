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
    'GetLinuxFunctionAppResult',
    'AwaitableGetLinuxFunctionAppResult',
    'get_linux_function_app',
    'get_linux_function_app_output',
]

@pulumi.output_type
class GetLinuxFunctionAppResult:
    """
    A collection of values returned by getLinuxFunctionApp.
    """
    def __init__(__self__, app_settings=None, auth_settings=None, auth_settings_v2s=None, backups=None, builtin_logging_enabled=None, client_certificate_enabled=None, client_certificate_exclusion_paths=None, client_certificate_mode=None, connection_strings=None, content_share_force_disabled=None, custom_domain_verification_id=None, daily_memory_time_quota=None, default_hostname=None, enabled=None, functions_extension_version=None, hosting_environment_id=None, https_only=None, id=None, identities=None, kind=None, location=None, name=None, outbound_ip_address_lists=None, outbound_ip_addresses=None, possible_outbound_ip_address_lists=None, possible_outbound_ip_addresses=None, resource_group_name=None, service_plan_id=None, site_configs=None, site_credentials=None, sticky_settings=None, storage_account_access_key=None, storage_account_name=None, storage_key_vault_secret_id=None, storage_uses_managed_identity=None, tags=None, virtual_network_subnet_id=None):
        if app_settings and not isinstance(app_settings, dict):
            raise TypeError("Expected argument 'app_settings' to be a dict")
        pulumi.set(__self__, "app_settings", app_settings)
        if auth_settings and not isinstance(auth_settings, list):
            raise TypeError("Expected argument 'auth_settings' to be a list")
        pulumi.set(__self__, "auth_settings", auth_settings)
        if auth_settings_v2s and not isinstance(auth_settings_v2s, list):
            raise TypeError("Expected argument 'auth_settings_v2s' to be a list")
        pulumi.set(__self__, "auth_settings_v2s", auth_settings_v2s)
        if backups and not isinstance(backups, list):
            raise TypeError("Expected argument 'backups' to be a list")
        pulumi.set(__self__, "backups", backups)
        if builtin_logging_enabled and not isinstance(builtin_logging_enabled, bool):
            raise TypeError("Expected argument 'builtin_logging_enabled' to be a bool")
        pulumi.set(__self__, "builtin_logging_enabled", builtin_logging_enabled)
        if client_certificate_enabled and not isinstance(client_certificate_enabled, bool):
            raise TypeError("Expected argument 'client_certificate_enabled' to be a bool")
        pulumi.set(__self__, "client_certificate_enabled", client_certificate_enabled)
        if client_certificate_exclusion_paths and not isinstance(client_certificate_exclusion_paths, str):
            raise TypeError("Expected argument 'client_certificate_exclusion_paths' to be a str")
        pulumi.set(__self__, "client_certificate_exclusion_paths", client_certificate_exclusion_paths)
        if client_certificate_mode and not isinstance(client_certificate_mode, str):
            raise TypeError("Expected argument 'client_certificate_mode' to be a str")
        pulumi.set(__self__, "client_certificate_mode", client_certificate_mode)
        if connection_strings and not isinstance(connection_strings, list):
            raise TypeError("Expected argument 'connection_strings' to be a list")
        pulumi.set(__self__, "connection_strings", connection_strings)
        if content_share_force_disabled and not isinstance(content_share_force_disabled, bool):
            raise TypeError("Expected argument 'content_share_force_disabled' to be a bool")
        pulumi.set(__self__, "content_share_force_disabled", content_share_force_disabled)
        if custom_domain_verification_id and not isinstance(custom_domain_verification_id, str):
            raise TypeError("Expected argument 'custom_domain_verification_id' to be a str")
        pulumi.set(__self__, "custom_domain_verification_id", custom_domain_verification_id)
        if daily_memory_time_quota and not isinstance(daily_memory_time_quota, int):
            raise TypeError("Expected argument 'daily_memory_time_quota' to be a int")
        pulumi.set(__self__, "daily_memory_time_quota", daily_memory_time_quota)
        if default_hostname and not isinstance(default_hostname, str):
            raise TypeError("Expected argument 'default_hostname' to be a str")
        pulumi.set(__self__, "default_hostname", default_hostname)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if functions_extension_version and not isinstance(functions_extension_version, str):
            raise TypeError("Expected argument 'functions_extension_version' to be a str")
        pulumi.set(__self__, "functions_extension_version", functions_extension_version)
        if hosting_environment_id and not isinstance(hosting_environment_id, str):
            raise TypeError("Expected argument 'hosting_environment_id' to be a str")
        pulumi.set(__self__, "hosting_environment_id", hosting_environment_id)
        if https_only and not isinstance(https_only, bool):
            raise TypeError("Expected argument 'https_only' to be a bool")
        pulumi.set(__self__, "https_only", https_only)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outbound_ip_address_lists and not isinstance(outbound_ip_address_lists, list):
            raise TypeError("Expected argument 'outbound_ip_address_lists' to be a list")
        pulumi.set(__self__, "outbound_ip_address_lists", outbound_ip_address_lists)
        if outbound_ip_addresses and not isinstance(outbound_ip_addresses, str):
            raise TypeError("Expected argument 'outbound_ip_addresses' to be a str")
        pulumi.set(__self__, "outbound_ip_addresses", outbound_ip_addresses)
        if possible_outbound_ip_address_lists and not isinstance(possible_outbound_ip_address_lists, list):
            raise TypeError("Expected argument 'possible_outbound_ip_address_lists' to be a list")
        pulumi.set(__self__, "possible_outbound_ip_address_lists", possible_outbound_ip_address_lists)
        if possible_outbound_ip_addresses and not isinstance(possible_outbound_ip_addresses, str):
            raise TypeError("Expected argument 'possible_outbound_ip_addresses' to be a str")
        pulumi.set(__self__, "possible_outbound_ip_addresses", possible_outbound_ip_addresses)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if service_plan_id and not isinstance(service_plan_id, str):
            raise TypeError("Expected argument 'service_plan_id' to be a str")
        pulumi.set(__self__, "service_plan_id", service_plan_id)
        if site_configs and not isinstance(site_configs, list):
            raise TypeError("Expected argument 'site_configs' to be a list")
        pulumi.set(__self__, "site_configs", site_configs)
        if site_credentials and not isinstance(site_credentials, list):
            raise TypeError("Expected argument 'site_credentials' to be a list")
        pulumi.set(__self__, "site_credentials", site_credentials)
        if sticky_settings and not isinstance(sticky_settings, list):
            raise TypeError("Expected argument 'sticky_settings' to be a list")
        pulumi.set(__self__, "sticky_settings", sticky_settings)
        if storage_account_access_key and not isinstance(storage_account_access_key, str):
            raise TypeError("Expected argument 'storage_account_access_key' to be a str")
        pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_account_name and not isinstance(storage_account_name, str):
            raise TypeError("Expected argument 'storage_account_name' to be a str")
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if storage_key_vault_secret_id and not isinstance(storage_key_vault_secret_id, str):
            raise TypeError("Expected argument 'storage_key_vault_secret_id' to be a str")
        pulumi.set(__self__, "storage_key_vault_secret_id", storage_key_vault_secret_id)
        if storage_uses_managed_identity and not isinstance(storage_uses_managed_identity, bool):
            raise TypeError("Expected argument 'storage_uses_managed_identity' to be a bool")
        pulumi.set(__self__, "storage_uses_managed_identity", storage_uses_managed_identity)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if virtual_network_subnet_id and not isinstance(virtual_network_subnet_id, str):
            raise TypeError("Expected argument 'virtual_network_subnet_id' to be a str")
        pulumi.set(__self__, "virtual_network_subnet_id", virtual_network_subnet_id)

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> Mapping[str, str]:
        """
        A map of key-value pairs for [App Settings](https://docs.microsoft.com/azure/azure-functions/functions-app-settings) and custom values.
        """
        return pulumi.get(self, "app_settings")

    @property
    @pulumi.getter(name="authSettings")
    def auth_settings(self) -> Sequence['outputs.GetLinuxFunctionAppAuthSettingResult']:
        """
        A `auth_settings` block as defined below.
        """
        return pulumi.get(self, "auth_settings")

    @property
    @pulumi.getter(name="authSettingsV2s")
    def auth_settings_v2s(self) -> Sequence['outputs.GetLinuxFunctionAppAuthSettingsV2Result']:
        """
        A `auth_settings_v2` block as defined below.
        """
        return pulumi.get(self, "auth_settings_v2s")

    @property
    @pulumi.getter
    def backups(self) -> Sequence['outputs.GetLinuxFunctionAppBackupResult']:
        """
        A `backup` block as defined below.
        """
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="builtinLoggingEnabled")
    def builtin_logging_enabled(self) -> bool:
        """
        Is built in logging enabled?
        """
        return pulumi.get(self, "builtin_logging_enabled")

    @property
    @pulumi.getter(name="clientCertificateEnabled")
    def client_certificate_enabled(self) -> bool:
        """
        Are Client Certificates enabled?
        """
        return pulumi.get(self, "client_certificate_enabled")

    @property
    @pulumi.getter(name="clientCertificateExclusionPaths")
    def client_certificate_exclusion_paths(self) -> str:
        """
        Paths to exclude when using client certificates, separated by ;
        """
        return pulumi.get(self, "client_certificate_exclusion_paths")

    @property
    @pulumi.getter(name="clientCertificateMode")
    def client_certificate_mode(self) -> str:
        """
        The mode of the Function App's client certificates requirement for incoming requests.
        """
        return pulumi.get(self, "client_certificate_mode")

    @property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(self) -> Sequence['outputs.GetLinuxFunctionAppConnectionStringResult']:
        """
        A `connection_string` blocks as defined below.
        """
        return pulumi.get(self, "connection_strings")

    @property
    @pulumi.getter(name="contentShareForceDisabled")
    def content_share_force_disabled(self) -> bool:
        """
        Are the settings for linking the Function App to storage suppressed?
        """
        return pulumi.get(self, "content_share_force_disabled")

    @property
    @pulumi.getter(name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> str:
        """
        The identifier used by App Service to perform domain ownership verification via DNS TXT record.
        """
        return pulumi.get(self, "custom_domain_verification_id")

    @property
    @pulumi.getter(name="dailyMemoryTimeQuota")
    def daily_memory_time_quota(self) -> int:
        """
        The amount of memory in gigabyte-seconds that your application is allowed to consume per day.
        """
        return pulumi.get(self, "daily_memory_time_quota")

    @property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> str:
        """
        The default hostname of the Linux Function App.
        """
        return pulumi.get(self, "default_hostname")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Is this backup job enabled?
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="functionsExtensionVersion")
    def functions_extension_version(self) -> str:
        """
        The runtime version associated with the Function App.
        """
        return pulumi.get(self, "functions_extension_version")

    @property
    @pulumi.getter(name="hostingEnvironmentId")
    def hosting_environment_id(self) -> str:
        """
        The ID of the App Service Environment used by Function App.
        """
        return pulumi.get(self, "hosting_environment_id")

    @property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> bool:
        """
        Can the Function App only be accessed via HTTPS?
        """
        return pulumi.get(self, "https_only")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetLinuxFunctionAppIdentityResult']:
        """
        A `identity` block as defined below.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The Kind value for this Linux Function App.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the Linux Function App exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Site Credentials Username used for publishing.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundIpAddressLists")
    def outbound_ip_address_lists(self) -> Sequence[str]:
        """
        A list of outbound IP addresses. For example `["52.23.25.3", "52.143.43.12"]`
        """
        return pulumi.get(self, "outbound_ip_address_lists")

    @property
    @pulumi.getter(name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> str:
        """
        A comma separated list of outbound IP addresses as a string. For example `52.23.25.3,52.143.43.12`.
        """
        return pulumi.get(self, "outbound_ip_addresses")

    @property
    @pulumi.getter(name="possibleOutboundIpAddressLists")
    def possible_outbound_ip_address_lists(self) -> Sequence[str]:
        """
        A list of possible outbound IP addresses, not all of which are necessarily in use. This is a superset of `outbound_ip_address_list`. For example `["52.23.25.3", "52.143.43.12"]`.
        """
        return pulumi.get(self, "possible_outbound_ip_address_lists")

    @property
    @pulumi.getter(name="possibleOutboundIpAddresses")
    def possible_outbound_ip_addresses(self) -> str:
        """
        A comma separated list of possible outbound IP addresses as a string. For example `52.23.25.3,52.143.43.12,52.143.43.17`. This is a superset of `outbound_ip_addresses`. For example `["52.23.25.3", "52.143.43.12","52.143.43.17"]`.
        """
        return pulumi.get(self, "possible_outbound_ip_addresses")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="servicePlanId")
    def service_plan_id(self) -> str:
        """
        The ID of the App Service Plan within which this Function App has been created.
        """
        return pulumi.get(self, "service_plan_id")

    @property
    @pulumi.getter(name="siteConfigs")
    def site_configs(self) -> Sequence['outputs.GetLinuxFunctionAppSiteConfigResult']:
        """
        A `site_config` block as defined below.
        """
        return pulumi.get(self, "site_configs")

    @property
    @pulumi.getter(name="siteCredentials")
    def site_credentials(self) -> Sequence['outputs.GetLinuxFunctionAppSiteCredentialResult']:
        """
        A `site_credential` block as defined below.
        """
        return pulumi.get(self, "site_credentials")

    @property
    @pulumi.getter(name="stickySettings")
    def sticky_settings(self) -> Sequence['outputs.GetLinuxFunctionAppStickySettingResult']:
        """
        A `sticky_settings` block as defined below.
        """
        return pulumi.get(self, "sticky_settings")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> str:
        """
        The access key used to access the backend storage account for the Function App.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> str:
        """
        The backend storage account name used by this Function App.
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="storageKeyVaultSecretId")
    def storage_key_vault_secret_id(self) -> str:
        """
        The Key Vault Secret ID, including version, that contains the Connection String to connect to the storage account for this Function App.
        """
        return pulumi.get(self, "storage_key_vault_secret_id")

    @property
    @pulumi.getter(name="storageUsesManagedIdentity")
    def storage_uses_managed_identity(self) -> bool:
        """
        Does the Function App use Managed Identity to access the storage account?
        """
        return pulumi.get(self, "storage_uses_managed_identity")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags which are assigned to the Linux Function App.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> str:
        """
        The Virtual Network Subnet ID used for this IP Restriction.
        """
        return pulumi.get(self, "virtual_network_subnet_id")


class AwaitableGetLinuxFunctionAppResult(GetLinuxFunctionAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLinuxFunctionAppResult(
            app_settings=self.app_settings,
            auth_settings=self.auth_settings,
            auth_settings_v2s=self.auth_settings_v2s,
            backups=self.backups,
            builtin_logging_enabled=self.builtin_logging_enabled,
            client_certificate_enabled=self.client_certificate_enabled,
            client_certificate_exclusion_paths=self.client_certificate_exclusion_paths,
            client_certificate_mode=self.client_certificate_mode,
            connection_strings=self.connection_strings,
            content_share_force_disabled=self.content_share_force_disabled,
            custom_domain_verification_id=self.custom_domain_verification_id,
            daily_memory_time_quota=self.daily_memory_time_quota,
            default_hostname=self.default_hostname,
            enabled=self.enabled,
            functions_extension_version=self.functions_extension_version,
            hosting_environment_id=self.hosting_environment_id,
            https_only=self.https_only,
            id=self.id,
            identities=self.identities,
            kind=self.kind,
            location=self.location,
            name=self.name,
            outbound_ip_address_lists=self.outbound_ip_address_lists,
            outbound_ip_addresses=self.outbound_ip_addresses,
            possible_outbound_ip_address_lists=self.possible_outbound_ip_address_lists,
            possible_outbound_ip_addresses=self.possible_outbound_ip_addresses,
            resource_group_name=self.resource_group_name,
            service_plan_id=self.service_plan_id,
            site_configs=self.site_configs,
            site_credentials=self.site_credentials,
            sticky_settings=self.sticky_settings,
            storage_account_access_key=self.storage_account_access_key,
            storage_account_name=self.storage_account_name,
            storage_key_vault_secret_id=self.storage_key_vault_secret_id,
            storage_uses_managed_identity=self.storage_uses_managed_identity,
            tags=self.tags,
            virtual_network_subnet_id=self.virtual_network_subnet_id)


def get_linux_function_app(name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLinuxFunctionAppResult:
    """
    Use this data source to access information about an existing Linux Function App.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_linux_function_app(name="existing",
        resource_group_name="existing")
    pulumi.export("id", example.id)
    ```


    :param str name: The name which should be used for this Linux Function App.
    :param str resource_group_name: The name of the Resource Group where the Linux Function App should exist.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:appservice/getLinuxFunctionApp:getLinuxFunctionApp', __args__, opts=opts, typ=GetLinuxFunctionAppResult).value

    return AwaitableGetLinuxFunctionAppResult(
        app_settings=__ret__.app_settings,
        auth_settings=__ret__.auth_settings,
        auth_settings_v2s=__ret__.auth_settings_v2s,
        backups=__ret__.backups,
        builtin_logging_enabled=__ret__.builtin_logging_enabled,
        client_certificate_enabled=__ret__.client_certificate_enabled,
        client_certificate_exclusion_paths=__ret__.client_certificate_exclusion_paths,
        client_certificate_mode=__ret__.client_certificate_mode,
        connection_strings=__ret__.connection_strings,
        content_share_force_disabled=__ret__.content_share_force_disabled,
        custom_domain_verification_id=__ret__.custom_domain_verification_id,
        daily_memory_time_quota=__ret__.daily_memory_time_quota,
        default_hostname=__ret__.default_hostname,
        enabled=__ret__.enabled,
        functions_extension_version=__ret__.functions_extension_version,
        hosting_environment_id=__ret__.hosting_environment_id,
        https_only=__ret__.https_only,
        id=__ret__.id,
        identities=__ret__.identities,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        outbound_ip_address_lists=__ret__.outbound_ip_address_lists,
        outbound_ip_addresses=__ret__.outbound_ip_addresses,
        possible_outbound_ip_address_lists=__ret__.possible_outbound_ip_address_lists,
        possible_outbound_ip_addresses=__ret__.possible_outbound_ip_addresses,
        resource_group_name=__ret__.resource_group_name,
        service_plan_id=__ret__.service_plan_id,
        site_configs=__ret__.site_configs,
        site_credentials=__ret__.site_credentials,
        sticky_settings=__ret__.sticky_settings,
        storage_account_access_key=__ret__.storage_account_access_key,
        storage_account_name=__ret__.storage_account_name,
        storage_key_vault_secret_id=__ret__.storage_key_vault_secret_id,
        storage_uses_managed_identity=__ret__.storage_uses_managed_identity,
        tags=__ret__.tags,
        virtual_network_subnet_id=__ret__.virtual_network_subnet_id)


@_utilities.lift_output_func(get_linux_function_app)
def get_linux_function_app_output(name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLinuxFunctionAppResult]:
    """
    Use this data source to access information about an existing Linux Function App.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_linux_function_app(name="existing",
        resource_group_name="existing")
    pulumi.export("id", example.id)
    ```


    :param str name: The name which should be used for this Linux Function App.
    :param str resource_group_name: The name of the Resource Group where the Linux Function App should exist.
    """
    ...
