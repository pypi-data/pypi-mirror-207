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

__all__ = ['EnvironmentDaprComponentArgs', 'EnvironmentDaprComponent']

@pulumi.input_type
class EnvironmentDaprComponentArgs:
    def __init__(__self__, *,
                 component_type: pulumi.Input[str],
                 container_app_environment_id: pulumi.Input[str],
                 version: pulumi.Input[str],
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadatas: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]]] = None):
        """
        The set of arguments for constructing a EnvironmentDaprComponent resource.
        :param pulumi.Input[str] component_type: The Dapr Component Type. For example `state.azure.blobstorage`.
        :param pulumi.Input[str] container_app_environment_id: The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        :param pulumi.Input[str] version: The version of the component.
        :param pulumi.Input[bool] ignore_errors: Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        :param pulumi.Input[str] init_timeout: The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]] metadatas: One or more `metadata` blocks as detailed below.
        :param pulumi.Input[str] name: The name for this Dapr component. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: A list of scopes to which this component applies.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]] secrets: A `secret` block as detailed below.
        """
        pulumi.set(__self__, "component_type", component_type)
        pulumi.set(__self__, "container_app_environment_id", container_app_environment_id)
        pulumi.set(__self__, "version", version)
        if ignore_errors is not None:
            pulumi.set(__self__, "ignore_errors", ignore_errors)
        if init_timeout is not None:
            pulumi.set(__self__, "init_timeout", init_timeout)
        if metadatas is not None:
            pulumi.set(__self__, "metadatas", metadatas)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if secrets is not None:
            pulumi.set(__self__, "secrets", secrets)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[str]:
        """
        The Dapr Component Type. For example `state.azure.blobstorage`.
        """
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter(name="containerAppEnvironmentId")
    def container_app_environment_id(self) -> pulumi.Input[str]:
        """
        The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "container_app_environment_id")

    @container_app_environment_id.setter
    def container_app_environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_app_environment_id", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        The version of the component.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        """
        return pulumi.get(self, "ignore_errors")

    @ignore_errors.setter
    def ignore_errors(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_errors", value)

    @property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> Optional[pulumi.Input[str]]:
        """
        The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        """
        return pulumi.get(self, "init_timeout")

    @init_timeout.setter
    def init_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "init_timeout", value)

    @property
    @pulumi.getter
    def metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]]]:
        """
        One or more `metadata` blocks as detailed below.
        """
        return pulumi.get(self, "metadatas")

    @metadatas.setter
    def metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]]]):
        pulumi.set(self, "metadatas", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for this Dapr component. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of scopes to which this component applies.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]]]:
        """
        A `secret` block as detailed below.
        """
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]]]):
        pulumi.set(self, "secrets", value)


@pulumi.input_type
class _EnvironmentDaprComponentState:
    def __init__(__self__, *,
                 component_type: Optional[pulumi.Input[str]] = None,
                 container_app_environment_id: Optional[pulumi.Input[str]] = None,
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadatas: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EnvironmentDaprComponent resources.
        :param pulumi.Input[str] component_type: The Dapr Component Type. For example `state.azure.blobstorage`.
        :param pulumi.Input[str] container_app_environment_id: The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] ignore_errors: Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        :param pulumi.Input[str] init_timeout: The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]] metadatas: One or more `metadata` blocks as detailed below.
        :param pulumi.Input[str] name: The name for this Dapr component. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: A list of scopes to which this component applies.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]] secrets: A `secret` block as detailed below.
        :param pulumi.Input[str] version: The version of the component.
        """
        if component_type is not None:
            pulumi.set(__self__, "component_type", component_type)
        if container_app_environment_id is not None:
            pulumi.set(__self__, "container_app_environment_id", container_app_environment_id)
        if ignore_errors is not None:
            pulumi.set(__self__, "ignore_errors", ignore_errors)
        if init_timeout is not None:
            pulumi.set(__self__, "init_timeout", init_timeout)
        if metadatas is not None:
            pulumi.set(__self__, "metadatas", metadatas)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if secrets is not None:
            pulumi.set(__self__, "secrets", secrets)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Dapr Component Type. For example `state.azure.blobstorage`.
        """
        return pulumi.get(self, "component_type")

    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "component_type", value)

    @property
    @pulumi.getter(name="containerAppEnvironmentId")
    def container_app_environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "container_app_environment_id")

    @container_app_environment_id.setter
    def container_app_environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_app_environment_id", value)

    @property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        """
        return pulumi.get(self, "ignore_errors")

    @ignore_errors.setter
    def ignore_errors(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_errors", value)

    @property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> Optional[pulumi.Input[str]]:
        """
        The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        """
        return pulumi.get(self, "init_timeout")

    @init_timeout.setter
    def init_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "init_timeout", value)

    @property
    @pulumi.getter
    def metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]]]:
        """
        One or more `metadata` blocks as detailed below.
        """
        return pulumi.get(self, "metadatas")

    @metadatas.setter
    def metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentMetadataArgs']]]]):
        pulumi.set(self, "metadatas", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for this Dapr component. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of scopes to which this component applies.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]]]:
        """
        A `secret` block as detailed below.
        """
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentDaprComponentSecretArgs']]]]):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the component.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class EnvironmentDaprComponent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 container_app_environment_id: Optional[pulumi.Input[str]] = None,
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentMetadataArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentSecretArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Dapr Component for a Container App Environment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018",
            retention_in_days=30)
        example_environment = azure.containerapp.Environment("exampleEnvironment",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            log_analytics_workspace_id=example_analytics_workspace.id)
        example_environment_dapr_component = azure.containerapp.EnvironmentDaprComponent("exampleEnvironmentDaprComponent",
            container_app_environment_id=example_environment.id,
            component_type="state.azure.blobstorage",
            version="v1")
        ```

        ## Import

        A Dapr Component for a Container App Environment can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:containerapp/environmentDaprComponent:EnvironmentDaprComponent example "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.App/managedEnvironments/myenv/daprComponents/mydaprcomponent"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] component_type: The Dapr Component Type. For example `state.azure.blobstorage`.
        :param pulumi.Input[str] container_app_environment_id: The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] ignore_errors: Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        :param pulumi.Input[str] init_timeout: The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentMetadataArgs']]]] metadatas: One or more `metadata` blocks as detailed below.
        :param pulumi.Input[str] name: The name for this Dapr component. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: A list of scopes to which this component applies.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentSecretArgs']]]] secrets: A `secret` block as detailed below.
        :param pulumi.Input[str] version: The version of the component.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentDaprComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Dapr Component for a Container App Environment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="PerGB2018",
            retention_in_days=30)
        example_environment = azure.containerapp.Environment("exampleEnvironment",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            log_analytics_workspace_id=example_analytics_workspace.id)
        example_environment_dapr_component = azure.containerapp.EnvironmentDaprComponent("exampleEnvironmentDaprComponent",
            container_app_environment_id=example_environment.id,
            component_type="state.azure.blobstorage",
            version="v1")
        ```

        ## Import

        A Dapr Component for a Container App Environment can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:containerapp/environmentDaprComponent:EnvironmentDaprComponent example "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resGroup1/providers/Microsoft.App/managedEnvironments/myenv/daprComponents/mydaprcomponent"
        ```

        :param str resource_name: The name of the resource.
        :param EnvironmentDaprComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentDaprComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 component_type: Optional[pulumi.Input[str]] = None,
                 container_app_environment_id: Optional[pulumi.Input[str]] = None,
                 ignore_errors: Optional[pulumi.Input[bool]] = None,
                 init_timeout: Optional[pulumi.Input[str]] = None,
                 metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentMetadataArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentSecretArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentDaprComponentArgs.__new__(EnvironmentDaprComponentArgs)

            if component_type is None and not opts.urn:
                raise TypeError("Missing required property 'component_type'")
            __props__.__dict__["component_type"] = component_type
            if container_app_environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'container_app_environment_id'")
            __props__.__dict__["container_app_environment_id"] = container_app_environment_id
            __props__.__dict__["ignore_errors"] = ignore_errors
            __props__.__dict__["init_timeout"] = init_timeout
            __props__.__dict__["metadatas"] = metadatas
            __props__.__dict__["name"] = name
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["secrets"] = None if secrets is None else pulumi.Output.secret(secrets)
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["secrets"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(EnvironmentDaprComponent, __self__).__init__(
            'azure:containerapp/environmentDaprComponent:EnvironmentDaprComponent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            component_type: Optional[pulumi.Input[str]] = None,
            container_app_environment_id: Optional[pulumi.Input[str]] = None,
            ignore_errors: Optional[pulumi.Input[bool]] = None,
            init_timeout: Optional[pulumi.Input[str]] = None,
            metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentMetadataArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentSecretArgs']]]]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'EnvironmentDaprComponent':
        """
        Get an existing EnvironmentDaprComponent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] component_type: The Dapr Component Type. For example `state.azure.blobstorage`.
        :param pulumi.Input[str] container_app_environment_id: The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] ignore_errors: Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        :param pulumi.Input[str] init_timeout: The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentMetadataArgs']]]] metadatas: One or more `metadata` blocks as detailed below.
        :param pulumi.Input[str] name: The name for this Dapr component. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: A list of scopes to which this component applies.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentDaprComponentSecretArgs']]]] secrets: A `secret` block as detailed below.
        :param pulumi.Input[str] version: The version of the component.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnvironmentDaprComponentState.__new__(_EnvironmentDaprComponentState)

        __props__.__dict__["component_type"] = component_type
        __props__.__dict__["container_app_environment_id"] = container_app_environment_id
        __props__.__dict__["ignore_errors"] = ignore_errors
        __props__.__dict__["init_timeout"] = init_timeout
        __props__.__dict__["metadatas"] = metadatas
        __props__.__dict__["name"] = name
        __props__.__dict__["scopes"] = scopes
        __props__.__dict__["secrets"] = secrets
        __props__.__dict__["version"] = version
        return EnvironmentDaprComponent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[str]:
        """
        The Dapr Component Type. For example `state.azure.blobstorage`.
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="containerAppEnvironmentId")
    def container_app_environment_id(self) -> pulumi.Output[str]:
        """
        The ID of the Container App Managed Environment for this Dapr Component. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "container_app_environment_id")

    @property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Dapr sidecar to continue initialisation if the component fails to load. Defaults to `false`
        """
        return pulumi.get(self, "ignore_errors")

    @property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        The timeout for component initialisation as a `ISO8601` formatted string. e.g. `5s`, `2h`, `1m`. Defaults to `5s`
        """
        return pulumi.get(self, "init_timeout")

    @property
    @pulumi.getter
    def metadatas(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentDaprComponentMetadata']]]:
        """
        One or more `metadata` blocks as detailed below.
        """
        return pulumi.get(self, "metadatas")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for this Dapr component. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of scopes to which this component applies.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def secrets(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentDaprComponentSecret']]]:
        """
        A `secret` block as detailed below.
        """
        return pulumi.get(self, "secrets")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the component.
        """
        return pulumi.get(self, "version")

