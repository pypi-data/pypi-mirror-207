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

__all__ = ['NetworkSliceArgs', 'NetworkSlice']

@pulumi.input_type
class NetworkSliceArgs:
    def __init__(__self__, *,
                 mobile_network_id: pulumi.Input[str],
                 single_network_slice_selection_assistance_information: pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkSlice resource.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs'] single_network_slice_selection_assistance_information: A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        :param pulumi.Input[str] description: A description for this Mobile Network Slice.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        pulumi.set(__self__, "single_network_slice_selection_assistance_information", single_network_slice_selection_assistance_information)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> pulumi.Input[str]:
        """
        The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "mobile_network_id")

    @mobile_network_id.setter
    def mobile_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "mobile_network_id", value)

    @property
    @pulumi.getter(name="singleNetworkSliceSelectionAssistanceInformation")
    def single_network_slice_selection_assistance_information(self) -> pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']:
        """
        A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        """
        return pulumi.get(self, "single_network_slice_selection_assistance_information")

    @single_network_slice_selection_assistance_information.setter
    def single_network_slice_selection_assistance_information(self, value: pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']):
        pulumi.set(self, "single_network_slice_selection_assistance_information", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this Mobile Network Slice.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _NetworkSliceState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 single_network_slice_selection_assistance_information: Optional[pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering NetworkSlice resources.
        :param pulumi.Input[str] description: A description for this Mobile Network Slice.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs'] single_network_slice_selection_assistance_information: A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mobile_network_id is not None:
            pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if single_network_slice_selection_assistance_information is not None:
            pulumi.set(__self__, "single_network_slice_selection_assistance_information", single_network_slice_selection_assistance_information)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this Mobile Network Slice.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "mobile_network_id")

    @mobile_network_id.setter
    def mobile_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mobile_network_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="singleNetworkSliceSelectionAssistanceInformation")
    def single_network_slice_selection_assistance_information(self) -> Optional[pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']]:
        """
        A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        """
        return pulumi.get(self, "single_network_slice_selection_assistance_information")

    @single_network_slice_selection_assistance_information.setter
    def single_network_slice_selection_assistance_information(self, value: Optional[pulumi.Input['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']]):
        pulumi.set(self, "single_network_slice_selection_assistance_information", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class NetworkSlice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 single_network_slice_selection_assistance_information: Optional[pulumi.Input[pulumi.InputType['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Mobile Network Slice.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_network = azure.mobile.Network("exampleNetwork",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            mobile_country_code="001",
            mobile_network_code="01")
        example_network_slice = azure.mobile.NetworkSlice("exampleNetworkSlice",
            mobile_network_id=azurerm_mobile_network["test"]["id"],
            location=example_resource_group.location,
            description="an example slice",
            single_network_slice_selection_assistance_information=azure.mobile.NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs(
                slice_service_type=1,
            ),
            tags={
                "key": "value",
            })
        ```

        ## Import

        Mobile Network Slice can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:mobile/networkSlice:NetworkSlice example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.MobileNetwork/mobileNetworks/mobileNetwork1/slices/slice1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for this Mobile Network Slice.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[pulumi.InputType['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']] single_network_slice_selection_assistance_information: A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkSliceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Mobile Network Slice.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_network = azure.mobile.Network("exampleNetwork",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            mobile_country_code="001",
            mobile_network_code="01")
        example_network_slice = azure.mobile.NetworkSlice("exampleNetworkSlice",
            mobile_network_id=azurerm_mobile_network["test"]["id"],
            location=example_resource_group.location,
            description="an example slice",
            single_network_slice_selection_assistance_information=azure.mobile.NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs(
                slice_service_type=1,
            ),
            tags={
                "key": "value",
            })
        ```

        ## Import

        Mobile Network Slice can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:mobile/networkSlice:NetworkSlice example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.MobileNetwork/mobileNetworks/mobileNetwork1/slices/slice1
        ```

        :param str resource_name: The name of the resource.
        :param NetworkSliceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkSliceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 single_network_slice_selection_assistance_information: Optional[pulumi.Input[pulumi.InputType['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkSliceArgs.__new__(NetworkSliceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            if mobile_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'mobile_network_id'")
            __props__.__dict__["mobile_network_id"] = mobile_network_id
            __props__.__dict__["name"] = name
            if single_network_slice_selection_assistance_information is None and not opts.urn:
                raise TypeError("Missing required property 'single_network_slice_selection_assistance_information'")
            __props__.__dict__["single_network_slice_selection_assistance_information"] = single_network_slice_selection_assistance_information
            __props__.__dict__["tags"] = tags
        super(NetworkSlice, __self__).__init__(
            'azure:mobile/networkSlice:NetworkSlice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            mobile_network_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            single_network_slice_selection_assistance_information: Optional[pulumi.Input[pulumi.InputType['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NetworkSlice':
        """
        Get an existing NetworkSlice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for this Mobile Network Slice.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[pulumi.InputType['NetworkSliceSingleNetworkSliceSelectionAssistanceInformationArgs']] single_network_slice_selection_assistance_information: A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkSliceState.__new__(_NetworkSliceState)

        __props__.__dict__["description"] = description
        __props__.__dict__["location"] = location
        __props__.__dict__["mobile_network_id"] = mobile_network_id
        __props__.__dict__["name"] = name
        __props__.__dict__["single_network_slice_selection_assistance_information"] = single_network_slice_selection_assistance_information
        __props__.__dict__["tags"] = tags
        return NetworkSlice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this Mobile Network Slice.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Mobile Network Slice should exist. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> pulumi.Output[str]:
        """
        The ID of Mobile Network which the Mobile Network Slice belongs to. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "mobile_network_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name which should be used for this Mobile Network Slice. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="singleNetworkSliceSelectionAssistanceInformation")
    def single_network_slice_selection_assistance_information(self) -> pulumi.Output['outputs.NetworkSliceSingleNetworkSliceSelectionAssistanceInformation']:
        """
        A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        """
        return pulumi.get(self, "single_network_slice_selection_assistance_information")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Mobile Network Slice.
        """
        return pulumi.get(self, "tags")

