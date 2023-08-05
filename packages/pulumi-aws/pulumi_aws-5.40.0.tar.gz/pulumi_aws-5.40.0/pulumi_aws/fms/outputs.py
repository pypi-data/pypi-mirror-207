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
    'PolicyExcludeMap',
    'PolicyIncludeMap',
    'PolicySecurityServicePolicyData',
]

@pulumi.output_type
class PolicyExcludeMap(dict):
    def __init__(__self__, *,
                 accounts: Optional[Sequence[str]] = None,
                 orgunits: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] accounts: A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        :param Sequence[str] orgunits: A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if orgunits is not None:
            pulumi.set(__self__, "orgunits", orgunits)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[str]]:
        """
        A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def orgunits(self) -> Optional[Sequence[str]]:
        """
        A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        return pulumi.get(self, "orgunits")


@pulumi.output_type
class PolicyIncludeMap(dict):
    def __init__(__self__, *,
                 accounts: Optional[Sequence[str]] = None,
                 orgunits: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] accounts: A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        :param Sequence[str] orgunits: A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if orgunits is not None:
            pulumi.set(__self__, "orgunits", orgunits)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[str]]:
        """
        A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def orgunits(self) -> Optional[Sequence[str]]:
        """
        A list of IDs of the AWS Organizational Units that you want to include for this AWS FMS Policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
        """
        return pulumi.get(self, "orgunits")


@pulumi.output_type
class PolicySecurityServicePolicyData(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "managedServiceData":
            suggest = "managed_service_data"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicySecurityServicePolicyData. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicySecurityServicePolicyData.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicySecurityServicePolicyData.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 managed_service_data: Optional[str] = None):
        """
        :param str type: The service that the policy is using to protect the resources. For the current list of supported types, please refer to the [AWS Firewall Manager SecurityServicePolicyData API Type Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html#fms-Type-SecurityServicePolicyData-Type).
        :param str managed_service_data: Details about the service that are specific to the service type, in JSON format. For service type `SHIELD_ADVANCED`, this is an empty string. Examples depending on `type` can be found in the [AWS Firewall Manager SecurityServicePolicyData API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html).
        """
        pulumi.set(__self__, "type", type)
        if managed_service_data is not None:
            pulumi.set(__self__, "managed_service_data", managed_service_data)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The service that the policy is using to protect the resources. For the current list of supported types, please refer to the [AWS Firewall Manager SecurityServicePolicyData API Type Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html#fms-Type-SecurityServicePolicyData-Type).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="managedServiceData")
    def managed_service_data(self) -> Optional[str]:
        """
        Details about the service that are specific to the service type, in JSON format. For service type `SHIELD_ADVANCED`, this is an empty string. Examples depending on `type` can be found in the [AWS Firewall Manager SecurityServicePolicyData API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html).
        """
        return pulumi.get(self, "managed_service_data")


