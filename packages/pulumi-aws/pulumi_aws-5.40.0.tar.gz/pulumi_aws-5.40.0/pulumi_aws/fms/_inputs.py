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
    'PolicyExcludeMapArgs',
    'PolicyIncludeMapArgs',
    'PolicySecurityServicePolicyDataArgs',
]

@pulumi.input_type
class PolicyExcludeMapArgs:
    def __init__(__self__, *,
                 accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 orgunits: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] accounts: A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] orgunits: A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if orgunits is not None:
            pulumi.set(__self__, "orgunits", orgunits)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter
    def orgunits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        return pulumi.get(self, "orgunits")

    @orgunits.setter
    def orgunits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "orgunits", value)


@pulumi.input_type
class PolicyIncludeMapArgs:
    def __init__(__self__, *,
                 accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 orgunits: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] accounts: A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] orgunits: A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if orgunits is not None:
            pulumi.set(__self__, "orgunits", orgunits)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter
    def orgunits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        return pulumi.get(self, "orgunits")

    @orgunits.setter
    def orgunits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "orgunits", value)


@pulumi.input_type
class PolicySecurityServicePolicyDataArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 managed_service_data: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The service that the policy is using to protect the resources. For the current list of supported types, please refer to the [AWS Firewall Manager SecurityServicePolicyData API Type Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html#fms-Type-SecurityServicePolicyData-Type).
        :param pulumi.Input[str] managed_service_data: Details about the service that are specific to the service type, in JSON format. For service type `SHIELD_ADVANCED`, this is an empty string. Examples depending on `type` can be found in the [AWS Firewall Manager SecurityServicePolicyData API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html).
        """
        pulumi.set(__self__, "type", type)
        if managed_service_data is not None:
            pulumi.set(__self__, "managed_service_data", managed_service_data)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The service that the policy is using to protect the resources. For the current list of supported types, please refer to the [AWS Firewall Manager SecurityServicePolicyData API Type Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html#fms-Type-SecurityServicePolicyData-Type).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="managedServiceData")
    def managed_service_data(self) -> Optional[pulumi.Input[str]]:
        """
        Details about the service that are specific to the service type, in JSON format. For service type `SHIELD_ADVANCED`, this is an empty string. Examples depending on `type` can be found in the [AWS Firewall Manager SecurityServicePolicyData API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html).
        """
        return pulumi.get(self, "managed_service_data")

    @managed_service_data.setter
    def managed_service_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_service_data", value)


