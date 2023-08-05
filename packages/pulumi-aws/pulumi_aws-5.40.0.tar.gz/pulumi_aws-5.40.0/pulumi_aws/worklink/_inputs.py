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
    'FleetIdentityProviderArgs',
    'FleetNetworkArgs',
]

@pulumi.input_type
class FleetIdentityProviderArgs:
    def __init__(__self__, *,
                 saml_metadata: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] saml_metadata: The SAML metadata document provided by the customer’s identity provider.
        :param pulumi.Input[str] type: The type of identity provider.
        """
        pulumi.set(__self__, "saml_metadata", saml_metadata)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="samlMetadata")
    def saml_metadata(self) -> pulumi.Input[str]:
        """
        The SAML metadata document provided by the customer’s identity provider.
        """
        return pulumi.get(self, "saml_metadata")

    @saml_metadata.setter
    def saml_metadata(self, value: pulumi.Input[str]):
        pulumi.set(self, "saml_metadata", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of identity provider.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class FleetNetworkArgs:
    def __init__(__self__, *,
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs associated with access to the provided subnets.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.
        :param pulumi.Input[str] vpc_id: The VPC ID with connectivity to associated websites.
        """
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of security group IDs associated with access to the provided subnets.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of subnet IDs used for X-ENI connections from Amazon WorkLink rendering containers.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The VPC ID with connectivity to associated websites.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)


