'''
# `datadog_security_monitoring_rule`

Refer to the Terraform Registory for docs: [`datadog_security_monitoring_rule`](https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule).
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


class SecurityMonitoringRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule datadog_security_monitoring_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        case: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleCase", typing.Dict[builtins.str, typing.Any]]]],
        message: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        has_extended_title: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union["SecurityMonitoringRuleOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQuery", typing.Dict[builtins.str, typing.Any]]]]] = None,
        signal_query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleSignalQuery", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule datadog_security_monitoring_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param case: case block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#case SecurityMonitoringRule#case}
        :param message: Message for generated signals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#message SecurityMonitoringRule#message}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        :param enabled: Whether the rule is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#enabled SecurityMonitoringRule#enabled}
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#filter SecurityMonitoringRule#filter}
        :param has_extended_title: Whether the notifications include the triggering group-by values in their title. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#has_extended_title SecurityMonitoringRule#has_extended_title}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#id SecurityMonitoringRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#options SecurityMonitoringRule#options}
        :param query: query block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        :param signal_query: signal_query block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#signal_query SecurityMonitoringRule#signal_query}
        :param tags: Tags for generated signals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#tags SecurityMonitoringRule#tags}
        :param type: The rule type. Valid values are ``log_detection``, ``workload_security``, ``signal_correlation``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#type SecurityMonitoringRule#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd00fd9aa3b1f81238f3c6c2a02ca88039dd987dec551b4ad0c13a2ac7b4daf9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SecurityMonitoringRuleConfig(
            case=case,
            message=message,
            name=name,
            enabled=enabled,
            filter=filter,
            has_extended_title=has_extended_title,
            id=id,
            options=options,
            query=query,
            signal_query=signal_query,
            tags=tags,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCase")
    def put_case(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleCase", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21843d0939b295598359f0f5578991649e09292c407a39271cda5a507f412892)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCase", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80552d55c26e24a98a10509de07dc5252b6360a31e1939f004d83f349fe9e782)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        *,
        keep_alive: jsii.Number,
        max_signal_duration: jsii.Number,
        decrease_criticality_based_on_env: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        detection_method: typing.Optional[builtins.str] = None,
        evaluation_window: typing.Optional[jsii.Number] = None,
        impossible_travel_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsImpossibleTravelOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        new_value_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsNewValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param keep_alive: Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window (in seconds). Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#keep_alive SecurityMonitoringRule#keep_alive}
        :param max_signal_duration: A signal will “close” regardless of the query being matched once the time exceeds the maximum duration (in seconds). This time is calculated from the first seen timestamp. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``, ``43200``, ``86400``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#max_signal_duration SecurityMonitoringRule#max_signal_duration}
        :param decrease_criticality_based_on_env: If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce noise. The decrement is applied when the environment tag of the signal starts with ``staging``, ``test``, or ``dev``. Only available when the rule type is ``log_detection``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#decrease_criticality_based_on_env SecurityMonitoringRule#decrease_criticality_based_on_env}
        :param detection_method: The detection method. Valid values are ``threshold``, ``new_value``, ``anomaly_detection``, ``impossible_travel``, ``hardcoded``, ``third_party``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#detection_method SecurityMonitoringRule#detection_method}
        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window and evaluates in real time. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#evaluation_window SecurityMonitoringRule#evaluation_window}
        :param impossible_travel_options: impossible_travel_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#impossible_travel_options SecurityMonitoringRule#impossible_travel_options}
        :param new_value_options: new_value_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#new_value_options SecurityMonitoringRule#new_value_options}
        '''
        value = SecurityMonitoringRuleOptions(
            keep_alive=keep_alive,
            max_signal_duration=max_signal_duration,
            decrease_criticality_based_on_env=decrease_criticality_based_on_env,
            detection_method=detection_method,
            evaluation_window=evaluation_window,
            impossible_travel_options=impossible_travel_options,
            new_value_options=new_value_options,
        )

        return typing.cast(None, jsii.invoke(self, "putOptions", [value]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQuery", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd984e93e3dcb7aac3e09285caddfe9aae641fd34dc939ae401cbb8880dc10c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQuery", [value]))

    @jsii.member(jsii_name="putSignalQuery")
    def put_signal_query(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleSignalQuery", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c537a52b6f9e5a364e6fe149795cc722359e5c9b6b914d2103299f84407ced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSignalQuery", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetHasExtendedTitle")
    def reset_has_extended_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHasExtendedTitle", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @jsii.member(jsii_name="resetSignalQuery")
    def reset_signal_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignalQuery", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="case")
    def case(self) -> "SecurityMonitoringRuleCaseList":
        return typing.cast("SecurityMonitoringRuleCaseList", jsii.get(self, "case"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "SecurityMonitoringRuleFilterList":
        return typing.cast("SecurityMonitoringRuleFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> "SecurityMonitoringRuleOptionsOutputReference":
        return typing.cast("SecurityMonitoringRuleOptionsOutputReference", jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "SecurityMonitoringRuleQueryList":
        return typing.cast("SecurityMonitoringRuleQueryList", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="signalQuery")
    def signal_query(self) -> "SecurityMonitoringRuleSignalQueryList":
        return typing.cast("SecurityMonitoringRuleSignalQueryList", jsii.get(self, "signalQuery"))

    @builtins.property
    @jsii.member(jsii_name="caseInput")
    def case_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleCase"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleCase"]]], jsii.get(self, "caseInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="hasExtendedTitleInput")
    def has_extended_title_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hasExtendedTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional["SecurityMonitoringRuleOptions"]:
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptions"], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="signalQueryInput")
    def signal_query_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleSignalQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleSignalQuery"]]], jsii.get(self, "signalQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__79c2cc02f1f7d0fb5475e36e3c668b6cf61c0b15ec4c3af9d7d0a56be5512c4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="hasExtendedTitle")
    def has_extended_title(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hasExtendedTitle"))

    @has_extended_title.setter
    def has_extended_title(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87277a0eb4c797984073d9df088e6c2ed9b28b7b0cc7c28dfe662d38123044a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hasExtendedTitle", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a2dd5cb6662f9dca5b1d351daa8f8c466849f76e255425e87f469b21b63457)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a9de83be685f9029f4bcca872f228e4a5e92d32c96e5b7efc62338a598fd15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10fc9bd81d8a79f06f7e1c8dbd87aa1cfcbf5c3dcdb9f9aaf7c456062aada94f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1309c6964d89e2a817ea67920d23678803dbe78221b5ab26f28aae8b4ae3deca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199c9a33aa378e32bc2bb89251dd5022dd0ddaa9b8cd8df3eb21dbc00c944814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleCase",
    jsii_struct_bases=[],
    name_mapping={
        "status": "status",
        "condition": "condition",
        "name": "name",
        "notifications": "notifications",
    },
)
class SecurityMonitoringRuleCase:
    def __init__(
        self,
        *,
        status: builtins.str,
        condition: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notifications: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param status: Severity of the Security Signal. Valid values are ``info``, ``low``, ``medium``, ``high``, ``critical``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#status SecurityMonitoringRule#status}
        :param condition: A rule case contains logical operations (``>``,``>=``, ``&&``, ``||``) to determine if a signal should be generated based on the event counts in the previously defined queries. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#condition SecurityMonitoringRule#condition}
        :param name: Name of the case. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        :param notifications: Notification targets for each rule case. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#notifications SecurityMonitoringRule#notifications}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be9ecb132ecadc5053f5b0553890fcdceb22f380336d4d877a920ef0e917ced6)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }
        if condition is not None:
            self._values["condition"] = condition
        if name is not None:
            self._values["name"] = name
        if notifications is not None:
            self._values["notifications"] = notifications

    @builtins.property
    def status(self) -> builtins.str:
        '''Severity of the Security Signal. Valid values are ``info``, ``low``, ``medium``, ``high``, ``critical``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#status SecurityMonitoringRule#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''A rule case contains logical operations (``>``,``>=``, ``&&``, ``||``) to determine if a signal should be generated based on the event counts in the previously defined queries.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#condition SecurityMonitoringRule#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the case.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notifications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Notification targets for each rule case.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#notifications SecurityMonitoringRule#notifications}
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleCase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleCaseList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleCaseList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4af5fab296d1d42f777966673fcbd95fa7d3e2619d8e52d4799a4fcd3a7a208)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SecurityMonitoringRuleCaseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cbda2d84beedee0d00a03d8ef0a53c1462a02c111bd7f46590679aecad269f1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleCaseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__437227749b9563b3dd5f95d1dc25e61f01b7115799e692655b39058ce6414015)
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
            type_hints = typing.get_type_hints(_typecheckingstub__545f10aa76750d99ba252f292b5e19f24ed1fa4aeac289d16fff1c47336dea68)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ca964d384bb024430539d3d3a24b30aac2830b4a96a8fa180fb53a5d32267dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleCase]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleCase]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleCase]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39776ddc56626b168e9f8d69054776a0dd7b8799cbe468863fec2d7355b208cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleCaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleCaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d86bb77cd1501a75b429bc099ba24fb7eba40ae625c5324a558f186cc061f54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNotifications")
    def reset_notifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifications", []))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationsInput")
    def notifications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994d4e6e57e4ffb752297ba19504bbea10794ccf8e8e154b74c98d9ee69e314c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2f6ad45a76cfe0dc0f49f0d11bbc8882bb10372aac394f9221fbfd1038d4e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notifications"))

    @notifications.setter
    def notifications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6854e55505c510e4ce54300a21b3ff5e8dfc0887645758fe44ed8bbfc4018a0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifications", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd2fa55bcad92f126a6c1244c013a7d9f55296fa1ee6104ecde0840a0e85660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleCase, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleCase, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleCase, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6887bad88cf805899b1ca19d8d73fd5fd666e2b1b50fb4cb4359f553adf52f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "case": "case",
        "message": "message",
        "name": "name",
        "enabled": "enabled",
        "filter": "filter",
        "has_extended_title": "hasExtendedTitle",
        "id": "id",
        "options": "options",
        "query": "query",
        "signal_query": "signalQuery",
        "tags": "tags",
        "type": "type",
    },
)
class SecurityMonitoringRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        case: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleCase, typing.Dict[builtins.str, typing.Any]]]],
        message: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        has_extended_title: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union["SecurityMonitoringRuleOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQuery", typing.Dict[builtins.str, typing.Any]]]]] = None,
        signal_query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleSignalQuery", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param case: case block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#case SecurityMonitoringRule#case}
        :param message: Message for generated signals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#message SecurityMonitoringRule#message}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        :param enabled: Whether the rule is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#enabled SecurityMonitoringRule#enabled}
        :param filter: filter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#filter SecurityMonitoringRule#filter}
        :param has_extended_title: Whether the notifications include the triggering group-by values in their title. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#has_extended_title SecurityMonitoringRule#has_extended_title}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#id SecurityMonitoringRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#options SecurityMonitoringRule#options}
        :param query: query block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        :param signal_query: signal_query block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#signal_query SecurityMonitoringRule#signal_query}
        :param tags: Tags for generated signals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#tags SecurityMonitoringRule#tags}
        :param type: The rule type. Valid values are ``log_detection``, ``workload_security``, ``signal_correlation``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#type SecurityMonitoringRule#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(options, dict):
            options = SecurityMonitoringRuleOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11fb48eb81a5c88e4dd36e60d914b894a63e04642134d6e62d2337bdb1639ab1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument case", value=case, expected_type=type_hints["case"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument has_extended_title", value=has_extended_title, expected_type=type_hints["has_extended_title"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument signal_query", value=signal_query, expected_type=type_hints["signal_query"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "case": case,
            "message": message,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if filter is not None:
            self._values["filter"] = filter
        if has_extended_title is not None:
            self._values["has_extended_title"] = has_extended_title
        if id is not None:
            self._values["id"] = id
        if options is not None:
            self._values["options"] = options
        if query is not None:
            self._values["query"] = query
        if signal_query is not None:
            self._values["signal_query"] = signal_query
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

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
    def case(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleCase]]:
        '''case block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#case SecurityMonitoringRule#case}
        '''
        result = self._values.get("case")
        assert result is not None, "Required property 'case' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleCase]], result)

    @builtins.property
    def message(self) -> builtins.str:
        '''Message for generated signals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#message SecurityMonitoringRule#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the rule is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#enabled SecurityMonitoringRule#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#filter SecurityMonitoringRule#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]], result)

    @builtins.property
    def has_extended_title(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the notifications include the triggering group-by values in their title.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#has_extended_title SecurityMonitoringRule#has_extended_title}
        '''
        result = self._values.get("has_extended_title")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#id SecurityMonitoringRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional["SecurityMonitoringRuleOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#options SecurityMonitoringRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptions"], result)

    @builtins.property
    def query(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]]:
        '''query block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]], result)

    @builtins.property
    def signal_query(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleSignalQuery"]]]:
        '''signal_query block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#signal_query SecurityMonitoringRule#signal_query}
        '''
        result = self._values.get("signal_query")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleSignalQuery"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags for generated signals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#tags SecurityMonitoringRule#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The rule type. Valid values are ``log_detection``, ``workload_security``, ``signal_correlation``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#type SecurityMonitoringRule#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleFilter",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "query": "query"},
)
class SecurityMonitoringRuleFilter:
    def __init__(self, *, action: builtins.str, query: builtins.str) -> None:
        '''
        :param action: The type of filtering action. Valid values are ``require``, ``suppress``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#action SecurityMonitoringRule#action}
        :param query: Query for selecting logs to apply the filtering action. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c866bf17fbaa97751b321daaeb1d7870b2fbcfdf8bdcc285606da3317f7f0ab)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "query": query,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''The type of filtering action. Valid values are ``require``, ``suppress``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#action SecurityMonitoringRule#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Query for selecting logs to apply the filtering action.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab69056cae7741c2e697d9329dc282917ed499775aff5504caf3113ac9e1bd25)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SecurityMonitoringRuleFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665044e86f49b6fd5262c7e90cc228cd1cc96c7e1f443e824f0339e7b4f47a2f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d484b7eb5784c420a0e8b96501c0dd8c92be0df59c7c5225e8eb3a0d022f5dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d44a13aec1c9f29530bf63924dac276252659e2afc9c4e26edc9e097a0de064)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da15a1014b2ae46501d264d5c96a59982599e3479caa42a79f979a1c0799de16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3892322b9369dc6f69dca4113fc31ce3def6cf1915a5acfd6e9710b91cf53e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71da086c92642ab7ca0d19c8840df1e48913064bc5776012cb51ebf341c2fb7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91d756d1cdc4ed79c7bf9934e614b2c85d7f411cd200c460c25378b12af7f15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf96323ee437d82fa7635b69244cde1bc85b65b309eec059370a8f33ed509c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7110dd4b72ee63f8fb0bce1b6ddb59d1dfbbc29907d8fcd73c9db86eaff35b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "keep_alive": "keepAlive",
        "max_signal_duration": "maxSignalDuration",
        "decrease_criticality_based_on_env": "decreaseCriticalityBasedOnEnv",
        "detection_method": "detectionMethod",
        "evaluation_window": "evaluationWindow",
        "impossible_travel_options": "impossibleTravelOptions",
        "new_value_options": "newValueOptions",
    },
)
class SecurityMonitoringRuleOptions:
    def __init__(
        self,
        *,
        keep_alive: jsii.Number,
        max_signal_duration: jsii.Number,
        decrease_criticality_based_on_env: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        detection_method: typing.Optional[builtins.str] = None,
        evaluation_window: typing.Optional[jsii.Number] = None,
        impossible_travel_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsImpossibleTravelOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        new_value_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsNewValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param keep_alive: Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window (in seconds). Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#keep_alive SecurityMonitoringRule#keep_alive}
        :param max_signal_duration: A signal will “close” regardless of the query being matched once the time exceeds the maximum duration (in seconds). This time is calculated from the first seen timestamp. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``, ``43200``, ``86400``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#max_signal_duration SecurityMonitoringRule#max_signal_duration}
        :param decrease_criticality_based_on_env: If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce noise. The decrement is applied when the environment tag of the signal starts with ``staging``, ``test``, or ``dev``. Only available when the rule type is ``log_detection``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#decrease_criticality_based_on_env SecurityMonitoringRule#decrease_criticality_based_on_env}
        :param detection_method: The detection method. Valid values are ``threshold``, ``new_value``, ``anomaly_detection``, ``impossible_travel``, ``hardcoded``, ``third_party``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#detection_method SecurityMonitoringRule#detection_method}
        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window and evaluates in real time. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#evaluation_window SecurityMonitoringRule#evaluation_window}
        :param impossible_travel_options: impossible_travel_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#impossible_travel_options SecurityMonitoringRule#impossible_travel_options}
        :param new_value_options: new_value_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#new_value_options SecurityMonitoringRule#new_value_options}
        '''
        if isinstance(impossible_travel_options, dict):
            impossible_travel_options = SecurityMonitoringRuleOptionsImpossibleTravelOptions(**impossible_travel_options)
        if isinstance(new_value_options, dict):
            new_value_options = SecurityMonitoringRuleOptionsNewValueOptions(**new_value_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2f7bae60c86359ebc4d68c51b2be49bf8e2e753c626fd4ed979c7be28af738)
            check_type(argname="argument keep_alive", value=keep_alive, expected_type=type_hints["keep_alive"])
            check_type(argname="argument max_signal_duration", value=max_signal_duration, expected_type=type_hints["max_signal_duration"])
            check_type(argname="argument decrease_criticality_based_on_env", value=decrease_criticality_based_on_env, expected_type=type_hints["decrease_criticality_based_on_env"])
            check_type(argname="argument detection_method", value=detection_method, expected_type=type_hints["detection_method"])
            check_type(argname="argument evaluation_window", value=evaluation_window, expected_type=type_hints["evaluation_window"])
            check_type(argname="argument impossible_travel_options", value=impossible_travel_options, expected_type=type_hints["impossible_travel_options"])
            check_type(argname="argument new_value_options", value=new_value_options, expected_type=type_hints["new_value_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keep_alive": keep_alive,
            "max_signal_duration": max_signal_duration,
        }
        if decrease_criticality_based_on_env is not None:
            self._values["decrease_criticality_based_on_env"] = decrease_criticality_based_on_env
        if detection_method is not None:
            self._values["detection_method"] = detection_method
        if evaluation_window is not None:
            self._values["evaluation_window"] = evaluation_window
        if impossible_travel_options is not None:
            self._values["impossible_travel_options"] = impossible_travel_options
        if new_value_options is not None:
            self._values["new_value_options"] = new_value_options

    @builtins.property
    def keep_alive(self) -> jsii.Number:
        '''Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window (in seconds).

        Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#keep_alive SecurityMonitoringRule#keep_alive}
        '''
        result = self._values.get("keep_alive")
        assert result is not None, "Required property 'keep_alive' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_signal_duration(self) -> jsii.Number:
        '''A signal will “close” regardless of the query being matched once the time exceeds the maximum duration (in seconds).

        This time is calculated from the first seen timestamp. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``, ``43200``, ``86400``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#max_signal_duration SecurityMonitoringRule#max_signal_duration}
        '''
        result = self._values.get("max_signal_duration")
        assert result is not None, "Required property 'max_signal_duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def decrease_criticality_based_on_env(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce noise.

        The decrement is applied when the environment tag of the signal starts with ``staging``, ``test``, or ``dev``. Only available when the rule type is ``log_detection``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#decrease_criticality_based_on_env SecurityMonitoringRule#decrease_criticality_based_on_env}
        '''
        result = self._values.get("decrease_criticality_based_on_env")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def detection_method(self) -> typing.Optional[builtins.str]:
        '''The detection method. Valid values are ``threshold``, ``new_value``, ``anomaly_detection``, ``impossible_travel``, ``hardcoded``, ``third_party``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#detection_method SecurityMonitoringRule#detection_method}
        '''
        result = self._values.get("detection_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_window(self) -> typing.Optional[jsii.Number]:
        '''A time window is specified to match when at least one of the cases matches true.

        This is a sliding window and evaluates in real time. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#evaluation_window SecurityMonitoringRule#evaluation_window}
        '''
        result = self._values.get("evaluation_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def impossible_travel_options(
        self,
    ) -> typing.Optional["SecurityMonitoringRuleOptionsImpossibleTravelOptions"]:
        '''impossible_travel_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#impossible_travel_options SecurityMonitoringRule#impossible_travel_options}
        '''
        result = self._values.get("impossible_travel_options")
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptionsImpossibleTravelOptions"], result)

    @builtins.property
    def new_value_options(
        self,
    ) -> typing.Optional["SecurityMonitoringRuleOptionsNewValueOptions"]:
        '''new_value_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#new_value_options SecurityMonitoringRule#new_value_options}
        '''
        result = self._values.get("new_value_options")
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptionsNewValueOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsImpossibleTravelOptions",
    jsii_struct_bases=[],
    name_mapping={"baseline_user_locations": "baselineUserLocations"},
)
class SecurityMonitoringRuleOptionsImpossibleTravelOptions:
    def __init__(
        self,
        *,
        baseline_user_locations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param baseline_user_locations: If true, signals are suppressed for the first 24 hours. During that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#baseline_user_locations SecurityMonitoringRule#baseline_user_locations}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db8e8b16fb596505bcc3f7b2501d629ea7f84e5e1c1058ae18d30c78bbb47df6)
            check_type(argname="argument baseline_user_locations", value=baseline_user_locations, expected_type=type_hints["baseline_user_locations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if baseline_user_locations is not None:
            self._values["baseline_user_locations"] = baseline_user_locations

    @builtins.property
    def baseline_user_locations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, signals are suppressed for the first 24 hours.

        During that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#baseline_user_locations SecurityMonitoringRule#baseline_user_locations}
        '''
        result = self._values.get("baseline_user_locations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleOptionsImpossibleTravelOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccadaaf759975edee0db51c47993d98b54459e2c30d80cca992cb809cf572c70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBaselineUserLocations")
    def reset_baseline_user_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineUserLocations", []))

    @builtins.property
    @jsii.member(jsii_name="baselineUserLocationsInput")
    def baseline_user_locations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "baselineUserLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineUserLocations")
    def baseline_user_locations(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "baselineUserLocations"))

    @baseline_user_locations.setter
    def baseline_user_locations(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2db6f8adfdd0ffd6d51a531490b61b321bb3ac5492060f7b77527f0bdb4f3025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baselineUserLocations", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f264f2cedb634c2324a2e53547d34c219c7466438ecef62ca60424e196c88e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsNewValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "forget_after": "forgetAfter",
        "learning_duration": "learningDuration",
        "learning_method": "learningMethod",
        "learning_threshold": "learningThreshold",
    },
)
class SecurityMonitoringRuleOptionsNewValueOptions:
    def __init__(
        self,
        *,
        forget_after: jsii.Number,
        learning_duration: typing.Optional[jsii.Number] = None,
        learning_method: typing.Optional[builtins.str] = None,
        learning_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forget_after: The duration in days after which a learned value is forgotten. Valid values are ``1``, ``2``, ``7``, ``14``, ``21``, ``28``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#forget_after SecurityMonitoringRule#forget_after}
        :param learning_duration: The duration in days during which values are learned, and after which signals will be generated for values that weren't learned. If set to 0, a signal will be generated for all new values after the first value is learned. Valid values are ``0``, ``1``, ``7``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_duration SecurityMonitoringRule#learning_duration}
        :param learning_method: The learning method used to determine when signals should be generated for values that weren't learned. Valid values are ``duration``, ``threshold``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_method SecurityMonitoringRule#learning_method}
        :param learning_threshold: A number of occurrences after which signals are generated for values that weren't learned. Valid values are ``0``, ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_threshold SecurityMonitoringRule#learning_threshold}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__549e4b89e82ed8c6c587a2adffb2382abe55bfe4e244c06f7bf7db9e55b21148)
            check_type(argname="argument forget_after", value=forget_after, expected_type=type_hints["forget_after"])
            check_type(argname="argument learning_duration", value=learning_duration, expected_type=type_hints["learning_duration"])
            check_type(argname="argument learning_method", value=learning_method, expected_type=type_hints["learning_method"])
            check_type(argname="argument learning_threshold", value=learning_threshold, expected_type=type_hints["learning_threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "forget_after": forget_after,
        }
        if learning_duration is not None:
            self._values["learning_duration"] = learning_duration
        if learning_method is not None:
            self._values["learning_method"] = learning_method
        if learning_threshold is not None:
            self._values["learning_threshold"] = learning_threshold

    @builtins.property
    def forget_after(self) -> jsii.Number:
        '''The duration in days after which a learned value is forgotten.

        Valid values are ``1``, ``2``, ``7``, ``14``, ``21``, ``28``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#forget_after SecurityMonitoringRule#forget_after}
        '''
        result = self._values.get("forget_after")
        assert result is not None, "Required property 'forget_after' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def learning_duration(self) -> typing.Optional[jsii.Number]:
        '''The duration in days during which values are learned, and after which signals will be generated for values that weren't learned.

        If set to 0, a signal will be generated for all new values after the first value is learned. Valid values are ``0``, ``1``, ``7``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_duration SecurityMonitoringRule#learning_duration}
        '''
        result = self._values.get("learning_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def learning_method(self) -> typing.Optional[builtins.str]:
        '''The learning method used to determine when signals should be generated for values that weren't learned.

        Valid values are ``duration``, ``threshold``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_method SecurityMonitoringRule#learning_method}
        '''
        result = self._values.get("learning_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def learning_threshold(self) -> typing.Optional[jsii.Number]:
        '''A number of occurrences after which signals are generated for values that weren't learned. Valid values are ``0``, ``1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_threshold SecurityMonitoringRule#learning_threshold}
        '''
        result = self._values.get("learning_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleOptionsNewValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleOptionsNewValueOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsNewValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d9e766c6abd7205ec9c5f682274f0ba3d897190a2c1c6bf9f4139b6b5381c69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLearningDuration")
    def reset_learning_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLearningDuration", []))

    @jsii.member(jsii_name="resetLearningMethod")
    def reset_learning_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLearningMethod", []))

    @jsii.member(jsii_name="resetLearningThreshold")
    def reset_learning_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLearningThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="forgetAfterInput")
    def forget_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "forgetAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="learningDurationInput")
    def learning_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "learningDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="learningMethodInput")
    def learning_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "learningMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="learningThresholdInput")
    def learning_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "learningThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="forgetAfter")
    def forget_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "forgetAfter"))

    @forget_after.setter
    def forget_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eb0b1c0e668079de485fb3ef35e45b5b8270e3b36ff031b70638e57d4e9e7b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forgetAfter", value)

    @builtins.property
    @jsii.member(jsii_name="learningDuration")
    def learning_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "learningDuration"))

    @learning_duration.setter
    def learning_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a39ba61c48fcc577b4d1c3560fa725786d2bd05ccb8eb6a919c94390c9b7859)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "learningDuration", value)

    @builtins.property
    @jsii.member(jsii_name="learningMethod")
    def learning_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "learningMethod"))

    @learning_method.setter
    def learning_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ff9a903552abd7ba112dc2475f5549a2f4e7cede9c1e56c1d847b088f5254a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "learningMethod", value)

    @builtins.property
    @jsii.member(jsii_name="learningThreshold")
    def learning_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "learningThreshold"))

    @learning_threshold.setter
    def learning_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a348d958a114a6e226ae9d68990b653669b14280fc2bf97735332be9c0cd2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "learningThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4888d3185d053f71f6a2d215f6771c04dae7078d79f722970a65e88bfb32da8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0a178de098c7dcea33300fc4c4cd6422bfea963ce52b6ae2316c8d045527671)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putImpossibleTravelOptions")
    def put_impossible_travel_options(
        self,
        *,
        baseline_user_locations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param baseline_user_locations: If true, signals are suppressed for the first 24 hours. During that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#baseline_user_locations SecurityMonitoringRule#baseline_user_locations}
        '''
        value = SecurityMonitoringRuleOptionsImpossibleTravelOptions(
            baseline_user_locations=baseline_user_locations
        )

        return typing.cast(None, jsii.invoke(self, "putImpossibleTravelOptions", [value]))

    @jsii.member(jsii_name="putNewValueOptions")
    def put_new_value_options(
        self,
        *,
        forget_after: jsii.Number,
        learning_duration: typing.Optional[jsii.Number] = None,
        learning_method: typing.Optional[builtins.str] = None,
        learning_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forget_after: The duration in days after which a learned value is forgotten. Valid values are ``1``, ``2``, ``7``, ``14``, ``21``, ``28``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#forget_after SecurityMonitoringRule#forget_after}
        :param learning_duration: The duration in days during which values are learned, and after which signals will be generated for values that weren't learned. If set to 0, a signal will be generated for all new values after the first value is learned. Valid values are ``0``, ``1``, ``7``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_duration SecurityMonitoringRule#learning_duration}
        :param learning_method: The learning method used to determine when signals should be generated for values that weren't learned. Valid values are ``duration``, ``threshold``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_method SecurityMonitoringRule#learning_method}
        :param learning_threshold: A number of occurrences after which signals are generated for values that weren't learned. Valid values are ``0``, ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#learning_threshold SecurityMonitoringRule#learning_threshold}
        '''
        value = SecurityMonitoringRuleOptionsNewValueOptions(
            forget_after=forget_after,
            learning_duration=learning_duration,
            learning_method=learning_method,
            learning_threshold=learning_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putNewValueOptions", [value]))

    @jsii.member(jsii_name="resetDecreaseCriticalityBasedOnEnv")
    def reset_decrease_criticality_based_on_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecreaseCriticalityBasedOnEnv", []))

    @jsii.member(jsii_name="resetDetectionMethod")
    def reset_detection_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetectionMethod", []))

    @jsii.member(jsii_name="resetEvaluationWindow")
    def reset_evaluation_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationWindow", []))

    @jsii.member(jsii_name="resetImpossibleTravelOptions")
    def reset_impossible_travel_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImpossibleTravelOptions", []))

    @jsii.member(jsii_name="resetNewValueOptions")
    def reset_new_value_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewValueOptions", []))

    @builtins.property
    @jsii.member(jsii_name="impossibleTravelOptions")
    def impossible_travel_options(
        self,
    ) -> SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference:
        return typing.cast(SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference, jsii.get(self, "impossibleTravelOptions"))

    @builtins.property
    @jsii.member(jsii_name="newValueOptions")
    def new_value_options(
        self,
    ) -> SecurityMonitoringRuleOptionsNewValueOptionsOutputReference:
        return typing.cast(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, jsii.get(self, "newValueOptions"))

    @builtins.property
    @jsii.member(jsii_name="decreaseCriticalityBasedOnEnvInput")
    def decrease_criticality_based_on_env_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "decreaseCriticalityBasedOnEnvInput"))

    @builtins.property
    @jsii.member(jsii_name="detectionMethodInput")
    def detection_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectionMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationWindowInput")
    def evaluation_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="impossibleTravelOptionsInput")
    def impossible_travel_options_input(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions], jsii.get(self, "impossibleTravelOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keepAliveInput")
    def keep_alive_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keepAliveInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSignalDurationInput")
    def max_signal_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSignalDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="newValueOptionsInput")
    def new_value_options_input(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions], jsii.get(self, "newValueOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="decreaseCriticalityBasedOnEnv")
    def decrease_criticality_based_on_env(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "decreaseCriticalityBasedOnEnv"))

    @decrease_criticality_based_on_env.setter
    def decrease_criticality_based_on_env(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eb8f3e31ed788579fcaedfb79d4a649cc04134da4368430e309ad95bfc88b7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decreaseCriticalityBasedOnEnv", value)

    @builtins.property
    @jsii.member(jsii_name="detectionMethod")
    def detection_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detectionMethod"))

    @detection_method.setter
    def detection_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed4917ef6954206b2b9e24a56823c0f54888225db2a3b34da20cd3be46c7955f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectionMethod", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationWindow")
    def evaluation_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationWindow"))

    @evaluation_window.setter
    def evaluation_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__084fb9d16bea45464790711a1e22a60de6f10e47f10b06a435a70044d9898b71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationWindow", value)

    @builtins.property
    @jsii.member(jsii_name="keepAlive")
    def keep_alive(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keepAlive"))

    @keep_alive.setter
    def keep_alive(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0a97acd18d55bf7c7ba0abe5a84a7cdae9d3e150ae9ea9ed7488bba8f032ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAlive", value)

    @builtins.property
    @jsii.member(jsii_name="maxSignalDuration")
    def max_signal_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSignalDuration"))

    @max_signal_duration.setter
    def max_signal_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5089c54f3899b05b452ce2f0a7ca9b64d5ffc60f719911e05dcd0dcf824ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSignalDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SecurityMonitoringRuleOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecurityMonitoringRuleOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dcf2674869388a8307dfcbcedb34156418c7243b113bbb814c22da4c7d00642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQuery",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "agent_rule": "agentRule",
        "aggregation": "aggregation",
        "distinct_fields": "distinctFields",
        "group_by_fields": "groupByFields",
        "metric": "metric",
        "metrics": "metrics",
        "name": "name",
    },
)
class SecurityMonitoringRuleQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        agent_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQueryAgentRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        aggregation: typing.Optional[builtins.str] = None,
        distinct_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        metric: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: Query to run on logs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        :param agent_rule: agent_rule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#agent_rule SecurityMonitoringRule#agent_rule}
        :param aggregation: The aggregation type. For Signal Correlation rules, it must be event_count. Valid values are ``count``, ``cardinality``, ``sum``, ``max``, ``new_value``, ``geo_data``, ``event_count``, ``none``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#aggregation SecurityMonitoringRule#aggregation}
        :param distinct_fields: Field for which the cardinality is measured. Sent as an array. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#distinct_fields SecurityMonitoringRule#distinct_fields}
        :param group_by_fields: Fields to group by. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#group_by_fields SecurityMonitoringRule#group_by_fields}
        :param metric: The target field to aggregate over when using the ``sum``, ``max``, or ``geo_data`` aggregations. **Deprecated.** Configure ``metrics`` instead. This attribute will be removed in the next major version of the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#metric SecurityMonitoringRule#metric}
        :param metrics: Group of target fields to aggregate over when using the ``sum``, ``max``, ``geo_data``, or ``new_value`` aggregations. The ``sum``, ``max``, and ``geo_data`` aggregations only accept one value in this list, whereas the ``new_value`` aggregation accepts up to five values. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#metrics SecurityMonitoringRule#metrics}
        :param name: Name of the query. Not compatible with ``new_value`` aggregations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e8f570b0171354820639da7d8575f7c19be01bb17e683a3669127e02c739aca)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument agent_rule", value=agent_rule, expected_type=type_hints["agent_rule"])
            check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
            check_type(argname="argument distinct_fields", value=distinct_fields, expected_type=type_hints["distinct_fields"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query": query,
        }
        if agent_rule is not None:
            self._values["agent_rule"] = agent_rule
        if aggregation is not None:
            self._values["aggregation"] = aggregation
        if distinct_fields is not None:
            self._values["distinct_fields"] = distinct_fields
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if metric is not None:
            self._values["metric"] = metric
        if metrics is not None:
            self._values["metrics"] = metrics
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def query(self) -> builtins.str:
        '''Query to run on logs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleQueryAgentRule"]]]:
        '''agent_rule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#agent_rule SecurityMonitoringRule#agent_rule}
        '''
        result = self._values.get("agent_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SecurityMonitoringRuleQueryAgentRule"]]], result)

    @builtins.property
    def aggregation(self) -> typing.Optional[builtins.str]:
        '''The aggregation type.

        For Signal Correlation rules, it must be event_count. Valid values are ``count``, ``cardinality``, ``sum``, ``max``, ``new_value``, ``geo_data``, ``event_count``, ``none``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#aggregation SecurityMonitoringRule#aggregation}
        '''
        result = self._values.get("aggregation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distinct_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Field for which the cardinality is measured. Sent as an array.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#distinct_fields SecurityMonitoringRule#distinct_fields}
        '''
        result = self._values.get("distinct_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fields to group by.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#group_by_fields SecurityMonitoringRule#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metric(self) -> typing.Optional[builtins.str]:
        '''The target field to aggregate over when using the ``sum``, ``max``, or ``geo_data`` aggregations.

        **Deprecated.** Configure ``metrics`` instead. This attribute will be removed in the next major version of the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#metric SecurityMonitoringRule#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Group of target fields to aggregate over when using the ``sum``, ``max``, ``geo_data``, or ``new_value`` aggregations.

        The ``sum``, ``max``, and ``geo_data`` aggregations only accept one value in this list, whereas the ``new_value`` aggregation accepts up to five values.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#metrics SecurityMonitoringRule#metrics}
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the query. Not compatible with ``new_value`` aggregations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryAgentRule",
    jsii_struct_bases=[],
    name_mapping={"agent_rule_id": "agentRuleId", "expression": "expression"},
)
class SecurityMonitoringRuleQueryAgentRule:
    def __init__(
        self,
        *,
        agent_rule_id: builtins.str,
        expression: builtins.str,
    ) -> None:
        '''
        :param agent_rule_id: **Deprecated**. It won't be applied anymore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#agent_rule_id SecurityMonitoringRule#agent_rule_id}
        :param expression: **Deprecated**. It won't be applied anymore. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#expression SecurityMonitoringRule#expression}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdfe13239dc740bfb832b869018ed53be671f89aeff0fa0f0b7503c00a5e055d)
            check_type(argname="argument agent_rule_id", value=agent_rule_id, expected_type=type_hints["agent_rule_id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_rule_id": agent_rule_id,
            "expression": expression,
        }

    @builtins.property
    def agent_rule_id(self) -> builtins.str:
        '''**Deprecated**. It won't be applied anymore.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#agent_rule_id SecurityMonitoringRule#agent_rule_id}
        '''
        result = self._values.get("agent_rule_id")
        assert result is not None, "Required property 'agent_rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> builtins.str:
        '''**Deprecated**. It won't be applied anymore.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#expression SecurityMonitoringRule#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleQueryAgentRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleQueryAgentRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryAgentRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bd8f076131df53fcff1edd65213177e7d36e440f62f61c60ebad2fca5da9429)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SecurityMonitoringRuleQueryAgentRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__004245166e93b36b2b71d68aae9e7f25f6d6dcd21d0a21f9749f93615329f9ff)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleQueryAgentRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6939439239ee603522d33490603a5496c6e75e553488f7f45f39f6b3157770b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e99f6bc42a94deb02bc3310de93246f8ee3d8015451c677a0befcd9a61c53b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__860f91d086f2a07fa25d818d06be120c2f178bf7513567a93582ae5e8c91b221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1533ae880f7716765c3118eaa8ad178ad75f6bccfd9e4ec4be775c59aac92884)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleQueryAgentRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryAgentRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__336d1f1607e88e3ffacb852af0bfa6603f01229396b748992c696cbb91910c0d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="agentRuleIdInput")
    def agent_rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentRuleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="agentRuleId")
    def agent_rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentRuleId"))

    @agent_rule_id.setter
    def agent_rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910dd2ecaa77048a39a2b96e33c82833407b8c845029204b220be5a9b54be967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuleId", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee98199254a17fe67dbb708e86bfc679a2cd085162cfe080f8e4bc01e175607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa683c94fdf04993a4599dc98f4826d68a6a9cceaa929a0843a9f8a556038b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleQueryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65366874071e6644bf8a0e7e80a0c0e2f7c31f724ec2b9b15992f0a689d3cf49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SecurityMonitoringRuleQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffdd383854bde9a20c6ab03af8b31f59381462522dbab803f7a9b970059ad33)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2311baf1e6a56be9912434967728a6c5d5ac470219f08eca5bb461ff5d1186c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6beda91c6822ba8533c22a7b7d766f69328148e370c815e81743b1c5c8f5b677)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9530b7f37c6a73545b3c960afe5b757c6298b335839e5ea4102c45edf7f9289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQuery]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__254a1c6494eb5015f046fb8bcc3e27ad830879f52605ef917ba4dd35ae1dd1a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleQueryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1065e8519613430d858e54084b0ff442e93d967b0a385ecbf87abc6475ea0a0f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAgentRule")
    def put_agent_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQueryAgentRule, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb99df23d35551417fb951e7d92f33e9762c412833a9a006bdb89f09b9d45922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAgentRule", [value]))

    @jsii.member(jsii_name="resetAgentRule")
    def reset_agent_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentRule", []))

    @jsii.member(jsii_name="resetAggregation")
    def reset_aggregation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregation", []))

    @jsii.member(jsii_name="resetDistinctFields")
    def reset_distinct_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistinctFields", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetMetrics")
    def reset_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetrics", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="agentRule")
    def agent_rule(self) -> SecurityMonitoringRuleQueryAgentRuleList:
        return typing.cast(SecurityMonitoringRuleQueryAgentRuleList, jsii.get(self, "agentRule"))

    @builtins.property
    @jsii.member(jsii_name="agentRuleInput")
    def agent_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]], jsii.get(self, "agentRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationInput")
    def aggregation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationInput"))

    @builtins.property
    @jsii.member(jsii_name="distinctFieldsInput")
    def distinct_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "distinctFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsInput")
    def metrics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metricsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregation")
    def aggregation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregation"))

    @aggregation.setter
    def aggregation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a03545b69d06f203d06f54ecb58fee4362b42882cadb2d8ba0ecf3f06a553f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregation", value)

    @builtins.property
    @jsii.member(jsii_name="distinctFields")
    def distinct_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "distinctFields"))

    @distinct_fields.setter
    def distinct_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ac1fc36bb840bf105e1ad56581a9f835b50f82d9a4725cf1d80d8ca9ef6a185)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distinctFields", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c276cef0c4f93b80c4651687330aef0e1bee295bd1613b5bd178159424f6f0d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metric"))

    @metric.setter
    def metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a7c5122401386e2ea1c4cf6e0586ac32aae456ad0d078e58ebc5f366b1c39e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metric", value)

    @builtins.property
    @jsii.member(jsii_name="metrics")
    def metrics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "metrics"))

    @metrics.setter
    def metrics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6aeaedb3bd88cb7041e050e1e8fa5ace8631356747fe3798eb543aa4cc5a752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metrics", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e833cf6cddeb31b26bd7ec1d3e956b2c9707add05c561538e7c082ce1f1421)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a4e9f218256f994b0e53d9e273cbd62e4836f21dea46900da60df2bb25b99c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleQuery, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleQuery, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleQuery, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c06fa9516f8b3aa9bbcb1c102402341f477a1f8ee0dba6edeadf86e229076c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleSignalQuery",
    jsii_struct_bases=[],
    name_mapping={
        "rule_id": "ruleId",
        "aggregation": "aggregation",
        "correlated_by_fields": "correlatedByFields",
        "correlated_query_index": "correlatedQueryIndex",
        "default_rule_id": "defaultRuleId",
        "name": "name",
    },
)
class SecurityMonitoringRuleSignalQuery:
    def __init__(
        self,
        *,
        rule_id: builtins.str,
        aggregation: typing.Optional[builtins.str] = None,
        correlated_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        correlated_query_index: typing.Optional[builtins.str] = None,
        default_rule_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rule_id: Rule ID of the signal to correlate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#rule_id SecurityMonitoringRule#rule_id}
        :param aggregation: The aggregation type. For Signal Correlation rules, it must be event_count. Valid values are ``count``, ``cardinality``, ``sum``, ``max``, ``new_value``, ``geo_data``, ``event_count``, ``none``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#aggregation SecurityMonitoringRule#aggregation}
        :param correlated_by_fields: Fields to correlate by. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#correlated_by_fields SecurityMonitoringRule#correlated_by_fields}
        :param correlated_query_index: Index of the rule query used to retrieve the correlated field. An empty string applies correlation on the non-projected per query attributes of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#correlated_query_index SecurityMonitoringRule#correlated_query_index}
        :param default_rule_id: Default Rule ID of the signal to correlate. This value is READ-ONLY. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#default_rule_id SecurityMonitoringRule#default_rule_id}
        :param name: Name of the query. Not compatible with ``new_value`` aggregations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5743294e4b1a55c33433176f0b84b892e0598d8df0a159b9efc26f3db420eee5)
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
            check_type(argname="argument correlated_by_fields", value=correlated_by_fields, expected_type=type_hints["correlated_by_fields"])
            check_type(argname="argument correlated_query_index", value=correlated_query_index, expected_type=type_hints["correlated_query_index"])
            check_type(argname="argument default_rule_id", value=default_rule_id, expected_type=type_hints["default_rule_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_id": rule_id,
        }
        if aggregation is not None:
            self._values["aggregation"] = aggregation
        if correlated_by_fields is not None:
            self._values["correlated_by_fields"] = correlated_by_fields
        if correlated_query_index is not None:
            self._values["correlated_query_index"] = correlated_query_index
        if default_rule_id is not None:
            self._values["default_rule_id"] = default_rule_id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def rule_id(self) -> builtins.str:
        '''Rule ID of the signal to correlate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#rule_id SecurityMonitoringRule#rule_id}
        '''
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregation(self) -> typing.Optional[builtins.str]:
        '''The aggregation type.

        For Signal Correlation rules, it must be event_count. Valid values are ``count``, ``cardinality``, ``sum``, ``max``, ``new_value``, ``geo_data``, ``event_count``, ``none``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#aggregation SecurityMonitoringRule#aggregation}
        '''
        result = self._values.get("aggregation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def correlated_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fields to correlate by.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#correlated_by_fields SecurityMonitoringRule#correlated_by_fields}
        '''
        result = self._values.get("correlated_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def correlated_query_index(self) -> typing.Optional[builtins.str]:
        '''Index of the rule query used to retrieve the correlated field.

        An empty string applies correlation on the non-projected per query attributes of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#correlated_query_index SecurityMonitoringRule#correlated_query_index}
        '''
        result = self._values.get("correlated_query_index")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_rule_id(self) -> typing.Optional[builtins.str]:
        '''Default Rule ID of the signal to correlate. This value is READ-ONLY.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#default_rule_id SecurityMonitoringRule#default_rule_id}
        '''
        result = self._values.get("default_rule_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the query. Not compatible with ``new_value`` aggregations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleSignalQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleSignalQueryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleSignalQueryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47e4d9a596a9a64276ea4b37ff7a6b9ea933e05fb44c68281af46073d07648d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SecurityMonitoringRuleSignalQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f5c78ceeb96a0b92349100b5df57e631dce14f4cf478de258e4b65342742d3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleSignalQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b1da958c1f9608647e98818849d162a19e35be99fcbd2335cb325290c1675ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__92a10b669fd27b35526981725688382ce29c73efdd1b21321ea24019ca4adde5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d72ca1371553ea67aba2d44432cfe02c44914ce410eaf0033e8871e31fd42ea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleSignalQuery]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleSignalQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleSignalQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dcd5ebedd895972f0eb8a5820965e9eea8dd8ccb96a6c1542c0608039043c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleSignalQueryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleSignalQueryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66932dfde47cb02b222a810d2b094aef7ac21793c32850ba127273d12e32fe5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAggregation")
    def reset_aggregation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregation", []))

    @jsii.member(jsii_name="resetCorrelatedByFields")
    def reset_correlated_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorrelatedByFields", []))

    @jsii.member(jsii_name="resetCorrelatedQueryIndex")
    def reset_correlated_query_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorrelatedQueryIndex", []))

    @jsii.member(jsii_name="resetDefaultRuleId")
    def reset_default_rule_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRuleId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationInput")
    def aggregation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationInput"))

    @builtins.property
    @jsii.member(jsii_name="correlatedByFieldsInput")
    def correlated_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "correlatedByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="correlatedQueryIndexInput")
    def correlated_query_index_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "correlatedQueryIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRuleIdInput")
    def default_rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRuleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleIdInput")
    def rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregation")
    def aggregation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregation"))

    @aggregation.setter
    def aggregation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e168337a66b11e8810175b5f10c7dfbb29bad53575af5e8f22e006e41634db9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregation", value)

    @builtins.property
    @jsii.member(jsii_name="correlatedByFields")
    def correlated_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "correlatedByFields"))

    @correlated_by_fields.setter
    def correlated_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f68035121f277f842862175a8ee304184427756bcbccffef4898af7fe107aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "correlatedByFields", value)

    @builtins.property
    @jsii.member(jsii_name="correlatedQueryIndex")
    def correlated_query_index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "correlatedQueryIndex"))

    @correlated_query_index.setter
    def correlated_query_index(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2005cef70befb3d867332925363c4cb2347d8903e8ae3d33ab05eba918678fff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "correlatedQueryIndex", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRuleId")
    def default_rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRuleId"))

    @default_rule_id.setter
    def default_rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7231ad6c363053d99416f4e445f268caf9ea2bb2263be7ff04ef9b7f852d68c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRuleId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c55867819610388d2310d8fd7eea0db0c3f12d56812c9da402ce7264a1a60c73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleId")
    def rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleId"))

    @rule_id.setter
    def rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca7526e1a5243d15405886f916a59495fa004e93506992d6f1ea30a864dd97f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleSignalQuery, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleSignalQuery, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleSignalQuery, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c41b99f214ca089784da2186e8edc35aa613ad830cd858adb5fa8510d1b0b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SecurityMonitoringRule",
    "SecurityMonitoringRuleCase",
    "SecurityMonitoringRuleCaseList",
    "SecurityMonitoringRuleCaseOutputReference",
    "SecurityMonitoringRuleConfig",
    "SecurityMonitoringRuleFilter",
    "SecurityMonitoringRuleFilterList",
    "SecurityMonitoringRuleFilterOutputReference",
    "SecurityMonitoringRuleOptions",
    "SecurityMonitoringRuleOptionsImpossibleTravelOptions",
    "SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference",
    "SecurityMonitoringRuleOptionsNewValueOptions",
    "SecurityMonitoringRuleOptionsNewValueOptionsOutputReference",
    "SecurityMonitoringRuleOptionsOutputReference",
    "SecurityMonitoringRuleQuery",
    "SecurityMonitoringRuleQueryAgentRule",
    "SecurityMonitoringRuleQueryAgentRuleList",
    "SecurityMonitoringRuleQueryAgentRuleOutputReference",
    "SecurityMonitoringRuleQueryList",
    "SecurityMonitoringRuleQueryOutputReference",
    "SecurityMonitoringRuleSignalQuery",
    "SecurityMonitoringRuleSignalQueryList",
    "SecurityMonitoringRuleSignalQueryOutputReference",
]

publication.publish()

def _typecheckingstub__dd00fd9aa3b1f81238f3c6c2a02ca88039dd987dec551b4ad0c13a2ac7b4daf9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    case: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleCase, typing.Dict[builtins.str, typing.Any]]]],
    message: builtins.str,
    name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    has_extended_title: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[SecurityMonitoringRuleOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQuery, typing.Dict[builtins.str, typing.Any]]]]] = None,
    signal_query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleSignalQuery, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__21843d0939b295598359f0f5578991649e09292c407a39271cda5a507f412892(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleCase, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80552d55c26e24a98a10509de07dc5252b6360a31e1939f004d83f349fe9e782(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd984e93e3dcb7aac3e09285caddfe9aae641fd34dc939ae401cbb8880dc10c6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQuery, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c537a52b6f9e5a364e6fe149795cc722359e5c9b6b914d2103299f84407ced(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleSignalQuery, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c2cc02f1f7d0fb5475e36e3c668b6cf61c0b15ec4c3af9d7d0a56be5512c4b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87277a0eb4c797984073d9df088e6c2ed9b28b7b0cc7c28dfe662d38123044a1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a2dd5cb6662f9dca5b1d351daa8f8c466849f76e255425e87f469b21b63457(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a9de83be685f9029f4bcca872f228e4a5e92d32c96e5b7efc62338a598fd15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10fc9bd81d8a79f06f7e1c8dbd87aa1cfcbf5c3dcdb9f9aaf7c456062aada94f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1309c6964d89e2a817ea67920d23678803dbe78221b5ab26f28aae8b4ae3deca(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199c9a33aa378e32bc2bb89251dd5022dd0ddaa9b8cd8df3eb21dbc00c944814(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9ecb132ecadc5053f5b0553890fcdceb22f380336d4d877a920ef0e917ced6(
    *,
    status: builtins.str,
    condition: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notifications: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4af5fab296d1d42f777966673fcbd95fa7d3e2619d8e52d4799a4fcd3a7a208(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cbda2d84beedee0d00a03d8ef0a53c1462a02c111bd7f46590679aecad269f1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437227749b9563b3dd5f95d1dc25e61f01b7115799e692655b39058ce6414015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__545f10aa76750d99ba252f292b5e19f24ed1fa4aeac289d16fff1c47336dea68(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca964d384bb024430539d3d3a24b30aac2830b4a96a8fa180fb53a5d32267dd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39776ddc56626b168e9f8d69054776a0dd7b8799cbe468863fec2d7355b208cf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleCase]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d86bb77cd1501a75b429bc099ba24fb7eba40ae625c5324a558f186cc061f54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994d4e6e57e4ffb752297ba19504bbea10794ccf8e8e154b74c98d9ee69e314c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f6ad45a76cfe0dc0f49f0d11bbc8882bb10372aac394f9221fbfd1038d4e00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6854e55505c510e4ce54300a21b3ff5e8dfc0887645758fe44ed8bbfc4018a0b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd2fa55bcad92f126a6c1244c013a7d9f55296fa1ee6104ecde0840a0e85660(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6887bad88cf805899b1ca19d8d73fd5fd666e2b1b50fb4cb4359f553adf52f44(
    value: typing.Optional[typing.Union[SecurityMonitoringRuleCase, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11fb48eb81a5c88e4dd36e60d914b894a63e04642134d6e62d2337bdb1639ab1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    case: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleCase, typing.Dict[builtins.str, typing.Any]]]],
    message: builtins.str,
    name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    has_extended_title: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[SecurityMonitoringRuleOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQuery, typing.Dict[builtins.str, typing.Any]]]]] = None,
    signal_query: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleSignalQuery, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c866bf17fbaa97751b321daaeb1d7870b2fbcfdf8bdcc285606da3317f7f0ab(
    *,
    action: builtins.str,
    query: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab69056cae7741c2e697d9329dc282917ed499775aff5504caf3113ac9e1bd25(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665044e86f49b6fd5262c7e90cc228cd1cc96c7e1f443e824f0339e7b4f47a2f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d484b7eb5784c420a0e8b96501c0dd8c92be0df59c7c5225e8eb3a0d022f5dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d44a13aec1c9f29530bf63924dac276252659e2afc9c4e26edc9e097a0de064(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da15a1014b2ae46501d264d5c96a59982599e3479caa42a79f979a1c0799de16(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3892322b9369dc6f69dca4113fc31ce3def6cf1915a5acfd6e9710b91cf53e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71da086c92642ab7ca0d19c8840df1e48913064bc5776012cb51ebf341c2fb7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91d756d1cdc4ed79c7bf9934e614b2c85d7f411cd200c460c25378b12af7f15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf96323ee437d82fa7635b69244cde1bc85b65b309eec059370a8f33ed509c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7110dd4b72ee63f8fb0bce1b6ddb59d1dfbbc29907d8fcd73c9db86eaff35b6(
    value: typing.Optional[typing.Union[SecurityMonitoringRuleFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2f7bae60c86359ebc4d68c51b2be49bf8e2e753c626fd4ed979c7be28af738(
    *,
    keep_alive: jsii.Number,
    max_signal_duration: jsii.Number,
    decrease_criticality_based_on_env: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    detection_method: typing.Optional[builtins.str] = None,
    evaluation_window: typing.Optional[jsii.Number] = None,
    impossible_travel_options: typing.Optional[typing.Union[SecurityMonitoringRuleOptionsImpossibleTravelOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    new_value_options: typing.Optional[typing.Union[SecurityMonitoringRuleOptionsNewValueOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8e8b16fb596505bcc3f7b2501d629ea7f84e5e1c1058ae18d30c78bbb47df6(
    *,
    baseline_user_locations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccadaaf759975edee0db51c47993d98b54459e2c30d80cca992cb809cf572c70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2db6f8adfdd0ffd6d51a531490b61b321bb3ac5492060f7b77527f0bdb4f3025(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f264f2cedb634c2324a2e53547d34c219c7466438ecef62ca60424e196c88e(
    value: typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__549e4b89e82ed8c6c587a2adffb2382abe55bfe4e244c06f7bf7db9e55b21148(
    *,
    forget_after: jsii.Number,
    learning_duration: typing.Optional[jsii.Number] = None,
    learning_method: typing.Optional[builtins.str] = None,
    learning_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9e766c6abd7205ec9c5f682274f0ba3d897190a2c1c6bf9f4139b6b5381c69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb0b1c0e668079de485fb3ef35e45b5b8270e3b36ff031b70638e57d4e9e7b9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a39ba61c48fcc577b4d1c3560fa725786d2bd05ccb8eb6a919c94390c9b7859(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ff9a903552abd7ba112dc2475f5549a2f4e7cede9c1e56c1d847b088f5254a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a348d958a114a6e226ae9d68990b653669b14280fc2bf97735332be9c0cd2a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4888d3185d053f71f6a2d215f6771c04dae7078d79f722970a65e88bfb32da8c(
    value: typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a178de098c7dcea33300fc4c4cd6422bfea963ce52b6ae2316c8d045527671(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb8f3e31ed788579fcaedfb79d4a649cc04134da4368430e309ad95bfc88b7b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4917ef6954206b2b9e24a56823c0f54888225db2a3b34da20cd3be46c7955f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__084fb9d16bea45464790711a1e22a60de6f10e47f10b06a435a70044d9898b71(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0a97acd18d55bf7c7ba0abe5a84a7cdae9d3e150ae9ea9ed7488bba8f032ea(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5089c54f3899b05b452ce2f0a7ca9b64d5ffc60f719911e05dcd0dcf824ea1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dcf2674869388a8307dfcbcedb34156418c7243b113bbb814c22da4c7d00642(
    value: typing.Optional[SecurityMonitoringRuleOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8f570b0171354820639da7d8575f7c19be01bb17e683a3669127e02c739aca(
    *,
    query: builtins.str,
    agent_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQueryAgentRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    aggregation: typing.Optional[builtins.str] = None,
    distinct_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    metric: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdfe13239dc740bfb832b869018ed53be671f89aeff0fa0f0b7503c00a5e055d(
    *,
    agent_rule_id: builtins.str,
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd8f076131df53fcff1edd65213177e7d36e440f62f61c60ebad2fca5da9429(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004245166e93b36b2b71d68aae9e7f25f6d6dcd21d0a21f9749f93615329f9ff(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6939439239ee603522d33490603a5496c6e75e553488f7f45f39f6b3157770b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e99f6bc42a94deb02bc3310de93246f8ee3d8015451c677a0befcd9a61c53b8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860f91d086f2a07fa25d818d06be120c2f178bf7513567a93582ae5e8c91b221(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1533ae880f7716765c3118eaa8ad178ad75f6bccfd9e4ec4be775c59aac92884(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__336d1f1607e88e3ffacb852af0bfa6603f01229396b748992c696cbb91910c0d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910dd2ecaa77048a39a2b96e33c82833407b8c845029204b220be5a9b54be967(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee98199254a17fe67dbb708e86bfc679a2cd085162cfe080f8e4bc01e175607(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa683c94fdf04993a4599dc98f4826d68a6a9cceaa929a0843a9f8a556038b4a(
    value: typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65366874071e6644bf8a0e7e80a0c0e2f7c31f724ec2b9b15992f0a689d3cf49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffdd383854bde9a20c6ab03af8b31f59381462522dbab803f7a9b970059ad33(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2311baf1e6a56be9912434967728a6c5d5ac470219f08eca5bb461ff5d1186c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6beda91c6822ba8533c22a7b7d766f69328148e370c815e81743b1c5c8f5b677(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9530b7f37c6a73545b3c960afe5b757c6298b335839e5ea4102c45edf7f9289(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__254a1c6494eb5015f046fb8bcc3e27ad830879f52605ef917ba4dd35ae1dd1a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleQuery]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1065e8519613430d858e54084b0ff442e93d967b0a385ecbf87abc6475ea0a0f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb99df23d35551417fb951e7d92f33e9762c412833a9a006bdb89f09b9d45922(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQueryAgentRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a03545b69d06f203d06f54ecb58fee4362b42882cadb2d8ba0ecf3f06a553f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ac1fc36bb840bf105e1ad56581a9f835b50f82d9a4725cf1d80d8ca9ef6a185(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c276cef0c4f93b80c4651687330aef0e1bee295bd1613b5bd178159424f6f0d8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a7c5122401386e2ea1c4cf6e0586ac32aae456ad0d078e58ebc5f366b1c39e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6aeaedb3bd88cb7041e050e1e8fa5ace8631356747fe3798eb543aa4cc5a752(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e833cf6cddeb31b26bd7ec1d3e956b2c9707add05c561538e7c082ce1f1421(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a4e9f218256f994b0e53d9e273cbd62e4836f21dea46900da60df2bb25b99c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06fa9516f8b3aa9bbcb1c102402341f477a1f8ee0dba6edeadf86e229076c2a(
    value: typing.Optional[typing.Union[SecurityMonitoringRuleQuery, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5743294e4b1a55c33433176f0b84b892e0598d8df0a159b9efc26f3db420eee5(
    *,
    rule_id: builtins.str,
    aggregation: typing.Optional[builtins.str] = None,
    correlated_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    correlated_query_index: typing.Optional[builtins.str] = None,
    default_rule_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47e4d9a596a9a64276ea4b37ff7a6b9ea933e05fb44c68281af46073d07648d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f5c78ceeb96a0b92349100b5df57e631dce14f4cf478de258e4b65342742d3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1da958c1f9608647e98818849d162a19e35be99fcbd2335cb325290c1675ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a10b669fd27b35526981725688382ce29c73efdd1b21321ea24019ca4adde5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d72ca1371553ea67aba2d44432cfe02c44914ce410eaf0033e8871e31fd42ea6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dcd5ebedd895972f0eb8a5820965e9eea8dd8ccb96a6c1542c0608039043c67(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SecurityMonitoringRuleSignalQuery]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66932dfde47cb02b222a810d2b094aef7ac21793c32850ba127273d12e32fe5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e168337a66b11e8810175b5f10c7dfbb29bad53575af5e8f22e006e41634db9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f68035121f277f842862175a8ee304184427756bcbccffef4898af7fe107aa0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2005cef70befb3d867332925363c4cb2347d8903e8ae3d33ab05eba918678fff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7231ad6c363053d99416f4e445f268caf9ea2bb2263be7ff04ef9b7f852d68c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55867819610388d2310d8fd7eea0db0c3f12d56812c9da402ce7264a1a60c73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca7526e1a5243d15405886f916a59495fa004e93506992d6f1ea30a864dd97f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c41b99f214ca089784da2186e8edc35aa613ad830cd858adb5fa8510d1b0b2(
    value: typing.Optional[typing.Union[SecurityMonitoringRuleSignalQuery, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
