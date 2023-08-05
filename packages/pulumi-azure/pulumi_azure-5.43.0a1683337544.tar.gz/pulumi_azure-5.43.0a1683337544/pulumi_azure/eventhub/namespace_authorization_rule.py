# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NamespaceAuthorizationRuleArgs', 'NamespaceAuthorizationRule']

@pulumi.input_type
class NamespaceAuthorizationRuleArgs:
    def __init__(__self__, *,
                 namespace_id: pulumi.Input[str],
                 listen: Optional[pulumi.Input[bool]] = None,
                 manage: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 send: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a NamespaceAuthorizationRule resource.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] listen: Grants listen access to this this Authorization Rule. Defaults to `false`.
        :param pulumi.Input[bool] manage: Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] send: Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        pulumi.set(__self__, "namespace_id", namespace_id)
        if listen is not None:
            pulumi.set(__self__, "listen", listen)
        if manage is not None:
            pulumi.set(__self__, "manage", manage)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if send is not None:
            pulumi.set(__self__, "send", send)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Input[str]:
        """
        Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter
    def listen(self) -> Optional[pulumi.Input[bool]]:
        """
        Grants listen access to this this Authorization Rule. Defaults to `false`.
        """
        return pulumi.get(self, "listen")

    @listen.setter
    def listen(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "listen", value)

    @property
    @pulumi.getter
    def manage(self) -> Optional[pulumi.Input[bool]]:
        """
        Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        """
        return pulumi.get(self, "manage")

    @manage.setter
    def manage(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "manage", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def send(self) -> Optional[pulumi.Input[bool]]:
        """
        Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        return pulumi.get(self, "send")

    @send.setter
    def send(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send", value)


@pulumi.input_type
class _NamespaceAuthorizationRuleState:
    def __init__(__self__, *,
                 listen: Optional[pulumi.Input[bool]] = None,
                 manage: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 primary_connection_string: Optional[pulumi.Input[str]] = None,
                 primary_connection_string_alias: Optional[pulumi.Input[str]] = None,
                 primary_key: Optional[pulumi.Input[str]] = None,
                 secondary_connection_string: Optional[pulumi.Input[str]] = None,
                 secondary_connection_string_alias: Optional[pulumi.Input[str]] = None,
                 secondary_key: Optional[pulumi.Input[str]] = None,
                 send: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering NamespaceAuthorizationRule resources.
        :param pulumi.Input[bool] listen: Grants listen access to this this Authorization Rule. Defaults to `false`.
        :param pulumi.Input[bool] manage: Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] primary_connection_string: The Primary Connection String for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[str] primary_connection_string_alias: The alias Primary Connection String for the ServiceBus Namespace, if the namespace is Geo DR paired.
        :param pulumi.Input[str] primary_key: The Primary Key for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[str] secondary_connection_string: The Secondary Connection String for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[str] secondary_connection_string_alias: The alias Secondary Connection String for the ServiceBus Namespace
        :param pulumi.Input[str] secondary_key: The Secondary Key for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[bool] send: Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        if listen is not None:
            pulumi.set(__self__, "listen", listen)
        if manage is not None:
            pulumi.set(__self__, "manage", manage)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)
        if primary_connection_string is not None:
            pulumi.set(__self__, "primary_connection_string", primary_connection_string)
        if primary_connection_string_alias is not None:
            pulumi.set(__self__, "primary_connection_string_alias", primary_connection_string_alias)
        if primary_key is not None:
            pulumi.set(__self__, "primary_key", primary_key)
        if secondary_connection_string is not None:
            pulumi.set(__self__, "secondary_connection_string", secondary_connection_string)
        if secondary_connection_string_alias is not None:
            pulumi.set(__self__, "secondary_connection_string_alias", secondary_connection_string_alias)
        if secondary_key is not None:
            pulumi.set(__self__, "secondary_key", secondary_key)
        if send is not None:
            pulumi.set(__self__, "send", send)

    @property
    @pulumi.getter
    def listen(self) -> Optional[pulumi.Input[bool]]:
        """
        Grants listen access to this this Authorization Rule. Defaults to `false`.
        """
        return pulumi.get(self, "listen")

    @listen.setter
    def listen(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "listen", value)

    @property
    @pulumi.getter
    def manage(self) -> Optional[pulumi.Input[bool]]:
        """
        Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        """
        return pulumi.get(self, "manage")

    @manage.setter
    def manage(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "manage", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The Primary Connection String for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "primary_connection_string")

    @primary_connection_string.setter
    def primary_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_connection_string", value)

    @property
    @pulumi.getter(name="primaryConnectionStringAlias")
    def primary_connection_string_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias Primary Connection String for the ServiceBus Namespace, if the namespace is Geo DR paired.
        """
        return pulumi.get(self, "primary_connection_string_alias")

    @primary_connection_string_alias.setter
    def primary_connection_string_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_connection_string_alias", value)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[str]]:
        """
        The Primary Key for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "primary_key")

    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_key", value)

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The Secondary Connection String for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "secondary_connection_string")

    @secondary_connection_string.setter
    def secondary_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_connection_string", value)

    @property
    @pulumi.getter(name="secondaryConnectionStringAlias")
    def secondary_connection_string_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias Secondary Connection String for the ServiceBus Namespace
        """
        return pulumi.get(self, "secondary_connection_string_alias")

    @secondary_connection_string_alias.setter
    def secondary_connection_string_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_connection_string_alias", value)

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[pulumi.Input[str]]:
        """
        The Secondary Key for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "secondary_key")

    @secondary_key.setter
    def secondary_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_key", value)

    @property
    @pulumi.getter
    def send(self) -> Optional[pulumi.Input[bool]]:
        """
        Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        return pulumi.get(self, "send")

    @send.setter
    def send(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send", value)


warnings.warn("""azure.eventhub.NamespaceAuthorizationRule has been deprecated in favor of azure.servicebus.NamespaceAuthorizationRule""", DeprecationWarning)


class NamespaceAuthorizationRule(pulumi.CustomResource):
    warnings.warn("""azure.eventhub.NamespaceAuthorizationRule has been deprecated in favor of azure.servicebus.NamespaceAuthorizationRule""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 listen: Optional[pulumi.Input[bool]] = None,
                 manage: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 send: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a ServiceBus Namespace authorization Rule within a ServiceBus.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_namespace = azure.servicebus.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            tags={
                "source": "example",
            })
        example_namespace_authorization_rule = azure.servicebus.NamespaceAuthorizationRule("exampleNamespaceAuthorizationRule",
            namespace_id=example_namespace.id,
            listen=True,
            send=True,
            manage=False)
        ```

        ## Import

        ServiceBus Namespace authorization rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/namespaceAuthorizationRule:NamespaceAuthorizationRule rule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ServiceBus/namespaces/namespace1/authorizationRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] listen: Grants listen access to this this Authorization Rule. Defaults to `false`.
        :param pulumi.Input[bool] manage: Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] send: Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceAuthorizationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a ServiceBus Namespace authorization Rule within a ServiceBus.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_namespace = azure.servicebus.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            tags={
                "source": "example",
            })
        example_namespace_authorization_rule = azure.servicebus.NamespaceAuthorizationRule("exampleNamespaceAuthorizationRule",
            namespace_id=example_namespace.id,
            listen=True,
            send=True,
            manage=False)
        ```

        ## Import

        ServiceBus Namespace authorization rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/namespaceAuthorizationRule:NamespaceAuthorizationRule rule1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ServiceBus/namespaces/namespace1/authorizationRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param NamespaceAuthorizationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceAuthorizationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 listen: Optional[pulumi.Input[bool]] = None,
                 manage: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 send: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""NamespaceAuthorizationRule is deprecated: azure.eventhub.NamespaceAuthorizationRule has been deprecated in favor of azure.servicebus.NamespaceAuthorizationRule""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceAuthorizationRuleArgs.__new__(NamespaceAuthorizationRuleArgs)

            __props__.__dict__["listen"] = listen
            __props__.__dict__["manage"] = manage
            __props__.__dict__["name"] = name
            if namespace_id is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_id'")
            __props__.__dict__["namespace_id"] = namespace_id
            __props__.__dict__["send"] = send
            __props__.__dict__["primary_connection_string"] = None
            __props__.__dict__["primary_connection_string_alias"] = None
            __props__.__dict__["primary_key"] = None
            __props__.__dict__["secondary_connection_string"] = None
            __props__.__dict__["secondary_connection_string_alias"] = None
            __props__.__dict__["secondary_key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["primaryConnectionString", "primaryConnectionStringAlias", "primaryKey", "secondaryConnectionString", "secondaryConnectionStringAlias", "secondaryKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(NamespaceAuthorizationRule, __self__).__init__(
            'azure:eventhub/namespaceAuthorizationRule:NamespaceAuthorizationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            listen: Optional[pulumi.Input[bool]] = None,
            manage: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_id: Optional[pulumi.Input[str]] = None,
            primary_connection_string: Optional[pulumi.Input[str]] = None,
            primary_connection_string_alias: Optional[pulumi.Input[str]] = None,
            primary_key: Optional[pulumi.Input[str]] = None,
            secondary_connection_string: Optional[pulumi.Input[str]] = None,
            secondary_connection_string_alias: Optional[pulumi.Input[str]] = None,
            secondary_key: Optional[pulumi.Input[str]] = None,
            send: Optional[pulumi.Input[bool]] = None) -> 'NamespaceAuthorizationRule':
        """
        Get an existing NamespaceAuthorizationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] listen: Grants listen access to this this Authorization Rule. Defaults to `false`.
        :param pulumi.Input[bool] manage: Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_id: Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] primary_connection_string: The Primary Connection String for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[str] primary_connection_string_alias: The alias Primary Connection String for the ServiceBus Namespace, if the namespace is Geo DR paired.
        :param pulumi.Input[str] primary_key: The Primary Key for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[str] secondary_connection_string: The Secondary Connection String for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[str] secondary_connection_string_alias: The alias Secondary Connection String for the ServiceBus Namespace
        :param pulumi.Input[str] secondary_key: The Secondary Key for the ServiceBus Namespace authorization Rule.
        :param pulumi.Input[bool] send: Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamespaceAuthorizationRuleState.__new__(_NamespaceAuthorizationRuleState)

        __props__.__dict__["listen"] = listen
        __props__.__dict__["manage"] = manage
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_id"] = namespace_id
        __props__.__dict__["primary_connection_string"] = primary_connection_string
        __props__.__dict__["primary_connection_string_alias"] = primary_connection_string_alias
        __props__.__dict__["primary_key"] = primary_key
        __props__.__dict__["secondary_connection_string"] = secondary_connection_string
        __props__.__dict__["secondary_connection_string_alias"] = secondary_connection_string_alias
        __props__.__dict__["secondary_key"] = secondary_key
        __props__.__dict__["send"] = send
        return NamespaceAuthorizationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def listen(self) -> pulumi.Output[Optional[bool]]:
        """
        Grants listen access to this this Authorization Rule. Defaults to `false`.
        """
        return pulumi.get(self, "listen")

    @property
    @pulumi.getter
    def manage(self) -> pulumi.Output[Optional[bool]]:
        """
        Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        """
        return pulumi.get(self, "manage")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID of the ServiceBus Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> pulumi.Output[str]:
        """
        The Primary Connection String for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "primary_connection_string")

    @property
    @pulumi.getter(name="primaryConnectionStringAlias")
    def primary_connection_string_alias(self) -> pulumi.Output[str]:
        """
        The alias Primary Connection String for the ServiceBus Namespace, if the namespace is Geo DR paired.
        """
        return pulumi.get(self, "primary_connection_string_alias")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> pulumi.Output[str]:
        """
        The Primary Key for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> pulumi.Output[str]:
        """
        The Secondary Connection String for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "secondary_connection_string")

    @property
    @pulumi.getter(name="secondaryConnectionStringAlias")
    def secondary_connection_string_alias(self) -> pulumi.Output[str]:
        """
        The alias Secondary Connection String for the ServiceBus Namespace
        """
        return pulumi.get(self, "secondary_connection_string_alias")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> pulumi.Output[str]:
        """
        The Secondary Key for the ServiceBus Namespace authorization Rule.
        """
        return pulumi.get(self, "secondary_key")

    @property
    @pulumi.getter
    def send(self) -> pulumi.Output[Optional[bool]]:
        """
        Grants send access to this this Authorization Rule. Defaults to `false`.
        """
        return pulumi.get(self, "send")

