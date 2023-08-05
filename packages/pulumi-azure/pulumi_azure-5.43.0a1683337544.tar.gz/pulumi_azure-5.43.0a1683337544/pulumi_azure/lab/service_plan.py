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

__all__ = ['ServicePlanArgs', 'ServicePlan']

@pulumi.input_type
class ServicePlanArgs:
    def __init__(__self__, *,
                 allowed_regions: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_group_name: pulumi.Input[str],
                 default_auto_shutdown: Optional[pulumi.Input['ServicePlanDefaultAutoShutdownArgs']] = None,
                 default_connection: Optional[pulumi.Input['ServicePlanDefaultConnectionArgs']] = None,
                 default_network_subnet_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support: Optional[pulumi.Input['ServicePlanSupportArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServicePlan resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_regions: The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input['ServicePlanDefaultAutoShutdownArgs'] default_auto_shutdown: A `default_auto_shutdown` block as defined below.
        :param pulumi.Input['ServicePlanDefaultConnectionArgs'] default_connection: A `default_connection` block as defined below.
        :param pulumi.Input[str] default_network_subnet_id: The resource ID of the Subnet for the Lab Service Plan network profile.
        :param pulumi.Input[str] location: The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Lab Service Plan. Changing this forces a new resource to be created.
        :param pulumi.Input[str] shared_gallery_id: The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        :param pulumi.Input['ServicePlanSupportArgs'] support: A `support` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Lab Service Plan.
        """
        pulumi.set(__self__, "allowed_regions", allowed_regions)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if default_auto_shutdown is not None:
            pulumi.set(__self__, "default_auto_shutdown", default_auto_shutdown)
        if default_connection is not None:
            pulumi.set(__self__, "default_connection", default_connection)
        if default_network_subnet_id is not None:
            pulumi.set(__self__, "default_network_subnet_id", default_network_subnet_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if shared_gallery_id is not None:
            pulumi.set(__self__, "shared_gallery_id", shared_gallery_id)
        if support is not None:
            pulumi.set(__self__, "support", support)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        """
        return pulumi.get(self, "allowed_regions")

    @allowed_regions.setter
    def allowed_regions(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_regions", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="defaultAutoShutdown")
    def default_auto_shutdown(self) -> Optional[pulumi.Input['ServicePlanDefaultAutoShutdownArgs']]:
        """
        A `default_auto_shutdown` block as defined below.
        """
        return pulumi.get(self, "default_auto_shutdown")

    @default_auto_shutdown.setter
    def default_auto_shutdown(self, value: Optional[pulumi.Input['ServicePlanDefaultAutoShutdownArgs']]):
        pulumi.set(self, "default_auto_shutdown", value)

    @property
    @pulumi.getter(name="defaultConnection")
    def default_connection(self) -> Optional[pulumi.Input['ServicePlanDefaultConnectionArgs']]:
        """
        A `default_connection` block as defined below.
        """
        return pulumi.get(self, "default_connection")

    @default_connection.setter
    def default_connection(self, value: Optional[pulumi.Input['ServicePlanDefaultConnectionArgs']]):
        pulumi.set(self, "default_connection", value)

    @property
    @pulumi.getter(name="defaultNetworkSubnetId")
    def default_network_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Subnet for the Lab Service Plan network profile.
        """
        return pulumi.get(self, "default_network_subnet_id")

    @default_network_subnet_id.setter
    def default_network_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_network_subnet_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Lab Service Plan. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        """
        return pulumi.get(self, "shared_gallery_id")

    @shared_gallery_id.setter
    def shared_gallery_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_gallery_id", value)

    @property
    @pulumi.getter
    def support(self) -> Optional[pulumi.Input['ServicePlanSupportArgs']]:
        """
        A `support` block as defined below.
        """
        return pulumi.get(self, "support")

    @support.setter
    def support(self, value: Optional[pulumi.Input['ServicePlanSupportArgs']]):
        pulumi.set(self, "support", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Lab Service Plan.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ServicePlanState:
    def __init__(__self__, *,
                 allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_auto_shutdown: Optional[pulumi.Input['ServicePlanDefaultAutoShutdownArgs']] = None,
                 default_connection: Optional[pulumi.Input['ServicePlanDefaultConnectionArgs']] = None,
                 default_network_subnet_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support: Optional[pulumi.Input['ServicePlanSupportArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ServicePlan resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_regions: The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        :param pulumi.Input['ServicePlanDefaultAutoShutdownArgs'] default_auto_shutdown: A `default_auto_shutdown` block as defined below.
        :param pulumi.Input['ServicePlanDefaultConnectionArgs'] default_connection: A `default_connection` block as defined below.
        :param pulumi.Input[str] default_network_subnet_id: The resource ID of the Subnet for the Lab Service Plan network profile.
        :param pulumi.Input[str] location: The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Lab Service Plan. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] shared_gallery_id: The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        :param pulumi.Input['ServicePlanSupportArgs'] support: A `support` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Lab Service Plan.
        """
        if allowed_regions is not None:
            pulumi.set(__self__, "allowed_regions", allowed_regions)
        if default_auto_shutdown is not None:
            pulumi.set(__self__, "default_auto_shutdown", default_auto_shutdown)
        if default_connection is not None:
            pulumi.set(__self__, "default_connection", default_connection)
        if default_network_subnet_id is not None:
            pulumi.set(__self__, "default_network_subnet_id", default_network_subnet_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if shared_gallery_id is not None:
            pulumi.set(__self__, "shared_gallery_id", shared_gallery_id)
        if support is not None:
            pulumi.set(__self__, "support", support)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        """
        return pulumi.get(self, "allowed_regions")

    @allowed_regions.setter
    def allowed_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_regions", value)

    @property
    @pulumi.getter(name="defaultAutoShutdown")
    def default_auto_shutdown(self) -> Optional[pulumi.Input['ServicePlanDefaultAutoShutdownArgs']]:
        """
        A `default_auto_shutdown` block as defined below.
        """
        return pulumi.get(self, "default_auto_shutdown")

    @default_auto_shutdown.setter
    def default_auto_shutdown(self, value: Optional[pulumi.Input['ServicePlanDefaultAutoShutdownArgs']]):
        pulumi.set(self, "default_auto_shutdown", value)

    @property
    @pulumi.getter(name="defaultConnection")
    def default_connection(self) -> Optional[pulumi.Input['ServicePlanDefaultConnectionArgs']]:
        """
        A `default_connection` block as defined below.
        """
        return pulumi.get(self, "default_connection")

    @default_connection.setter
    def default_connection(self, value: Optional[pulumi.Input['ServicePlanDefaultConnectionArgs']]):
        pulumi.set(self, "default_connection", value)

    @property
    @pulumi.getter(name="defaultNetworkSubnetId")
    def default_network_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Subnet for the Lab Service Plan network profile.
        """
        return pulumi.get(self, "default_network_subnet_id")

    @default_network_subnet_id.setter
    def default_network_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_network_subnet_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Lab Service Plan. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        """
        return pulumi.get(self, "shared_gallery_id")

    @shared_gallery_id.setter
    def shared_gallery_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_gallery_id", value)

    @property
    @pulumi.getter
    def support(self) -> Optional[pulumi.Input['ServicePlanSupportArgs']]:
        """
        A `support` block as defined below.
        """
        return pulumi.get(self, "support")

    @support.setter
    def support(self, value: Optional[pulumi.Input['ServicePlanSupportArgs']]):
        pulumi.set(self, "support", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Lab Service Plan.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ServicePlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_auto_shutdown: Optional[pulumi.Input[pulumi.InputType['ServicePlanDefaultAutoShutdownArgs']]] = None,
                 default_connection: Optional[pulumi.Input[pulumi.InputType['ServicePlanDefaultConnectionArgs']]] = None,
                 default_network_subnet_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support: Optional[pulumi.Input[pulumi.InputType['ServicePlanSupportArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Lab Service Plan.

        > **Note:** Before using this resource, it's required to submit the request of registering the provider with Azure CLI `az provider register --namespace Microsoft.LabServices`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service_plan = azure.lab.ServicePlan("exampleServicePlan",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            allowed_regions=[example_resource_group.location])
        ```

        ## Import

        Lab Service Plans can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:lab/servicePlan:ServicePlan example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.LabServices/labPlans/labPlan1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_regions: The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        :param pulumi.Input[pulumi.InputType['ServicePlanDefaultAutoShutdownArgs']] default_auto_shutdown: A `default_auto_shutdown` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServicePlanDefaultConnectionArgs']] default_connection: A `default_connection` block as defined below.
        :param pulumi.Input[str] default_network_subnet_id: The resource ID of the Subnet for the Lab Service Plan network profile.
        :param pulumi.Input[str] location: The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Lab Service Plan. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] shared_gallery_id: The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        :param pulumi.Input[pulumi.InputType['ServicePlanSupportArgs']] support: A `support` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Lab Service Plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServicePlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Lab Service Plan.

        > **Note:** Before using this resource, it's required to submit the request of registering the provider with Azure CLI `az provider register --namespace Microsoft.LabServices`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service_plan = azure.lab.ServicePlan("exampleServicePlan",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            allowed_regions=[example_resource_group.location])
        ```

        ## Import

        Lab Service Plans can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:lab/servicePlan:ServicePlan example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.LabServices/labPlans/labPlan1
        ```

        :param str resource_name: The name of the resource.
        :param ServicePlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServicePlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_auto_shutdown: Optional[pulumi.Input[pulumi.InputType['ServicePlanDefaultAutoShutdownArgs']]] = None,
                 default_connection: Optional[pulumi.Input[pulumi.InputType['ServicePlanDefaultConnectionArgs']]] = None,
                 default_network_subnet_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support: Optional[pulumi.Input[pulumi.InputType['ServicePlanSupportArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServicePlanArgs.__new__(ServicePlanArgs)

            if allowed_regions is None and not opts.urn:
                raise TypeError("Missing required property 'allowed_regions'")
            __props__.__dict__["allowed_regions"] = allowed_regions
            __props__.__dict__["default_auto_shutdown"] = default_auto_shutdown
            __props__.__dict__["default_connection"] = default_connection
            __props__.__dict__["default_network_subnet_id"] = default_network_subnet_id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["shared_gallery_id"] = shared_gallery_id
            __props__.__dict__["support"] = support
            __props__.__dict__["tags"] = tags
        super(ServicePlan, __self__).__init__(
            'azure:lab/servicePlan:ServicePlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            default_auto_shutdown: Optional[pulumi.Input[pulumi.InputType['ServicePlanDefaultAutoShutdownArgs']]] = None,
            default_connection: Optional[pulumi.Input[pulumi.InputType['ServicePlanDefaultConnectionArgs']]] = None,
            default_network_subnet_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            shared_gallery_id: Optional[pulumi.Input[str]] = None,
            support: Optional[pulumi.Input[pulumi.InputType['ServicePlanSupportArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ServicePlan':
        """
        Get an existing ServicePlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_regions: The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        :param pulumi.Input[pulumi.InputType['ServicePlanDefaultAutoShutdownArgs']] default_auto_shutdown: A `default_auto_shutdown` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServicePlanDefaultConnectionArgs']] default_connection: A `default_connection` block as defined below.
        :param pulumi.Input[str] default_network_subnet_id: The resource ID of the Subnet for the Lab Service Plan network profile.
        :param pulumi.Input[str] location: The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Lab Service Plan. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] shared_gallery_id: The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        :param pulumi.Input[pulumi.InputType['ServicePlanSupportArgs']] support: A `support` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Lab Service Plan.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServicePlanState.__new__(_ServicePlanState)

        __props__.__dict__["allowed_regions"] = allowed_regions
        __props__.__dict__["default_auto_shutdown"] = default_auto_shutdown
        __props__.__dict__["default_connection"] = default_connection
        __props__.__dict__["default_network_subnet_id"] = default_network_subnet_id
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["shared_gallery_id"] = shared_gallery_id
        __props__.__dict__["support"] = support
        __props__.__dict__["tags"] = tags
        return ServicePlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> pulumi.Output[Sequence[str]]:
        """
        The allowed regions for the lab creator to use when creating labs using this Lab Service Plan. The allowed region's count must be between `1` and `28`.
        """
        return pulumi.get(self, "allowed_regions")

    @property
    @pulumi.getter(name="defaultAutoShutdown")
    def default_auto_shutdown(self) -> pulumi.Output[Optional['outputs.ServicePlanDefaultAutoShutdown']]:
        """
        A `default_auto_shutdown` block as defined below.
        """
        return pulumi.get(self, "default_auto_shutdown")

    @property
    @pulumi.getter(name="defaultConnection")
    def default_connection(self) -> pulumi.Output[Optional['outputs.ServicePlanDefaultConnection']]:
        """
        A `default_connection` block as defined below.
        """
        return pulumi.get(self, "default_connection")

    @property
    @pulumi.getter(name="defaultNetworkSubnetId")
    def default_network_subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the Subnet for the Lab Service Plan network profile.
        """
        return pulumi.get(self, "default_network_subnet_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Lab Service Plan. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Lab Service Plan should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the Shared Image Gallery attached to this Lab Service Plan. When saving a lab template virtual machine image it will be persisted in this gallery. The shared images from the gallery can be made available to use when creating new labs.
        """
        return pulumi.get(self, "shared_gallery_id")

    @property
    @pulumi.getter
    def support(self) -> pulumi.Output[Optional['outputs.ServicePlanSupport']]:
        """
        A `support` block as defined below.
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Lab Service Plan.
        """
        return pulumi.get(self, "tags")

