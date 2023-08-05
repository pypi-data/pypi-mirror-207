'''
# `aws_dynamodb_table`

Refer to the Terraform Registory for docs: [`aws_dynamodb_table`](https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DynamodbTable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTable",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table aws_dynamodb_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableAttribute", typing.Dict[builtins.str, typing.Any]]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableGlobalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hash_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableLocalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        point_in_time_recovery: typing.Optional[typing.Union["DynamodbTablePointInTimeRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        range_key: typing.Optional[builtins.str] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableReplica", typing.Dict[builtins.str, typing.Any]]]]] = None,
        restore_date_time: typing.Optional[builtins.str] = None,
        restore_source_name: typing.Optional[builtins.str] = None,
        restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_side_encryption: typing.Optional[typing.Union["DynamodbTableServerSideEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stream_view_type: typing.Optional[builtins.str] = None,
        table_class: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DynamodbTableTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["DynamodbTableTtl", typing.Dict[builtins.str, typing.Any]]] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table aws_dynamodb_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#attribute DynamodbTable#attribute}
        :param billing_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#billing_mode DynamodbTable#billing_mode}.
        :param deletion_protection_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#deletion_protection_enabled DynamodbTable#deletion_protection_enabled}.
        :param global_secondary_index: global_secondary_index block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#global_secondary_index DynamodbTable#global_secondary_index}
        :param hash_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#hash_key DynamodbTable#hash_key}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#id DynamodbTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_secondary_index: local_secondary_index block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#local_secondary_index DynamodbTable#local_secondary_index}
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}
        :param range_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.
        :param read_capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#read_capacity DynamodbTable#read_capacity}.
        :param replica: replica block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#replica DynamodbTable#replica}
        :param restore_date_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_date_time DynamodbTable#restore_date_time}.
        :param restore_source_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_source_name DynamodbTable#restore_source_name}.
        :param restore_to_latest_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_to_latest_time DynamodbTable#restore_to_latest_time}.
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#server_side_encryption DynamodbTable#server_side_encryption}
        :param stream_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#stream_enabled DynamodbTable#stream_enabled}.
        :param stream_view_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#stream_view_type DynamodbTable#stream_view_type}.
        :param table_class: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#table_class DynamodbTable#table_class}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#tags DynamodbTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#tags_all DynamodbTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#timeouts DynamodbTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#ttl DynamodbTable#ttl}
        :param write_capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#write_capacity DynamodbTable#write_capacity}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b33d5bdfd1849e705d1c43f7bb8e268f2cbe5afb89bc1d051b68b7a4c87274)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DynamodbTableConfig(
            name=name,
            attribute=attribute,
            billing_mode=billing_mode,
            deletion_protection_enabled=deletion_protection_enabled,
            global_secondary_index=global_secondary_index,
            hash_key=hash_key,
            id=id,
            local_secondary_index=local_secondary_index,
            point_in_time_recovery=point_in_time_recovery,
            range_key=range_key,
            read_capacity=read_capacity,
            replica=replica,
            restore_date_time=restore_date_time,
            restore_source_name=restore_source_name,
            restore_to_latest_time=restore_to_latest_time,
            server_side_encryption=server_side_encryption,
            stream_enabled=stream_enabled,
            stream_view_type=stream_view_type,
            table_class=table_class,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            ttl=ttl,
            write_capacity=write_capacity,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAttribute")
    def put_attribute(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableAttribute", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5d3c897b64c6c6a9e0a38eda94e626c45d0c5dd3597bff492102de947bd7d32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttribute", [value]))

    @jsii.member(jsii_name="putGlobalSecondaryIndex")
    def put_global_secondary_index(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableGlobalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30b0b912faa3eae3f70d096aec19f81ec6f43b4d3fae80c4042d9bc63ce355a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGlobalSecondaryIndex", [value]))

    @jsii.member(jsii_name="putLocalSecondaryIndex")
    def put_local_secondary_index(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableLocalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c6dee6715c159f2154a5cf5f20ba953d9b5ac70f79016b5f8683b45eb154b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocalSecondaryIndex", [value]))

    @jsii.member(jsii_name="putPointInTimeRecovery")
    def put_point_in_time_recovery(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        value = DynamodbTablePointInTimeRecovery(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putPointInTimeRecovery", [value]))

    @jsii.member(jsii_name="putReplica")
    def put_replica(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableReplica", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06b32e75d943fbe760d6e722f3433c45811267562fffc8a68daab40b5b8da7d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putReplica", [value]))

    @jsii.member(jsii_name="putServerSideEncryption")
    def put_server_side_encryption(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.
        '''
        value = DynamodbTableServerSideEncryption(
            enabled=enabled, kms_key_arn=kms_key_arn
        )

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryption", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#create DynamodbTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#delete DynamodbTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#update DynamodbTable#update}.
        '''
        value = DynamodbTableTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTtl")
    def put_ttl(
        self,
        *,
        attribute_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#attribute_name DynamodbTable#attribute_name}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        value = DynamodbTableTtl(attribute_name=attribute_name, enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putTtl", [value]))

    @jsii.member(jsii_name="resetAttribute")
    def reset_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttribute", []))

    @jsii.member(jsii_name="resetBillingMode")
    def reset_billing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBillingMode", []))

    @jsii.member(jsii_name="resetDeletionProtectionEnabled")
    def reset_deletion_protection_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtectionEnabled", []))

    @jsii.member(jsii_name="resetGlobalSecondaryIndex")
    def reset_global_secondary_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalSecondaryIndex", []))

    @jsii.member(jsii_name="resetHashKey")
    def reset_hash_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHashKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocalSecondaryIndex")
    def reset_local_secondary_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalSecondaryIndex", []))

    @jsii.member(jsii_name="resetPointInTimeRecovery")
    def reset_point_in_time_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecovery", []))

    @jsii.member(jsii_name="resetRangeKey")
    def reset_range_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKey", []))

    @jsii.member(jsii_name="resetReadCapacity")
    def reset_read_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadCapacity", []))

    @jsii.member(jsii_name="resetReplica")
    def reset_replica(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplica", []))

    @jsii.member(jsii_name="resetRestoreDateTime")
    def reset_restore_date_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreDateTime", []))

    @jsii.member(jsii_name="resetRestoreSourceName")
    def reset_restore_source_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreSourceName", []))

    @jsii.member(jsii_name="resetRestoreToLatestTime")
    def reset_restore_to_latest_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreToLatestTime", []))

    @jsii.member(jsii_name="resetServerSideEncryption")
    def reset_server_side_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryption", []))

    @jsii.member(jsii_name="resetStreamEnabled")
    def reset_stream_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamEnabled", []))

    @jsii.member(jsii_name="resetStreamViewType")
    def reset_stream_view_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamViewType", []))

    @jsii.member(jsii_name="resetTableClass")
    def reset_table_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableClass", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetWriteCapacity")
    def reset_write_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteCapacity", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> "DynamodbTableAttributeList":
        return typing.cast("DynamodbTableAttributeList", jsii.get(self, "attribute"))

    @builtins.property
    @jsii.member(jsii_name="globalSecondaryIndex")
    def global_secondary_index(self) -> "DynamodbTableGlobalSecondaryIndexList":
        return typing.cast("DynamodbTableGlobalSecondaryIndexList", jsii.get(self, "globalSecondaryIndex"))

    @builtins.property
    @jsii.member(jsii_name="localSecondaryIndex")
    def local_secondary_index(self) -> "DynamodbTableLocalSecondaryIndexList":
        return typing.cast("DynamodbTableLocalSecondaryIndexList", jsii.get(self, "localSecondaryIndex"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> "DynamodbTablePointInTimeRecoveryOutputReference":
        return typing.cast("DynamodbTablePointInTimeRecoveryOutputReference", jsii.get(self, "pointInTimeRecovery"))

    @builtins.property
    @jsii.member(jsii_name="replica")
    def replica(self) -> "DynamodbTableReplicaList":
        return typing.cast("DynamodbTableReplicaList", jsii.get(self, "replica"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> "DynamodbTableServerSideEncryptionOutputReference":
        return typing.cast("DynamodbTableServerSideEncryptionOutputReference", jsii.get(self, "serverSideEncryption"))

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @builtins.property
    @jsii.member(jsii_name="streamLabel")
    def stream_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamLabel"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DynamodbTableTimeoutsOutputReference":
        return typing.cast("DynamodbTableTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> "DynamodbTableTtlOutputReference":
        return typing.cast("DynamodbTableTtlOutputReference", jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableAttribute"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableAttribute"]]], jsii.get(self, "attributeInput"))

    @builtins.property
    @jsii.member(jsii_name="billingModeInput")
    def billing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionEnabledInput")
    def deletion_protection_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deletionProtectionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="globalSecondaryIndexInput")
    def global_secondary_index_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]], jsii.get(self, "globalSecondaryIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyInput")
    def hash_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localSecondaryIndexInput")
    def local_secondary_index_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]], jsii.get(self, "localSecondaryIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryInput")
    def point_in_time_recovery_input(
        self,
    ) -> typing.Optional["DynamodbTablePointInTimeRecovery"]:
        return typing.cast(typing.Optional["DynamodbTablePointInTimeRecovery"], jsii.get(self, "pointInTimeRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyInput")
    def range_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="readCapacityInput")
    def read_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaInput")
    def replica_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]], jsii.get(self, "replicaInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreDateTimeInput")
    def restore_date_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreDateTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreSourceNameInput")
    def restore_source_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreSourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreToLatestTimeInput")
    def restore_to_latest_time_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "restoreToLatestTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionInput")
    def server_side_encryption_input(
        self,
    ) -> typing.Optional["DynamodbTableServerSideEncryption"]:
        return typing.cast(typing.Optional["DynamodbTableServerSideEncryption"], jsii.get(self, "serverSideEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="streamEnabledInput")
    def stream_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "streamEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="streamViewTypeInput")
    def stream_view_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamViewTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tableClassInput")
    def table_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableClassInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DynamodbTableTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DynamodbTableTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional["DynamodbTableTtl"]:
        return typing.cast(typing.Optional["DynamodbTableTtl"], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="writeCapacityInput")
    def write_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="billingMode")
    def billing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3c7bee0af2b2be096c74b759885b4679f40e8120ba91484aab3fdc1dd6c003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingMode", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deletionProtectionEnabled"))

    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d10d233745ee7d9ea760497794027a77acb63d87682918a3c0b67e1bd57624b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtectionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="hashKey")
    def hash_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKey"))

    @hash_key.setter
    def hash_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87194fc82907b02b4f296ec1f6c029271dfa23724c17fe979a7045e25df5afab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKey", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ae7ef85603022c1dca8cf01bf547bc43150ad4d2d651a8c8f0cd3fc14d4d93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9489fc32fa98bc78d6e3b547b90021c399056b2fb598486999a9a0fd63d8d38d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKey")
    def range_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKey"))

    @range_key.setter
    def range_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7717400be74d87238017104fb443454ecae5ff1aa8b04bb33f376e027e52a8e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKey", value)

    @builtins.property
    @jsii.member(jsii_name="readCapacity")
    def read_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readCapacity"))

    @read_capacity.setter
    def read_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__503b130ec215d542027ebd1ab07396da223da166cf84eea918d9942cd25f53a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="restoreDateTime")
    def restore_date_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreDateTime"))

    @restore_date_time.setter
    def restore_date_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c09ac827345f3b38ae9a4f12dec6315cbbd2f07ebb4e2043664f099d4ac549)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreDateTime", value)

    @builtins.property
    @jsii.member(jsii_name="restoreSourceName")
    def restore_source_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreSourceName"))

    @restore_source_name.setter
    def restore_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e643c8947c6975290fa8ec2a07a1581f08da27a835c8723d5be67402519006c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="restoreToLatestTime")
    def restore_to_latest_time(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "restoreToLatestTime"))

    @restore_to_latest_time.setter
    def restore_to_latest_time(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0507a5a148aa1938fac2ce502885d179e493fdd41fcb4932a6d6a8d27ad45187)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreToLatestTime", value)

    @builtins.property
    @jsii.member(jsii_name="streamEnabled")
    def stream_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "streamEnabled"))

    @stream_enabled.setter
    def stream_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d860a6a5afd133eebea613c23cbffca79b16c74f6d4105e736c064798381ad3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="streamViewType")
    def stream_view_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamViewType"))

    @stream_view_type.setter
    def stream_view_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8f9955e28aa9e7aef4fe176f225699582e53ddb64876965fe95719bb03b24a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamViewType", value)

    @builtins.property
    @jsii.member(jsii_name="tableClass")
    def table_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableClass"))

    @table_class.setter
    def table_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af077df7f7b0745304fbee9b9494e884efcc95c87078daf951d1e73fc5ff8cd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableClass", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__347f56cdd57aca01b8ca3d2b02c9b6aaed4128c51753a21997f976d10f9b52a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__576f8f1c39f56193f2a4bfe6b6cbbffdb646e20b276e46a08306162839cb3da3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="writeCapacity")
    def write_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writeCapacity"))

    @write_capacity.setter
    def write_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f99b2ddc135d07ee0f8fea7e99d59584eda8d993592afef57b85c0836a1bacb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeCapacity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableAttribute",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class DynamodbTableAttribute:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#type DynamodbTable#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356c9d5e509da6ea0bdb0b33b04d19c819036ea2e492d0bfcd5f22b25a727c40)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#type DynamodbTable#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableAttribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableAttributeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableAttributeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7133a294f9aa1a8125bbf8035e5da64c5c4cb320e8692f8cb0c35586451ee573)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DynamodbTableAttributeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091de9e4614ef19bc7ffcc8a5fb47e7146054c13c81d64f8d6e43bafb42fe00b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableAttributeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2918f281ca2ef49f03791ee275bfc629183796770eebc7ae9e7f26263d2b483)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58554496a62240d9b66f9cf6c18ab094ddc449d492a082aa1aea5ae455bdde4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a3a091133e11b5b483704a78a13c47ecbc8cdefc14aec4c7c5cb39055515b8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f45abc1f7abb63037af43c7ac70de964b352902cd8c59a6a9f972c0e4e9aaa45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableAttributeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableAttributeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6faf0c6d650e7d1d5770bb1c194551850d4df71953d01c2a5d669baa603cf414)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2071f2592f0ef5e96d1b36f216831276962606484c6250cf10507041195b7794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e18e2273107a557d03559ca6825e47a83eca157024c098f2585c596029a531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5891dacc8f966d4d1f4909b81cbd3658d8cffd9764b0987f7a36f75ef456ab05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "attribute": "attribute",
        "billing_mode": "billingMode",
        "deletion_protection_enabled": "deletionProtectionEnabled",
        "global_secondary_index": "globalSecondaryIndex",
        "hash_key": "hashKey",
        "id": "id",
        "local_secondary_index": "localSecondaryIndex",
        "point_in_time_recovery": "pointInTimeRecovery",
        "range_key": "rangeKey",
        "read_capacity": "readCapacity",
        "replica": "replica",
        "restore_date_time": "restoreDateTime",
        "restore_source_name": "restoreSourceName",
        "restore_to_latest_time": "restoreToLatestTime",
        "server_side_encryption": "serverSideEncryption",
        "stream_enabled": "streamEnabled",
        "stream_view_type": "streamViewType",
        "table_class": "tableClass",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "ttl": "ttl",
        "write_capacity": "writeCapacity",
    },
)
class DynamodbTableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableGlobalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hash_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableLocalSecondaryIndex", typing.Dict[builtins.str, typing.Any]]]]] = None,
        point_in_time_recovery: typing.Optional[typing.Union["DynamodbTablePointInTimeRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        range_key: typing.Optional[builtins.str] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DynamodbTableReplica", typing.Dict[builtins.str, typing.Any]]]]] = None,
        restore_date_time: typing.Optional[builtins.str] = None,
        restore_source_name: typing.Optional[builtins.str] = None,
        restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_side_encryption: typing.Optional[typing.Union["DynamodbTableServerSideEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stream_view_type: typing.Optional[builtins.str] = None,
        table_class: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DynamodbTableTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["DynamodbTableTtl", typing.Dict[builtins.str, typing.Any]]] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#attribute DynamodbTable#attribute}
        :param billing_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#billing_mode DynamodbTable#billing_mode}.
        :param deletion_protection_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#deletion_protection_enabled DynamodbTable#deletion_protection_enabled}.
        :param global_secondary_index: global_secondary_index block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#global_secondary_index DynamodbTable#global_secondary_index}
        :param hash_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#hash_key DynamodbTable#hash_key}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#id DynamodbTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_secondary_index: local_secondary_index block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#local_secondary_index DynamodbTable#local_secondary_index}
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}
        :param range_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.
        :param read_capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#read_capacity DynamodbTable#read_capacity}.
        :param replica: replica block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#replica DynamodbTable#replica}
        :param restore_date_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_date_time DynamodbTable#restore_date_time}.
        :param restore_source_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_source_name DynamodbTable#restore_source_name}.
        :param restore_to_latest_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_to_latest_time DynamodbTable#restore_to_latest_time}.
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#server_side_encryption DynamodbTable#server_side_encryption}
        :param stream_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#stream_enabled DynamodbTable#stream_enabled}.
        :param stream_view_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#stream_view_type DynamodbTable#stream_view_type}.
        :param table_class: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#table_class DynamodbTable#table_class}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#tags DynamodbTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#tags_all DynamodbTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#timeouts DynamodbTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#ttl DynamodbTable#ttl}
        :param write_capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#write_capacity DynamodbTable#write_capacity}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(point_in_time_recovery, dict):
            point_in_time_recovery = DynamodbTablePointInTimeRecovery(**point_in_time_recovery)
        if isinstance(server_side_encryption, dict):
            server_side_encryption = DynamodbTableServerSideEncryption(**server_side_encryption)
        if isinstance(timeouts, dict):
            timeouts = DynamodbTableTimeouts(**timeouts)
        if isinstance(ttl, dict):
            ttl = DynamodbTableTtl(**ttl)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a6731f7c9f5f6e76002aed7e593b8fc75e28a65e53b2cc41dd8b4d0c5ccc069)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
            check_type(argname="argument billing_mode", value=billing_mode, expected_type=type_hints["billing_mode"])
            check_type(argname="argument deletion_protection_enabled", value=deletion_protection_enabled, expected_type=type_hints["deletion_protection_enabled"])
            check_type(argname="argument global_secondary_index", value=global_secondary_index, expected_type=type_hints["global_secondary_index"])
            check_type(argname="argument hash_key", value=hash_key, expected_type=type_hints["hash_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local_secondary_index", value=local_secondary_index, expected_type=type_hints["local_secondary_index"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument range_key", value=range_key, expected_type=type_hints["range_key"])
            check_type(argname="argument read_capacity", value=read_capacity, expected_type=type_hints["read_capacity"])
            check_type(argname="argument replica", value=replica, expected_type=type_hints["replica"])
            check_type(argname="argument restore_date_time", value=restore_date_time, expected_type=type_hints["restore_date_time"])
            check_type(argname="argument restore_source_name", value=restore_source_name, expected_type=type_hints["restore_source_name"])
            check_type(argname="argument restore_to_latest_time", value=restore_to_latest_time, expected_type=type_hints["restore_to_latest_time"])
            check_type(argname="argument server_side_encryption", value=server_side_encryption, expected_type=type_hints["server_side_encryption"])
            check_type(argname="argument stream_enabled", value=stream_enabled, expected_type=type_hints["stream_enabled"])
            check_type(argname="argument stream_view_type", value=stream_view_type, expected_type=type_hints["stream_view_type"])
            check_type(argname="argument table_class", value=table_class, expected_type=type_hints["table_class"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument write_capacity", value=write_capacity, expected_type=type_hints["write_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if attribute is not None:
            self._values["attribute"] = attribute
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if deletion_protection_enabled is not None:
            self._values["deletion_protection_enabled"] = deletion_protection_enabled
        if global_secondary_index is not None:
            self._values["global_secondary_index"] = global_secondary_index
        if hash_key is not None:
            self._values["hash_key"] = hash_key
        if id is not None:
            self._values["id"] = id
        if local_secondary_index is not None:
            self._values["local_secondary_index"] = local_secondary_index
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if range_key is not None:
            self._values["range_key"] = range_key
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if replica is not None:
            self._values["replica"] = replica
        if restore_date_time is not None:
            self._values["restore_date_time"] = restore_date_time
        if restore_source_name is not None:
            self._values["restore_source_name"] = restore_source_name
        if restore_to_latest_time is not None:
            self._values["restore_to_latest_time"] = restore_to_latest_time
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if stream_enabled is not None:
            self._values["stream_enabled"] = stream_enabled
        if stream_view_type is not None:
            self._values["stream_view_type"] = stream_view_type
        if table_class is not None:
            self._values["table_class"] = table_class
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if ttl is not None:
            self._values["ttl"] = ttl
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]]:
        '''attribute block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#attribute DynamodbTable#attribute}
        '''
        result = self._values.get("attribute")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#billing_mode DynamodbTable#billing_mode}.'''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#deletion_protection_enabled DynamodbTable#deletion_protection_enabled}.'''
        result = self._values.get("deletion_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def global_secondary_index(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]]:
        '''global_secondary_index block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#global_secondary_index DynamodbTable#global_secondary_index}
        '''
        result = self._values.get("global_secondary_index")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableGlobalSecondaryIndex"]]], result)

    @builtins.property
    def hash_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#hash_key DynamodbTable#hash_key}.'''
        result = self._values.get("hash_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#id DynamodbTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_secondary_index(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]]:
        '''local_secondary_index block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#local_secondary_index DynamodbTable#local_secondary_index}
        '''
        result = self._values.get("local_secondary_index")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableLocalSecondaryIndex"]]], result)

    @builtins.property
    def point_in_time_recovery(
        self,
    ) -> typing.Optional["DynamodbTablePointInTimeRecovery"]:
        '''point_in_time_recovery block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional["DynamodbTablePointInTimeRecovery"], result)

    @builtins.property
    def range_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.'''
        result = self._values.get("range_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#read_capacity DynamodbTable#read_capacity}.'''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replica(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]]:
        '''replica block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#replica DynamodbTable#replica}
        '''
        result = self._values.get("replica")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DynamodbTableReplica"]]], result)

    @builtins.property
    def restore_date_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_date_time DynamodbTable#restore_date_time}.'''
        result = self._values.get("restore_date_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_source_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_source_name DynamodbTable#restore_source_name}.'''
        result = self._values.get("restore_source_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_to_latest_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#restore_to_latest_time DynamodbTable#restore_to_latest_time}.'''
        result = self._values.get("restore_to_latest_time")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def server_side_encryption(
        self,
    ) -> typing.Optional["DynamodbTableServerSideEncryption"]:
        '''server_side_encryption block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#server_side_encryption DynamodbTable#server_side_encryption}
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional["DynamodbTableServerSideEncryption"], result)

    @builtins.property
    def stream_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#stream_enabled DynamodbTable#stream_enabled}.'''
        result = self._values.get("stream_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def stream_view_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#stream_view_type DynamodbTable#stream_view_type}.'''
        result = self._values.get("stream_view_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#table_class DynamodbTable#table_class}.'''
        result = self._values.get("table_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#tags DynamodbTable#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#tags_all DynamodbTable#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DynamodbTableTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#timeouts DynamodbTable#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DynamodbTableTimeouts"], result)

    @builtins.property
    def ttl(self) -> typing.Optional["DynamodbTableTtl"]:
        '''ttl block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#ttl DynamodbTable#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional["DynamodbTableTtl"], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#write_capacity DynamodbTable#write_capacity}.'''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableGlobalSecondaryIndex",
    jsii_struct_bases=[],
    name_mapping={
        "hash_key": "hashKey",
        "name": "name",
        "projection_type": "projectionType",
        "non_key_attributes": "nonKeyAttributes",
        "range_key": "rangeKey",
        "read_capacity": "readCapacity",
        "write_capacity": "writeCapacity",
    },
)
class DynamodbTableGlobalSecondaryIndex:
    def __init__(
        self,
        *,
        hash_key: builtins.str,
        name: builtins.str,
        projection_type: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        range_key: typing.Optional[builtins.str] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hash_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#hash_key DynamodbTable#hash_key}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.
        :param projection_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#projection_type DynamodbTable#projection_type}.
        :param non_key_attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.
        :param range_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.
        :param read_capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#read_capacity DynamodbTable#read_capacity}.
        :param write_capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#write_capacity DynamodbTable#write_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07ecc22b70b38f7a6af6e28531add315f1b2b1651a7849e3ce6ad4c893b5f071)
            check_type(argname="argument hash_key", value=hash_key, expected_type=type_hints["hash_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument projection_type", value=projection_type, expected_type=type_hints["projection_type"])
            check_type(argname="argument non_key_attributes", value=non_key_attributes, expected_type=type_hints["non_key_attributes"])
            check_type(argname="argument range_key", value=range_key, expected_type=type_hints["range_key"])
            check_type(argname="argument read_capacity", value=read_capacity, expected_type=type_hints["read_capacity"])
            check_type(argname="argument write_capacity", value=write_capacity, expected_type=type_hints["write_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hash_key": hash_key,
            "name": name,
            "projection_type": projection_type,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes
        if range_key is not None:
            self._values["range_key"] = range_key
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

    @builtins.property
    def hash_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#hash_key DynamodbTable#hash_key}.'''
        result = self._values.get("hash_key")
        assert result is not None, "Required property 'hash_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def projection_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#projection_type DynamodbTable#projection_type}.'''
        result = self._values.get("projection_type")
        assert result is not None, "Required property 'projection_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.'''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def range_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.'''
        result = self._values.get("range_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#read_capacity DynamodbTable#read_capacity}.'''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#write_capacity DynamodbTable#write_capacity}.'''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableGlobalSecondaryIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableGlobalSecondaryIndexList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableGlobalSecondaryIndexList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae644a4027f99f69ad1d1b4e6379138978514711eda41b0ef8ee60a9ad8daee8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DynamodbTableGlobalSecondaryIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a8e081f7ea414633db066f81ad4e7ecb8c82ec1eb87bac77c11b2d52b1a994a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableGlobalSecondaryIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709fc7b8e4a9505275a20c2fbfee21427eed77f6d92b85a68e2f26be8f2b4f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0df098805383a84aad98dbb40c540b3495824604db26bb8d0f6b25be9241eb90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9880c3648fbde8632e323e0da4b7cc71551f3a1db9fb0961d23cccf06426bd19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f00c61edced4f0c0c178973ac6a0b127a261ebe6f7aa1ee9d3f5a78a01da103c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableGlobalSecondaryIndexOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableGlobalSecondaryIndexOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f94de53d7b19b654302b7a85097659f4ff2ee8107ff340e02b015685c4582d55)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNonKeyAttributes")
    def reset_non_key_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonKeyAttributes", []))

    @jsii.member(jsii_name="resetRangeKey")
    def reset_range_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKey", []))

    @jsii.member(jsii_name="resetReadCapacity")
    def reset_read_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadCapacity", []))

    @jsii.member(jsii_name="resetWriteCapacity")
    def reset_write_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="hashKeyInput")
    def hash_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributesInput")
    def non_key_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nonKeyAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectionTypeInput")
    def projection_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyInput")
    def range_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="readCapacityInput")
    def read_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="writeCapacityInput")
    def write_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKey")
    def hash_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKey"))

    @hash_key.setter
    def hash_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510a03d8d07639c6225505f5daca4c32d8c3d629c47740dc0d52a70fe94b28fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85f1b5c656ab814ff37f43928a8cc3dab7952d1fb72d9f2d41457d9a5fa7060c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributes")
    def non_key_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nonKeyAttributes"))

    @non_key_attributes.setter
    def non_key_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cd2cc9e8a838bb77e19374efd204bfb10ad0c9c92c8551a4867d87918cb6eee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonKeyAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="projectionType")
    def projection_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectionType"))

    @projection_type.setter
    def projection_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d71e36a74051bb5378518e17d444c8d7a5201aa7fe9c118eb0edb399b96ddf45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectionType", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKey")
    def range_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKey"))

    @range_key.setter
    def range_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36c132e9dd33868c44f5da182a9596c8be558adfb312a71d6deddbc09cdfd11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKey", value)

    @builtins.property
    @jsii.member(jsii_name="readCapacity")
    def read_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readCapacity"))

    @read_capacity.setter
    def read_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3761a69dffdc4626e5ab9d7b159946a45cbb47a753baf3a9f01d3fbc2b50f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="writeCapacity")
    def write_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writeCapacity"))

    @write_capacity.setter
    def write_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffeb8711986b0912ec9f9240cbb171ae2adf56f66d8c03953cbebffa0d8ff756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fbb5d1d01dc1e29eb6a2701c50e58e29e73b1b67c86f3fc862400801e5aa168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableLocalSecondaryIndex",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "projection_type": "projectionType",
        "range_key": "rangeKey",
        "non_key_attributes": "nonKeyAttributes",
    },
)
class DynamodbTableLocalSecondaryIndex:
    def __init__(
        self,
        *,
        name: builtins.str,
        projection_type: builtins.str,
        range_key: builtins.str,
        non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.
        :param projection_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#projection_type DynamodbTable#projection_type}.
        :param range_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.
        :param non_key_attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e1bc725ecab35b7f5a4801db9cd0dbe7cec06fc55efb0691992c58226723f1e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument projection_type", value=projection_type, expected_type=type_hints["projection_type"])
            check_type(argname="argument range_key", value=range_key, expected_type=type_hints["range_key"])
            check_type(argname="argument non_key_attributes", value=non_key_attributes, expected_type=type_hints["non_key_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "projection_type": projection_type,
            "range_key": range_key,
        }
        if non_key_attributes is not None:
            self._values["non_key_attributes"] = non_key_attributes

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#name DynamodbTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def projection_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#projection_type DynamodbTable#projection_type}.'''
        result = self._values.get("projection_type")
        assert result is not None, "Required property 'projection_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#range_key DynamodbTable#range_key}.'''
        result = self._values.get("range_key")
        assert result is not None, "Required property 'range_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def non_key_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#non_key_attributes DynamodbTable#non_key_attributes}.'''
        result = self._values.get("non_key_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableLocalSecondaryIndex(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableLocalSecondaryIndexList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableLocalSecondaryIndexList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1da1623eeca273a3d7c8ede44e4f4076a515dcd78750344b3cd977d6ed037a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DynamodbTableLocalSecondaryIndexOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ebc5ad7631149d78805e4a0f1c78bc6025b77e8700b8496ecdf42f27a6d102c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableLocalSecondaryIndexOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f589f95595edaba708678fd1a4c804d44753a988411d9fb5925d907e23360c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__133a9a462df56fe56b955304507c5c5755fd8d7f8a95da220ba341a9d1ea4ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffff088fe9e295af445e0e323ea062f0cb85d460eb5ca6840d38281b27a05043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77236c3d0d6733e5be1831d4906f8a958f5e5e226d8794e5c5333abda4988ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableLocalSecondaryIndexOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableLocalSecondaryIndexOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cfb86c44035417bbb0fc13b4b419f8e78ea6970f8170ff03d894fcca0d1d03c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNonKeyAttributes")
    def reset_non_key_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonKeyAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributesInput")
    def non_key_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nonKeyAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectionTypeInput")
    def projection_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyInput")
    def range_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3d6035f5250eb6ff97db71bd6a77e61db28dfa9ac981e0c631aa2009bafe7e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nonKeyAttributes")
    def non_key_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nonKeyAttributes"))

    @non_key_attributes.setter
    def non_key_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6d374ae7f061ef58b26e92aa9189561f78accff3abb513d3a872daca83d889e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonKeyAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="projectionType")
    def projection_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectionType"))

    @projection_type.setter
    def projection_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d07d9e18402a6c3f34aea0739691a30e683b8d507697c4f3cc546b79fa33eedb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectionType", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKey")
    def range_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKey"))

    @range_key.setter
    def range_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34b89b25cdc8a70228120b766446f1fb95eb97178248976db773ff261089215e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10beff218043583a4bb719ab74c25f7a2e45a29f8d9fb1cc6128956952c25710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTablePointInTimeRecovery",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class DynamodbTablePointInTimeRecovery:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5204bef78e35469da4f3a1c59a6783818966a493145845512ba7142665e82f5)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTablePointInTimeRecovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTablePointInTimeRecoveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTablePointInTimeRecoveryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00fdfdcd923ad95dac885058623c71c273bb8f45bb31d8bf916b35d81dd1dc4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932bf01b91532f5429718fed186df56944e241d0cb2479623060b790f56b2535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DynamodbTablePointInTimeRecovery]:
        return typing.cast(typing.Optional[DynamodbTablePointInTimeRecovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DynamodbTablePointInTimeRecovery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa359bdaeae88e3a6374bbb69b6960afbbd97dd2c511cc1ad6c97463eb567d1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableReplica",
    jsii_struct_bases=[],
    name_mapping={
        "region_name": "regionName",
        "kms_key_arn": "kmsKeyArn",
        "point_in_time_recovery": "pointInTimeRecovery",
        "propagate_tags": "propagateTags",
    },
)
class DynamodbTableReplica:
    def __init__(
        self,
        *,
        region_name: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        point_in_time_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        propagate_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param region_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#region_name DynamodbTable#region_name}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.
        :param point_in_time_recovery: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#propagate_tags DynamodbTable#propagate_tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa7d53e86495ed09dc942a584987f31910041b9260b9b53ce316e5463f2af102)
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region_name": region_name,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags

    @builtins.property
    def region_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#region_name DynamodbTable#region_name}.'''
        result = self._values.get("region_name")
        assert result is not None, "Required property 'region_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time_recovery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#point_in_time_recovery DynamodbTable#point_in_time_recovery}.'''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def propagate_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#propagate_tags DynamodbTable#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableReplica(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableReplicaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableReplicaList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c29ae5c055dd2dc0ae5a3b597a0faa30e2aea3859765010bf31c8b6df55cbc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DynamodbTableReplicaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d702889fcfc7c8d02a4deab2d66bfa1222b2e83bdf6703627de844ca11de42ff)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DynamodbTableReplicaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0061e340f2cb8f0512f77267aa236f5e53defaab0cc5a8b54ff40aababe226f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09118ca6eef3ee9762e52cb6929414ba52e0a23142ccd4f5b567b80a9e714e06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d342e2b8834ad53dac7a441e4d589c5e6ae7049e883910dad67e8c68ca41f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__460c68be0c073979577e7e66d12975041c755ce2d7c2ada36321555ecb92c8e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DynamodbTableReplicaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableReplicaOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7bcc2501056aa118ca9fb7f9ea6cd862a282dff1820ece00ee09d06e17708bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPointInTimeRecovery")
    def reset_point_in_time_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecovery", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @builtins.property
    @jsii.member(jsii_name="streamLabel")
    def stream_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamLabel"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryInput")
    def point_in_time_recovery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pointInTimeRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionNameInput")
    def region_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7953d430dfcc5a0735f714a9f7f20906f46eb1ab7db37fe7fc637f6c6837e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "pointInTimeRecovery"))

    @point_in_time_recovery.setter
    def point_in_time_recovery(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eee00885402717bc426b9d26b6cb6c148755f5a688bc6d1d3e6b31f813fd47d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTimeRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__693981845b6fc0a6563ae0d8cbe40dbbef6d2d5ef63604cd0ea29ce23f7d4624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="regionName")
    def region_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionName"))

    @region_name.setter
    def region_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c0b3cb30fc31e8dff99eb72b0475de3ef6fb9c15578047b03c83e98d89ac277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a0f8b185ff3a99140e6775a59a198550c05b6f227215cbd25d9613d89e0502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableServerSideEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "kms_key_arn": "kmsKeyArn"},
)
class DynamodbTableServerSideEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d3eba487abe61832b9f64357e936eafc72b7c3e824778134322b7ddcc47d07)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#kms_key_arn DynamodbTable#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableServerSideEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableServerSideEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableServerSideEncryptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2088a0afb49083d9832ac9c835ad414ec1c9f58af72502e8e0be01019fcfc3d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__378be53a697fb38a15aff2cbedb7b88cdacc014209d244e29fb74cdfab7e577b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f851f4b0f5e049d0096364c3eed77e2231b97ffe8d2044fc4b13671bb976bdae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DynamodbTableServerSideEncryption]:
        return typing.cast(typing.Optional[DynamodbTableServerSideEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DynamodbTableServerSideEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2552999f02ef255ceaee4063962053ce9d654491779e0cd285132c01f859dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DynamodbTableTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#create DynamodbTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#delete DynamodbTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#update DynamodbTable#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc5bf40239ac5caca97e0e0eef4bea96cb1fce81639dd121b1521352001cc34)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#create DynamodbTable#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#delete DynamodbTable#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#update DynamodbTable#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2591818c96530894e5aca682408cff04c4a1b5f6ad8c92a599a6eb48a0bb8050)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0a020cdf2b69db4d30e09223a45ece899dd4687aeac297cd5e4b422ccaf4887)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ea0d13ced0ba67c6e2cca392bb8d78a6734068fa99a31622b091bf5f8fe315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fe538da10cc4d21339496184cb1bcfe6e724ca189e0dc182b384d30ceb01644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24409822d48a0d8fce0388ca5dcb332f4ff070fe06f0e9b986cb9f6da866b453)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableTtl",
    jsii_struct_bases=[],
    name_mapping={"attribute_name": "attributeName", "enabled": "enabled"},
)
class DynamodbTableTtl:
    def __init__(
        self,
        *,
        attribute_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param attribute_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#attribute_name DynamodbTable#attribute_name}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83abe35bf0176a8556badca820681d3360a2f478b436d84ea64bfccac5461a53)
            check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_name": attribute_name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def attribute_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#attribute_name DynamodbTable#attribute_name}.'''
        result = self._values.get("attribute_name")
        assert result is not None, "Required property 'attribute_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/dynamodb_table#enabled DynamodbTable#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamodbTableTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamodbTableTtlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dynamodbTable.DynamodbTableTtlOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b90cc026f91796f60a439d96bcfe2b755f34c0f6eb2fd23fa040aef07b745e88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__956234ca56c7934e4f359bb5c8d53f84ee9257ddc1d3fc21533d2c39d5b6d77b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b952fca027ae8a89d7a9af35d0bab926a030c2ad04631c94f24ca7a2737b3ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DynamodbTableTtl]:
        return typing.cast(typing.Optional[DynamodbTableTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DynamodbTableTtl]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0f5d18a54025fea3ecbe241725b0c9bdd225256114b06ceac929e6ca06af469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DynamodbTable",
    "DynamodbTableAttribute",
    "DynamodbTableAttributeList",
    "DynamodbTableAttributeOutputReference",
    "DynamodbTableConfig",
    "DynamodbTableGlobalSecondaryIndex",
    "DynamodbTableGlobalSecondaryIndexList",
    "DynamodbTableGlobalSecondaryIndexOutputReference",
    "DynamodbTableLocalSecondaryIndex",
    "DynamodbTableLocalSecondaryIndexList",
    "DynamodbTableLocalSecondaryIndexOutputReference",
    "DynamodbTablePointInTimeRecovery",
    "DynamodbTablePointInTimeRecoveryOutputReference",
    "DynamodbTableReplica",
    "DynamodbTableReplicaList",
    "DynamodbTableReplicaOutputReference",
    "DynamodbTableServerSideEncryption",
    "DynamodbTableServerSideEncryptionOutputReference",
    "DynamodbTableTimeouts",
    "DynamodbTableTimeoutsOutputReference",
    "DynamodbTableTtl",
    "DynamodbTableTtlOutputReference",
]

publication.publish()

def _typecheckingstub__e5b33d5bdfd1849e705d1c43f7bb8e268f2cbe5afb89bc1d051b68b7a4c87274(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
    billing_mode: typing.Optional[builtins.str] = None,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableGlobalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hash_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableLocalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    point_in_time_recovery: typing.Optional[typing.Union[DynamodbTablePointInTimeRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    range_key: typing.Optional[builtins.str] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableReplica, typing.Dict[builtins.str, typing.Any]]]]] = None,
    restore_date_time: typing.Optional[builtins.str] = None,
    restore_source_name: typing.Optional[builtins.str] = None,
    restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_side_encryption: typing.Optional[typing.Union[DynamodbTableServerSideEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stream_view_type: typing.Optional[builtins.str] = None,
    table_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DynamodbTableTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    ttl: typing.Optional[typing.Union[DynamodbTableTtl, typing.Dict[builtins.str, typing.Any]]] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5d3c897b64c6c6a9e0a38eda94e626c45d0c5dd3597bff492102de947bd7d32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b0b912faa3eae3f70d096aec19f81ec6f43b4d3fae80c4042d9bc63ce355a4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableGlobalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c6dee6715c159f2154a5cf5f20ba953d9b5ac70f79016b5f8683b45eb154b2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableLocalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06b32e75d943fbe760d6e722f3433c45811267562fffc8a68daab40b5b8da7d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableReplica, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3c7bee0af2b2be096c74b759885b4679f40e8120ba91484aab3fdc1dd6c003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d10d233745ee7d9ea760497794027a77acb63d87682918a3c0b67e1bd57624b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87194fc82907b02b4f296ec1f6c029271dfa23724c17fe979a7045e25df5afab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ae7ef85603022c1dca8cf01bf547bc43150ad4d2d651a8c8f0cd3fc14d4d93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9489fc32fa98bc78d6e3b547b90021c399056b2fb598486999a9a0fd63d8d38d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7717400be74d87238017104fb443454ecae5ff1aa8b04bb33f376e027e52a8e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__503b130ec215d542027ebd1ab07396da223da166cf84eea918d9942cd25f53a8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c09ac827345f3b38ae9a4f12dec6315cbbd2f07ebb4e2043664f099d4ac549(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e643c8947c6975290fa8ec2a07a1581f08da27a835c8723d5be67402519006c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0507a5a148aa1938fac2ce502885d179e493fdd41fcb4932a6d6a8d27ad45187(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d860a6a5afd133eebea613c23cbffca79b16c74f6d4105e736c064798381ad3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8f9955e28aa9e7aef4fe176f225699582e53ddb64876965fe95719bb03b24a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af077df7f7b0745304fbee9b9494e884efcc95c87078daf951d1e73fc5ff8cd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__347f56cdd57aca01b8ca3d2b02c9b6aaed4128c51753a21997f976d10f9b52a6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576f8f1c39f56193f2a4bfe6b6cbbffdb646e20b276e46a08306162839cb3da3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f99b2ddc135d07ee0f8fea7e99d59584eda8d993592afef57b85c0836a1bacb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356c9d5e509da6ea0bdb0b33b04d19c819036ea2e492d0bfcd5f22b25a727c40(
    *,
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7133a294f9aa1a8125bbf8035e5da64c5c4cb320e8692f8cb0c35586451ee573(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091de9e4614ef19bc7ffcc8a5fb47e7146054c13c81d64f8d6e43bafb42fe00b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2918f281ca2ef49f03791ee275bfc629183796770eebc7ae9e7f26263d2b483(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58554496a62240d9b66f9cf6c18ab094ddc449d492a082aa1aea5ae455bdde4c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3a091133e11b5b483704a78a13c47ecbc8cdefc14aec4c7c5cb39055515b8b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45abc1f7abb63037af43c7ac70de964b352902cd8c59a6a9f972c0e4e9aaa45(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableAttribute]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6faf0c6d650e7d1d5770bb1c194551850d4df71953d01c2a5d669baa603cf414(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2071f2592f0ef5e96d1b36f216831276962606484c6250cf10507041195b7794(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e18e2273107a557d03559ca6825e47a83eca157024c098f2585c596029a531(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5891dacc8f966d4d1f4909b81cbd3658d8cffd9764b0987f7a36f75ef456ab05(
    value: typing.Optional[typing.Union[DynamodbTableAttribute, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a6731f7c9f5f6e76002aed7e593b8fc75e28a65e53b2cc41dd8b4d0c5ccc069(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    attribute: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableAttribute, typing.Dict[builtins.str, typing.Any]]]]] = None,
    billing_mode: typing.Optional[builtins.str] = None,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    global_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableGlobalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hash_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    local_secondary_index: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableLocalSecondaryIndex, typing.Dict[builtins.str, typing.Any]]]]] = None,
    point_in_time_recovery: typing.Optional[typing.Union[DynamodbTablePointInTimeRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    range_key: typing.Optional[builtins.str] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    replica: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DynamodbTableReplica, typing.Dict[builtins.str, typing.Any]]]]] = None,
    restore_date_time: typing.Optional[builtins.str] = None,
    restore_source_name: typing.Optional[builtins.str] = None,
    restore_to_latest_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_side_encryption: typing.Optional[typing.Union[DynamodbTableServerSideEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    stream_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stream_view_type: typing.Optional[builtins.str] = None,
    table_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DynamodbTableTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    ttl: typing.Optional[typing.Union[DynamodbTableTtl, typing.Dict[builtins.str, typing.Any]]] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ecc22b70b38f7a6af6e28531add315f1b2b1651a7849e3ce6ad4c893b5f071(
    *,
    hash_key: builtins.str,
    name: builtins.str,
    projection_type: builtins.str,
    non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    range_key: typing.Optional[builtins.str] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae644a4027f99f69ad1d1b4e6379138978514711eda41b0ef8ee60a9ad8daee8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8e081f7ea414633db066f81ad4e7ecb8c82ec1eb87bac77c11b2d52b1a994a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709fc7b8e4a9505275a20c2fbfee21427eed77f6d92b85a68e2f26be8f2b4f95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df098805383a84aad98dbb40c540b3495824604db26bb8d0f6b25be9241eb90(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9880c3648fbde8632e323e0da4b7cc71551f3a1db9fb0961d23cccf06426bd19(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00c61edced4f0c0c178973ac6a0b127a261ebe6f7aa1ee9d3f5a78a01da103c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableGlobalSecondaryIndex]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94de53d7b19b654302b7a85097659f4ff2ee8107ff340e02b015685c4582d55(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510a03d8d07639c6225505f5daca4c32d8c3d629c47740dc0d52a70fe94b28fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f1b5c656ab814ff37f43928a8cc3dab7952d1fb72d9f2d41457d9a5fa7060c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cd2cc9e8a838bb77e19374efd204bfb10ad0c9c92c8551a4867d87918cb6eee(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d71e36a74051bb5378518e17d444c8d7a5201aa7fe9c118eb0edb399b96ddf45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36c132e9dd33868c44f5da182a9596c8be558adfb312a71d6deddbc09cdfd11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3761a69dffdc4626e5ab9d7b159946a45cbb47a753baf3a9f01d3fbc2b50f54(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffeb8711986b0912ec9f9240cbb171ae2adf56f66d8c03953cbebffa0d8ff756(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbb5d1d01dc1e29eb6a2701c50e58e29e73b1b67c86f3fc862400801e5aa168(
    value: typing.Optional[typing.Union[DynamodbTableGlobalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1bc725ecab35b7f5a4801db9cd0dbe7cec06fc55efb0691992c58226723f1e(
    *,
    name: builtins.str,
    projection_type: builtins.str,
    range_key: builtins.str,
    non_key_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1da1623eeca273a3d7c8ede44e4f4076a515dcd78750344b3cd977d6ed037a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ebc5ad7631149d78805e4a0f1c78bc6025b77e8700b8496ecdf42f27a6d102c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f589f95595edaba708678fd1a4c804d44753a988411d9fb5925d907e23360c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__133a9a462df56fe56b955304507c5c5755fd8d7f8a95da220ba341a9d1ea4ec2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffff088fe9e295af445e0e323ea062f0cb85d460eb5ca6840d38281b27a05043(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77236c3d0d6733e5be1831d4906f8a958f5e5e226d8794e5c5333abda4988ac5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableLocalSecondaryIndex]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cfb86c44035417bbb0fc13b4b419f8e78ea6970f8170ff03d894fcca0d1d03c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d6035f5250eb6ff97db71bd6a77e61db28dfa9ac981e0c631aa2009bafe7e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d374ae7f061ef58b26e92aa9189561f78accff3abb513d3a872daca83d889e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07d9e18402a6c3f34aea0739691a30e683b8d507697c4f3cc546b79fa33eedb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b89b25cdc8a70228120b766446f1fb95eb97178248976db773ff261089215e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10beff218043583a4bb719ab74c25f7a2e45a29f8d9fb1cc6128956952c25710(
    value: typing.Optional[typing.Union[DynamodbTableLocalSecondaryIndex, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5204bef78e35469da4f3a1c59a6783818966a493145845512ba7142665e82f5(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00fdfdcd923ad95dac885058623c71c273bb8f45bb31d8bf916b35d81dd1dc4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932bf01b91532f5429718fed186df56944e241d0cb2479623060b790f56b2535(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa359bdaeae88e3a6374bbb69b6960afbbd97dd2c511cc1ad6c97463eb567d1d(
    value: typing.Optional[DynamodbTablePointInTimeRecovery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa7d53e86495ed09dc942a584987f31910041b9260b9b53ce316e5463f2af102(
    *,
    region_name: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
    point_in_time_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    propagate_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c29ae5c055dd2dc0ae5a3b597a0faa30e2aea3859765010bf31c8b6df55cbc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d702889fcfc7c8d02a4deab2d66bfa1222b2e83bdf6703627de844ca11de42ff(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0061e340f2cb8f0512f77267aa236f5e53defaab0cc5a8b54ff40aababe226f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09118ca6eef3ee9762e52cb6929414ba52e0a23142ccd4f5b567b80a9e714e06(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d342e2b8834ad53dac7a441e4d589c5e6ae7049e883910dad67e8c68ca41f7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__460c68be0c073979577e7e66d12975041c755ce2d7c2ada36321555ecb92c8e9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DynamodbTableReplica]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7bcc2501056aa118ca9fb7f9ea6cd862a282dff1820ece00ee09d06e17708bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7953d430dfcc5a0735f714a9f7f20906f46eb1ab7db37fe7fc637f6c6837e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eee00885402717bc426b9d26b6cb6c148755f5a688bc6d1d3e6b31f813fd47d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__693981845b6fc0a6563ae0d8cbe40dbbef6d2d5ef63604cd0ea29ce23f7d4624(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c0b3cb30fc31e8dff99eb72b0475de3ef6fb9c15578047b03c83e98d89ac277(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a0f8b185ff3a99140e6775a59a198550c05b6f227215cbd25d9613d89e0502(
    value: typing.Optional[typing.Union[DynamodbTableReplica, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d3eba487abe61832b9f64357e936eafc72b7c3e824778134322b7ddcc47d07(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2088a0afb49083d9832ac9c835ad414ec1c9f58af72502e8e0be01019fcfc3d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__378be53a697fb38a15aff2cbedb7b88cdacc014209d244e29fb74cdfab7e577b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f851f4b0f5e049d0096364c3eed77e2231b97ffe8d2044fc4b13671bb976bdae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2552999f02ef255ceaee4063962053ce9d654491779e0cd285132c01f859dc(
    value: typing.Optional[DynamodbTableServerSideEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc5bf40239ac5caca97e0e0eef4bea96cb1fce81639dd121b1521352001cc34(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2591818c96530894e5aca682408cff04c4a1b5f6ad8c92a599a6eb48a0bb8050(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a020cdf2b69db4d30e09223a45ece899dd4687aeac297cd5e4b422ccaf4887(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74ea0d13ced0ba67c6e2cca392bb8d78a6734068fa99a31622b091bf5f8fe315(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe538da10cc4d21339496184cb1bcfe6e724ca189e0dc182b384d30ceb01644(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24409822d48a0d8fce0388ca5dcb332f4ff070fe06f0e9b986cb9f6da866b453(
    value: typing.Optional[typing.Union[DynamodbTableTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83abe35bf0176a8556badca820681d3360a2f478b436d84ea64bfccac5461a53(
    *,
    attribute_name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b90cc026f91796f60a439d96bcfe2b755f34c0f6eb2fd23fa040aef07b745e88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__956234ca56c7934e4f359bb5c8d53f84ee9257ddc1d3fc21533d2c39d5b6d77b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b952fca027ae8a89d7a9af35d0bab926a030c2ad04631c94f24ca7a2737b3ef(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0f5d18a54025fea3ecbe241725b0c9bdd225256114b06ceac929e6ca06af469(
    value: typing.Optional[DynamodbTableTtl],
) -> None:
    """Type checking stubs"""
    pass
