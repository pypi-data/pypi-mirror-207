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

__all__ = ['FrontdoorSecretArgs', 'FrontdoorSecret']

@pulumi.input_type
class FrontdoorSecretArgs:
    def __init__(__self__, *,
                 cdn_frontdoor_profile_id: pulumi.Input[str],
                 secret: pulumi.Input['FrontdoorSecretSecretArgs'],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FrontdoorSecret resource.
        :param pulumi.Input[str] cdn_frontdoor_profile_id: The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input['FrontdoorSecretSecretArgs'] secret: A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input[str] name: The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        """
        pulumi.set(__self__, "cdn_frontdoor_profile_id", cdn_frontdoor_profile_id)
        pulumi.set(__self__, "secret", secret)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="cdnFrontdoorProfileId")
    def cdn_frontdoor_profile_id(self) -> pulumi.Input[str]:
        """
        The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "cdn_frontdoor_profile_id")

    @cdn_frontdoor_profile_id.setter
    def cdn_frontdoor_profile_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cdn_frontdoor_profile_id", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input['FrontdoorSecretSecretArgs']:
        """
        A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input['FrontdoorSecretSecretArgs']):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FrontdoorSecretState:
    def __init__(__self__, *,
                 cdn_frontdoor_profile_id: Optional[pulumi.Input[str]] = None,
                 cdn_frontdoor_profile_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input['FrontdoorSecretSecretArgs']] = None):
        """
        Input properties used for looking up and filtering FrontdoorSecret resources.
        :param pulumi.Input[str] cdn_frontdoor_profile_id: The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input[str] cdn_frontdoor_profile_name: The name of the Front Door Profile containing this Front Door Secret.
        :param pulumi.Input[str] name: The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input['FrontdoorSecretSecretArgs'] secret: A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        """
        if cdn_frontdoor_profile_id is not None:
            pulumi.set(__self__, "cdn_frontdoor_profile_id", cdn_frontdoor_profile_id)
        if cdn_frontdoor_profile_name is not None:
            pulumi.set(__self__, "cdn_frontdoor_profile_name", cdn_frontdoor_profile_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="cdnFrontdoorProfileId")
    def cdn_frontdoor_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "cdn_frontdoor_profile_id")

    @cdn_frontdoor_profile_id.setter
    def cdn_frontdoor_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cdn_frontdoor_profile_id", value)

    @property
    @pulumi.getter(name="cdnFrontdoorProfileName")
    def cdn_frontdoor_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Front Door Profile containing this Front Door Secret.
        """
        return pulumi.get(self, "cdn_frontdoor_profile_name")

    @cdn_frontdoor_profile_name.setter
    def cdn_frontdoor_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cdn_frontdoor_profile_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input['FrontdoorSecretSecretArgs']]:
        """
        A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input['FrontdoorSecretSecretArgs']]):
        pulumi.set(self, "secret", value)


class FrontdoorSecret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cdn_frontdoor_profile_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[pulumi.InputType['FrontdoorSecretSecretArgs']]] = None,
                 __props__=None):
        """
        Manages a Front Door (standard/premium) Secret.

        ## Example Usage

        ```python
        import pulumi
        import base64
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        current = azure.core.get_client_config()
        frontdoor = azuread.get_service_principal(display_name="Microsoft.Azure.Cdn")
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=azurerm_resource_group["example"]["location"],
            resource_group_name=azurerm_resource_group["example"]["name"],
            tenant_id=current.tenant_id,
            sku_name="premium",
            soft_delete_retention_days=7,
            network_acls=azure.keyvault.KeyVaultNetworkAclsArgs(
                default_action="Deny",
                bypass="AzureServices",
                ip_rules=["10.0.0.0/24"],
            ),
            access_policies=[
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=current.tenant_id,
                    object_id=frontdoor.object_id,
                    secret_permissions=["Get"],
                ),
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=current.tenant_id,
                    object_id=current.object_id,
                    certificate_permissions=[
                        "Get",
                        "Import",
                        "Delete",
                        "Purge",
                    ],
                    secret_permissions=["Get"],
                ),
            ])
        example_certificate = azure.keyvault.Certificate("exampleCertificate",
            key_vault_id=azurerm_key_vault["test"]["id"],
            certificate=azure.keyvault.CertificateCertificateArgs(
                contents=(lambda path: base64.b64encode(open(path).read().encode()).decode())("my-certificate.pfx"),
            ))
        example_frontdoor_secret = azure.cdn.FrontdoorSecret("exampleFrontdoorSecret",
            cdn_frontdoor_profile_id=azurerm_cdn_frontdoor_profile["test"]["id"],
            secret=azure.cdn.FrontdoorSecretSecretArgs(
                customer_certificates=[azure.cdn.FrontdoorSecretSecretCustomerCertificateArgs(
                    key_vault_certificate_id=azurerm_key_vault_certificate["test"]["id"],
                )],
            ))
        ```

        ## Import

        Front Door Secrets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cdn/frontdoorSecret:FrontdoorSecret example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.Cdn/profiles/profile1/secrets/secrets1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cdn_frontdoor_profile_id: The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input[str] name: The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input[pulumi.InputType['FrontdoorSecretSecretArgs']] secret: A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FrontdoorSecretArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Front Door (standard/premium) Secret.

        ## Example Usage

        ```python
        import pulumi
        import base64
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        current = azure.core.get_client_config()
        frontdoor = azuread.get_service_principal(display_name="Microsoft.Azure.Cdn")
        example_key_vault = azure.keyvault.KeyVault("exampleKeyVault",
            location=azurerm_resource_group["example"]["location"],
            resource_group_name=azurerm_resource_group["example"]["name"],
            tenant_id=current.tenant_id,
            sku_name="premium",
            soft_delete_retention_days=7,
            network_acls=azure.keyvault.KeyVaultNetworkAclsArgs(
                default_action="Deny",
                bypass="AzureServices",
                ip_rules=["10.0.0.0/24"],
            ),
            access_policies=[
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=current.tenant_id,
                    object_id=frontdoor.object_id,
                    secret_permissions=["Get"],
                ),
                azure.keyvault.KeyVaultAccessPolicyArgs(
                    tenant_id=current.tenant_id,
                    object_id=current.object_id,
                    certificate_permissions=[
                        "Get",
                        "Import",
                        "Delete",
                        "Purge",
                    ],
                    secret_permissions=["Get"],
                ),
            ])
        example_certificate = azure.keyvault.Certificate("exampleCertificate",
            key_vault_id=azurerm_key_vault["test"]["id"],
            certificate=azure.keyvault.CertificateCertificateArgs(
                contents=(lambda path: base64.b64encode(open(path).read().encode()).decode())("my-certificate.pfx"),
            ))
        example_frontdoor_secret = azure.cdn.FrontdoorSecret("exampleFrontdoorSecret",
            cdn_frontdoor_profile_id=azurerm_cdn_frontdoor_profile["test"]["id"],
            secret=azure.cdn.FrontdoorSecretSecretArgs(
                customer_certificates=[azure.cdn.FrontdoorSecretSecretCustomerCertificateArgs(
                    key_vault_certificate_id=azurerm_key_vault_certificate["test"]["id"],
                )],
            ))
        ```

        ## Import

        Front Door Secrets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:cdn/frontdoorSecret:FrontdoorSecret example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.Cdn/profiles/profile1/secrets/secrets1
        ```

        :param str resource_name: The name of the resource.
        :param FrontdoorSecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FrontdoorSecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cdn_frontdoor_profile_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[pulumi.InputType['FrontdoorSecretSecretArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FrontdoorSecretArgs.__new__(FrontdoorSecretArgs)

            if cdn_frontdoor_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'cdn_frontdoor_profile_id'")
            __props__.__dict__["cdn_frontdoor_profile_id"] = cdn_frontdoor_profile_id
            __props__.__dict__["name"] = name
            if secret is None and not opts.urn:
                raise TypeError("Missing required property 'secret'")
            __props__.__dict__["secret"] = secret
            __props__.__dict__["cdn_frontdoor_profile_name"] = None
        super(FrontdoorSecret, __self__).__init__(
            'azure:cdn/frontdoorSecret:FrontdoorSecret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cdn_frontdoor_profile_id: Optional[pulumi.Input[str]] = None,
            cdn_frontdoor_profile_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            secret: Optional[pulumi.Input[pulumi.InputType['FrontdoorSecretSecretArgs']]] = None) -> 'FrontdoorSecret':
        """
        Get an existing FrontdoorSecret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cdn_frontdoor_profile_id: The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input[str] cdn_frontdoor_profile_name: The name of the Front Door Profile containing this Front Door Secret.
        :param pulumi.Input[str] name: The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        :param pulumi.Input[pulumi.InputType['FrontdoorSecretSecretArgs']] secret: A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FrontdoorSecretState.__new__(_FrontdoorSecretState)

        __props__.__dict__["cdn_frontdoor_profile_id"] = cdn_frontdoor_profile_id
        __props__.__dict__["cdn_frontdoor_profile_name"] = cdn_frontdoor_profile_name
        __props__.__dict__["name"] = name
        __props__.__dict__["secret"] = secret
        return FrontdoorSecret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cdnFrontdoorProfileId")
    def cdn_frontdoor_profile_id(self) -> pulumi.Output[str]:
        """
        The Resource ID of the Front Door Profile. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "cdn_frontdoor_profile_id")

    @property
    @pulumi.getter(name="cdnFrontdoorProfileName")
    def cdn_frontdoor_profile_name(self) -> pulumi.Output[str]:
        """
        The name of the Front Door Profile containing this Front Door Secret.
        """
        return pulumi.get(self, "cdn_frontdoor_profile_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Front Door Secret. Possible values must start with a letter or a number, only contain letters, numbers and hyphens and have a length of between 2 and 260 characters. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output['outputs.FrontdoorSecretSecret']:
        """
        A `secret` block as defined below. Changing this forces a new Front Door Secret to be created.
        """
        return pulumi.get(self, "secret")

