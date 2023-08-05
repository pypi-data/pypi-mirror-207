# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'FunctionJavaScriptUDFInputArgs',
    'FunctionJavaScriptUDFOutputArgs',
    'FunctionJavascriptUdaInputArgs',
    'FunctionJavascriptUdaOutputArgs',
    'JobIdentityArgs',
    'JobJobStorageAccountArgs',
    'OutputBlobSerializationArgs',
    'OutputEventHubSerializationArgs',
    'OutputServiceBusQueueSerializationArgs',
    'OutputServicebusTopicSerializationArgs',
    'ReferenceInputBlobSerializationArgs',
    'StreamInputBlobSerializationArgs',
    'StreamInputEventHubSerializationArgs',
    'StreamInputEventHubV2SerializationArgs',
    'StreamInputIotHubSerializationArgs',
]

@pulumi.input_type
class FunctionJavaScriptUDFInputArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 configuration_parameter: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] type: The Data Type for the Input Argument of this JavaScript Function. Possible values include `array`, `any`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        :param pulumi.Input[bool] configuration_parameter: Is this input parameter a configuration parameter? Defaults to `false`.
        """
        pulumi.set(__self__, "type", type)
        if configuration_parameter is not None:
            pulumi.set(__self__, "configuration_parameter", configuration_parameter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The Data Type for the Input Argument of this JavaScript Function. Possible values include `array`, `any`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="configurationParameter")
    def configuration_parameter(self) -> Optional[pulumi.Input[bool]]:
        """
        Is this input parameter a configuration parameter? Defaults to `false`.
        """
        return pulumi.get(self, "configuration_parameter")

    @configuration_parameter.setter
    def configuration_parameter(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "configuration_parameter", value)


@pulumi.input_type
class FunctionJavaScriptUDFOutputArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] type: The Data Type output from this JavaScript Function. Possible values include `array`, `any`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        """
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The Data Type output from this JavaScript Function. Possible values include `array`, `any`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class FunctionJavascriptUdaInputArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 configuration_parameter: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] type: The input data type of this JavaScript Function. Possible values include `any`, `array`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        :param pulumi.Input[bool] configuration_parameter: Is this input parameter a configuration parameter? Defaults to `false`.
        """
        pulumi.set(__self__, "type", type)
        if configuration_parameter is not None:
            pulumi.set(__self__, "configuration_parameter", configuration_parameter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The input data type of this JavaScript Function. Possible values include `any`, `array`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="configurationParameter")
    def configuration_parameter(self) -> Optional[pulumi.Input[bool]]:
        """
        Is this input parameter a configuration parameter? Defaults to `false`.
        """
        return pulumi.get(self, "configuration_parameter")

    @configuration_parameter.setter
    def configuration_parameter(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "configuration_parameter", value)


@pulumi.input_type
class FunctionJavascriptUdaOutputArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] type: The output data type from this JavaScript Function. Possible values include `any`, `array`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        """
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The output data type from this JavaScript Function. Possible values include `any`, `array`, `bigint`, `datetime`, `float`, `nvarchar(max)` and `record`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class JobIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the type of Managed Service Identity that should be configured on this Stream Analytics Job. The only possible value is `SystemAssigned`.
        :param pulumi.Input[str] principal_id: The Principal ID associated with this Managed Service Identity.
        :param pulumi.Input[str] tenant_id: The Tenant ID associated with this Managed Service Identity.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Specifies the type of Managed Service Identity that should be configured on this Stream Analytics Job. The only possible value is `SystemAssigned`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class JobJobStorageAccountArgs:
    def __init__(__self__, *,
                 account_key: pulumi.Input[str],
                 account_name: pulumi.Input[str],
                 authentication_mode: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] account_key: The account key for the Azure storage account.
        :param pulumi.Input[str] account_name: The name of the Azure storage account.
        :param pulumi.Input[str] authentication_mode: The authentication mode of the storage account. The only supported value is `ConnectionString`. Defaults to `ConnectionString`.
        """
        pulumi.set(__self__, "account_key", account_key)
        pulumi.set(__self__, "account_name", account_name)
        if authentication_mode is not None:
            pulumi.set(__self__, "authentication_mode", authentication_mode)

    @property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> pulumi.Input[str]:
        """
        The account key for the Azure storage account.
        """
        return pulumi.get(self, "account_key")

    @account_key.setter
    def account_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_key", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure storage account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The authentication mode of the storage account. The only supported value is `ConnectionString`. Defaults to `ConnectionString`.
        """
        return pulumi.get(self, "authentication_mode")

    @authentication_mode.setter
    def authentication_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_mode", value)


@pulumi.input_type
class OutputBlobSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        :param pulumi.Input[str] format: Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)
        if format is not None:
            pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class OutputEventHubSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        :param pulumi.Input[str] format: Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)
        if format is not None:
            pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class OutputServiceBusQueueSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        :param pulumi.Input[str] format: Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)
        if format is not None:
            pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class OutputServicebusTopicSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        :param pulumi.Input[str] format: Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)
        if format is not None:
            pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for outgoing data streams. Possible values are `Avro`, `Csv`, `Json` and `Parquet`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the format of the JSON the output will be written in. Possible values are `Array` and `LineSeparated`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class ReferenceInputBlobSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for the reference data. Possible values are `Avro`, `Csv` and `Json`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for the reference data. Possible values are `Avro`, `Csv` and `Json`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)


@pulumi.input_type
class StreamInputBlobSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)


@pulumi.input_type
class StreamInputEventHubSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)


@pulumi.input_type
class StreamInputEventHubV2SerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)


@pulumi.input_type
class StreamInputIotHubSerializationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 encoding: Optional[pulumi.Input[str]] = None,
                 field_delimiter: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        :param pulumi.Input[str] encoding: The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        :param pulumi.Input[str] field_delimiter: The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        pulumi.set(__self__, "type", type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if field_delimiter is not None:
            pulumi.set(__self__, "field_delimiter", field_delimiter)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The serialization format used for incoming data streams. Possible values are `Avro`, `Csv` and `Json`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[str]]:
        """
        The encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. It currently can only be set to `UTF8`.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[str]]:
        """
        The delimiter that will be used to separate comma-separated value (CSV) records. Possible values are ` ` (space), `,` (comma), `	` (tab), `|` (pipe) and `;`.
        """
        return pulumi.get(self, "field_delimiter")

    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field_delimiter", value)


