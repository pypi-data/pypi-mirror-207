'''
# `aws_cognito_user_pool_domain`

Refer to the Terraform Registory for docs: [`aws_cognito_user_pool_domain`](https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain).
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


class CognitoUserPoolDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoUserPoolDomain.CognitoUserPoolDomain",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain aws_cognito_user_pool_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        user_pool_id: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain aws_cognito_user_pool_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#domain CognitoUserPoolDomain#domain}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#user_pool_id CognitoUserPoolDomain#user_pool_id}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#certificate_arn CognitoUserPoolDomain#certificate_arn}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#id CognitoUserPoolDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e49c8deb33aa06442ac8d2268438a2455931bf6230bd106c8bc7bfdf3c78ac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CognitoUserPoolDomainConfig(
            domain=domain,
            user_pool_id=user_pool_id,
            certificate_arn=certificate_arn,
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

    @jsii.member(jsii_name="resetCertificateArn")
    def reset_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateArn", []))

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
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDistribution")
    def cloudfront_distribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontDistribution"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDistributionArn")
    def cloudfront_distribution_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontDistributionArn"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDistributionZoneId")
    def cloudfront_distribution_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontDistributionZoneId"))

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3fdce047dd267d978756081252cf3304be5f24df0803bc645cfd5b00cd7d6e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84c86c857d56d3deb0c22af788650874c9d741e3417f69554f2c9e7baf19bd2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691db1a720ce148891a52a90192f8b255bf1300180fcea8855683722cbfaee49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60cd1777434825e52a1dc9c904b7c64e95b3b8819a30040621955dca48a567ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoUserPoolDomain.CognitoUserPoolDomainConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "user_pool_id": "userPoolId",
        "certificate_arn": "certificateArn",
        "id": "id",
    },
)
class CognitoUserPoolDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain: builtins.str,
        user_pool_id: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
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
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#domain CognitoUserPoolDomain#domain}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#user_pool_id CognitoUserPoolDomain#user_pool_id}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#certificate_arn CognitoUserPoolDomain#certificate_arn}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#id CognitoUserPoolDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a17c8dc9d5e5ad96370b14072bcf27cb2dbdb005793884eeefab45906eeda8f6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "user_pool_id": user_pool_id,
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
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
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
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#domain CognitoUserPoolDomain#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#user_pool_id CognitoUserPoolDomain#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#certificate_arn CognitoUserPoolDomain#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/cognito_user_pool_domain#id CognitoUserPoolDomain#id}.

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
        return "CognitoUserPoolDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CognitoUserPoolDomain",
    "CognitoUserPoolDomainConfig",
]

publication.publish()

def _typecheckingstub__f6e49c8deb33aa06442ac8d2268438a2455931bf6230bd106c8bc7bfdf3c78ac(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain: builtins.str,
    user_pool_id: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e3fdce047dd267d978756081252cf3304be5f24df0803bc645cfd5b00cd7d6e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84c86c857d56d3deb0c22af788650874c9d741e3417f69554f2c9e7baf19bd2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691db1a720ce148891a52a90192f8b255bf1300180fcea8855683722cbfaee49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60cd1777434825e52a1dc9c904b7c64e95b3b8819a30040621955dca48a567ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17c8dc9d5e5ad96370b14072bcf27cb2dbdb005793884eeefab45906eeda8f6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    user_pool_id: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
