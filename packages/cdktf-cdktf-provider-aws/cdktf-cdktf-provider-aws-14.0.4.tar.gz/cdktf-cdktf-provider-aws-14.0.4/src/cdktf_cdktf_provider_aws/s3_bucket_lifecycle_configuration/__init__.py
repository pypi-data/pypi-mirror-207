'''
# `aws_s3_bucket_lifecycle_configuration`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_lifecycle_configuration`](https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration).
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


class S3BucketLifecycleConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfiguration",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration aws_s3_bucket_lifecycle_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration aws_s3_bucket_lifecycle_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#bucket S3BucketLifecycleConfiguration#bucket}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#rule S3BucketLifecycleConfiguration#rule}
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expected_bucket_owner S3BucketLifecycleConfiguration#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c665aeb4bc15d8d767346fa2023804c200df224243b4f95dc98b66e1d2baabd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketLifecycleConfigurationConfig(
            bucket=bucket,
            rule=rule,
            expected_bucket_owner=expected_bucket_owner,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d61e8de218b9934fe0622e3341140e2715756eae15776253b1cec0c51acae01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetExpectedBucketOwner")
    def reset_expected_bucket_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedBucketOwner", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "S3BucketLifecycleConfigurationRuleList":
        return typing.cast("S3BucketLifecycleConfigurationRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwnerInput")
    def expected_bucket_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedBucketOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8e2ef1e8dae35bac433c0eb008d6122a8d254008dfec65248eb39e84c8c7b4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwner")
    def expected_bucket_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expectedBucketOwner"))

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a076453ce1e795bc2eeb81dd2d7a1fc76b2ca45197a036a14b8d6cd71799932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedBucketOwner", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__467e049eea406ba203217c590a15839ff3474b605410072bc03fdcf12ad1359f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "rule": "rule",
        "expected_bucket_owner": "expectedBucketOwner",
        "id": "id",
    },
)
class S3BucketLifecycleConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRule", typing.Dict[builtins.str, typing.Any]]]],
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#bucket S3BucketLifecycleConfiguration#bucket}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#rule S3BucketLifecycleConfiguration#rule}
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expected_bucket_owner S3BucketLifecycleConfiguration#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde2b56e6e739e234adc4bec87e35031b9da0efb27a9e65781bb831d7113fe83)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "rule": rule,
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
        if expected_bucket_owner is not None:
            self._values["expected_bucket_owner"] = expected_bucket_owner
        if id is not None:
            self._values["id"] = id

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#bucket S3BucketLifecycleConfiguration#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#rule S3BucketLifecycleConfiguration#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRule"]], result)

    @builtins.property
    def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expected_bucket_owner S3BucketLifecycleConfiguration#expected_bucket_owner}.'''
        result = self._values.get("expected_bucket_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRule",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "status": "status",
        "abort_incomplete_multipart_upload": "abortIncompleteMultipartUpload",
        "expiration": "expiration",
        "filter": "filter",
        "noncurrent_version_expiration": "noncurrentVersionExpiration",
        "noncurrent_version_transition": "noncurrentVersionTransition",
        "prefix": "prefix",
        "transition": "transition",
    },
)
class S3BucketLifecycleConfigurationRule:
    def __init__(
        self,
        *,
        id: builtins.str,
        status: builtins.str,
        abort_incomplete_multipart_upload: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload", typing.Dict[builtins.str, typing.Any]]] = None,
        expiration: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleExpiration", typing.Dict[builtins.str, typing.Any]]] = None,
        filter: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleFilter", typing.Dict[builtins.str, typing.Any]]] = None,
        noncurrent_version_expiration: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration", typing.Dict[builtins.str, typing.Any]]] = None,
        noncurrent_version_transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        prefix: typing.Optional[builtins.str] = None,
        transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRuleTransition", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#status S3BucketLifecycleConfiguration#status}.
        :param abort_incomplete_multipart_upload: abort_incomplete_multipart_upload block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#abort_incomplete_multipart_upload S3BucketLifecycleConfiguration#abort_incomplete_multipart_upload}
        :param expiration: expiration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expiration S3BucketLifecycleConfiguration#expiration}
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#filter S3BucketLifecycleConfiguration#filter}
        :param noncurrent_version_expiration: noncurrent_version_expiration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_version_expiration S3BucketLifecycleConfiguration#noncurrent_version_expiration}
        :param noncurrent_version_transition: noncurrent_version_transition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_version_transition S3BucketLifecycleConfiguration#noncurrent_version_transition}
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param transition: transition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#transition S3BucketLifecycleConfiguration#transition}
        '''
        if isinstance(abort_incomplete_multipart_upload, dict):
            abort_incomplete_multipart_upload = S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(**abort_incomplete_multipart_upload)
        if isinstance(expiration, dict):
            expiration = S3BucketLifecycleConfigurationRuleExpiration(**expiration)
        if isinstance(filter, dict):
            filter = S3BucketLifecycleConfigurationRuleFilter(**filter)
        if isinstance(noncurrent_version_expiration, dict):
            noncurrent_version_expiration = S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(**noncurrent_version_expiration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32def251d252c4eb9b9dfea6a848798d53c721e457861bc8db8dc58e2202cf75)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument abort_incomplete_multipart_upload", value=abort_incomplete_multipart_upload, expected_type=type_hints["abort_incomplete_multipart_upload"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument noncurrent_version_expiration", value=noncurrent_version_expiration, expected_type=type_hints["noncurrent_version_expiration"])
            check_type(argname="argument noncurrent_version_transition", value=noncurrent_version_transition, expected_type=type_hints["noncurrent_version_transition"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument transition", value=transition, expected_type=type_hints["transition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "status": status,
        }
        if abort_incomplete_multipart_upload is not None:
            self._values["abort_incomplete_multipart_upload"] = abort_incomplete_multipart_upload
        if expiration is not None:
            self._values["expiration"] = expiration
        if filter is not None:
            self._values["filter"] = filter
        if noncurrent_version_expiration is not None:
            self._values["noncurrent_version_expiration"] = noncurrent_version_expiration
        if noncurrent_version_transition is not None:
            self._values["noncurrent_version_transition"] = noncurrent_version_transition
        if prefix is not None:
            self._values["prefix"] = prefix
        if transition is not None:
            self._values["transition"] = transition

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#id S3BucketLifecycleConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#status S3BucketLifecycleConfiguration#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def abort_incomplete_multipart_upload(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload"]:
        '''abort_incomplete_multipart_upload block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#abort_incomplete_multipart_upload S3BucketLifecycleConfiguration#abort_incomplete_multipart_upload}
        '''
        result = self._values.get("abort_incomplete_multipart_upload")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload"], result)

    @builtins.property
    def expiration(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleExpiration"]:
        '''expiration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expiration S3BucketLifecycleConfiguration#expiration}
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleExpiration"], result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#filter S3BucketLifecycleConfiguration#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilter"], result)

    @builtins.property
    def noncurrent_version_expiration(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration"]:
        '''noncurrent_version_expiration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_version_expiration S3BucketLifecycleConfiguration#noncurrent_version_expiration}
        '''
        result = self._values.get("noncurrent_version_expiration")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration"], result)

    @builtins.property
    def noncurrent_version_transition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition"]]]:
        '''noncurrent_version_transition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_version_transition S3BucketLifecycleConfiguration#noncurrent_version_transition}
        '''
        result = self._values.get("noncurrent_version_transition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition"]]], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]]:
        '''transition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#transition S3BucketLifecycleConfiguration#transition}
        '''
        result = self._values.get("transition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload",
    jsii_struct_bases=[],
    name_mapping={"days_after_initiation": "daysAfterInitiation"},
)
class S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload:
    def __init__(
        self,
        *,
        days_after_initiation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_after_initiation: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days_after_initiation S3BucketLifecycleConfiguration#days_after_initiation}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0882e4d6040d00ef270ab5b94b30a3073693d972ccdb58e54794b292ced0cc)
            check_type(argname="argument days_after_initiation", value=days_after_initiation, expected_type=type_hints["days_after_initiation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if days_after_initiation is not None:
            self._values["days_after_initiation"] = days_after_initiation

    @builtins.property
    def days_after_initiation(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days_after_initiation S3BucketLifecycleConfiguration#days_after_initiation}.'''
        result = self._values.get("days_after_initiation")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b463d7182bd5ae8a17b0587057646235a08edd3e4cd931f18c6f32dbe7890e0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDaysAfterInitiation")
    def reset_days_after_initiation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysAfterInitiation", []))

    @builtins.property
    @jsii.member(jsii_name="daysAfterInitiationInput")
    def days_after_initiation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysAfterInitiationInput"))

    @builtins.property
    @jsii.member(jsii_name="daysAfterInitiation")
    def days_after_initiation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysAfterInitiation"))

    @days_after_initiation.setter
    def days_after_initiation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d7c4bb39e7d7fdebc96df613e49af09a2a9dc686f944cdf6527e8cfb10b785c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysAfterInitiation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5a51686bebb4f674c30a11df53824e0648f9488560119b8871077f7b906de9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleExpiration",
    jsii_struct_bases=[],
    name_mapping={
        "date": "date",
        "days": "days",
        "expired_object_delete_marker": "expiredObjectDeleteMarker",
    },
)
class S3BucketLifecycleConfigurationRuleExpiration:
    def __init__(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param date: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.
        :param days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.
        :param expired_object_delete_marker: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expired_object_delete_marker S3BucketLifecycleConfiguration#expired_object_delete_marker}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3440df8bf1905dd98961122dd9adf453bc24389fb66ae2052bae35f54d10905a)
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            check_type(argname="argument expired_object_delete_marker", value=expired_object_delete_marker, expected_type=type_hints["expired_object_delete_marker"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if date is not None:
            self._values["date"] = date
        if days is not None:
            self._values["days"] = days
        if expired_object_delete_marker is not None:
            self._values["expired_object_delete_marker"] = expired_object_delete_marker

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.'''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def expired_object_delete_marker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expired_object_delete_marker S3BucketLifecycleConfiguration#expired_object_delete_marker}.'''
        result = self._values.get("expired_object_delete_marker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleExpiration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleExpirationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleExpirationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c7ddc17a74412b3d74e26fccb21324ffe8cc316a51e937ba7252f8815079720)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDate")
    def reset_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDate", []))

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @jsii.member(jsii_name="resetExpiredObjectDeleteMarker")
    def reset_expired_object_delete_marker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiredObjectDeleteMarker", []))

    @builtins.property
    @jsii.member(jsii_name="dateInput")
    def date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateInput"))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="expiredObjectDeleteMarkerInput")
    def expired_object_delete_marker_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "expiredObjectDeleteMarkerInput"))

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "date"))

    @date.setter
    def date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__625c32d05be69db6ccc43c244e99b16306152e746825ef315e3820c95d209b6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ce83b266cba3a29aafc80ce196f74543f70a484b32fbb54918c1d28b53f816)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "expiredObjectDeleteMarker"))

    @expired_object_delete_marker.setter
    def expired_object_delete_marker(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece217b80f0805626e9aecb3124fccfda320d6944ba03309789177eeb6db6892)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiredObjectDeleteMarker", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleExpiration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleExpiration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a49d8537e5c402a007d7ec09402f7f1ca9a80cb685eb72746b56ed30753d6646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilter",
    jsii_struct_bases=[],
    name_mapping={
        "and_": "and",
        "object_size_greater_than": "objectSizeGreaterThan",
        "object_size_less_than": "objectSizeLessThan",
        "prefix": "prefix",
        "tag": "tag",
    },
)
class S3BucketLifecycleConfigurationRuleFilter:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleFilterAnd", typing.Dict[builtins.str, typing.Any]]] = None,
        object_size_greater_than: typing.Optional[builtins.str] = None,
        object_size_less_than: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union["S3BucketLifecycleConfigurationRuleFilterTag", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#and S3BucketLifecycleConfiguration#and}
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#tag S3BucketLifecycleConfiguration#tag}
        '''
        if isinstance(and_, dict):
            and_ = S3BucketLifecycleConfigurationRuleFilterAnd(**and_)
        if isinstance(tag, dict):
            tag = S3BucketLifecycleConfigurationRuleFilterTag(**tag)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de1c6a793578625f9eacd1775519cb4aba1240e729e90e0104a99b20104777b1)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument object_size_greater_than", value=object_size_greater_than, expected_type=type_hints["object_size_greater_than"])
            check_type(argname="argument object_size_less_than", value=object_size_less_than, expected_type=type_hints["object_size_less_than"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if object_size_greater_than is not None:
            self._values["object_size_greater_than"] = object_size_greater_than
        if object_size_less_than is not None:
            self._values["object_size_less_than"] = object_size_less_than
        if prefix is not None:
            self._values["prefix"] = prefix
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def and_(self) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilterAnd"]:
        '''and block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#and S3BucketLifecycleConfiguration#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilterAnd"], result)

    @builtins.property
    def object_size_greater_than(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.'''
        result = self._values.get("object_size_greater_than")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_size_less_than(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.'''
        result = self._values.get("object_size_less_than")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"]:
        '''tag block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#tag S3BucketLifecycleConfiguration#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterAnd",
    jsii_struct_bases=[],
    name_mapping={
        "object_size_greater_than": "objectSizeGreaterThan",
        "object_size_less_than": "objectSizeLessThan",
        "prefix": "prefix",
        "tags": "tags",
    },
)
class S3BucketLifecycleConfigurationRuleFilterAnd:
    def __init__(
        self,
        *,
        object_size_greater_than: typing.Optional[jsii.Number] = None,
        object_size_less_than: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#tags S3BucketLifecycleConfiguration#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef52e0f92bce35e16a6bb0ebfde51ab13eeb0def814da5789b661950bf065e4b)
            check_type(argname="argument object_size_greater_than", value=object_size_greater_than, expected_type=type_hints["object_size_greater_than"])
            check_type(argname="argument object_size_less_than", value=object_size_less_than, expected_type=type_hints["object_size_less_than"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if object_size_greater_than is not None:
            self._values["object_size_greater_than"] = object_size_greater_than
        if object_size_less_than is not None:
            self._values["object_size_less_than"] = object_size_less_than
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def object_size_greater_than(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.'''
        result = self._values.get("object_size_greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def object_size_less_than(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.'''
        result = self._values.get("object_size_less_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#tags S3BucketLifecycleConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleFilterAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleFilterAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a45b042d623797c1f4b01be4bd84686f79964cb29cabd22ae611cc5d5ab9190d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetObjectSizeGreaterThan")
    def reset_object_size_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeGreaterThan", []))

    @jsii.member(jsii_name="resetObjectSizeLessThan")
    def reset_object_size_less_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeLessThan", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThanInput")
    def object_size_greater_than_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "objectSizeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThanInput")
    def object_size_less_than_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "objectSizeLessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "objectSizeGreaterThan"))

    @object_size_greater_than.setter
    def object_size_greater_than(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bdd112ac0d11a87de23eece6917f0129286d5d89745338fdca7098f7ab1e18b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThan")
    def object_size_less_than(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "objectSizeLessThan"))

    @object_size_less_than.setter
    def object_size_less_than(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c662ada573ab5acacc6a3f0c704d051309e32f1ca1a32d68c2375cbb03e7fe8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeLessThan", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e95a046c1eb6f491e29ffbd7abfbb14e37026729f72e0ace1422a1a1f08b75b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59169e2bba391901c7676bac5c14f08af3ff5dc8beb9ce6dd8aeac2848ce8961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db27606ca8c942b2fb41a3d33d547d048c2fbbc7cdd77f97cc0fbf66d3bd5a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c797d395d1d4de594fba0dcf53516145a8d1fcc6558e12baced1d7f94d80c92d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        *,
        object_size_greater_than: typing.Optional[jsii.Number] = None,
        object_size_less_than: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#tags S3BucketLifecycleConfiguration#tags}.
        '''
        value = S3BucketLifecycleConfigurationRuleFilterAnd(
            object_size_greater_than=object_size_greater_than,
            object_size_less_than=object_size_less_than,
            prefix=prefix,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#key S3BucketLifecycleConfiguration#key}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#value S3BucketLifecycleConfiguration#value}.
        '''
        value_ = S3BucketLifecycleConfigurationRuleFilterTag(key=key, value=value)

        return typing.cast(None, jsii.invoke(self, "putTag", [value_]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @jsii.member(jsii_name="resetObjectSizeGreaterThan")
    def reset_object_size_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeGreaterThan", []))

    @jsii.member(jsii_name="resetObjectSizeLessThan")
    def reset_object_size_less_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSizeLessThan", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> S3BucketLifecycleConfigurationRuleFilterAndOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleFilterAndOutputReference, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "S3BucketLifecycleConfigurationRuleFilterTagOutputReference":
        return typing.cast("S3BucketLifecycleConfigurationRuleFilterTagOutputReference", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(self) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThanInput")
    def object_size_greater_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectSizeGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThanInput")
    def object_size_less_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectSizeLessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"]:
        return typing.cast(typing.Optional["S3BucketLifecycleConfigurationRuleFilterTag"], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectSizeGreaterThan"))

    @object_size_greater_than.setter
    def object_size_greater_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1fdb609a6c0cdef484c5ed4145d1672b003d62f432eeb4c4b64bb3a07e49eba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeGreaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="objectSizeLessThan")
    def object_size_less_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectSizeLessThan"))

    @object_size_less_than.setter
    def object_size_less_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ab9d203c03d6f1998637a3f3e8ac15b54ae2d532cce345066973a1e34da35e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectSizeLessThan", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__141cf0cd7aa2a11c0a6a774ff95b6990f3f583a992e1a4eb0306c2f3b32318cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilter]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__532da2fb5aa4e0979622a83f5f6b973ba87db7825937f377dee9a900b1351df3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class S3BucketLifecycleConfigurationRuleFilterTag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#key S3BucketLifecycleConfiguration#key}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#value S3BucketLifecycleConfiguration#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__299bb55f8b3096200b5c244e85ce86cd4ca5786715665901da29cfbc5961e9eb)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#key S3BucketLifecycleConfiguration#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#value S3BucketLifecycleConfiguration#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleFilterTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleFilterTagOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleFilterTagOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6df9d59e6ad6b0d804fba2bff8438f541b89cdbaf07c2e2f64e4d44be381cb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0361044650487467a9e2d982f9a01b8a2934e9ed1c087f3ea5d21ad060fc1944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69cda426e92b46ca576fd463f08530855d0e0f78accb4247e74b3ac71cfdad19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa980258ab2f822aaf157786683dbcd1ac29b0046730c3b8b4c265c2c7dd56a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5209cfa4a3d53496ebfe0696657aef9ff13807e2956f07b130b5b4f238e0e6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleConfigurationRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b079d463a8f2abfd0d52b6236b3e468f1843c9fddc4fd3daf2edd2b031ad03b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleConfigurationRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab3dfc74adef5ea336112b3116161e8ec55e62e0963cfd8579bd8c5498b16d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13e70f57b51fa5a446d589307da4d14cc12ed9d998b3f0672ec7c60c87be1267)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c51e88b04ec15fec8e4c648e1bf987bd75aa7348852f4546a56ed2aefbce102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c2d41d7f27e64663bc6be46a5415f770d8de3c98936f5c7c42fcc966cc4be8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration",
    jsii_struct_bases=[],
    name_mapping={
        "newer_noncurrent_versions": "newerNoncurrentVersions",
        "noncurrent_days": "noncurrentDays",
    },
)
class S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration:
    def __init__(
        self,
        *,
        newer_noncurrent_versions: typing.Optional[builtins.str] = None,
        noncurrent_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param newer_noncurrent_versions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.
        :param noncurrent_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6601832e8f95f0bb0e79a9d0e9a3675536036959c91d0a75af7149abfa4ca883)
            check_type(argname="argument newer_noncurrent_versions", value=newer_noncurrent_versions, expected_type=type_hints["newer_noncurrent_versions"])
            check_type(argname="argument noncurrent_days", value=noncurrent_days, expected_type=type_hints["noncurrent_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if newer_noncurrent_versions is not None:
            self._values["newer_noncurrent_versions"] = newer_noncurrent_versions
        if noncurrent_days is not None:
            self._values["noncurrent_days"] = noncurrent_days

    @builtins.property
    def newer_noncurrent_versions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.'''
        result = self._values.get("newer_noncurrent_versions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noncurrent_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.'''
        result = self._values.get("noncurrent_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c45f95c82f31bfd51b69c013a1be0ed6ee87160134ad31a716ae987484d627a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNewerNoncurrentVersions")
    def reset_newer_noncurrent_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewerNoncurrentVersions", []))

    @jsii.member(jsii_name="resetNoncurrentDays")
    def reset_noncurrent_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentDays", []))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersionsInput")
    def newer_noncurrent_versions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newerNoncurrentVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentDaysInput")
    def noncurrent_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "noncurrentDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "newerNoncurrentVersions"))

    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572031465409ac4583c58897b29714b727d233e840871212a4b8263988206098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newerNoncurrentVersions", value)

    @builtins.property
    @jsii.member(jsii_name="noncurrentDays")
    def noncurrent_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "noncurrentDays"))

    @noncurrent_days.setter
    def noncurrent_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ed96ac0a9e32ffb8dea24eb46a3ba1f69bcd27c9b2d51b17cc63319faf1ef3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noncurrentDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc034fe82e8678b4762cf6e20aaae4ac0863d7b93f8bed1e18b7ba127d8d18a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition",
    jsii_struct_bases=[],
    name_mapping={
        "storage_class": "storageClass",
        "newer_noncurrent_versions": "newerNoncurrentVersions",
        "noncurrent_days": "noncurrentDays",
    },
)
class S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        newer_noncurrent_versions: typing.Optional[builtins.str] = None,
        noncurrent_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.
        :param newer_noncurrent_versions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.
        :param noncurrent_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c66e4991e7d21e8e626dc66c36509dde8417bb690fc46f8697e8ca73e1f7a48)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument newer_noncurrent_versions", value=newer_noncurrent_versions, expected_type=type_hints["newer_noncurrent_versions"])
            check_type(argname="argument noncurrent_days", value=noncurrent_days, expected_type=type_hints["noncurrent_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if newer_noncurrent_versions is not None:
            self._values["newer_noncurrent_versions"] = newer_noncurrent_versions
        if noncurrent_days is not None:
            self._values["noncurrent_days"] = noncurrent_days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.'''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def newer_noncurrent_versions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.'''
        result = self._values.get("newer_noncurrent_versions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noncurrent_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.'''
        result = self._values.get("noncurrent_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7fec2531f5ba52f9cc979707c9a9d032c3fdf2dd29029f2903d8828a58f73b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db1b2b62d0b753a6681a3a67bbfad3960a85bc9b34733dd801dafdcae2bc8f1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1684cd2ed7d026a12f1b4aa7cd059bc30253af0a73a4b425346b1bcdfc195fc8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b84c68951e2155eee27403036e091657f1c778ae49a72e0f35ecacb6c8126ab9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2afdb47477c9e5442d0ec75c78fad226af6e6d601c0aee65db2dd5f65704c5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb0e6c7dad1127fa732c4eab18bc41ee66571a00e8a0e2b96381b696f90e593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2df3443db6d9a44b6099bc79c240ad356a061098c85bc32e3b3e48875ff49a34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNewerNoncurrentVersions")
    def reset_newer_noncurrent_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewerNoncurrentVersions", []))

    @jsii.member(jsii_name="resetNoncurrentDays")
    def reset_noncurrent_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentDays", []))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersionsInput")
    def newer_noncurrent_versions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newerNoncurrentVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentDaysInput")
    def noncurrent_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "noncurrentDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "newerNoncurrentVersions"))

    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55764f4a7896cbbd2608a70edc533cc99890c1b63cdcaff822646a895259e974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newerNoncurrentVersions", value)

    @builtins.property
    @jsii.member(jsii_name="noncurrentDays")
    def noncurrent_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "noncurrentDays"))

    @noncurrent_days.setter
    def noncurrent_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f67b8086cc08de70601cb550382e9a020230fc1109d93d9cb05408b9787a0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noncurrentDays", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e46730965ee43a799a77a2866788d24804ccba29bc351794996f058270d9cf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f326b8c0038c922b4ccb4ce9cf9d0c6841b1fc00f97136a9049887cffc17d08f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4aef660b3661e841c5c200ae9c6b0373368ad91a1e2a0af7635e0ce90f781af4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAbortIncompleteMultipartUpload")
    def put_abort_incomplete_multipart_upload(
        self,
        *,
        days_after_initiation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days_after_initiation: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days_after_initiation S3BucketLifecycleConfiguration#days_after_initiation}.
        '''
        value = S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(
            days_after_initiation=days_after_initiation
        )

        return typing.cast(None, jsii.invoke(self, "putAbortIncompleteMultipartUpload", [value]))

    @jsii.member(jsii_name="putExpiration")
    def put_expiration(
        self,
        *,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
        expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param date: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.
        :param days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.
        :param expired_object_delete_marker: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#expired_object_delete_marker S3BucketLifecycleConfiguration#expired_object_delete_marker}.
        '''
        value = S3BucketLifecycleConfigurationRuleExpiration(
            date=date,
            days=days,
            expired_object_delete_marker=expired_object_delete_marker,
        )

        return typing.cast(None, jsii.invoke(self, "putExpiration", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        and_: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterAnd, typing.Dict[builtins.str, typing.Any]]] = None,
        object_size_greater_than: typing.Optional[builtins.str] = None,
        object_size_less_than: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        tag: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterTag, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#and S3BucketLifecycleConfiguration#and}
        :param object_size_greater_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_greater_than S3BucketLifecycleConfiguration#object_size_greater_than}.
        :param object_size_less_than: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#object_size_less_than S3BucketLifecycleConfiguration#object_size_less_than}.
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#prefix S3BucketLifecycleConfiguration#prefix}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#tag S3BucketLifecycleConfiguration#tag}
        '''
        value = S3BucketLifecycleConfigurationRuleFilter(
            and_=and_,
            object_size_greater_than=object_size_greater_than,
            object_size_less_than=object_size_less_than,
            prefix=prefix,
            tag=tag,
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putNoncurrentVersionExpiration")
    def put_noncurrent_version_expiration(
        self,
        *,
        newer_noncurrent_versions: typing.Optional[builtins.str] = None,
        noncurrent_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param newer_noncurrent_versions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#newer_noncurrent_versions S3BucketLifecycleConfiguration#newer_noncurrent_versions}.
        :param noncurrent_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#noncurrent_days S3BucketLifecycleConfiguration#noncurrent_days}.
        '''
        value = S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(
            newer_noncurrent_versions=newer_noncurrent_versions,
            noncurrent_days=noncurrent_days,
        )

        return typing.cast(None, jsii.invoke(self, "putNoncurrentVersionExpiration", [value]))

    @jsii.member(jsii_name="putNoncurrentVersionTransition")
    def put_noncurrent_version_transition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b06b1ed6c06101ae900a2ba618d219764d63c629960c273aea5cc95f944fc9e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNoncurrentVersionTransition", [value]))

    @jsii.member(jsii_name="putTransition")
    def put_transition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLifecycleConfigurationRuleTransition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97fc981d7febb03b920cf70ada9578f844a5569ba55169b59e080b5c4f912886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransition", [value]))

    @jsii.member(jsii_name="resetAbortIncompleteMultipartUpload")
    def reset_abort_incomplete_multipart_upload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbortIncompleteMultipartUpload", []))

    @jsii.member(jsii_name="resetExpiration")
    def reset_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiration", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetNoncurrentVersionExpiration")
    def reset_noncurrent_version_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentVersionExpiration", []))

    @jsii.member(jsii_name="resetNoncurrentVersionTransition")
    def reset_noncurrent_version_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentVersionTransition", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTransition")
    def reset_transition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransition", []))

    @builtins.property
    @jsii.member(jsii_name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(
        self,
    ) -> S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference, jsii.get(self, "abortIncompleteMultipartUpload"))

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> S3BucketLifecycleConfigurationRuleExpirationOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleExpirationOutputReference, jsii.get(self, "expiration"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> S3BucketLifecycleConfigurationRuleFilterOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(
        self,
    ) -> S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference:
        return typing.cast(S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference, jsii.get(self, "noncurrentVersionExpiration"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionTransition")
    def noncurrent_version_transition(
        self,
    ) -> S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList:
        return typing.cast(S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList, jsii.get(self, "noncurrentVersionTransition"))

    @builtins.property
    @jsii.member(jsii_name="transition")
    def transition(self) -> "S3BucketLifecycleConfigurationRuleTransitionList":
        return typing.cast("S3BucketLifecycleConfigurationRuleTransitionList", jsii.get(self, "transition"))

    @builtins.property
    @jsii.member(jsii_name="abortIncompleteMultipartUploadInput")
    def abort_incomplete_multipart_upload_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload], jsii.get(self, "abortIncompleteMultipartUploadInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInput")
    def expiration_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleExpiration], jsii.get(self, "expirationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[S3BucketLifecycleConfigurationRuleFilter]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleFilter], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionExpirationInput")
    def noncurrent_version_expiration_input(
        self,
    ) -> typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration]:
        return typing.cast(typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration], jsii.get(self, "noncurrentVersionExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentVersionTransitionInput")
    def noncurrent_version_transition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]], jsii.get(self, "noncurrentVersionTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionInput")
    def transition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLifecycleConfigurationRuleTransition"]]], jsii.get(self, "transitionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3bd9221e86760273eac02605e9bdb3c3f2c7b61a0a1f195ae2f08be39554d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f301d475157f21d8adccd1672c93c331916ed6735ee27099fe807d2a74af2696)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a651f523f30eb5aeed52fd3644377ed7ab89d02445145f61668e749d20b95f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04dc829ea006afc8978c25b8fbe5338e692793423334414672f32e25475a51d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleTransition",
    jsii_struct_bases=[],
    name_mapping={"storage_class": "storageClass", "date": "date", "days": "days"},
)
class S3BucketLifecycleConfigurationRuleTransition:
    def __init__(
        self,
        *,
        storage_class: builtins.str,
        date: typing.Optional[builtins.str] = None,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param storage_class: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.
        :param date: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.
        :param days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fafabe32b91610b2f392debff43a917a688b8be8609f8ba8df89710d05a4f045)
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_class": storage_class,
        }
        if date is not None:
            self._values["date"] = date
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#storage_class S3BucketLifecycleConfiguration#storage_class}.'''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#date S3BucketLifecycleConfiguration#date}.'''
        result = self._values.get("date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/s3_bucket_lifecycle_configuration#days S3BucketLifecycleConfiguration#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLifecycleConfigurationRuleTransition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLifecycleConfigurationRuleTransitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleTransitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28c41c1563e0a3191789ad9a70b380c973e085dfed73a40011404636d1d59cd7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3BucketLifecycleConfigurationRuleTransitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90dc4516af6271aec38fe7f4a0001fd4b4f3dc7e554401813863a699d92e3c4b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLifecycleConfigurationRuleTransitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__042f0c11cd37c2a11d727503a16aede609211dc3fa636423c01dc5cacd405728)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47d3a71a60f0d9e7d53eb45b842ffff45e0ff0a115c9a29b2701bbcf5464be0c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__acf1cb7b5d4f5eb3b7d6093d8f985be923b4afb645b2efb33e5f27ec41c5edfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1094eb3a72f75edd2335bd6c07b8bbb15bdce0f39336c7f77be9ba6e104ddb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketLifecycleConfigurationRuleTransitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketLifecycleConfiguration.S3BucketLifecycleConfigurationRuleTransitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dbf62b12c21a0a38096b4c0c92e6cb4787bddae47705778748e1e61d4d997df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDate")
    def reset_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDate", []))

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="dateInput")
    def date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateInput"))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "date"))

    @date.setter
    def date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__943817b9da94c79c62bf25178a7ddba5963ab28b69e99c0ed892359a13ef94f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d949a7c0dd8d769b59ddce281845c9009992734ec55c4993a1665cc224d8bb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__370cbcdb0c11c66de617ec8c0ecb288b43ee58f45fe8e08ebfbf0d632a6e110c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2f985c2a51ebd1409d087d7e73548f086199a3015cff6f2ae593701f7bab49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketLifecycleConfiguration",
    "S3BucketLifecycleConfigurationConfig",
    "S3BucketLifecycleConfigurationRule",
    "S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload",
    "S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadOutputReference",
    "S3BucketLifecycleConfigurationRuleExpiration",
    "S3BucketLifecycleConfigurationRuleExpirationOutputReference",
    "S3BucketLifecycleConfigurationRuleFilter",
    "S3BucketLifecycleConfigurationRuleFilterAnd",
    "S3BucketLifecycleConfigurationRuleFilterAndOutputReference",
    "S3BucketLifecycleConfigurationRuleFilterOutputReference",
    "S3BucketLifecycleConfigurationRuleFilterTag",
    "S3BucketLifecycleConfigurationRuleFilterTagOutputReference",
    "S3BucketLifecycleConfigurationRuleList",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionExpirationOutputReference",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionList",
    "S3BucketLifecycleConfigurationRuleNoncurrentVersionTransitionOutputReference",
    "S3BucketLifecycleConfigurationRuleOutputReference",
    "S3BucketLifecycleConfigurationRuleTransition",
    "S3BucketLifecycleConfigurationRuleTransitionList",
    "S3BucketLifecycleConfigurationRuleTransitionOutputReference",
]

publication.publish()

def _typecheckingstub__0c665aeb4bc15d8d767346fa2023804c200df224243b4f95dc98b66e1d2baabd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9d61e8de218b9934fe0622e3341140e2715756eae15776253b1cec0c51acae01(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8e2ef1e8dae35bac433c0eb008d6122a8d254008dfec65248eb39e84c8c7b4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a076453ce1e795bc2eeb81dd2d7a1fc76b2ca45197a036a14b8d6cd71799932(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467e049eea406ba203217c590a15839ff3474b605410072bc03fdcf12ad1359f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde2b56e6e739e234adc4bec87e35031b9da0efb27a9e65781bb831d7113fe83(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRule, typing.Dict[builtins.str, typing.Any]]]],
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32def251d252c4eb9b9dfea6a848798d53c721e457861bc8db8dc58e2202cf75(
    *,
    id: builtins.str,
    status: builtins.str,
    abort_incomplete_multipart_upload: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload, typing.Dict[builtins.str, typing.Any]]] = None,
    expiration: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleExpiration, typing.Dict[builtins.str, typing.Any]]] = None,
    filter: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilter, typing.Dict[builtins.str, typing.Any]]] = None,
    noncurrent_version_expiration: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration, typing.Dict[builtins.str, typing.Any]]] = None,
    noncurrent_version_transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]]] = None,
    prefix: typing.Optional[builtins.str] = None,
    transition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleTransition, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0882e4d6040d00ef270ab5b94b30a3073693d972ccdb58e54794b292ced0cc(
    *,
    days_after_initiation: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b463d7182bd5ae8a17b0587057646235a08edd3e4cd931f18c6f32dbe7890e0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d7c4bb39e7d7fdebc96df613e49af09a2a9dc686f944cdf6527e8cfb10b785c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5a51686bebb4f674c30a11df53824e0648f9488560119b8871077f7b906de9(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3440df8bf1905dd98961122dd9adf453bc24389fb66ae2052bae35f54d10905a(
    *,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
    expired_object_delete_marker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7ddc17a74412b3d74e26fccb21324ffe8cc316a51e937ba7252f8815079720(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625c32d05be69db6ccc43c244e99b16306152e746825ef315e3820c95d209b6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ce83b266cba3a29aafc80ce196f74543f70a484b32fbb54918c1d28b53f816(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece217b80f0805626e9aecb3124fccfda320d6944ba03309789177eeb6db6892(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a49d8537e5c402a007d7ec09402f7f1ca9a80cb685eb72746b56ed30753d6646(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleExpiration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1c6a793578625f9eacd1775519cb4aba1240e729e90e0104a99b20104777b1(
    *,
    and_: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterAnd, typing.Dict[builtins.str, typing.Any]]] = None,
    object_size_greater_than: typing.Optional[builtins.str] = None,
    object_size_less_than: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    tag: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleFilterTag, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef52e0f92bce35e16a6bb0ebfde51ab13eeb0def814da5789b661950bf065e4b(
    *,
    object_size_greater_than: typing.Optional[jsii.Number] = None,
    object_size_less_than: typing.Optional[jsii.Number] = None,
    prefix: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a45b042d623797c1f4b01be4bd84686f79964cb29cabd22ae611cc5d5ab9190d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bdd112ac0d11a87de23eece6917f0129286d5d89745338fdca7098f7ab1e18b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c662ada573ab5acacc6a3f0c704d051309e32f1ca1a32d68c2375cbb03e7fe8c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e95a046c1eb6f491e29ffbd7abfbb14e37026729f72e0ace1422a1a1f08b75b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59169e2bba391901c7676bac5c14f08af3ff5dc8beb9ce6dd8aeac2848ce8961(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db27606ca8c942b2fb41a3d33d547d048c2fbbc7cdd77f97cc0fbf66d3bd5a60(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterAnd],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c797d395d1d4de594fba0dcf53516145a8d1fcc6558e12baced1d7f94d80c92d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fdb609a6c0cdef484c5ed4145d1672b003d62f432eeb4c4b64bb3a07e49eba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ab9d203c03d6f1998637a3f3e8ac15b54ae2d532cce345066973a1e34da35e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__141cf0cd7aa2a11c0a6a774ff95b6990f3f583a992e1a4eb0306c2f3b32318cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__532da2fb5aa4e0979622a83f5f6b973ba87db7825937f377dee9a900b1351df3(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleFilter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299bb55f8b3096200b5c244e85ce86cd4ca5786715665901da29cfbc5961e9eb(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6df9d59e6ad6b0d804fba2bff8438f541b89cdbaf07c2e2f64e4d44be381cb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0361044650487467a9e2d982f9a01b8a2934e9ed1c087f3ea5d21ad060fc1944(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69cda426e92b46ca576fd463f08530855d0e0f78accb4247e74b3ac71cfdad19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa980258ab2f822aaf157786683dbcd1ac29b0046730c3b8b4c265c2c7dd56a2(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleFilterTag],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5209cfa4a3d53496ebfe0696657aef9ff13807e2956f07b130b5b4f238e0e6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b079d463a8f2abfd0d52b6236b3e468f1843c9fddc4fd3daf2edd2b031ad03b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab3dfc74adef5ea336112b3116161e8ec55e62e0963cfd8579bd8c5498b16d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e70f57b51fa5a446d589307da4d14cc12ed9d998b3f0672ec7c60c87be1267(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c51e88b04ec15fec8e4c648e1bf987bd75aa7348852f4546a56ed2aefbce102(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2d41d7f27e64663bc6be46a5415f770d8de3c98936f5c7c42fcc966cc4be8d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6601832e8f95f0bb0e79a9d0e9a3675536036959c91d0a75af7149abfa4ca883(
    *,
    newer_noncurrent_versions: typing.Optional[builtins.str] = None,
    noncurrent_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45f95c82f31bfd51b69c013a1be0ed6ee87160134ad31a716ae987484d627a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572031465409ac4583c58897b29714b727d233e840871212a4b8263988206098(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ed96ac0a9e32ffb8dea24eb46a3ba1f69bcd27c9b2d51b17cc63319faf1ef3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc034fe82e8678b4762cf6e20aaae4ac0863d7b93f8bed1e18b7ba127d8d18a6(
    value: typing.Optional[S3BucketLifecycleConfigurationRuleNoncurrentVersionExpiration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c66e4991e7d21e8e626dc66c36509dde8417bb690fc46f8697e8ca73e1f7a48(
    *,
    storage_class: builtins.str,
    newer_noncurrent_versions: typing.Optional[builtins.str] = None,
    noncurrent_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7fec2531f5ba52f9cc979707c9a9d032c3fdf2dd29029f2903d8828a58f73b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db1b2b62d0b753a6681a3a67bbfad3960a85bc9b34733dd801dafdcae2bc8f1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1684cd2ed7d026a12f1b4aa7cd059bc30253af0a73a4b425346b1bcdfc195fc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84c68951e2155eee27403036e091657f1c778ae49a72e0f35ecacb6c8126ab9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2afdb47477c9e5442d0ec75c78fad226af6e6d601c0aee65db2dd5f65704c5c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb0e6c7dad1127fa732c4eab18bc41ee66571a00e8a0e2b96381b696f90e593(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df3443db6d9a44b6099bc79c240ad356a061098c85bc32e3b3e48875ff49a34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55764f4a7896cbbd2608a70edc533cc99890c1b63cdcaff822646a895259e974(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f67b8086cc08de70601cb550382e9a020230fc1109d93d9cb05408b9787a0a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e46730965ee43a799a77a2866788d24804ccba29bc351794996f058270d9cf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f326b8c0038c922b4ccb4ce9cf9d0c6841b1fc00f97136a9049887cffc17d08f(
    value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aef660b3661e841c5c200ae9c6b0373368ad91a1e2a0af7635e0ce90f781af4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b06b1ed6c06101ae900a2ba618d219764d63c629960c273aea5cc95f944fc9e8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleNoncurrentVersionTransition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97fc981d7febb03b920cf70ada9578f844a5569ba55169b59e080b5c4f912886(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLifecycleConfigurationRuleTransition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3bd9221e86760273eac02605e9bdb3c3f2c7b61a0a1f195ae2f08be39554d41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f301d475157f21d8adccd1672c93c331916ed6735ee27099fe807d2a74af2696(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a651f523f30eb5aeed52fd3644377ed7ab89d02445145f61668e749d20b95f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04dc829ea006afc8978c25b8fbe5338e692793423334414672f32e25475a51d(
    value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafabe32b91610b2f392debff43a917a688b8be8609f8ba8df89710d05a4f045(
    *,
    storage_class: builtins.str,
    date: typing.Optional[builtins.str] = None,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28c41c1563e0a3191789ad9a70b380c973e085dfed73a40011404636d1d59cd7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90dc4516af6271aec38fe7f4a0001fd4b4f3dc7e554401813863a699d92e3c4b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__042f0c11cd37c2a11d727503a16aede609211dc3fa636423c01dc5cacd405728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d3a71a60f0d9e7d53eb45b842ffff45e0ff0a115c9a29b2701bbcf5464be0c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf1cb7b5d4f5eb3b7d6093d8f985be923b4afb645b2efb33e5f27ec41c5edfc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1094eb3a72f75edd2335bd6c07b8bbb15bdce0f39336c7f77be9ba6e104ddb6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLifecycleConfigurationRuleTransition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbf62b12c21a0a38096b4c0c92e6cb4787bddae47705778748e1e61d4d997df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943817b9da94c79c62bf25178a7ddba5963ab28b69e99c0ed892359a13ef94f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d949a7c0dd8d769b59ddce281845c9009992734ec55c4993a1665cc224d8bb4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370cbcdb0c11c66de617ec8c0ecb288b43ee58f45fe8e08ebfbf0d632a6e110c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2f985c2a51ebd1409d087d7e73548f086199a3015cff6f2ae593701f7bab49(
    value: typing.Optional[typing.Union[S3BucketLifecycleConfigurationRuleTransition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
