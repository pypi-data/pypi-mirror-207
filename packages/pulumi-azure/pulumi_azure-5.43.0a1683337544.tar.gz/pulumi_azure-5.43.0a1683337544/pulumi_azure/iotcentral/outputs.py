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
    'ApplicationIdentity',
    'ApplicationNetworkRuleSetIpRule',
]

@pulumi.output_type
class ApplicationIdentity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        :param str type: Specifies the type of Managed Service Identity that should be configured on this IoT Central Application. The only possible value is `SystemAssigned`.
        :param str principal_id: The Principal ID associated with this Managed Service Identity.
        :param str tenant_id: The Tenant ID associated with this Managed Service Identity.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the type of Managed Service Identity that should be configured on this IoT Central Application. The only possible value is `SystemAssigned`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The Principal ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class ApplicationNetworkRuleSetIpRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ipMask":
            suggest = "ip_mask"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationNetworkRuleSetIpRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationNetworkRuleSetIpRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationNetworkRuleSetIpRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ip_mask: str,
                 name: str):
        """
        :param str ip_mask: The IP address range in CIDR notation for the IP Rule.
        :param str name: The name of the IP Rule
        """
        pulumi.set(__self__, "ip_mask", ip_mask)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> str:
        """
        The IP address range in CIDR notation for the IP Rule.
        """
        return pulumi.get(self, "ip_mask")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the IP Rule
        """
        return pulumi.get(self, "name")


