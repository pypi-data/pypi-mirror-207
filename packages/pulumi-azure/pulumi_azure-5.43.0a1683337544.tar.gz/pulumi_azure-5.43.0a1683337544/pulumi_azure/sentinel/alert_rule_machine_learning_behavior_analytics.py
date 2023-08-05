# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AlertRuleMachineLearningBehaviorAnalyticsArgs', 'AlertRuleMachineLearningBehaviorAnalytics']

@pulumi.input_type
class AlertRuleMachineLearningBehaviorAnalyticsArgs:
    def __init__(__self__, *,
                 alert_rule_template_guid: pulumi.Input[str],
                 log_analytics_workspace_id: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AlertRuleMachineLearningBehaviorAnalytics resource.
        :param pulumi.Input[str] alert_rule_template_guid: The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[bool] enabled: Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        pulumi.set(__self__, "alert_rule_template_guid", alert_rule_template_guid)
        pulumi.set(__self__, "log_analytics_workspace_id", log_analytics_workspace_id)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="alertRuleTemplateGuid")
    def alert_rule_template_guid(self) -> pulumi.Input[str]:
        """
        The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "alert_rule_template_guid")

    @alert_rule_template_guid.setter
    def alert_rule_template_guid(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_rule_template_guid", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "log_analytics_workspace_id", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AlertRuleMachineLearningBehaviorAnalyticsState:
    def __init__(__self__, *,
                 alert_rule_template_guid: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AlertRuleMachineLearningBehaviorAnalytics resources.
        :param pulumi.Input[str] alert_rule_template_guid: The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[bool] enabled: Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[str] name: The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        if alert_rule_template_guid is not None:
            pulumi.set(__self__, "alert_rule_template_guid", alert_rule_template_guid)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if log_analytics_workspace_id is not None:
            pulumi.set(__self__, "log_analytics_workspace_id", log_analytics_workspace_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="alertRuleTemplateGuid")
    def alert_rule_template_guid(self) -> Optional[pulumi.Input[str]]:
        """
        The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "alert_rule_template_guid")

    @alert_rule_template_guid.setter
    def alert_rule_template_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_rule_template_guid", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_analytics_workspace_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class AlertRuleMachineLearningBehaviorAnalytics(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_rule_template_guid: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Sentinel Machine Learning Behavior Analytics Alert Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding", workspace_id=example_analytics_workspace.id)
        example_alert_rule_machine_learning_behavior_analytics = azure.sentinel.AlertRuleMachineLearningBehaviorAnalytics("exampleAlertRuleMachineLearningBehaviorAnalytics",
            log_analytics_workspace_id=example_analytics_workspace.id,
            alert_rule_template_guid="737a2ce1-70a3-4968-9e90-3e6aca836abf")
        ```

        ## Import

        Sentinel Machine Learning Behavior Analytics Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/alertRuleMachineLearningBehaviorAnalytics:AlertRuleMachineLearningBehaviorAnalytics example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/alertRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_rule_template_guid: The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[bool] enabled: Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[str] name: The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertRuleMachineLearningBehaviorAnalyticsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Sentinel Machine Learning Behavior Analytics Alert Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018")
        example_log_analytics_workspace_onboarding = azure.sentinel.LogAnalyticsWorkspaceOnboarding("exampleLogAnalyticsWorkspaceOnboarding", workspace_id=example_analytics_workspace.id)
        example_alert_rule_machine_learning_behavior_analytics = azure.sentinel.AlertRuleMachineLearningBehaviorAnalytics("exampleAlertRuleMachineLearningBehaviorAnalytics",
            log_analytics_workspace_id=example_analytics_workspace.id,
            alert_rule_template_guid="737a2ce1-70a3-4968-9e90-3e6aca836abf")
        ```

        ## Import

        Sentinel Machine Learning Behavior Analytics Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/alertRuleMachineLearningBehaviorAnalytics:AlertRuleMachineLearningBehaviorAnalytics example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/alertRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param AlertRuleMachineLearningBehaviorAnalyticsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertRuleMachineLearningBehaviorAnalyticsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_rule_template_guid: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlertRuleMachineLearningBehaviorAnalyticsArgs.__new__(AlertRuleMachineLearningBehaviorAnalyticsArgs)

            if alert_rule_template_guid is None and not opts.urn:
                raise TypeError("Missing required property 'alert_rule_template_guid'")
            __props__.__dict__["alert_rule_template_guid"] = alert_rule_template_guid
            __props__.__dict__["enabled"] = enabled
            if log_analytics_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'log_analytics_workspace_id'")
            __props__.__dict__["log_analytics_workspace_id"] = log_analytics_workspace_id
            __props__.__dict__["name"] = name
        super(AlertRuleMachineLearningBehaviorAnalytics, __self__).__init__(
            'azure:sentinel/alertRuleMachineLearningBehaviorAnalytics:AlertRuleMachineLearningBehaviorAnalytics',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alert_rule_template_guid: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'AlertRuleMachineLearningBehaviorAnalytics':
        """
        Get an existing AlertRuleMachineLearningBehaviorAnalytics resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_rule_template_guid: The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[bool] enabled: Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        :param pulumi.Input[str] name: The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AlertRuleMachineLearningBehaviorAnalyticsState.__new__(_AlertRuleMachineLearningBehaviorAnalyticsState)

        __props__.__dict__["alert_rule_template_guid"] = alert_rule_template_guid
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["log_analytics_workspace_id"] = log_analytics_workspace_id
        __props__.__dict__["name"] = name
        return AlertRuleMachineLearningBehaviorAnalytics(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alertRuleTemplateGuid")
    def alert_rule_template_guid(self) -> pulumi.Output[str]:
        """
        The GUID of the alert rule template which is used for this Sentinel Machine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "alert_rule_template_guid")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should this Sentinel Machine Learning Behavior Analytics Alert Rule be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Log Analytics Workspace this SentinelMachine Learning Behavior Analytics Alert Rule belongs to. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this SentinelMachine Learning Behavior Analytics Alert Rule. Changing this forces a new Sentinel Machine Learning Behavior Analytics Alert Rule to be created.
        """
        return pulumi.get(self, "name")

