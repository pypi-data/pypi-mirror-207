# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DicomServiceAuthenticationArgs',
    'DicomServiceIdentityArgs',
    'DicomServicePrivateEndpointArgs',
    'FhirServiceAuthenticationArgs',
    'FhirServiceCorsArgs',
    'FhirServiceIdentityArgs',
    'FhirServiceOciArtifactArgs',
    'MedtechServiceIdentityArgs',
    'ServiceAuthenticationConfigurationArgs',
    'ServiceCorsConfigurationArgs',
    'WorkspacePrivateEndpointConnectionArgs',
]

@pulumi.input_type
class DicomServiceAuthenticationArgs:
    def __init__(__self__, *,
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authority: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] audiences: The intended audience to receive authentication tokens for the service. The default value is <https://dicom.azurehealthcareapis.azure.com>
        """
        if audiences is not None:
            pulumi.set(__self__, "audiences", audiences)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The intended audience to receive authentication tokens for the service. The default value is <https://dicom.azurehealthcareapis.azure.com>
        """
        return pulumi.get(self, "audiences")

    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "audiences", value)

    @property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authority", value)


@pulumi.input_type
class DicomServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The type of identity used for the Healthcare DICOM service. Possible values are `UserAssigned`, `SystemAssigned` and `SystemAssigned, UserAssigned`. If `UserAssigned` is set, an `identity_ids` must be set as well.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: A list of User Assigned Identity IDs which should be assigned to this Healthcare DICOM service.
        """
        pulumi.set(__self__, "type", type)
        if identity_ids is not None:
            pulumi.set(__self__, "identity_ids", identity_ids)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of identity used for the Healthcare DICOM service. Possible values are `UserAssigned`, `SystemAssigned` and `SystemAssigned, UserAssigned`. If `UserAssigned` is set, an `identity_ids` must be set as well.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of User Assigned Identity IDs which should be assigned to this Healthcare DICOM service.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class DicomServicePrivateEndpointArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The ID of the Healthcare DICOM Service.
        :param pulumi.Input[str] name: Specifies the name of the Healthcare DICOM Service. Changing this forces a new Healthcare DICOM Service to be created.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Healthcare DICOM Service.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Healthcare DICOM Service. Changing this forces a new Healthcare DICOM Service to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class FhirServiceAuthenticationArgs:
    def __init__(__self__, *,
                 audience: pulumi.Input[str],
                 authority: pulumi.Input[str],
                 smart_proxy_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] audience: The intended audience to receive authentication tokens for the service. The default value is `https://<name>.fhir.azurehealthcareapis.com`.
        :param pulumi.Input[bool] smart_proxy_enabled: Whether smart proxy is enabled.
        """
        pulumi.set(__self__, "audience", audience)
        pulumi.set(__self__, "authority", authority)
        if smart_proxy_enabled is not None:
            pulumi.set(__self__, "smart_proxy_enabled", smart_proxy_enabled)

    @property
    @pulumi.getter
    def audience(self) -> pulumi.Input[str]:
        """
        The intended audience to receive authentication tokens for the service. The default value is `https://<name>.fhir.azurehealthcareapis.com`.
        """
        return pulumi.get(self, "audience")

    @audience.setter
    def audience(self, value: pulumi.Input[str]):
        pulumi.set(self, "audience", value)

    @property
    @pulumi.getter
    def authority(self) -> pulumi.Input[str]:
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: pulumi.Input[str]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether smart proxy is enabled.
        """
        return pulumi.get(self, "smart_proxy_enabled")

    @smart_proxy_enabled.setter
    def smart_proxy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "smart_proxy_enabled", value)


@pulumi.input_type
class FhirServiceCorsArgs:
    def __init__(__self__, *,
                 allowed_headers: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allowed_methods: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allowed_origins: pulumi.Input[Sequence[pulumi.Input[str]]],
                 credentials_allowed: Optional[pulumi.Input[bool]] = None,
                 max_age_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_headers: A set of headers to be allowed via CORS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_methods: The methods to be allowed via CORS. Possible values are `DELETE`, `GET`, `HEAD`, `MERGE`, `POST`, `OPTIONS`, `PATCH` and `PUT`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_origins: A set of origins to be allowed via CORS.
        :param pulumi.Input[bool] credentials_allowed: If credentials are allowed via CORS.
        :param pulumi.Input[int] max_age_in_seconds: The max age to be allowed via CORS.
        """
        pulumi.set(__self__, "allowed_headers", allowed_headers)
        pulumi.set(__self__, "allowed_methods", allowed_methods)
        pulumi.set(__self__, "allowed_origins", allowed_origins)
        if credentials_allowed is not None:
            pulumi.set(__self__, "credentials_allowed", credentials_allowed)
        if max_age_in_seconds is not None:
            pulumi.set(__self__, "max_age_in_seconds", max_age_in_seconds)

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A set of headers to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_headers")

    @allowed_headers.setter
    def allowed_headers(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_headers", value)

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The methods to be allowed via CORS. Possible values are `DELETE`, `GET`, `HEAD`, `MERGE`, `POST`, `OPTIONS`, `PATCH` and `PUT`.
        """
        return pulumi.get(self, "allowed_methods")

    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_methods", value)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A set of origins to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_origins")

    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_origins", value)

    @property
    @pulumi.getter(name="credentialsAllowed")
    def credentials_allowed(self) -> Optional[pulumi.Input[bool]]:
        """
        If credentials are allowed via CORS.
        """
        return pulumi.get(self, "credentials_allowed")

    @credentials_allowed.setter
    def credentials_allowed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "credentials_allowed", value)

    @property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The max age to be allowed via CORS.
        """
        return pulumi.get(self, "max_age_in_seconds")

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_age_in_seconds", value)


@pulumi.input_type
class FhirServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The type of managed identity to assign. Possible values are `UserAssigned` and `SystemAssigned`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: A list of one or more Resource IDs for User Assigned Managed identities to assign. Required when `type` is set to `UserAssigned`.
        """
        pulumi.set(__self__, "type", type)
        if identity_ids is not None:
            pulumi.set(__self__, "identity_ids", identity_ids)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of managed identity to assign. Possible values are `UserAssigned` and `SystemAssigned`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of one or more Resource IDs for User Assigned Managed identities to assign. Required when `type` is set to `UserAssigned`.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class FhirServiceOciArtifactArgs:
    def __init__(__self__, *,
                 login_server: pulumi.Input[str],
                 digest: Optional[pulumi.Input[str]] = None,
                 image_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] login_server: An Azure container registry used for export operations of the service instance.
        :param pulumi.Input[str] digest: A digest of an image within Azure container registry used for export operations of the service instance to narrow the artifacts down.
        :param pulumi.Input[str] image_name: An image within Azure container registry used for export operations of the service instance.
        """
        pulumi.set(__self__, "login_server", login_server)
        if digest is not None:
            pulumi.set(__self__, "digest", digest)
        if image_name is not None:
            pulumi.set(__self__, "image_name", image_name)

    @property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> pulumi.Input[str]:
        """
        An Azure container registry used for export operations of the service instance.
        """
        return pulumi.get(self, "login_server")

    @login_server.setter
    def login_server(self, value: pulumi.Input[str]):
        pulumi.set(self, "login_server", value)

    @property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input[str]]:
        """
        A digest of an image within Azure container registry used for export operations of the service instance to narrow the artifacts down.
        """
        return pulumi.get(self, "digest")

    @digest.setter
    def digest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "digest", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        """
        An image within Azure container registry used for export operations of the service instance.
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)


@pulumi.input_type
class MedtechServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the type of Managed Service Identity that should be configured on this Healthcare Med Tech Service. Possible values are `SystemAssigned`.
        :param pulumi.Input[str] principal_id: The Principal ID associated with this System Assigned Managed Service Identity.
        :param pulumi.Input[str] tenant_id: The Tenant ID associated with this System Assigned Managed Service Identity.
        """
        pulumi.set(__self__, "type", type)
        if identity_ids is not None:
            pulumi.set(__self__, "identity_ids", identity_ids)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Specifies the type of Managed Service Identity that should be configured on this Healthcare Med Tech Service. Possible values are `SystemAssigned`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID associated with this System Assigned Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID associated with this System Assigned Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class ServiceAuthenticationConfigurationArgs:
    def __init__(__self__, *,
                 audience: Optional[pulumi.Input[str]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 smart_proxy_enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] audience: The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com
        :param pulumi.Input[str] authority: The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
               Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.
        :param pulumi.Input[bool] smart_proxy_enabled: (Boolean) Enables the 'SMART on FHIR' option for mobile and web implementations.
        """
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if smart_proxy_enabled is not None:
            pulumi.set(__self__, "smart_proxy_enabled", smart_proxy_enabled)

    @property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[str]]:
        """
        The intended audience to receive authentication tokens for the service. The default value is https://azurehealthcareapis.com
        """
        return pulumi.get(self, "audience")

    @audience.setter
    def audience(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audience", value)

    @property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Active Directory (tenant) that serves as the authentication authority to access the service. The default authority is the Directory defined in the authentication scheme in use when running this provider.
        Authority must be registered to Azure AD and in the following format: https://{Azure-AD-endpoint}/{tenant-id}.
        """
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        (Boolean) Enables the 'SMART on FHIR' option for mobile and web implementations.
        """
        return pulumi.get(self, "smart_proxy_enabled")

    @smart_proxy_enabled.setter
    def smart_proxy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "smart_proxy_enabled", value)


@pulumi.input_type
class ServiceCorsConfigurationArgs:
    def __init__(__self__, *,
                 allow_credentials: Optional[pulumi.Input[bool]] = None,
                 allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_origins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 max_age_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[bool] allow_credentials: (Boolean) If credentials are allowed via CORS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_headers: A set of headers to be allowed via CORS.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_methods: The methods to be allowed via CORS. Possible values are `DELETE`, `GET`, `HEAD`, `MERGE`, `POST`, `OPTIONS`, `PATCH` and `PUT`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_origins: A set of origins to be allowed via CORS.
        :param pulumi.Input[int] max_age_in_seconds: The max age to be allowed via CORS.
        """
        if allow_credentials is not None:
            pulumi.set(__self__, "allow_credentials", allow_credentials)
        if allowed_headers is not None:
            pulumi.set(__self__, "allowed_headers", allowed_headers)
        if allowed_methods is not None:
            pulumi.set(__self__, "allowed_methods", allowed_methods)
        if allowed_origins is not None:
            pulumi.set(__self__, "allowed_origins", allowed_origins)
        if max_age_in_seconds is not None:
            pulumi.set(__self__, "max_age_in_seconds", max_age_in_seconds)

    @property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        (Boolean) If credentials are allowed via CORS.
        """
        return pulumi.get(self, "allow_credentials")

    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_credentials", value)

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of headers to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_headers")

    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_headers", value)

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The methods to be allowed via CORS. Possible values are `DELETE`, `GET`, `HEAD`, `MERGE`, `POST`, `OPTIONS`, `PATCH` and `PUT`.
        """
        return pulumi.get(self, "allowed_methods")

    @allowed_methods.setter
    def allowed_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_methods", value)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of origins to be allowed via CORS.
        """
        return pulumi.get(self, "allowed_origins")

    @allowed_origins.setter
    def allowed_origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_origins", value)

    @property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The max age to be allowed via CORS.
        """
        return pulumi.get(self, "max_age_in_seconds")

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_age_in_seconds", value)


@pulumi.input_type
class WorkspacePrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The ID of the Healthcare Workspace.
        :param pulumi.Input[str] name: Specifies the name of the Healthcare Workspace. Changing this forces a new Healthcare Workspace to be created.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Healthcare Workspace.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Healthcare Workspace. Changing this forces a new Healthcare Workspace to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


