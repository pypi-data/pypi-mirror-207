# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._enums import *

__all__ = [
    'GetAmiBlockDeviceMappingResult',
    'GetAmiFilterResult',
    'GetAmiIdsFilterResult',
    'GetAmiProductCodeResult',
    'GetAutoscalingGroupsFilterResult',
    'GetAvailabilityZoneFilterResult',
    'GetAvailabilityZonesFilterResult',
    'GetElasticIpFilterResult',
    'GetPrefixListFilterResult',
    'GetRegionsFilterResult',
]

@pulumi.output_type
class GetAmiBlockDeviceMappingResult(dict):
    def __init__(__self__, *,
                 device_name: str,
                 ebs: Mapping[str, str],
                 no_device: str,
                 virtual_name: str):
        """
        :param str device_name: Physical name of the device.
        :param Mapping[str, str] ebs: Map containing EBS information, if the device is EBS based. Unlike most object attributes, these are accessed directly (e.g., `ebs.volume_size` or `ebs["volume_size"]`) rather than accessed through the first element of a list (e.g., `ebs[0].volume_size`).
        :param str no_device: Suppresses the specified device included in the block device mapping of the AMI.
        :param str virtual_name: Virtual device name (for instance stores).
        """
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "ebs", ebs)
        pulumi.set(__self__, "no_device", no_device)
        pulumi.set(__self__, "virtual_name", virtual_name)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> str:
        """
        Physical name of the device.
        """
        return pulumi.get(self, "device_name")

    @property
    @pulumi.getter
    def ebs(self) -> Mapping[str, str]:
        """
        Map containing EBS information, if the device is EBS based. Unlike most object attributes, these are accessed directly (e.g., `ebs.volume_size` or `ebs["volume_size"]`) rather than accessed through the first element of a list (e.g., `ebs[0].volume_size`).
        """
        return pulumi.get(self, "ebs")

    @property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> str:
        """
        Suppresses the specified device included in the block device mapping of the AMI.
        """
        return pulumi.get(self, "no_device")

    @property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> str:
        """
        Virtual device name (for instance stores).
        """
        return pulumi.get(self, "virtual_name")


@pulumi.output_type
class GetAmiFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the AMI that was provided during image creation.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the AMI that was provided during image creation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GetAmiIdsFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GetAmiProductCodeResult(dict):
    def __init__(__self__, *,
                 product_code_id: str,
                 product_code_type: str):
        pulumi.set(__self__, "product_code_id", product_code_id)
        pulumi.set(__self__, "product_code_type", product_code_type)

    @property
    @pulumi.getter(name="productCodeId")
    def product_code_id(self) -> str:
        return pulumi.get(self, "product_code_id")

    @property
    @pulumi.getter(name="productCodeType")
    def product_code_type(self) -> str:
        return pulumi.get(self, "product_code_type")


@pulumi.output_type
class GetAutoscalingGroupsFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the DescribeAutoScalingGroup filter. The recommended values are: `tag-key`, `tag-value`, and `tag:<tag name>`
        :param Sequence[str] values: Value of the filter.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the DescribeAutoScalingGroup filter. The recommended values are: `tag-key`, `tag-value`, and `tag:<tag name>`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Value of the filter.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetAvailabilityZoneFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
        :param Sequence[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetAvailabilityZonesFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
        :param Sequence[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetElasticIpFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GetPrefixListFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the filter field. Valid values can be found in the [EC2 DescribePrefixLists API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html).
        :param Sequence[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter field. Valid values can be found in the [EC2 DescribePrefixLists API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetRegionsFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the filter field. Valid values can be found in the [describe-regions AWS CLI Reference][1].
        :param Sequence[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter field. Valid values can be found in the [describe-regions AWS CLI Reference][1].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        return pulumi.get(self, "values")


