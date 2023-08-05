'''
# `aws_sagemaker_workteam`

Refer to the Terraform Registory for docs: [`aws_sagemaker_workteam`](https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam).
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


class SagemakerWorkteam(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteam",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam aws_sagemaker_workteam}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        description: builtins.str,
        member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerWorkteamMemberDefinition", typing.Dict[builtins.str, typing.Any]]]],
        workforce_name: builtins.str,
        workteam_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        notification_configuration: typing.Optional[typing.Union["SagemakerWorkteamNotificationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam aws_sagemaker_workteam} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#description SagemakerWorkteam#description}.
        :param member_definition: member_definition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#member_definition SagemakerWorkteam#member_definition}
        :param workforce_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#workforce_name SagemakerWorkteam#workforce_name}.
        :param workteam_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#workteam_name SagemakerWorkteam#workteam_name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#id SagemakerWorkteam#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_configuration: notification_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#notification_configuration SagemakerWorkteam#notification_configuration}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#tags SagemakerWorkteam#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#tags_all SagemakerWorkteam#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__553a680a6049e44a944da0b7b178c49265e02e9ad0781d8ddc8d05d093af73f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerWorkteamConfig(
            description=description,
            member_definition=member_definition,
            workforce_name=workforce_name,
            workteam_name=workteam_name,
            id=id,
            notification_configuration=notification_configuration,
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

    @jsii.member(jsii_name="putMemberDefinition")
    def put_member_definition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerWorkteamMemberDefinition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882279c7caef9b0956843ba256e89b708cb85e84e6fd2fc5c50e5b34861169c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMemberDefinition", [value]))

    @jsii.member(jsii_name="putNotificationConfiguration")
    def put_notification_configuration(
        self,
        *,
        notification_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_topic_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#notification_topic_arn SagemakerWorkteam#notification_topic_arn}.
        '''
        value = SagemakerWorkteamNotificationConfiguration(
            notification_topic_arn=notification_topic_arn
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationConfiguration")
    def reset_notification_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfiguration", []))

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
    @jsii.member(jsii_name="memberDefinition")
    def member_definition(self) -> "SagemakerWorkteamMemberDefinitionList":
        return typing.cast("SagemakerWorkteamMemberDefinitionList", jsii.get(self, "memberDefinition"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> "SagemakerWorkteamNotificationConfigurationOutputReference":
        return typing.cast("SagemakerWorkteamNotificationConfigurationOutputReference", jsii.get(self, "notificationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="subdomain")
    def subdomain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdomain"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="memberDefinitionInput")
    def member_definition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]]], jsii.get(self, "memberDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigurationInput")
    def notification_configuration_input(
        self,
    ) -> typing.Optional["SagemakerWorkteamNotificationConfiguration"]:
        return typing.cast(typing.Optional["SagemakerWorkteamNotificationConfiguration"], jsii.get(self, "notificationConfigurationInput"))

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
    @jsii.member(jsii_name="workforceNameInput")
    def workforce_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workforceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="workteamNameInput")
    def workteam_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workteamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd55598c8a3370cc0311d1a1bc237a0a3ce58cc132fd4df1b345f353fbd04ed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9ddd1fc9d2ca6ff4c791fdd88d5f8a1afb49383b429757521fe867556f41021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524daeb4555bf1324c125a36575a63bdb2c5f4f636c1076031221b26141783f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c004e7b92318f6ac09c23b08a15d87a1d9a7832e124502207bbcab2cb4e0dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="workforceName")
    def workforce_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workforceName"))

    @workforce_name.setter
    def workforce_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0770a1298b35903ed2ecbc22b0ea71de1e710e41804ee779efd0eb23183f427a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workforceName", value)

    @builtins.property
    @jsii.member(jsii_name="workteamName")
    def workteam_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workteamName"))

    @workteam_name.setter
    def workteam_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a173d042facd238f06bddfe3e3f761e6aab52a60f812d32dc7b80dc8c88f1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workteamName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "member_definition": "memberDefinition",
        "workforce_name": "workforceName",
        "workteam_name": "workteamName",
        "id": "id",
        "notification_configuration": "notificationConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerWorkteamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        description: builtins.str,
        member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerWorkteamMemberDefinition", typing.Dict[builtins.str, typing.Any]]]],
        workforce_name: builtins.str,
        workteam_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        notification_configuration: typing.Optional[typing.Union["SagemakerWorkteamNotificationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#description SagemakerWorkteam#description}.
        :param member_definition: member_definition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#member_definition SagemakerWorkteam#member_definition}
        :param workforce_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#workforce_name SagemakerWorkteam#workforce_name}.
        :param workteam_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#workteam_name SagemakerWorkteam#workteam_name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#id SagemakerWorkteam#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_configuration: notification_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#notification_configuration SagemakerWorkteam#notification_configuration}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#tags SagemakerWorkteam#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#tags_all SagemakerWorkteam#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(notification_configuration, dict):
            notification_configuration = SagemakerWorkteamNotificationConfiguration(**notification_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5688e9e6b2f7440b334ca5e28007270003336ba280fe2f24fce80519c1fede19)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument member_definition", value=member_definition, expected_type=type_hints["member_definition"])
            check_type(argname="argument workforce_name", value=workforce_name, expected_type=type_hints["workforce_name"])
            check_type(argname="argument workteam_name", value=workteam_name, expected_type=type_hints["workteam_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_configuration", value=notification_configuration, expected_type=type_hints["notification_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "member_definition": member_definition,
            "workforce_name": workforce_name,
            "workteam_name": workteam_name,
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
        if id is not None:
            self._values["id"] = id
        if notification_configuration is not None:
            self._values["notification_configuration"] = notification_configuration
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
    def description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#description SagemakerWorkteam#description}.'''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_definition(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]]:
        '''member_definition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#member_definition SagemakerWorkteam#member_definition}
        '''
        result = self._values.get("member_definition")
        assert result is not None, "Required property 'member_definition' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]], result)

    @builtins.property
    def workforce_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#workforce_name SagemakerWorkteam#workforce_name}.'''
        result = self._values.get("workforce_name")
        assert result is not None, "Required property 'workforce_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workteam_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#workteam_name SagemakerWorkteam#workteam_name}.'''
        result = self._values.get("workteam_name")
        assert result is not None, "Required property 'workteam_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#id SagemakerWorkteam#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_configuration(
        self,
    ) -> typing.Optional["SagemakerWorkteamNotificationConfiguration"]:
        '''notification_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#notification_configuration SagemakerWorkteam#notification_configuration}
        '''
        result = self._values.get("notification_configuration")
        return typing.cast(typing.Optional["SagemakerWorkteamNotificationConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#tags SagemakerWorkteam#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#tags_all SagemakerWorkteam#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "cognito_member_definition": "cognitoMemberDefinition",
        "oidc_member_definition": "oidcMemberDefinition",
    },
)
class SagemakerWorkteamMemberDefinition:
    def __init__(
        self,
        *,
        cognito_member_definition: typing.Optional[typing.Union["SagemakerWorkteamMemberDefinitionCognitoMemberDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        oidc_member_definition: typing.Optional[typing.Union["SagemakerWorkteamMemberDefinitionOidcMemberDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cognito_member_definition: cognito_member_definition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#cognito_member_definition SagemakerWorkteam#cognito_member_definition}
        :param oidc_member_definition: oidc_member_definition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#oidc_member_definition SagemakerWorkteam#oidc_member_definition}
        '''
        if isinstance(cognito_member_definition, dict):
            cognito_member_definition = SagemakerWorkteamMemberDefinitionCognitoMemberDefinition(**cognito_member_definition)
        if isinstance(oidc_member_definition, dict):
            oidc_member_definition = SagemakerWorkteamMemberDefinitionOidcMemberDefinition(**oidc_member_definition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264e549dea3c643e3e70ed5373cac14dd5f79e3377a24df664b0c902b659481e)
            check_type(argname="argument cognito_member_definition", value=cognito_member_definition, expected_type=type_hints["cognito_member_definition"])
            check_type(argname="argument oidc_member_definition", value=oidc_member_definition, expected_type=type_hints["oidc_member_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cognito_member_definition is not None:
            self._values["cognito_member_definition"] = cognito_member_definition
        if oidc_member_definition is not None:
            self._values["oidc_member_definition"] = oidc_member_definition

    @builtins.property
    def cognito_member_definition(
        self,
    ) -> typing.Optional["SagemakerWorkteamMemberDefinitionCognitoMemberDefinition"]:
        '''cognito_member_definition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#cognito_member_definition SagemakerWorkteam#cognito_member_definition}
        '''
        result = self._values.get("cognito_member_definition")
        return typing.cast(typing.Optional["SagemakerWorkteamMemberDefinitionCognitoMemberDefinition"], result)

    @builtins.property
    def oidc_member_definition(
        self,
    ) -> typing.Optional["SagemakerWorkteamMemberDefinitionOidcMemberDefinition"]:
        '''oidc_member_definition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#oidc_member_definition SagemakerWorkteam#oidc_member_definition}
        '''
        result = self._values.get("oidc_member_definition")
        return typing.cast(typing.Optional["SagemakerWorkteamMemberDefinitionOidcMemberDefinition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamMemberDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionCognitoMemberDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "user_group": "userGroup",
        "user_pool": "userPool",
    },
)
class SagemakerWorkteamMemberDefinitionCognitoMemberDefinition:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        user_group: builtins.str,
        user_pool: builtins.str,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#client_id SagemakerWorkteam#client_id}.
        :param user_group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#user_group SagemakerWorkteam#user_group}.
        :param user_pool: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#user_pool SagemakerWorkteam#user_pool}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d98c03f56c945b7b2fed3d94f1dfdc2b428a0bdfb7e96ca626114a4bf9fbb3a)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument user_group", value=user_group, expected_type=type_hints["user_group"])
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "user_group": user_group,
            "user_pool": user_pool,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#client_id SagemakerWorkteam#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#user_group SagemakerWorkteam#user_group}.'''
        result = self._values.get("user_group")
        assert result is not None, "Required property 'user_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#user_pool SagemakerWorkteam#user_pool}.'''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamMemberDefinitionCognitoMemberDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ec49f57cb9b1c5683de47321e30e4218543252b9837d74d681042a7ca79d08d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupInput")
    def user_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolInput")
    def user_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96c61e07c14a6e596e8d9755c32c35aabb73cbbdcb463093e1174c54fb9fb23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="userGroup")
    def user_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userGroup"))

    @user_group.setter
    def user_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8fea4b24fd650007b16c4a7226d94fa0eaff4f597a2b2347436ac9f587db04e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroup", value)

    @builtins.property
    @jsii.member(jsii_name="userPool")
    def user_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPool"))

    @user_pool.setter
    def user_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcffee8620c15fd6141666f13c5b1888fedde6e23a67f49e8fe0920c7657f0ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPool", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c91ccd8a2180822c85a5ce5f558776ed0ac89ed3acf2347345fc68f0f01d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerWorkteamMemberDefinitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__980562309a58c4a4bc40cfa8b28f5a1cf190b589438c33935e81255188f2acc9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerWorkteamMemberDefinitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96f70e62940afe02c7b6ae143fec718722bc17102f22cbafb96feb40d0cebf8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerWorkteamMemberDefinitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba962ac054f9c4f0a4fc652cba1ef81db6707121f481fed777daf239437fa5ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed63e884785a91d8443e67491f15c12d3ece386a75f2fa6451f286cba1ffab64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d008296883826aa37de33854a4b81897caf1a6db55bf6f8727af1d2692d2456)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ee5c007bba2865327002f909675a372ba3e5b01c73b1a63ed4a02f214ca854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionOidcMemberDefinition",
    jsii_struct_bases=[],
    name_mapping={"groups": "groups"},
)
class SagemakerWorkteamMemberDefinitionOidcMemberDefinition:
    def __init__(self, *, groups: typing.Sequence[builtins.str]) -> None:
        '''
        :param groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#groups SagemakerWorkteam#groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f697760f4935780d33b99e9ce8755f57df0f841206af138c389aff9658b711)
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "groups": groups,
        }

    @builtins.property
    def groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#groups SagemakerWorkteam#groups}.'''
        result = self._values.get("groups")
        assert result is not None, "Required property 'groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamMemberDefinitionOidcMemberDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2491f8310e37be8778c93f731e92aba55075b331ba55ee5dc742fef1aa32c8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12b447b30a6f521875bfa7f7f25265273ce8c3a7fa4e93cffe59be1a8753e0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f60ab39299dca20786c2be7d35b8b9cf7b1cd0f8fc8cb7137764e5408a312b3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerWorkteamMemberDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__370231fa248581d0c2bec3525394a3bbb58045c4e2951ec26357a8b9b65369eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCognitoMemberDefinition")
    def put_cognito_member_definition(
        self,
        *,
        client_id: builtins.str,
        user_group: builtins.str,
        user_pool: builtins.str,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#client_id SagemakerWorkteam#client_id}.
        :param user_group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#user_group SagemakerWorkteam#user_group}.
        :param user_pool: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#user_pool SagemakerWorkteam#user_pool}.
        '''
        value = SagemakerWorkteamMemberDefinitionCognitoMemberDefinition(
            client_id=client_id, user_group=user_group, user_pool=user_pool
        )

        return typing.cast(None, jsii.invoke(self, "putCognitoMemberDefinition", [value]))

    @jsii.member(jsii_name="putOidcMemberDefinition")
    def put_oidc_member_definition(
        self,
        *,
        groups: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#groups SagemakerWorkteam#groups}.
        '''
        value = SagemakerWorkteamMemberDefinitionOidcMemberDefinition(groups=groups)

        return typing.cast(None, jsii.invoke(self, "putOidcMemberDefinition", [value]))

    @jsii.member(jsii_name="resetCognitoMemberDefinition")
    def reset_cognito_member_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCognitoMemberDefinition", []))

    @jsii.member(jsii_name="resetOidcMemberDefinition")
    def reset_oidc_member_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcMemberDefinition", []))

    @builtins.property
    @jsii.member(jsii_name="cognitoMemberDefinition")
    def cognito_member_definition(
        self,
    ) -> SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference:
        return typing.cast(SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference, jsii.get(self, "cognitoMemberDefinition"))

    @builtins.property
    @jsii.member(jsii_name="oidcMemberDefinition")
    def oidc_member_definition(
        self,
    ) -> SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference:
        return typing.cast(SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference, jsii.get(self, "oidcMemberDefinition"))

    @builtins.property
    @jsii.member(jsii_name="cognitoMemberDefinitionInput")
    def cognito_member_definition_input(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition], jsii.get(self, "cognitoMemberDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcMemberDefinitionInput")
    def oidc_member_definition_input(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition], jsii.get(self, "oidcMemberDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822fbe624e52c043c7df5cf3349bc856b119b7c3208168148d64ebef8e19354c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamNotificationConfiguration",
    jsii_struct_bases=[],
    name_mapping={"notification_topic_arn": "notificationTopicArn"},
)
class SagemakerWorkteamNotificationConfiguration:
    def __init__(
        self,
        *,
        notification_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_topic_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#notification_topic_arn SagemakerWorkteam#notification_topic_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac05fff26ffbf5927fdf4f7a3261747b6ed6db3da47e6d0a59dbcaa4af07b3d)
            check_type(argname="argument notification_topic_arn", value=notification_topic_arn, expected_type=type_hints["notification_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.66.1/docs/resources/sagemaker_workteam#notification_topic_arn SagemakerWorkteam#notification_topic_arn}.'''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamNotificationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerWorkteamNotificationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerWorkteam.SagemakerWorkteamNotificationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a0e65058980296bb91c9bf3a0b4a9b1894755aa7f22d7f768eb004751521d41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotificationTopicArn")
    def reset_notification_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationTopicArn", []))

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArnInput")
    def notification_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fab8f37099b9c190babba31063d4653c8caf2ac41df2b680b35e1fbe2df5c1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerWorkteamNotificationConfiguration]:
        return typing.cast(typing.Optional[SagemakerWorkteamNotificationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerWorkteamNotificationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a5cc54abfc6c4d07f0e878bb70d7dcf12e24d89ead384b55516b737fc545ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerWorkteam",
    "SagemakerWorkteamConfig",
    "SagemakerWorkteamMemberDefinition",
    "SagemakerWorkteamMemberDefinitionCognitoMemberDefinition",
    "SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference",
    "SagemakerWorkteamMemberDefinitionList",
    "SagemakerWorkteamMemberDefinitionOidcMemberDefinition",
    "SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference",
    "SagemakerWorkteamMemberDefinitionOutputReference",
    "SagemakerWorkteamNotificationConfiguration",
    "SagemakerWorkteamNotificationConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__553a680a6049e44a944da0b7b178c49265e02e9ad0781d8ddc8d05d093af73f6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    description: builtins.str,
    member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerWorkteamMemberDefinition, typing.Dict[builtins.str, typing.Any]]]],
    workforce_name: builtins.str,
    workteam_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    notification_configuration: typing.Optional[typing.Union[SagemakerWorkteamNotificationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__882279c7caef9b0956843ba256e89b708cb85e84e6fd2fc5c50e5b34861169c6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerWorkteamMemberDefinition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd55598c8a3370cc0311d1a1bc237a0a3ce58cc132fd4df1b345f353fbd04ed4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9ddd1fc9d2ca6ff4c791fdd88d5f8a1afb49383b429757521fe867556f41021(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524daeb4555bf1324c125a36575a63bdb2c5f4f636c1076031221b26141783f9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c004e7b92318f6ac09c23b08a15d87a1d9a7832e124502207bbcab2cb4e0dd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0770a1298b35903ed2ecbc22b0ea71de1e710e41804ee779efd0eb23183f427a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a173d042facd238f06bddfe3e3f761e6aab52a60f812d32dc7b80dc8c88f1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5688e9e6b2f7440b334ca5e28007270003336ba280fe2f24fce80519c1fede19(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: builtins.str,
    member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerWorkteamMemberDefinition, typing.Dict[builtins.str, typing.Any]]]],
    workforce_name: builtins.str,
    workteam_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    notification_configuration: typing.Optional[typing.Union[SagemakerWorkteamNotificationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264e549dea3c643e3e70ed5373cac14dd5f79e3377a24df664b0c902b659481e(
    *,
    cognito_member_definition: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    oidc_member_definition: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinitionOidcMemberDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d98c03f56c945b7b2fed3d94f1dfdc2b428a0bdfb7e96ca626114a4bf9fbb3a(
    *,
    client_id: builtins.str,
    user_group: builtins.str,
    user_pool: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ec49f57cb9b1c5683de47321e30e4218543252b9837d74d681042a7ca79d08d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96c61e07c14a6e596e8d9755c32c35aabb73cbbdcb463093e1174c54fb9fb23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8fea4b24fd650007b16c4a7226d94fa0eaff4f597a2b2347436ac9f587db04e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcffee8620c15fd6141666f13c5b1888fedde6e23a67f49e8fe0920c7657f0ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c91ccd8a2180822c85a5ce5f558776ed0ac89ed3acf2347345fc68f0f01d80(
    value: typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980562309a58c4a4bc40cfa8b28f5a1cf190b589438c33935e81255188f2acc9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96f70e62940afe02c7b6ae143fec718722bc17102f22cbafb96feb40d0cebf8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba962ac054f9c4f0a4fc652cba1ef81db6707121f481fed777daf239437fa5ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed63e884785a91d8443e67491f15c12d3ece386a75f2fa6451f286cba1ffab64(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d008296883826aa37de33854a4b81897caf1a6db55bf6f8727af1d2692d2456(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ee5c007bba2865327002f909675a372ba3e5b01c73b1a63ed4a02f214ca854(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f697760f4935780d33b99e9ce8755f57df0f841206af138c389aff9658b711(
    *,
    groups: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2491f8310e37be8778c93f731e92aba55075b331ba55ee5dc742fef1aa32c8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12b447b30a6f521875bfa7f7f25265273ce8c3a7fa4e93cffe59be1a8753e0d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60ab39299dca20786c2be7d35b8b9cf7b1cd0f8fc8cb7137764e5408a312b3b(
    value: typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370231fa248581d0c2bec3525394a3bbb58045c4e2951ec26357a8b9b65369eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822fbe624e52c043c7df5cf3349bc856b119b7c3208168148d64ebef8e19354c(
    value: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac05fff26ffbf5927fdf4f7a3261747b6ed6db3da47e6d0a59dbcaa4af07b3d(
    *,
    notification_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0e65058980296bb91c9bf3a0b4a9b1894755aa7f22d7f768eb004751521d41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fab8f37099b9c190babba31063d4653c8caf2ac41df2b680b35e1fbe2df5c1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a5cc54abfc6c4d07f0e878bb70d7dcf12e24d89ead384b55516b737fc545ba4(
    value: typing.Optional[SagemakerWorkteamNotificationConfiguration],
) -> None:
    """Type checking stubs"""
    pass
