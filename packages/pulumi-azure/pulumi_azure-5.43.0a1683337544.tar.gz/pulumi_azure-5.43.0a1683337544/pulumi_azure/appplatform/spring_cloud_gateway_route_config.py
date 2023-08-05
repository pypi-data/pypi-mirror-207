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

__all__ = ['SpringCloudGatewayRouteConfigArgs', 'SpringCloudGatewayRouteConfig']

@pulumi.input_type
class SpringCloudGatewayRouteConfigArgs:
    def __init__(__self__, *,
                 spring_cloud_gateway_id: pulumi.Input[str],
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_api: Optional[pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs']] = None,
                 predicates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]]] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
                 sso_validation_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a SpringCloudGatewayRouteConfig resource.
        :param pulumi.Input[str] spring_cloud_gateway_id: The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] filters: Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs'] open_api: One or more `open_api` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] predicates: Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        :param pulumi.Input[str] protocol: Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        :param pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]] routes: One or more `route` blocks as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud App.
        :param pulumi.Input[bool] sso_validation_enabled: Should the sso validation be enabled in app level?
        """
        pulumi.set(__self__, "spring_cloud_gateway_id", spring_cloud_gateway_id)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if open_api is not None:
            pulumi.set(__self__, "open_api", open_api)
        if predicates is not None:
            pulumi.set(__self__, "predicates", predicates)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)
        if spring_cloud_app_id is not None:
            pulumi.set(__self__, "spring_cloud_app_id", spring_cloud_app_id)
        if sso_validation_enabled is not None:
            pulumi.set(__self__, "sso_validation_enabled", sso_validation_enabled)

    @property
    @pulumi.getter(name="springCloudGatewayId")
    def spring_cloud_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        """
        return pulumi.get(self, "spring_cloud_gateway_id")

    @spring_cloud_gateway_id.setter
    def spring_cloud_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "spring_cloud_gateway_id", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="openApi")
    def open_api(self) -> Optional[pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs']]:
        """
        One or more `open_api` blocks as defined below.
        """
        return pulumi.get(self, "open_api")

    @open_api.setter
    def open_api(self, value: Optional[pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs']]):
        pulumi.set(self, "open_api", value)

    @property
    @pulumi.getter
    def predicates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        """
        return pulumi.get(self, "predicates")

    @predicates.setter
    def predicates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "predicates", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]]]:
        """
        One or more `route` blocks as defined below.
        """
        return pulumi.get(self, "routes")

    @routes.setter
    def routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]]]):
        pulumi.set(self, "routes", value)

    @property
    @pulumi.getter(name="springCloudAppId")
    def spring_cloud_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud App.
        """
        return pulumi.get(self, "spring_cloud_app_id")

    @spring_cloud_app_id.setter
    def spring_cloud_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_app_id", value)

    @property
    @pulumi.getter(name="ssoValidationEnabled")
    def sso_validation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the sso validation be enabled in app level?
        """
        return pulumi.get(self, "sso_validation_enabled")

    @sso_validation_enabled.setter
    def sso_validation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sso_validation_enabled", value)


@pulumi.input_type
class _SpringCloudGatewayRouteConfigState:
    def __init__(__self__, *,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_api: Optional[pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs']] = None,
                 predicates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]]] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
                 spring_cloud_gateway_id: Optional[pulumi.Input[str]] = None,
                 sso_validation_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering SpringCloudGatewayRouteConfig resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] filters: Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs'] open_api: One or more `open_api` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] predicates: Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        :param pulumi.Input[str] protocol: Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        :param pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]] routes: One or more `route` blocks as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud App.
        :param pulumi.Input[str] spring_cloud_gateway_id: The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input[bool] sso_validation_enabled: Should the sso validation be enabled in app level?
        """
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if open_api is not None:
            pulumi.set(__self__, "open_api", open_api)
        if predicates is not None:
            pulumi.set(__self__, "predicates", predicates)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)
        if spring_cloud_app_id is not None:
            pulumi.set(__self__, "spring_cloud_app_id", spring_cloud_app_id)
        if spring_cloud_gateway_id is not None:
            pulumi.set(__self__, "spring_cloud_gateway_id", spring_cloud_gateway_id)
        if sso_validation_enabled is not None:
            pulumi.set(__self__, "sso_validation_enabled", sso_validation_enabled)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="openApi")
    def open_api(self) -> Optional[pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs']]:
        """
        One or more `open_api` blocks as defined below.
        """
        return pulumi.get(self, "open_api")

    @open_api.setter
    def open_api(self, value: Optional[pulumi.Input['SpringCloudGatewayRouteConfigOpenApiArgs']]):
        pulumi.set(self, "open_api", value)

    @property
    @pulumi.getter
    def predicates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        """
        return pulumi.get(self, "predicates")

    @predicates.setter
    def predicates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "predicates", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]]]:
        """
        One or more `route` blocks as defined below.
        """
        return pulumi.get(self, "routes")

    @routes.setter
    def routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SpringCloudGatewayRouteConfigRouteArgs']]]]):
        pulumi.set(self, "routes", value)

    @property
    @pulumi.getter(name="springCloudAppId")
    def spring_cloud_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud App.
        """
        return pulumi.get(self, "spring_cloud_app_id")

    @spring_cloud_app_id.setter
    def spring_cloud_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_app_id", value)

    @property
    @pulumi.getter(name="springCloudGatewayId")
    def spring_cloud_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        """
        return pulumi.get(self, "spring_cloud_gateway_id")

    @spring_cloud_gateway_id.setter
    def spring_cloud_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spring_cloud_gateway_id", value)

    @property
    @pulumi.getter(name="ssoValidationEnabled")
    def sso_validation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the sso validation be enabled in app level?
        """
        return pulumi.get(self, "sso_validation_enabled")

    @sso_validation_enabled.setter
    def sso_validation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sso_validation_enabled", value)


class SpringCloudGatewayRouteConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_api: Optional[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigOpenApiArgs']]] = None,
                 predicates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigRouteArgs']]]]] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
                 spring_cloud_gateway_id: Optional[pulumi.Input[str]] = None,
                 sso_validation_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a Spring Cloud Gateway Route Config.

        > **NOTE:** This resource is applicable only for Spring Cloud Service with enterprise tier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="E0")
        example_spring_cloud_app = azure.appplatform.SpringCloudApp("exampleSpringCloudApp",
            resource_group_name=example_resource_group.name,
            service_name=example_spring_cloud_service.name)
        example_spring_cloud_gateway = azure.appplatform.SpringCloudGateway("exampleSpringCloudGateway", spring_cloud_service_id=example_spring_cloud_service.id)
        example_spring_cloud_gateway_route_config = azure.appplatform.SpringCloudGatewayRouteConfig("exampleSpringCloudGatewayRouteConfig",
            spring_cloud_gateway_id=example_spring_cloud_gateway.id,
            spring_cloud_app_id=example_spring_cloud_app.id,
            protocol="HTTPS",
            routes=[azure.appplatform.SpringCloudGatewayRouteConfigRouteArgs(
                description="example description",
                filters=[
                    "StripPrefix=2",
                    "RateLimit=1,1s",
                ],
                order=1,
                predicates=["Path=/api5/customer/**"],
                sso_validation_enabled=True,
                title="myApp route config",
                token_relay=True,
                uri="https://www.example.com",
                classification_tags=[
                    "tag1",
                    "tag2",
                ],
            )])
        ```

        ## Import

        Spring Cloud Gateway Route Configs can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudGatewayRouteConfig:SpringCloudGatewayRouteConfig example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.AppPlatform/spring/service1/gateways/gateway1/routeConfigs/routeConfig1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] filters: Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigOpenApiArgs']] open_api: One or more `open_api` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] predicates: Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        :param pulumi.Input[str] protocol: Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigRouteArgs']]]] routes: One or more `route` blocks as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud App.
        :param pulumi.Input[str] spring_cloud_gateway_id: The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input[bool] sso_validation_enabled: Should the sso validation be enabled in app level?
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpringCloudGatewayRouteConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Spring Cloud Gateway Route Config.

        > **NOTE:** This resource is applicable only for Spring Cloud Service with enterprise tier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_spring_cloud_service = azure.appplatform.SpringCloudService("exampleSpringCloudService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku_name="E0")
        example_spring_cloud_app = azure.appplatform.SpringCloudApp("exampleSpringCloudApp",
            resource_group_name=example_resource_group.name,
            service_name=example_spring_cloud_service.name)
        example_spring_cloud_gateway = azure.appplatform.SpringCloudGateway("exampleSpringCloudGateway", spring_cloud_service_id=example_spring_cloud_service.id)
        example_spring_cloud_gateway_route_config = azure.appplatform.SpringCloudGatewayRouteConfig("exampleSpringCloudGatewayRouteConfig",
            spring_cloud_gateway_id=example_spring_cloud_gateway.id,
            spring_cloud_app_id=example_spring_cloud_app.id,
            protocol="HTTPS",
            routes=[azure.appplatform.SpringCloudGatewayRouteConfigRouteArgs(
                description="example description",
                filters=[
                    "StripPrefix=2",
                    "RateLimit=1,1s",
                ],
                order=1,
                predicates=["Path=/api5/customer/**"],
                sso_validation_enabled=True,
                title="myApp route config",
                token_relay=True,
                uri="https://www.example.com",
                classification_tags=[
                    "tag1",
                    "tag2",
                ],
            )])
        ```

        ## Import

        Spring Cloud Gateway Route Configs can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appplatform/springCloudGatewayRouteConfig:SpringCloudGatewayRouteConfig example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.AppPlatform/spring/service1/gateways/gateway1/routeConfigs/routeConfig1
        ```

        :param str resource_name: The name of the resource.
        :param SpringCloudGatewayRouteConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpringCloudGatewayRouteConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_api: Optional[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigOpenApiArgs']]] = None,
                 predicates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigRouteArgs']]]]] = None,
                 spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
                 spring_cloud_gateway_id: Optional[pulumi.Input[str]] = None,
                 sso_validation_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SpringCloudGatewayRouteConfigArgs.__new__(SpringCloudGatewayRouteConfigArgs)

            __props__.__dict__["filters"] = filters
            __props__.__dict__["name"] = name
            __props__.__dict__["open_api"] = open_api
            __props__.__dict__["predicates"] = predicates
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["routes"] = routes
            __props__.__dict__["spring_cloud_app_id"] = spring_cloud_app_id
            if spring_cloud_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'spring_cloud_gateway_id'")
            __props__.__dict__["spring_cloud_gateway_id"] = spring_cloud_gateway_id
            __props__.__dict__["sso_validation_enabled"] = sso_validation_enabled
        super(SpringCloudGatewayRouteConfig, __self__).__init__(
            'azure:appplatform/springCloudGatewayRouteConfig:SpringCloudGatewayRouteConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            open_api: Optional[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigOpenApiArgs']]] = None,
            predicates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigRouteArgs']]]]] = None,
            spring_cloud_app_id: Optional[pulumi.Input[str]] = None,
            spring_cloud_gateway_id: Optional[pulumi.Input[str]] = None,
            sso_validation_enabled: Optional[pulumi.Input[bool]] = None) -> 'SpringCloudGatewayRouteConfig':
        """
        Get an existing SpringCloudGatewayRouteConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] filters: Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        :param pulumi.Input[str] name: The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigOpenApiArgs']] open_api: One or more `open_api` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] predicates: Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        :param pulumi.Input[str] protocol: Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpringCloudGatewayRouteConfigRouteArgs']]]] routes: One or more `route` blocks as defined below.
        :param pulumi.Input[str] spring_cloud_app_id: The ID of the Spring Cloud App.
        :param pulumi.Input[str] spring_cloud_gateway_id: The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        :param pulumi.Input[bool] sso_validation_enabled: Should the sso validation be enabled in app level?
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SpringCloudGatewayRouteConfigState.__new__(_SpringCloudGatewayRouteConfigState)

        __props__.__dict__["filters"] = filters
        __props__.__dict__["name"] = name
        __props__.__dict__["open_api"] = open_api
        __props__.__dict__["predicates"] = predicates
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["routes"] = routes
        __props__.__dict__["spring_cloud_app_id"] = spring_cloud_app_id
        __props__.__dict__["spring_cloud_gateway_id"] = spring_cloud_gateway_id
        __props__.__dict__["sso_validation_enabled"] = sso_validation_enabled
        return SpringCloudGatewayRouteConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies a list of filters which are used to modify the request before sending it to the target endpoint, or the received response in app level.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Spring Cloud Gateway Route Config. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openApi")
    def open_api(self) -> pulumi.Output[Optional['outputs.SpringCloudGatewayRouteConfigOpenApi']]:
        """
        One or more `open_api` blocks as defined below.
        """
        return pulumi.get(self, "open_api")

    @property
    @pulumi.getter
    def predicates(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies a list of conditions to evaluate a route for each request in app level. Each predicate may be evaluated against request headers and parameter values. All of the predicates associated with a route must evaluate to true for the route to be matched to the request.
        """
        return pulumi.get(self, "predicates")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the protocol of routed Spring Cloud App. Allowed values are `HTTP` and `HTTPS`. Defaults to `HTTP`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional[Sequence['outputs.SpringCloudGatewayRouteConfigRoute']]]:
        """
        One or more `route` blocks as defined below.
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter(name="springCloudAppId")
    def spring_cloud_app_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Spring Cloud App.
        """
        return pulumi.get(self, "spring_cloud_app_id")

    @property
    @pulumi.getter(name="springCloudGatewayId")
    def spring_cloud_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the Spring Cloud Gateway. Changing this forces a new Spring Cloud Gateway Route Config to be created.
        """
        return pulumi.get(self, "spring_cloud_gateway_id")

    @property
    @pulumi.getter(name="ssoValidationEnabled")
    def sso_validation_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the sso validation be enabled in app level?
        """
        return pulumi.get(self, "sso_validation_enabled")

