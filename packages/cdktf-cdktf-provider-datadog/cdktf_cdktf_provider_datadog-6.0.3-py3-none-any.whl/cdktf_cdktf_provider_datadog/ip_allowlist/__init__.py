'''
# `datadog_ip_allowlist`

Refer to the Terraform Registory for docs: [`datadog_ip_allowlist`](https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist).
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


class IpAllowlist(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.ipAllowlist.IpAllowlist",
):
    '''Represents a {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist datadog_ip_allowlist}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        entry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IpAllowlistEntry", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist datadog_ip_allowlist} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param enabled: Whether the IP Allowlist is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#enabled IpAllowlist#enabled}
        :param entry: entry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#entry IpAllowlist#entry}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#id IpAllowlist#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a06fa955715535b5140c71ed2711b9daa69243c0280e86ab106b0d7fd06ae61)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IpAllowlistConfig(
            enabled=enabled,
            entry=entry,
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

    @jsii.member(jsii_name="putEntry")
    def put_entry(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IpAllowlistEntry", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9789b97d276bcabd7c1299a9f0d47db13dcc23e1bc811bd32433a5da43b1810)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntry", [value]))

    @jsii.member(jsii_name="resetEntry")
    def reset_entry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntry", []))

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
    @jsii.member(jsii_name="entry")
    def entry(self) -> "IpAllowlistEntryList":
        return typing.cast("IpAllowlistEntryList", jsii.get(self, "entry"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="entryInput")
    def entry_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IpAllowlistEntry"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IpAllowlistEntry"]]], jsii.get(self, "entryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__cfc26adfda09c3dfc91b133d4c763d485dd68ed595383e43f5de9ae7fff75d0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de39619488cfdbcc15e87c114b36ae8f5eba8de763936b3933bd21f566454a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.ipAllowlist.IpAllowlistConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "enabled": "enabled",
        "entry": "entry",
        "id": "id",
    },
)
class IpAllowlistConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        entry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IpAllowlistEntry", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param enabled: Whether the IP Allowlist is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#enabled IpAllowlist#enabled}
        :param entry: entry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#entry IpAllowlist#entry}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#id IpAllowlist#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__148f80245e58ef38722e9bce33028dcc676d270ae821a0d300febe6dc3b87b82)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
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
        if entry is not None:
            self._values["entry"] = entry
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
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether the IP Allowlist is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#enabled IpAllowlist#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def entry(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IpAllowlistEntry"]]]:
        '''entry block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#entry IpAllowlist#entry}
        '''
        result = self._values.get("entry")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IpAllowlistEntry"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#id IpAllowlist#id}.

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
        return "IpAllowlistConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.ipAllowlist.IpAllowlistEntry",
    jsii_struct_bases=[],
    name_mapping={"cidr_block": "cidrBlock", "note": "note"},
)
class IpAllowlistEntry:
    def __init__(
        self,
        *,
        cidr_block: builtins.str,
        note: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cidr_block: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#cidr_block IpAllowlist#cidr_block}.
        :param note: Note accompanying IP address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#note IpAllowlist#note}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed1775e3262bafba154f69db144d128952916a84fc430355f70e08430a2b267f)
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument note", value=note, expected_type=type_hints["note"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr_block": cidr_block,
        }
        if note is not None:
            self._values["note"] = note

    @builtins.property
    def cidr_block(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#cidr_block IpAllowlist#cidr_block}.'''
        result = self._values.get("cidr_block")
        assert result is not None, "Required property 'cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def note(self) -> typing.Optional[builtins.str]:
        '''Note accompanying IP address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/datadog/datadog/3.25.0/docs/resources/ip_allowlist#note IpAllowlist#note}
        '''
        result = self._values.get("note")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpAllowlistEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IpAllowlistEntryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.ipAllowlist.IpAllowlistEntryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18a8e3ea244890c8288b608f22a79bd256322a59734fa6160df0fba25fcc7f75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IpAllowlistEntryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__973844b4acfabdcaf2728aaa9076df3e328e49c177edc0f00e5db6b96a4803df)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IpAllowlistEntryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044ddf7d0f29ae24c88d0ff84437c1daaee88f0eec166769b0db65fe8a8bfc18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e02ed7eca1e245e138dd48e6e9a0f2e4eb1ae14373563a5a09f0c475d724567)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1603e4035d79576cf74e85d7cae2b69d1b85906af85982d42e55a6efb9e14de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IpAllowlistEntry]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IpAllowlistEntry]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IpAllowlistEntry]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c183d3b6a275ac861c9edf121cd7cc232f5c92dadfe31a21777192890bdb4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IpAllowlistEntryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.ipAllowlist.IpAllowlistEntryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebbc2477c53e94c678e2e702fbab482bd53db9c0f3aeb053376144dd8d44e760)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNote")
    def reset_note(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNote", []))

    @builtins.property
    @jsii.member(jsii_name="cidrBlockInput")
    def cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="noteInput")
    def note_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrBlock"))

    @cidr_block.setter
    def cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a1d1602536b13bf28b57ff0e4b41711b97a73061623bd6cea7cf9f7952cd26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="note")
    def note(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "note"))

    @note.setter
    def note(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc3c1c5147af9bb5bc40b5a71c54dce537248f5815f2068610bccabbde7715c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "note", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IpAllowlistEntry, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IpAllowlistEntry, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IpAllowlistEntry, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c86c585a8282f0bb83f4c03cccb9e206c14b6c4fee8706ef0556bde78a61d08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IpAllowlist",
    "IpAllowlistConfig",
    "IpAllowlistEntry",
    "IpAllowlistEntryList",
    "IpAllowlistEntryOutputReference",
]

publication.publish()

def _typecheckingstub__3a06fa955715535b5140c71ed2711b9daa69243c0280e86ab106b0d7fd06ae61(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    entry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IpAllowlistEntry, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__c9789b97d276bcabd7c1299a9f0d47db13dcc23e1bc811bd32433a5da43b1810(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IpAllowlistEntry, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc26adfda09c3dfc91b133d4c763d485dd68ed595383e43f5de9ae7fff75d0e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de39619488cfdbcc15e87c114b36ae8f5eba8de763936b3933bd21f566454a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__148f80245e58ef38722e9bce33028dcc676d270ae821a0d300febe6dc3b87b82(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    entry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IpAllowlistEntry, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1775e3262bafba154f69db144d128952916a84fc430355f70e08430a2b267f(
    *,
    cidr_block: builtins.str,
    note: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a8e3ea244890c8288b608f22a79bd256322a59734fa6160df0fba25fcc7f75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__973844b4acfabdcaf2728aaa9076df3e328e49c177edc0f00e5db6b96a4803df(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044ddf7d0f29ae24c88d0ff84437c1daaee88f0eec166769b0db65fe8a8bfc18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e02ed7eca1e245e138dd48e6e9a0f2e4eb1ae14373563a5a09f0c475d724567(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1603e4035d79576cf74e85d7cae2b69d1b85906af85982d42e55a6efb9e14de(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c183d3b6a275ac861c9edf121cd7cc232f5c92dadfe31a21777192890bdb4b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IpAllowlistEntry]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebbc2477c53e94c678e2e702fbab482bd53db9c0f3aeb053376144dd8d44e760(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a1d1602536b13bf28b57ff0e4b41711b97a73061623bd6cea7cf9f7952cd26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc3c1c5147af9bb5bc40b5a71c54dce537248f5815f2068610bccabbde7715c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c86c585a8282f0bb83f4c03cccb9e206c14b6c4fee8706ef0556bde78a61d08(
    value: typing.Optional[typing.Union[IpAllowlistEntry, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
