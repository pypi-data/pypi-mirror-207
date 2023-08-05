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

__all__ = ['DatasetJsonArgs', 'DatasetJson']

@pulumi.input_type
class DatasetJsonArgs:
    def __init__(__self__, *,
                 data_factory_id: pulumi.Input[str],
                 linked_service_name: pulumi.Input[str],
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 azure_blob_storage_location: Optional[pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 http_server_location: Optional[pulumi.Input['DatasetJsonHttpServerLocationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]]] = None):
        """
        The set of arguments for constructing a DatasetJson resource.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] linked_service_name: The Data Factory Linked Service name in which to associate the Dataset with.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: A map of additional properties to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] annotations: List of tags that can be used for describing the Data Factory Dataset.
        :param pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs'] azure_blob_storage_location: A `azure_blob_storage_location` block as defined below.
        :param pulumi.Input[str] description: The description for the Data Factory Dataset.
        :param pulumi.Input[str] encoding: The encoding format for the file.
        :param pulumi.Input[str] folder: The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        :param pulumi.Input['DatasetJsonHttpServerLocationArgs'] http_server_location: A `http_server_location` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]] schema_columns: A `schema_column` block as defined below.
        """
        pulumi.set(__self__, "data_factory_id", data_factory_id)
        pulumi.set(__self__, "linked_service_name", linked_service_name)
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if azure_blob_storage_location is not None:
            pulumi.set(__self__, "azure_blob_storage_location", azure_blob_storage_location)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if http_server_location is not None:
            pulumi.set(__self__, "http_server_location", http_server_location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if schema_columns is not None:
            pulumi.set(__self__, "schema_columns", schema_columns)

    @property
    @pulumi.getter(name="dataFactoryId")
    def data_factory_id(self) -> pulumi.Input[str]:
        """
        The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_id")

    @data_factory_id.setter
    def data_factory_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_factory_id", value)

    @property
    @pulumi.getter(name="linkedServiceName")
    def linked_service_name(self) -> pulumi.Input[str]:
        """
        The Data Factory Linked Service name in which to associate the Dataset with.
        """
        return pulumi.get(self, "linked_service_name")

    @linked_service_name.setter
    def linked_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "linked_service_name", value)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of additional properties to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "additional_properties")

    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_properties", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of tags that can be used for describing the Data Factory Dataset.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="azureBlobStorageLocation")
    def azure_blob_storage_location(self) -> Optional[pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs']]:
        """
        A `azure_blob_storage_location` block as defined below.
        """
        return pulumi.get(self, "azure_blob_storage_location")

    @azure_blob_storage_location.setter
    def azure_blob_storage_location(self, value: Optional[pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs']]):
        pulumi.set(self, "azure_blob_storage_location", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the Data Factory Dataset.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding format for the file.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter(name="httpServerLocation")
    def http_server_location(self) -> Optional[pulumi.Input['DatasetJsonHttpServerLocationArgs']]:
        """
        A `http_server_location` block as defined below.
        """
        return pulumi.get(self, "http_server_location")

    @http_server_location.setter
    def http_server_location(self, value: Optional[pulumi.Input['DatasetJsonHttpServerLocationArgs']]):
        pulumi.set(self, "http_server_location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of parameters to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="schemaColumns")
    def schema_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]]]:
        """
        A `schema_column` block as defined below.
        """
        return pulumi.get(self, "schema_columns")

    @schema_columns.setter
    def schema_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]]]):
        pulumi.set(self, "schema_columns", value)


@pulumi.input_type
class _DatasetJsonState:
    def __init__(__self__, *,
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 azure_blob_storage_location: Optional[pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs']] = None,
                 data_factory_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 http_server_location: Optional[pulumi.Input['DatasetJsonHttpServerLocationArgs']] = None,
                 linked_service_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]]] = None):
        """
        Input properties used for looking up and filtering DatasetJson resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: A map of additional properties to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] annotations: List of tags that can be used for describing the Data Factory Dataset.
        :param pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs'] azure_blob_storage_location: A `azure_blob_storage_location` block as defined below.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] description: The description for the Data Factory Dataset.
        :param pulumi.Input[str] encoding: The encoding format for the file.
        :param pulumi.Input[str] folder: The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        :param pulumi.Input['DatasetJsonHttpServerLocationArgs'] http_server_location: A `http_server_location` block as defined below.
        :param pulumi.Input[str] linked_service_name: The Data Factory Linked Service name in which to associate the Dataset with.
        :param pulumi.Input[str] name: Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]] schema_columns: A `schema_column` block as defined below.
        """
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if azure_blob_storage_location is not None:
            pulumi.set(__self__, "azure_blob_storage_location", azure_blob_storage_location)
        if data_factory_id is not None:
            pulumi.set(__self__, "data_factory_id", data_factory_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if http_server_location is not None:
            pulumi.set(__self__, "http_server_location", http_server_location)
        if linked_service_name is not None:
            pulumi.set(__self__, "linked_service_name", linked_service_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if schema_columns is not None:
            pulumi.set(__self__, "schema_columns", schema_columns)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of additional properties to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "additional_properties")

    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_properties", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of tags that can be used for describing the Data Factory Dataset.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="azureBlobStorageLocation")
    def azure_blob_storage_location(self) -> Optional[pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs']]:
        """
        A `azure_blob_storage_location` block as defined below.
        """
        return pulumi.get(self, "azure_blob_storage_location")

    @azure_blob_storage_location.setter
    def azure_blob_storage_location(self, value: Optional[pulumi.Input['DatasetJsonAzureBlobStorageLocationArgs']]):
        pulumi.set(self, "azure_blob_storage_location", value)

    @property
    @pulumi.getter(name="dataFactoryId")
    def data_factory_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_id")

    @data_factory_id.setter
    def data_factory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_factory_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the Data Factory Dataset.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding format for the file.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter(name="httpServerLocation")
    def http_server_location(self) -> Optional[pulumi.Input['DatasetJsonHttpServerLocationArgs']]:
        """
        A `http_server_location` block as defined below.
        """
        return pulumi.get(self, "http_server_location")

    @http_server_location.setter
    def http_server_location(self, value: Optional[pulumi.Input['DatasetJsonHttpServerLocationArgs']]):
        pulumi.set(self, "http_server_location", value)

    @property
    @pulumi.getter(name="linkedServiceName")
    def linked_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Factory Linked Service name in which to associate the Dataset with.
        """
        return pulumi.get(self, "linked_service_name")

    @linked_service_name.setter
    def linked_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_service_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of parameters to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="schemaColumns")
    def schema_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]]]:
        """
        A `schema_column` block as defined below.
        """
        return pulumi.get(self, "schema_columns")

    @schema_columns.setter
    def schema_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatasetJsonSchemaColumnArgs']]]]):
        pulumi.set(self, "schema_columns", value)


class DatasetJson(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 azure_blob_storage_location: Optional[pulumi.Input[pulumi.InputType['DatasetJsonAzureBlobStorageLocationArgs']]] = None,
                 data_factory_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 http_server_location: Optional[pulumi.Input[pulumi.InputType['DatasetJsonHttpServerLocationArgs']]] = None,
                 linked_service_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetJsonSchemaColumnArgs']]]]] = None,
                 __props__=None):
        """
        Manages an Azure JSON Dataset inside an Azure Data Factory.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_factory = azure.datafactory.Factory("exampleFactory",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_linked_service_web = azure.datafactory.LinkedServiceWeb("exampleLinkedServiceWeb",
            data_factory_id=example_factory.id,
            authentication_type="Anonymous",
            url="https://www.bing.com")
        example_dataset_json = azure.datafactory.DatasetJson("exampleDatasetJson",
            data_factory_id=example_factory.id,
            linked_service_name=example_linked_service_web.name,
            http_server_location=azure.datafactory.DatasetJsonHttpServerLocationArgs(
                relative_url="/fizz/buzz/",
                path="foo/bar/",
                filename="foo.txt",
            ),
            encoding="UTF-8")
        ```

        ## Import

        Data Factory Datasets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datafactory/datasetJson:DatasetJson example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.DataFactory/factories/example/datasets/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: A map of additional properties to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] annotations: List of tags that can be used for describing the Data Factory Dataset.
        :param pulumi.Input[pulumi.InputType['DatasetJsonAzureBlobStorageLocationArgs']] azure_blob_storage_location: A `azure_blob_storage_location` block as defined below.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] description: The description for the Data Factory Dataset.
        :param pulumi.Input[str] encoding: The encoding format for the file.
        :param pulumi.Input[str] folder: The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        :param pulumi.Input[pulumi.InputType['DatasetJsonHttpServerLocationArgs']] http_server_location: A `http_server_location` block as defined below.
        :param pulumi.Input[str] linked_service_name: The Data Factory Linked Service name in which to associate the Dataset with.
        :param pulumi.Input[str] name: Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetJsonSchemaColumnArgs']]]] schema_columns: A `schema_column` block as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetJsonArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure JSON Dataset inside an Azure Data Factory.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_factory = azure.datafactory.Factory("exampleFactory",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_linked_service_web = azure.datafactory.LinkedServiceWeb("exampleLinkedServiceWeb",
            data_factory_id=example_factory.id,
            authentication_type="Anonymous",
            url="https://www.bing.com")
        example_dataset_json = azure.datafactory.DatasetJson("exampleDatasetJson",
            data_factory_id=example_factory.id,
            linked_service_name=example_linked_service_web.name,
            http_server_location=azure.datafactory.DatasetJsonHttpServerLocationArgs(
                relative_url="/fizz/buzz/",
                path="foo/bar/",
                filename="foo.txt",
            ),
            encoding="UTF-8")
        ```

        ## Import

        Data Factory Datasets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datafactory/datasetJson:DatasetJson example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.DataFactory/factories/example/datasets/example
        ```

        :param str resource_name: The name of the resource.
        :param DatasetJsonArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetJsonArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 azure_blob_storage_location: Optional[pulumi.Input[pulumi.InputType['DatasetJsonAzureBlobStorageLocationArgs']]] = None,
                 data_factory_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 http_server_location: Optional[pulumi.Input[pulumi.InputType['DatasetJsonHttpServerLocationArgs']]] = None,
                 linked_service_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetJsonSchemaColumnArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasetJsonArgs.__new__(DatasetJsonArgs)

            __props__.__dict__["additional_properties"] = additional_properties
            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["azure_blob_storage_location"] = azure_blob_storage_location
            if data_factory_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_factory_id'")
            __props__.__dict__["data_factory_id"] = data_factory_id
            __props__.__dict__["description"] = description
            __props__.__dict__["encoding"] = encoding
            __props__.__dict__["folder"] = folder
            __props__.__dict__["http_server_location"] = http_server_location
            if linked_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'linked_service_name'")
            __props__.__dict__["linked_service_name"] = linked_service_name
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["schema_columns"] = schema_columns
        super(DatasetJson, __self__).__init__(
            'azure:datafactory/datasetJson:DatasetJson',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            azure_blob_storage_location: Optional[pulumi.Input[pulumi.InputType['DatasetJsonAzureBlobStorageLocationArgs']]] = None,
            data_factory_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encoding: Optional[pulumi.Input[str]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            http_server_location: Optional[pulumi.Input[pulumi.InputType['DatasetJsonHttpServerLocationArgs']]] = None,
            linked_service_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetJsonSchemaColumnArgs']]]]] = None) -> 'DatasetJson':
        """
        Get an existing DatasetJson resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: A map of additional properties to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] annotations: List of tags that can be used for describing the Data Factory Dataset.
        :param pulumi.Input[pulumi.InputType['DatasetJsonAzureBlobStorageLocationArgs']] azure_blob_storage_location: A `azure_blob_storage_location` block as defined below.
        :param pulumi.Input[str] data_factory_id: The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        :param pulumi.Input[str] description: The description for the Data Factory Dataset.
        :param pulumi.Input[str] encoding: The encoding format for the file.
        :param pulumi.Input[str] folder: The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        :param pulumi.Input[pulumi.InputType['DatasetJsonHttpServerLocationArgs']] http_server_location: A `http_server_location` block as defined below.
        :param pulumi.Input[str] linked_service_name: The Data Factory Linked Service name in which to associate the Dataset with.
        :param pulumi.Input[str] name: Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetJsonSchemaColumnArgs']]]] schema_columns: A `schema_column` block as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetJsonState.__new__(_DatasetJsonState)

        __props__.__dict__["additional_properties"] = additional_properties
        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["azure_blob_storage_location"] = azure_blob_storage_location
        __props__.__dict__["data_factory_id"] = data_factory_id
        __props__.__dict__["description"] = description
        __props__.__dict__["encoding"] = encoding
        __props__.__dict__["folder"] = folder
        __props__.__dict__["http_server_location"] = http_server_location
        __props__.__dict__["linked_service_name"] = linked_service_name
        __props__.__dict__["name"] = name
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["schema_columns"] = schema_columns
        return DatasetJson(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of additional properties to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "additional_properties")

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of tags that can be used for describing the Data Factory Dataset.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="azureBlobStorageLocation")
    def azure_blob_storage_location(self) -> pulumi.Output[Optional['outputs.DatasetJsonAzureBlobStorageLocation']]:
        """
        A `azure_blob_storage_location` block as defined below.
        """
        return pulumi.get(self, "azure_blob_storage_location")

    @property
    @pulumi.getter(name="dataFactoryId")
    def data_factory_id(self) -> pulumi.Output[str]:
        """
        The Data Factory ID in which to associate the Linked Service with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for the Data Factory Dataset.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encoding(self) -> pulumi.Output[Optional[str]]:
        """
        The encoding format for the file.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[str]]:
        """
        The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter(name="httpServerLocation")
    def http_server_location(self) -> pulumi.Output[Optional['outputs.DatasetJsonHttpServerLocation']]:
        """
        A `http_server_location` block as defined below.
        """
        return pulumi.get(self, "http_server_location")

    @property
    @pulumi.getter(name="linkedServiceName")
    def linked_service_name(self) -> pulumi.Output[str]:
        """
        The Data Factory Linked Service name in which to associate the Dataset with.
        """
        return pulumi.get(self, "linked_service_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of parameters to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="schemaColumns")
    def schema_columns(self) -> pulumi.Output[Optional[Sequence['outputs.DatasetJsonSchemaColumn']]]:
        """
        A `schema_column` block as defined below.
        """
        return pulumi.get(self, "schema_columns")

