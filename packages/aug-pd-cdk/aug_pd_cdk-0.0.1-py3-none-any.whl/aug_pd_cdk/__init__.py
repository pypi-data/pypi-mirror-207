'''
# replace this
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

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_apigateway as _aws_cdk_aws_apigateway_ceddda9d
import aws_cdk.aws_dynamodb as _aws_cdk_aws_dynamodb_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import constructs as _constructs_77d1e7e8


class Service(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aug-pd-ckd.Service",
):
    def __init__(
        self,
        scope: _aws_cdk_ceddda9d.Stack,
        id: builtins.str,
        *,
        code_directory: builtins.str,
        table_props: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.TableProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param code_directory: 
        :param table_props: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa0c22c47380c740f428aa2bf1c162409fcc162321da3832ccf33ae1e18e2c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServiceProps(code_directory=code_directory, table_props=table_props)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> _aws_cdk_aws_lambda_ceddda9d.Function:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.Function, jsii.get(self, "function"))

    @function.setter
    def function(self, value: _aws_cdk_aws_lambda_ceddda9d.Function) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6df542a17c5719d8e22786c17260aa893391d40925b953df4c057b8174251ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "function", value)

    @builtins.property
    @jsii.member(jsii_name="restApi")
    def rest_api(self) -> _aws_cdk_aws_apigateway_ceddda9d.LambdaRestApi:
        return typing.cast(_aws_cdk_aws_apigateway_ceddda9d.LambdaRestApi, jsii.get(self, "restApi"))

    @rest_api.setter
    def rest_api(self, value: _aws_cdk_aws_apigateway_ceddda9d.LambdaRestApi) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc31cbc2e997bee941e6d6881251c8f0eb3b6203ea72945f392d3c5e3a7f8c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restApi", value)

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Table]:
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Table], jsii.get(self, "table"))

    @table.setter
    def table(
        self,
        value: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Table],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df1658bfae2abba4319ed90f66f3d82c4730afca0c89a142cfe0344c393db02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)


@jsii.data_type(
    jsii_type="aug-pd-ckd.ServiceProps",
    jsii_struct_bases=[],
    name_mapping={"code_directory": "codeDirectory", "table_props": "tableProps"},
)
class ServiceProps:
    def __init__(
        self,
        *,
        code_directory: builtins.str,
        table_props: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.TableProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param code_directory: 
        :param table_props: 
        '''
        if isinstance(table_props, dict):
            table_props = _aws_cdk_aws_dynamodb_ceddda9d.TableProps(**table_props)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c95a32645c3d883e4322a55163b9d2942bf0272b571e85ca85dd09d98750e405)
            check_type(argname="argument code_directory", value=code_directory, expected_type=type_hints["code_directory"])
            check_type(argname="argument table_props", value=table_props, expected_type=type_hints["table_props"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_directory": code_directory,
        }
        if table_props is not None:
            self._values["table_props"] = table_props

    @builtins.property
    def code_directory(self) -> builtins.str:
        result = self._values.get("code_directory")
        assert result is not None, "Required property 'code_directory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_props(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableProps]:
        result = self._values.get("table_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Service",
    "ServiceProps",
]

publication.publish()

def _typecheckingstub__afa0c22c47380c740f428aa2bf1c162409fcc162321da3832ccf33ae1e18e2c0(
    scope: _aws_cdk_ceddda9d.Stack,
    id: builtins.str,
    *,
    code_directory: builtins.str,
    table_props: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.TableProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6df542a17c5719d8e22786c17260aa893391d40925b953df4c057b8174251ce(
    value: _aws_cdk_aws_lambda_ceddda9d.Function,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc31cbc2e997bee941e6d6881251c8f0eb3b6203ea72945f392d3c5e3a7f8c5b(
    value: _aws_cdk_aws_apigateway_ceddda9d.LambdaRestApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df1658bfae2abba4319ed90f66f3d82c4730afca0c89a142cfe0344c393db02(
    value: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Table],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c95a32645c3d883e4322a55163b9d2942bf0272b571e85ca85dd09d98750e405(
    *,
    code_directory: builtins.str,
    table_props: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.TableProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
