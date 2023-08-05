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

__all__ = ['ManagedInstanceFailoverGroupArgs', 'ManagedInstanceFailoverGroup']

@pulumi.input_type
class ManagedInstanceFailoverGroupArgs:
    def __init__(__self__, *,
                 managed_instance_id: pulumi.Input[str],
                 partner_managed_instance_id: pulumi.Input[str],
                 read_write_endpoint_failover_policy: pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs'],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 readonly_endpoint_failover_policy_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ManagedInstanceFailoverGroup resource.
        :param pulumi.Input[str] managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] partner_managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        :param pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs'] read_write_endpoint_failover_policy: A `read_write_endpoint_failover_policy` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] readonly_endpoint_failover_policy_enabled: Failover policy for the read-only endpoint. Defaults to `true`.
        """
        pulumi.set(__self__, "managed_instance_id", managed_instance_id)
        pulumi.set(__self__, "partner_managed_instance_id", partner_managed_instance_id)
        pulumi.set(__self__, "read_write_endpoint_failover_policy", read_write_endpoint_failover_policy)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if readonly_endpoint_failover_policy_enabled is not None:
            pulumi.set(__self__, "readonly_endpoint_failover_policy_enabled", readonly_endpoint_failover_policy_enabled)

    @property
    @pulumi.getter(name="managedInstanceId")
    def managed_instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "managed_instance_id")

    @managed_instance_id.setter
    def managed_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_id", value)

    @property
    @pulumi.getter(name="partnerManagedInstanceId")
    def partner_managed_instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "partner_managed_instance_id")

    @partner_managed_instance_id.setter
    def partner_managed_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "partner_managed_instance_id", value)

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']:
        """
        A `read_write_endpoint_failover_policy` block as defined below.
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @read_write_endpoint_failover_policy.setter
    def read_write_endpoint_failover_policy(self, value: pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']):
        pulumi.set(self, "read_write_endpoint_failover_policy", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicyEnabled")
    def readonly_endpoint_failover_policy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Failover policy for the read-only endpoint. Defaults to `true`.
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy_enabled")

    @readonly_endpoint_failover_policy_enabled.setter
    def readonly_endpoint_failover_policy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "readonly_endpoint_failover_policy_enabled", value)


@pulumi.input_type
class _ManagedInstanceFailoverGroupState:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_managed_instance_id: Optional[pulumi.Input[str]] = None,
                 partner_regions: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedInstanceFailoverGroupPartnerRegionArgs']]]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']] = None,
                 readonly_endpoint_failover_policy_enabled: Optional[pulumi.Input[bool]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ManagedInstanceFailoverGroup resources.
        :param pulumi.Input[str] location: The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] partner_managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['ManagedInstanceFailoverGroupPartnerRegionArgs']]] partner_regions: A `partner_region` block as defined below.
        :param pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs'] read_write_endpoint_failover_policy: A `read_write_endpoint_failover_policy` block as defined below.
        :param pulumi.Input[bool] readonly_endpoint_failover_policy_enabled: Failover policy for the read-only endpoint. Defaults to `true`.
        :param pulumi.Input[str] role: The partner replication role of the Managed Instance Failover Group.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_instance_id is not None:
            pulumi.set(__self__, "managed_instance_id", managed_instance_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if partner_managed_instance_id is not None:
            pulumi.set(__self__, "partner_managed_instance_id", partner_managed_instance_id)
        if partner_regions is not None:
            pulumi.set(__self__, "partner_regions", partner_regions)
        if read_write_endpoint_failover_policy is not None:
            pulumi.set(__self__, "read_write_endpoint_failover_policy", read_write_endpoint_failover_policy)
        if readonly_endpoint_failover_policy_enabled is not None:
            pulumi.set(__self__, "readonly_endpoint_failover_policy_enabled", readonly_endpoint_failover_policy_enabled)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedInstanceId")
    def managed_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "managed_instance_id")

    @managed_instance_id.setter
    def managed_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_instance_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="partnerManagedInstanceId")
    def partner_managed_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "partner_managed_instance_id")

    @partner_managed_instance_id.setter
    def partner_managed_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_managed_instance_id", value)

    @property
    @pulumi.getter(name="partnerRegions")
    def partner_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagedInstanceFailoverGroupPartnerRegionArgs']]]]:
        """
        A `partner_region` block as defined below.
        """
        return pulumi.get(self, "partner_regions")

    @partner_regions.setter
    def partner_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedInstanceFailoverGroupPartnerRegionArgs']]]]):
        pulumi.set(self, "partner_regions", value)

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> Optional[pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']]:
        """
        A `read_write_endpoint_failover_policy` block as defined below.
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @read_write_endpoint_failover_policy.setter
    def read_write_endpoint_failover_policy(self, value: Optional[pulumi.Input['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']]):
        pulumi.set(self, "read_write_endpoint_failover_policy", value)

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicyEnabled")
    def readonly_endpoint_failover_policy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Failover policy for the read-only endpoint. Defaults to `true`.
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy_enabled")

    @readonly_endpoint_failover_policy_enabled.setter
    def readonly_endpoint_failover_policy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "readonly_endpoint_failover_policy_enabled", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The partner replication role of the Managed Instance Failover Group.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


class ManagedInstanceFailoverGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_managed_instance_id: Optional[pulumi.Input[str]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
                 readonly_endpoint_failover_policy_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        ## Import

        SQL Instance Failover Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:mssql/managedInstanceFailoverGroup:ManagedInstanceFailoverGroup example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Sql/locations/Location/instanceFailoverGroups/failoverGroup1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] partner_managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']] read_write_endpoint_failover_policy: A `read_write_endpoint_failover_policy` block as defined below.
        :param pulumi.Input[bool] readonly_endpoint_failover_policy_enabled: Failover policy for the read-only endpoint. Defaults to `true`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstanceFailoverGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        SQL Instance Failover Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:mssql/managedInstanceFailoverGroup:ManagedInstanceFailoverGroup example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Sql/locations/Location/instanceFailoverGroups/failoverGroup1
        ```

        :param str resource_name: The name of the resource.
        :param ManagedInstanceFailoverGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstanceFailoverGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_managed_instance_id: Optional[pulumi.Input[str]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
                 readonly_endpoint_failover_policy_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedInstanceFailoverGroupArgs.__new__(ManagedInstanceFailoverGroupArgs)

            __props__.__dict__["location"] = location
            if managed_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_id'")
            __props__.__dict__["managed_instance_id"] = managed_instance_id
            __props__.__dict__["name"] = name
            if partner_managed_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'partner_managed_instance_id'")
            __props__.__dict__["partner_managed_instance_id"] = partner_managed_instance_id
            if read_write_endpoint_failover_policy is None and not opts.urn:
                raise TypeError("Missing required property 'read_write_endpoint_failover_policy'")
            __props__.__dict__["read_write_endpoint_failover_policy"] = read_write_endpoint_failover_policy
            __props__.__dict__["readonly_endpoint_failover_policy_enabled"] = readonly_endpoint_failover_policy_enabled
            __props__.__dict__["partner_regions"] = None
            __props__.__dict__["role"] = None
        super(ManagedInstanceFailoverGroup, __self__).__init__(
            'azure:mssql/managedInstanceFailoverGroup:ManagedInstanceFailoverGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            managed_instance_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            partner_managed_instance_id: Optional[pulumi.Input[str]] = None,
            partner_regions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupPartnerRegionArgs']]]]] = None,
            read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
            readonly_endpoint_failover_policy_enabled: Optional[pulumi.Input[bool]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'ManagedInstanceFailoverGroup':
        """
        Get an existing ManagedInstanceFailoverGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] partner_managed_instance_id: The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupPartnerRegionArgs']]]] partner_regions: A `partner_region` block as defined below.
        :param pulumi.Input[pulumi.InputType['ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicyArgs']] read_write_endpoint_failover_policy: A `read_write_endpoint_failover_policy` block as defined below.
        :param pulumi.Input[bool] readonly_endpoint_failover_policy_enabled: Failover policy for the read-only endpoint. Defaults to `true`.
        :param pulumi.Input[str] role: The partner replication role of the Managed Instance Failover Group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagedInstanceFailoverGroupState.__new__(_ManagedInstanceFailoverGroupState)

        __props__.__dict__["location"] = location
        __props__.__dict__["managed_instance_id"] = managed_instance_id
        __props__.__dict__["name"] = name
        __props__.__dict__["partner_managed_instance_id"] = partner_managed_instance_id
        __props__.__dict__["partner_regions"] = partner_regions
        __props__.__dict__["read_write_endpoint_failover_policy"] = read_write_endpoint_failover_policy
        __props__.__dict__["readonly_endpoint_failover_policy_enabled"] = readonly_endpoint_failover_policy_enabled
        __props__.__dict__["role"] = role
        return ManagedInstanceFailoverGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Managed Instance Failover Group should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedInstanceId")
    def managed_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the Azure SQL Managed Instance which will be replicated using a Managed Instance Failover Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "managed_instance_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Managed Instance Failover Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerManagedInstanceId")
    def partner_managed_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the Azure SQL Managed Instance which will be replicated to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "partner_managed_instance_id")

    @property
    @pulumi.getter(name="partnerRegions")
    def partner_regions(self) -> pulumi.Output[Sequence['outputs.ManagedInstanceFailoverGroupPartnerRegion']]:
        """
        A `partner_region` block as defined below.
        """
        return pulumi.get(self, "partner_regions")

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> pulumi.Output['outputs.ManagedInstanceFailoverGroupReadWriteEndpointFailoverPolicy']:
        """
        A `read_write_endpoint_failover_policy` block as defined below.
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicyEnabled")
    def readonly_endpoint_failover_policy_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Failover policy for the read-only endpoint. Defaults to `true`.
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy_enabled")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The partner replication role of the Managed Instance Failover Group.
        """
        return pulumi.get(self, "role")

