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

__all__ = [
    'GetProxyResult',
    'AwaitableGetProxyResult',
    'get_proxy',
    'get_proxy_output',
]

@pulumi.output_type
class GetProxyResult:
    """
    A collection of values returned by getProxy.
    """
    def __init__(__self__, arn=None, auths=None, debug_logging=None, endpoint=None, engine_family=None, id=None, idle_client_timeout=None, name=None, require_tls=None, role_arn=None, vpc_id=None, vpc_security_group_ids=None, vpc_subnet_ids=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auths and not isinstance(auths, list):
            raise TypeError("Expected argument 'auths' to be a list")
        pulumi.set(__self__, "auths", auths)
        if debug_logging and not isinstance(debug_logging, bool):
            raise TypeError("Expected argument 'debug_logging' to be a bool")
        pulumi.set(__self__, "debug_logging", debug_logging)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if engine_family and not isinstance(engine_family, str):
            raise TypeError("Expected argument 'engine_family' to be a str")
        pulumi.set(__self__, "engine_family", engine_family)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idle_client_timeout and not isinstance(idle_client_timeout, int):
            raise TypeError("Expected argument 'idle_client_timeout' to be a int")
        pulumi.set(__self__, "idle_client_timeout", idle_client_timeout)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if require_tls and not isinstance(require_tls, bool):
            raise TypeError("Expected argument 'require_tls' to be a bool")
        pulumi.set(__self__, "require_tls", require_tls)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError("Expected argument 'vpc_security_group_ids' to be a list")
        pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)
        if vpc_subnet_ids and not isinstance(vpc_subnet_ids, list):
            raise TypeError("Expected argument 'vpc_subnet_ids' to be a list")
        pulumi.set(__self__, "vpc_subnet_ids", vpc_subnet_ids)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the DB Proxy.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def auths(self) -> Sequence['outputs.GetProxyAuthResult']:
        """
        Configuration(s) with authorization mechanisms to connect to the associated instance or cluster.
        """
        return pulumi.get(self, "auths")

    @property
    @pulumi.getter(name="debugLogging")
    def debug_logging(self) -> bool:
        """
        Whether the proxy includes detailed information about SQL statements in its logs.
        """
        return pulumi.get(self, "debug_logging")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Endpoint that you can use to connect to the DB proxy.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="engineFamily")
    def engine_family(self) -> str:
        """
        Kinds of databases that the proxy can connect to.
        """
        return pulumi.get(self, "engine_family")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idleClientTimeout")
    def idle_client_timeout(self) -> int:
        """
        Number of seconds a connection to the proxy can have no activity before the proxy drops the client connection.
        """
        return pulumi.get(self, "idle_client_timeout")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> bool:
        """
        Whether Transport Layer Security (TLS) encryption is required for connections to the proxy.
        """
        return pulumi.get(self, "require_tls")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        ARN for the IAM role that the proxy uses to access Amazon Secrets Manager.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        Provides the VPC ID of the DB proxy.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Sequence[str]:
        """
        Provides a list of VPC security groups that the proxy belongs to.
        """
        return pulumi.get(self, "vpc_security_group_ids")

    @property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> Sequence[str]:
        """
        EC2 subnet IDs for the proxy.
        """
        return pulumi.get(self, "vpc_subnet_ids")


class AwaitableGetProxyResult(GetProxyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProxyResult(
            arn=self.arn,
            auths=self.auths,
            debug_logging=self.debug_logging,
            endpoint=self.endpoint,
            engine_family=self.engine_family,
            id=self.id,
            idle_client_timeout=self.idle_client_timeout,
            name=self.name,
            require_tls=self.require_tls,
            role_arn=self.role_arn,
            vpc_id=self.vpc_id,
            vpc_security_group_ids=self.vpc_security_group_ids,
            vpc_subnet_ids=self.vpc_subnet_ids)


def get_proxy(name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProxyResult:
    """
    Use this data source to get information about a DB Proxy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    proxy = aws.rds.get_proxy(name="my-test-db-proxy")
    ```


    :param str name: Name of the DB proxy.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:rds/getProxy:getProxy', __args__, opts=opts, typ=GetProxyResult).value

    return AwaitableGetProxyResult(
        arn=__ret__.arn,
        auths=__ret__.auths,
        debug_logging=__ret__.debug_logging,
        endpoint=__ret__.endpoint,
        engine_family=__ret__.engine_family,
        id=__ret__.id,
        idle_client_timeout=__ret__.idle_client_timeout,
        name=__ret__.name,
        require_tls=__ret__.require_tls,
        role_arn=__ret__.role_arn,
        vpc_id=__ret__.vpc_id,
        vpc_security_group_ids=__ret__.vpc_security_group_ids,
        vpc_subnet_ids=__ret__.vpc_subnet_ids)


@_utilities.lift_output_func(get_proxy)
def get_proxy_output(name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProxyResult]:
    """
    Use this data source to get information about a DB Proxy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    proxy = aws.rds.get_proxy(name="my-test-db-proxy")
    ```


    :param str name: Name of the DB proxy.
    """
    ...
