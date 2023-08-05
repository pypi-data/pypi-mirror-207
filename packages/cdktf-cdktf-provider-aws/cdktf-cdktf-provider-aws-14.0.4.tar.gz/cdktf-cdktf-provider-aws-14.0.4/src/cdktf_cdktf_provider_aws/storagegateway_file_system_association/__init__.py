'''
# `aws_storagegateway_file_system_association`

Refer to the Terraform Registory for docs: [`aws_storagegateway_file_system_association`](https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association).
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


class StoragegatewayFileSystemAssociation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayFileSystemAssociation.StoragegatewayFileSystemAssociation",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association aws_storagegateway_file_system_association}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        gateway_arn: builtins.str,
        location_arn: builtins.str,
        password: builtins.str,
        username: builtins.str,
        audit_destination_arn: typing.Optional[builtins.str] = None,
        cache_attributes: typing.Optional[typing.Union["StoragegatewayFileSystemAssociationCacheAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association aws_storagegateway_file_system_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gateway_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#gateway_arn StoragegatewayFileSystemAssociation#gateway_arn}.
        :param location_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#location_arn StoragegatewayFileSystemAssociation#location_arn}.
        :param password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#password StoragegatewayFileSystemAssociation#password}.
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#username StoragegatewayFileSystemAssociation#username}.
        :param audit_destination_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#audit_destination_arn StoragegatewayFileSystemAssociation#audit_destination_arn}.
        :param cache_attributes: cache_attributes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#cache_attributes StoragegatewayFileSystemAssociation#cache_attributes}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#id StoragegatewayFileSystemAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#tags StoragegatewayFileSystemAssociation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#tags_all StoragegatewayFileSystemAssociation#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f6c9c26a7ad9eafb4ed769a35ee6f747ab1a3dc67113bfd4cbddae481a8f5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StoragegatewayFileSystemAssociationConfig(
            gateway_arn=gateway_arn,
            location_arn=location_arn,
            password=password,
            username=username,
            audit_destination_arn=audit_destination_arn,
            cache_attributes=cache_attributes,
            id=id,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCacheAttributes")
    def put_cache_attributes(
        self,
        *,
        cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_stale_timeout_in_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#cache_stale_timeout_in_seconds StoragegatewayFileSystemAssociation#cache_stale_timeout_in_seconds}.
        '''
        value = StoragegatewayFileSystemAssociationCacheAttributes(
            cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds
        )

        return typing.cast(None, jsii.invoke(self, "putCacheAttributes", [value]))

    @jsii.member(jsii_name="resetAuditDestinationArn")
    def reset_audit_destination_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditDestinationArn", []))

    @jsii.member(jsii_name="resetCacheAttributes")
    def reset_cache_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

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
    @jsii.member(jsii_name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> "StoragegatewayFileSystemAssociationCacheAttributesOutputReference":
        return typing.cast("StoragegatewayFileSystemAssociationCacheAttributesOutputReference", jsii.get(self, "cacheAttributes"))

    @builtins.property
    @jsii.member(jsii_name="auditDestinationArnInput")
    def audit_destination_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditDestinationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheAttributesInput")
    def cache_attributes_input(
        self,
    ) -> typing.Optional["StoragegatewayFileSystemAssociationCacheAttributes"]:
        return typing.cast(typing.Optional["StoragegatewayFileSystemAssociationCacheAttributes"], jsii.get(self, "cacheAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayArnInput")
    def gateway_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationArnInput")
    def location_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

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
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="auditDestinationArn")
    def audit_destination_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditDestinationArn"))

    @audit_destination_arn.setter
    def audit_destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ee72721a7d684aef424e505ae12aa07599f404c6b1d7e52ef4446d7fb745f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditDestinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayArn")
    def gateway_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayArn"))

    @gateway_arn.setter
    def gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5258534308947b4cc42a42425e6649e58791b33c1b15178249a177243804bf83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5dc6989fa547530160c55375fc03bea1724f6c4acf9fb7c601e0d98283f1bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="locationArn")
    def location_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationArn"))

    @location_arn.setter
    def location_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6da464163f109c34f24721fbcff2b8681bbd8196d3dcd9545f90e566ea37d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationArn", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e716dc5c5f4542f43116745a7b09257819d19118db463be0e1d9171263812b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b38520f70b544c1e1ccfbd5d8f8d0ba7cb2ae9310b08faa6fb407141fe4eb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__178dd0030301c03d1051985409015aa39243b45d8639728d403e3cfa6ad77f9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26dc674ff2ee158ea20b5e6662cd25db1a40d4223efe897f34ad69772d11a27d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayFileSystemAssociation.StoragegatewayFileSystemAssociationCacheAttributes",
    jsii_struct_bases=[],
    name_mapping={"cache_stale_timeout_in_seconds": "cacheStaleTimeoutInSeconds"},
)
class StoragegatewayFileSystemAssociationCacheAttributes:
    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_stale_timeout_in_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#cache_stale_timeout_in_seconds StoragegatewayFileSystemAssociation#cache_stale_timeout_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfc6c5770e184db4a6d4823c47229c7b1364110587ffb44eb313ac98910e504e)
            check_type(argname="argument cache_stale_timeout_in_seconds", value=cache_stale_timeout_in_seconds, expected_type=type_hints["cache_stale_timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cache_stale_timeout_in_seconds is not None:
            self._values["cache_stale_timeout_in_seconds"] = cache_stale_timeout_in_seconds

    @builtins.property
    def cache_stale_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#cache_stale_timeout_in_seconds StoragegatewayFileSystemAssociation#cache_stale_timeout_in_seconds}.'''
        result = self._values.get("cache_stale_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayFileSystemAssociationCacheAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayFileSystemAssociationCacheAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayFileSystemAssociation.StoragegatewayFileSystemAssociationCacheAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a22d65841933d2345272227ab2ce6a51979bf6af9391a14a26c6b1900242e200)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCacheStaleTimeoutInSeconds")
    def reset_cache_stale_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheStaleTimeoutInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="cacheStaleTimeoutInSecondsInput")
    def cache_stale_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cacheStaleTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cacheStaleTimeoutInSeconds"))

    @cache_stale_timeout_in_seconds.setter
    def cache_stale_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6646d2596175db98c84ee6dd6971d04157f261cbfd73846cd66c381ca598744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheStaleTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayFileSystemAssociationCacheAttributes]:
        return typing.cast(typing.Optional[StoragegatewayFileSystemAssociationCacheAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayFileSystemAssociationCacheAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f12dc61265789894e7d65d4028988e2ef7ec1eb08ca206142f87f944f49f12f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayFileSystemAssociation.StoragegatewayFileSystemAssociationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gateway_arn": "gatewayArn",
        "location_arn": "locationArn",
        "password": "password",
        "username": "username",
        "audit_destination_arn": "auditDestinationArn",
        "cache_attributes": "cacheAttributes",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class StoragegatewayFileSystemAssociationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        gateway_arn: builtins.str,
        location_arn: builtins.str,
        password: builtins.str,
        username: builtins.str,
        audit_destination_arn: typing.Optional[builtins.str] = None,
        cache_attributes: typing.Optional[typing.Union[StoragegatewayFileSystemAssociationCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param gateway_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#gateway_arn StoragegatewayFileSystemAssociation#gateway_arn}.
        :param location_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#location_arn StoragegatewayFileSystemAssociation#location_arn}.
        :param password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#password StoragegatewayFileSystemAssociation#password}.
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#username StoragegatewayFileSystemAssociation#username}.
        :param audit_destination_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#audit_destination_arn StoragegatewayFileSystemAssociation#audit_destination_arn}.
        :param cache_attributes: cache_attributes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#cache_attributes StoragegatewayFileSystemAssociation#cache_attributes}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#id StoragegatewayFileSystemAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#tags StoragegatewayFileSystemAssociation#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#tags_all StoragegatewayFileSystemAssociation#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cache_attributes, dict):
            cache_attributes = StoragegatewayFileSystemAssociationCacheAttributes(**cache_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a3bcdc2fede3a5ad0b32ca183f219cc3457c51f5621bd55f949e18a55ca3d1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument audit_destination_arn", value=audit_destination_arn, expected_type=type_hints["audit_destination_arn"])
            check_type(argname="argument cache_attributes", value=cache_attributes, expected_type=type_hints["cache_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_arn": gateway_arn,
            "location_arn": location_arn,
            "password": password,
            "username": username,
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
        if audit_destination_arn is not None:
            self._values["audit_destination_arn"] = audit_destination_arn
        if cache_attributes is not None:
            self._values["cache_attributes"] = cache_attributes
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def gateway_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#gateway_arn StoragegatewayFileSystemAssociation#gateway_arn}.'''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#location_arn StoragegatewayFileSystemAssociation#location_arn}.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#password StoragegatewayFileSystemAssociation#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#username StoragegatewayFileSystemAssociation#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_destination_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#audit_destination_arn StoragegatewayFileSystemAssociation#audit_destination_arn}.'''
        result = self._values.get("audit_destination_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_attributes(
        self,
    ) -> typing.Optional[StoragegatewayFileSystemAssociationCacheAttributes]:
        '''cache_attributes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#cache_attributes StoragegatewayFileSystemAssociation#cache_attributes}
        '''
        result = self._values.get("cache_attributes")
        return typing.cast(typing.Optional[StoragegatewayFileSystemAssociationCacheAttributes], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#id StoragegatewayFileSystemAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#tags StoragegatewayFileSystemAssociation#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/storagegateway_file_system_association#tags_all StoragegatewayFileSystemAssociation#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayFileSystemAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StoragegatewayFileSystemAssociation",
    "StoragegatewayFileSystemAssociationCacheAttributes",
    "StoragegatewayFileSystemAssociationCacheAttributesOutputReference",
    "StoragegatewayFileSystemAssociationConfig",
]

publication.publish()

def _typecheckingstub__d0f6c9c26a7ad9eafb4ed769a35ee6f747ab1a3dc67113bfd4cbddae481a8f5d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    gateway_arn: builtins.str,
    location_arn: builtins.str,
    password: builtins.str,
    username: builtins.str,
    audit_destination_arn: typing.Optional[builtins.str] = None,
    cache_attributes: typing.Optional[typing.Union[StoragegatewayFileSystemAssociationCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__e0ee72721a7d684aef424e505ae12aa07599f404c6b1d7e52ef4446d7fb745f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5258534308947b4cc42a42425e6649e58791b33c1b15178249a177243804bf83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5dc6989fa547530160c55375fc03bea1724f6c4acf9fb7c601e0d98283f1bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6da464163f109c34f24721fbcff2b8681bbd8196d3dcd9545f90e566ea37d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e716dc5c5f4542f43116745a7b09257819d19118db463be0e1d9171263812b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b38520f70b544c1e1ccfbd5d8f8d0ba7cb2ae9310b08faa6fb407141fe4eb6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178dd0030301c03d1051985409015aa39243b45d8639728d403e3cfa6ad77f9a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26dc674ff2ee158ea20b5e6662cd25db1a40d4223efe897f34ad69772d11a27d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfc6c5770e184db4a6d4823c47229c7b1364110587ffb44eb313ac98910e504e(
    *,
    cache_stale_timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a22d65841933d2345272227ab2ce6a51979bf6af9391a14a26c6b1900242e200(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6646d2596175db98c84ee6dd6971d04157f261cbfd73846cd66c381ca598744(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f12dc61265789894e7d65d4028988e2ef7ec1eb08ca206142f87f944f49f12f(
    value: typing.Optional[StoragegatewayFileSystemAssociationCacheAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a3bcdc2fede3a5ad0b32ca183f219cc3457c51f5621bd55f949e18a55ca3d1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gateway_arn: builtins.str,
    location_arn: builtins.str,
    password: builtins.str,
    username: builtins.str,
    audit_destination_arn: typing.Optional[builtins.str] = None,
    cache_attributes: typing.Optional[typing.Union[StoragegatewayFileSystemAssociationCacheAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
