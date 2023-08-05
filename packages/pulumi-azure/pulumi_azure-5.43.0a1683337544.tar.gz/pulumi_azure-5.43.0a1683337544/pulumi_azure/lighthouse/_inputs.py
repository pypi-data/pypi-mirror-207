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
    'DefinitionAuthorizationArgs',
    'DefinitionEligibleAuthorizationArgs',
    'DefinitionEligibleAuthorizationJustInTimeAccessPolicyArgs',
    'DefinitionEligibleAuthorizationJustInTimeAccessPolicyApproverArgs',
    'DefinitionPlanArgs',
]

@pulumi.input_type
class DefinitionAuthorizationArgs:
    def __init__(__self__, *,
                 principal_id: pulumi.Input[str],
                 role_definition_id: pulumi.Input[str],
                 delegated_role_definition_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_display_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] principal_id: Principal ID of the security group/service principal/user that would be assigned permissions to the projected subscription.
        :param pulumi.Input[str] role_definition_id: The role definition identifier. This role will define the permissions that are granted to the principal. This cannot be an `Owner` role.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] delegated_role_definition_ids: The set of role definition ids which define all the permissions that the principal id can assign.
        :param pulumi.Input[str] principal_display_name: The display name of the security group/service principal/user that would be assigned permissions to the projected subscription.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if delegated_role_definition_ids is not None:
            pulumi.set(__self__, "delegated_role_definition_ids", delegated_role_definition_ids)
        if principal_display_name is not None:
            pulumi.set(__self__, "principal_display_name", principal_display_name)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        Principal ID of the security group/service principal/user that would be assigned permissions to the projected subscription.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[str]:
        """
        The role definition identifier. This role will define the permissions that are granted to the principal. This cannot be an `Owner` role.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter(name="delegatedRoleDefinitionIds")
    def delegated_role_definition_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of role definition ids which define all the permissions that the principal id can assign.
        """
        return pulumi.get(self, "delegated_role_definition_ids")

    @delegated_role_definition_ids.setter
    def delegated_role_definition_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "delegated_role_definition_ids", value)

    @property
    @pulumi.getter(name="principalDisplayName")
    def principal_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the security group/service principal/user that would be assigned permissions to the projected subscription.
        """
        return pulumi.get(self, "principal_display_name")

    @principal_display_name.setter
    def principal_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_display_name", value)


@pulumi.input_type
class DefinitionEligibleAuthorizationArgs:
    def __init__(__self__, *,
                 principal_id: pulumi.Input[str],
                 role_definition_id: pulumi.Input[str],
                 just_in_time_access_policy: Optional[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyArgs']] = None,
                 principal_display_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] principal_id: The Principal ID of the Azure Active Directory.
        :param pulumi.Input[str] role_definition_id: The Principal ID of the Azure built-in role that defines the permissions that the Azure Active Directory will have on the projected scope.
        :param pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyArgs'] just_in_time_access_policy: A `just_in_time_access_policy` block as defined below.
        :param pulumi.Input[str] principal_display_name: The display name of the Azure Active Directory Principal.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if just_in_time_access_policy is not None:
            pulumi.set(__self__, "just_in_time_access_policy", just_in_time_access_policy)
        if principal_display_name is not None:
            pulumi.set(__self__, "principal_display_name", principal_display_name)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        The Principal ID of the Azure Active Directory.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[str]:
        """
        The Principal ID of the Azure built-in role that defines the permissions that the Azure Active Directory will have on the projected scope.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter(name="justInTimeAccessPolicy")
    def just_in_time_access_policy(self) -> Optional[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyArgs']]:
        """
        A `just_in_time_access_policy` block as defined below.
        """
        return pulumi.get(self, "just_in_time_access_policy")

    @just_in_time_access_policy.setter
    def just_in_time_access_policy(self, value: Optional[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyArgs']]):
        pulumi.set(self, "just_in_time_access_policy", value)

    @property
    @pulumi.getter(name="principalDisplayName")
    def principal_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the Azure Active Directory Principal.
        """
        return pulumi.get(self, "principal_display_name")

    @principal_display_name.setter
    def principal_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_display_name", value)


@pulumi.input_type
class DefinitionEligibleAuthorizationJustInTimeAccessPolicyArgs:
    def __init__(__self__, *,
                 approvers: Optional[pulumi.Input[Sequence[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyApproverArgs']]]] = None,
                 maximum_activation_duration: Optional[pulumi.Input[str]] = None,
                 multi_factor_auth_provider: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyApproverArgs']]] approvers: An `approver` block as defined below.
        :param pulumi.Input[str] maximum_activation_duration: The maximum access duration in ISO 8601 format for just-in-time access requests. Defaults to `PT8H`.
        :param pulumi.Input[str] multi_factor_auth_provider: The multi-factor authorization provider to be used for just-in-time access requests. Possible value is `Azure`.
        """
        if approvers is not None:
            pulumi.set(__self__, "approvers", approvers)
        if maximum_activation_duration is not None:
            pulumi.set(__self__, "maximum_activation_duration", maximum_activation_duration)
        if multi_factor_auth_provider is not None:
            pulumi.set(__self__, "multi_factor_auth_provider", multi_factor_auth_provider)

    @property
    @pulumi.getter
    def approvers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyApproverArgs']]]]:
        """
        An `approver` block as defined below.
        """
        return pulumi.get(self, "approvers")

    @approvers.setter
    def approvers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DefinitionEligibleAuthorizationJustInTimeAccessPolicyApproverArgs']]]]):
        pulumi.set(self, "approvers", value)

    @property
    @pulumi.getter(name="maximumActivationDuration")
    def maximum_activation_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum access duration in ISO 8601 format for just-in-time access requests. Defaults to `PT8H`.
        """
        return pulumi.get(self, "maximum_activation_duration")

    @maximum_activation_duration.setter
    def maximum_activation_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maximum_activation_duration", value)

    @property
    @pulumi.getter(name="multiFactorAuthProvider")
    def multi_factor_auth_provider(self) -> Optional[pulumi.Input[str]]:
        """
        The multi-factor authorization provider to be used for just-in-time access requests. Possible value is `Azure`.
        """
        return pulumi.get(self, "multi_factor_auth_provider")

    @multi_factor_auth_provider.setter
    def multi_factor_auth_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "multi_factor_auth_provider", value)


@pulumi.input_type
class DefinitionEligibleAuthorizationJustInTimeAccessPolicyApproverArgs:
    def __init__(__self__, *,
                 principal_id: pulumi.Input[str],
                 principal_display_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] principal_id: The Principal ID of the Azure Active Directory principal for the approver.
        :param pulumi.Input[str] principal_display_name: The display name of the Azure Active Directory Principal for the approver.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        if principal_display_name is not None:
            pulumi.set(__self__, "principal_display_name", principal_display_name)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        The Principal ID of the Azure Active Directory principal for the approver.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="principalDisplayName")
    def principal_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the Azure Active Directory Principal for the approver.
        """
        return pulumi.get(self, "principal_display_name")

    @principal_display_name.setter
    def principal_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_display_name", value)


@pulumi.input_type
class DefinitionPlanArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 product: pulumi.Input[str],
                 publisher: pulumi.Input[str],
                 version: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The plan name of the marketplace offer.
        :param pulumi.Input[str] product: The product code of the plan.
        :param pulumi.Input[str] publisher: The publisher ID of the plan.
        :param pulumi.Input[str] version: The version of the plan.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "product", product)
        pulumi.set(__self__, "publisher", publisher)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The plan name of the marketplace offer.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def product(self) -> pulumi.Input[str]:
        """
        The product code of the plan.
        """
        return pulumi.get(self, "product")

    @product.setter
    def product(self, value: pulumi.Input[str]):
        pulumi.set(self, "product", value)

    @property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[str]:
        """
        The publisher ID of the plan.
        """
        return pulumi.get(self, "publisher")

    @publisher.setter
    def publisher(self, value: pulumi.Input[str]):
        pulumi.set(self, "publisher", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        The version of the plan.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)


