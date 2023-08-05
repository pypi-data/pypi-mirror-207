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
    'GetAgreementResult',
    'AwaitableGetAgreementResult',
    'get_agreement',
    'get_agreement_output',
]

@pulumi.output_type
class GetAgreementResult:
    """
    A collection of values returned by getAgreement.
    """
    def __init__(__self__, id=None, license_text_link=None, offer=None, plan=None, privacy_policy_link=None, publisher=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if license_text_link and not isinstance(license_text_link, str):
            raise TypeError("Expected argument 'license_text_link' to be a str")
        pulumi.set(__self__, "license_text_link", license_text_link)
        if offer and not isinstance(offer, str):
            raise TypeError("Expected argument 'offer' to be a str")
        pulumi.set(__self__, "offer", offer)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if privacy_policy_link and not isinstance(privacy_policy_link, str):
            raise TypeError("Expected argument 'privacy_policy_link' to be a str")
        pulumi.set(__self__, "privacy_policy_link", privacy_policy_link)
        if publisher and not isinstance(publisher, str):
            raise TypeError("Expected argument 'publisher' to be a str")
        pulumi.set(__self__, "publisher", publisher)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="licenseTextLink")
    def license_text_link(self) -> str:
        return pulumi.get(self, "license_text_link")

    @property
    @pulumi.getter
    def offer(self) -> str:
        return pulumi.get(self, "offer")

    @property
    @pulumi.getter
    def plan(self) -> str:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="privacyPolicyLink")
    def privacy_policy_link(self) -> str:
        return pulumi.get(self, "privacy_policy_link")

    @property
    @pulumi.getter
    def publisher(self) -> str:
        return pulumi.get(self, "publisher")


class AwaitableGetAgreementResult(GetAgreementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgreementResult(
            id=self.id,
            license_text_link=self.license_text_link,
            offer=self.offer,
            plan=self.plan,
            privacy_policy_link=self.privacy_policy_link,
            publisher=self.publisher)


def get_agreement(offer: Optional[str] = None,
                  plan: Optional[str] = None,
                  publisher: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgreementResult:
    """
    Uses this data source to access information about an existing Marketplace Agreement.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    barracuda = azure.marketplace.get_agreement(publisher="barracudanetworks",
        offer="waf",
        plan="hourly")
    pulumi.export("azurermMarketplaceAgreementId", data["azurerm_marketplace_agreement"]["id"])
    ```


    :param str offer: The Offer of the Marketplace Image.
    :param str plan: The Plan of the Marketplace Image.
    :param str publisher: The Publisher of the Marketplace Image.
    """
    __args__ = dict()
    __args__['offer'] = offer
    __args__['plan'] = plan
    __args__['publisher'] = publisher
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:marketplace/getAgreement:getAgreement', __args__, opts=opts, typ=GetAgreementResult).value

    return AwaitableGetAgreementResult(
        id=__ret__.id,
        license_text_link=__ret__.license_text_link,
        offer=__ret__.offer,
        plan=__ret__.plan,
        privacy_policy_link=__ret__.privacy_policy_link,
        publisher=__ret__.publisher)


@_utilities.lift_output_func(get_agreement)
def get_agreement_output(offer: Optional[pulumi.Input[str]] = None,
                         plan: Optional[pulumi.Input[str]] = None,
                         publisher: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgreementResult]:
    """
    Uses this data source to access information about an existing Marketplace Agreement.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    barracuda = azure.marketplace.get_agreement(publisher="barracudanetworks",
        offer="waf",
        plan="hourly")
    pulumi.export("azurermMarketplaceAgreementId", data["azurerm_marketplace_agreement"]["id"])
    ```


    :param str offer: The Offer of the Marketplace Image.
    :param str plan: The Plan of the Marketplace Image.
    :param str publisher: The Publisher of the Marketplace Image.
    """
    ...
