# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FirewallRuleArgs', 'FirewallRule']

@pulumi.input_type
class FirewallRuleArgs:
    def __init__(__self__, *,
                 end_ip_address: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 start_ip_address: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallRule resource.
        :param pulumi.Input[str] end_ip_address: The ending IP address to allow through the firewall for this rule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The starting IP address to allow through the firewall for this rule.
        :param pulumi.Input[str] name: The name of the firewall rule. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "end_ip_address", end_ip_address)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        pulumi.set(__self__, "start_ip_address", start_ip_address)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[str]:
        """
        The ending IP address to allow through the firewall for this rule.
        """
        return pulumi.get(self, "end_ip_address")

    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "end_ip_address", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[str]:
        """
        The starting IP address to allow through the firewall for this rule.
        """
        return pulumi.get(self, "start_ip_address")

    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the firewall rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FirewallRuleState:
    def __init__(__self__, *,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FirewallRule resources.
        :param pulumi.Input[str] end_ip_address: The ending IP address to allow through the firewall for this rule.
        :param pulumi.Input[str] name: The name of the firewall rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The starting IP address to allow through the firewall for this rule.
        """
        if end_ip_address is not None:
            pulumi.set(__self__, "end_ip_address", end_ip_address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if start_ip_address is not None:
            pulumi.set(__self__, "start_ip_address", start_ip_address)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The ending IP address to allow through the firewall for this rule.
        """
        return pulumi.get(self, "end_ip_address")

    @end_ip_address.setter
    def end_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the firewall rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The starting IP address to allow through the firewall for this rule.
        """
        return pulumi.get(self, "start_ip_address")

    @start_ip_address.setter
    def start_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_ip_address", value)


class FirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_sql_server = azure.sql.SqlServer("exampleSqlServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="4dm1n157r470r",
            administrator_login_password="4-v3ry-53cr37-p455w0rd")
        example_firewall_rule = azure.sql.FirewallRule("exampleFirewallRule",
            resource_group_name=example_resource_group.name,
            server_name=example_sql_server.name,
            start_ip_address="10.0.17.62",
            end_ip_address="10.0.17.62")
        ```

        ## Import

        SQL Firewall Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sql/firewallRule:FirewallRule rule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Sql/servers/myserver/firewallRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_ip_address: The ending IP address to allow through the firewall for this rule.
        :param pulumi.Input[str] name: The name of the firewall rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The starting IP address to allow through the firewall for this rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_sql_server = azure.sql.SqlServer("exampleSqlServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="4dm1n157r470r",
            administrator_login_password="4-v3ry-53cr37-p455w0rd")
        example_firewall_rule = azure.sql.FirewallRule("exampleFirewallRule",
            resource_group_name=example_resource_group.name,
            server_name=example_sql_server.name,
            start_ip_address="10.0.17.62",
            end_ip_address="10.0.17.62")
        ```

        ## Import

        SQL Firewall Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sql/firewallRule:FirewallRule rule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Sql/servers/myserver/firewallRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param FirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_ip_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 start_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallRuleArgs.__new__(FirewallRuleArgs)

            if end_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'end_ip_address'")
            __props__.__dict__["end_ip_address"] = end_ip_address
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            if start_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'start_ip_address'")
            __props__.__dict__["start_ip_address"] = start_ip_address
        super(FirewallRule, __self__).__init__(
            'azure:sql/firewallRule:FirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            end_ip_address: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            server_name: Optional[pulumi.Input[str]] = None,
            start_ip_address: Optional[pulumi.Input[str]] = None) -> 'FirewallRule':
        """
        Get an existing FirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_ip_address: The ending IP address to allow through the firewall for this rule.
        :param pulumi.Input[str] name: The name of the firewall rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] start_ip_address: The starting IP address to allow through the firewall for this rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallRuleState.__new__(_FirewallRuleState)

        __props__.__dict__["end_ip_address"] = end_ip_address
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["server_name"] = server_name
        __props__.__dict__["start_ip_address"] = start_ip_address
        return FirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Output[str]:
        """
        The ending IP address to allow through the firewall for this rule.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the firewall rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the SQL Server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[str]:
        """
        The name of the SQL Server on which to create the Firewall Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Output[str]:
        """
        The starting IP address to allow through the firewall for this rule.
        """
        return pulumi.get(self, "start_ip_address")

