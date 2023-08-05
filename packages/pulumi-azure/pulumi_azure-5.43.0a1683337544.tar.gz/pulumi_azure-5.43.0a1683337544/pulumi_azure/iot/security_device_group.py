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

__all__ = ['SecurityDeviceGroupArgs', 'SecurityDeviceGroup']

@pulumi.input_type
class SecurityDeviceGroupArgs:
    def __init__(__self__, *,
                 iothub_id: pulumi.Input[str],
                 allow_rule: Optional[pulumi.Input['SecurityDeviceGroupAllowRuleArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 range_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]]] = None):
        """
        The set of arguments for constructing a SecurityDeviceGroup resource.
        :param pulumi.Input[str] iothub_id: The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        :param pulumi.Input['SecurityDeviceGroupAllowRuleArgs'] allow_rule: an `allow_rule` blocks as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]] range_rules: One or more `range_rule` blocks as defined below.
        """
        pulumi.set(__self__, "iothub_id", iothub_id)
        if allow_rule is not None:
            pulumi.set(__self__, "allow_rule", allow_rule)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if range_rules is not None:
            pulumi.set(__self__, "range_rules", range_rules)

    @property
    @pulumi.getter(name="iothubId")
    def iothub_id(self) -> pulumi.Input[str]:
        """
        The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "iothub_id")

    @iothub_id.setter
    def iothub_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "iothub_id", value)

    @property
    @pulumi.getter(name="allowRule")
    def allow_rule(self) -> Optional[pulumi.Input['SecurityDeviceGroupAllowRuleArgs']]:
        """
        an `allow_rule` blocks as defined below.
        """
        return pulumi.get(self, "allow_rule")

    @allow_rule.setter
    def allow_rule(self, value: Optional[pulumi.Input['SecurityDeviceGroupAllowRuleArgs']]):
        pulumi.set(self, "allow_rule", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rangeRules")
    def range_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]]]:
        """
        One or more `range_rule` blocks as defined below.
        """
        return pulumi.get(self, "range_rules")

    @range_rules.setter
    def range_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]]]):
        pulumi.set(self, "range_rules", value)


@pulumi.input_type
class _SecurityDeviceGroupState:
    def __init__(__self__, *,
                 allow_rule: Optional[pulumi.Input['SecurityDeviceGroupAllowRuleArgs']] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 range_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering SecurityDeviceGroup resources.
        :param pulumi.Input['SecurityDeviceGroupAllowRuleArgs'] allow_rule: an `allow_rule` blocks as defined below.
        :param pulumi.Input[str] iothub_id: The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]] range_rules: One or more `range_rule` blocks as defined below.
        """
        if allow_rule is not None:
            pulumi.set(__self__, "allow_rule", allow_rule)
        if iothub_id is not None:
            pulumi.set(__self__, "iothub_id", iothub_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if range_rules is not None:
            pulumi.set(__self__, "range_rules", range_rules)

    @property
    @pulumi.getter(name="allowRule")
    def allow_rule(self) -> Optional[pulumi.Input['SecurityDeviceGroupAllowRuleArgs']]:
        """
        an `allow_rule` blocks as defined below.
        """
        return pulumi.get(self, "allow_rule")

    @allow_rule.setter
    def allow_rule(self, value: Optional[pulumi.Input['SecurityDeviceGroupAllowRuleArgs']]):
        pulumi.set(self, "allow_rule", value)

    @property
    @pulumi.getter(name="iothubId")
    def iothub_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "iothub_id")

    @iothub_id.setter
    def iothub_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iothub_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rangeRules")
    def range_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]]]:
        """
        One or more `range_rule` blocks as defined below.
        """
        return pulumi.get(self, "range_rules")

    @range_rules.setter
    def range_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityDeviceGroupRangeRuleArgs']]]]):
        pulumi.set(self, "range_rules", value)


class SecurityDeviceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_rule: Optional[pulumi.Input[pulumi.InputType['SecurityDeviceGroupAllowRuleArgs']]] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 range_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityDeviceGroupRangeRuleArgs']]]]] = None,
                 __props__=None):
        """
        Manages a Iot Security Device Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_io_t_hub = azure.iot.IoTHub("exampleIoTHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku=azure.iot.IoTHubSkuArgs(
                name="S1",
                capacity=1,
            ))
        example_security_solution = azure.iot.SecuritySolution("exampleSecuritySolution",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            display_name="Iot Security Solution",
            iothub_ids=[example_io_t_hub.id])
        example_security_device_group = azure.iot.SecurityDeviceGroup("exampleSecurityDeviceGroup",
            iothub_id=example_io_t_hub.id,
            allow_rule=azure.iot.SecurityDeviceGroupAllowRuleArgs(
                connection_to_ips_not_alloweds=["10.0.0.0/24"],
            ),
            range_rules=[azure.iot.SecurityDeviceGroupRangeRuleArgs(
                type="ActiveConnectionsNotInAllowedRange",
                min=0,
                max=30,
                duration="PT5M",
            )],
            opts=pulumi.ResourceOptions(depends_on=[example_security_solution]))
        ```

        ## Import

        Iot Security Device Group can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/securityDeviceGroup:SecurityDeviceGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.Devices/iotHubs/hub1/providers/Microsoft.Security/deviceSecurityGroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecurityDeviceGroupAllowRuleArgs']] allow_rule: an `allow_rule` blocks as defined below.
        :param pulumi.Input[str] iothub_id: The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityDeviceGroupRangeRuleArgs']]]] range_rules: One or more `range_rule` blocks as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityDeviceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Iot Security Device Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_io_t_hub = azure.iot.IoTHub("exampleIoTHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku=azure.iot.IoTHubSkuArgs(
                name="S1",
                capacity=1,
            ))
        example_security_solution = azure.iot.SecuritySolution("exampleSecuritySolution",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            display_name="Iot Security Solution",
            iothub_ids=[example_io_t_hub.id])
        example_security_device_group = azure.iot.SecurityDeviceGroup("exampleSecurityDeviceGroup",
            iothub_id=example_io_t_hub.id,
            allow_rule=azure.iot.SecurityDeviceGroupAllowRuleArgs(
                connection_to_ips_not_alloweds=["10.0.0.0/24"],
            ),
            range_rules=[azure.iot.SecurityDeviceGroupRangeRuleArgs(
                type="ActiveConnectionsNotInAllowedRange",
                min=0,
                max=30,
                duration="PT5M",
            )],
            opts=pulumi.ResourceOptions(depends_on=[example_security_solution]))
        ```

        ## Import

        Iot Security Device Group can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/securityDeviceGroup:SecurityDeviceGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.Devices/iotHubs/hub1/providers/Microsoft.Security/deviceSecurityGroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param SecurityDeviceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityDeviceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_rule: Optional[pulumi.Input[pulumi.InputType['SecurityDeviceGroupAllowRuleArgs']]] = None,
                 iothub_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 range_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityDeviceGroupRangeRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityDeviceGroupArgs.__new__(SecurityDeviceGroupArgs)

            __props__.__dict__["allow_rule"] = allow_rule
            if iothub_id is None and not opts.urn:
                raise TypeError("Missing required property 'iothub_id'")
            __props__.__dict__["iothub_id"] = iothub_id
            __props__.__dict__["name"] = name
            __props__.__dict__["range_rules"] = range_rules
        super(SecurityDeviceGroup, __self__).__init__(
            'azure:iot/securityDeviceGroup:SecurityDeviceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_rule: Optional[pulumi.Input[pulumi.InputType['SecurityDeviceGroupAllowRuleArgs']]] = None,
            iothub_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            range_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityDeviceGroupRangeRuleArgs']]]]] = None) -> 'SecurityDeviceGroup':
        """
        Get an existing SecurityDeviceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecurityDeviceGroupAllowRuleArgs']] allow_rule: an `allow_rule` blocks as defined below.
        :param pulumi.Input[str] iothub_id: The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityDeviceGroupRangeRuleArgs']]]] range_rules: One or more `range_rule` blocks as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityDeviceGroupState.__new__(_SecurityDeviceGroupState)

        __props__.__dict__["allow_rule"] = allow_rule
        __props__.__dict__["iothub_id"] = iothub_id
        __props__.__dict__["name"] = name
        __props__.__dict__["range_rules"] = range_rules
        return SecurityDeviceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowRule")
    def allow_rule(self) -> pulumi.Output[Optional['outputs.SecurityDeviceGroupAllowRule']]:
        """
        an `allow_rule` blocks as defined below.
        """
        return pulumi.get(self, "allow_rule")

    @property
    @pulumi.getter(name="iothubId")
    def iothub_id(self) -> pulumi.Output[str]:
        """
        The ID of the IoT Hub which to link the Security Device Group to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "iothub_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Device Security Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rangeRules")
    def range_rules(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityDeviceGroupRangeRule']]]:
        """
        One or more `range_rule` blocks as defined below.
        """
        return pulumi.get(self, "range_rules")

