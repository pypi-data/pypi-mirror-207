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
from ._inputs import *

__all__ = [
    'GetSpotPriceResult',
    'AwaitableGetSpotPriceResult',
    'get_spot_price',
    'get_spot_price_output',
]

@pulumi.output_type
class GetSpotPriceResult:
    """
    A collection of values returned by getSpotPrice.
    """
    def __init__(__self__, availability_zone=None, filters=None, id=None, instance_type=None, spot_price=None, spot_price_timestamp=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if spot_price and not isinstance(spot_price, str):
            raise TypeError("Expected argument 'spot_price' to be a str")
        pulumi.set(__self__, "spot_price", spot_price)
        if spot_price_timestamp and not isinstance(spot_price_timestamp, str):
            raise TypeError("Expected argument 'spot_price_timestamp' to be a str")
        pulumi.set(__self__, "spot_price_timestamp", spot_price_timestamp)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSpotPriceFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> str:
        """
        Most recent Spot Price value for the given instance type and AZ.
        """
        return pulumi.get(self, "spot_price")

    @property
    @pulumi.getter(name="spotPriceTimestamp")
    def spot_price_timestamp(self) -> str:
        """
        The timestamp at which the Spot Price value was published.
        """
        return pulumi.get(self, "spot_price_timestamp")


class AwaitableGetSpotPriceResult(GetSpotPriceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpotPriceResult(
            availability_zone=self.availability_zone,
            filters=self.filters,
            id=self.id,
            instance_type=self.instance_type,
            spot_price=self.spot_price,
            spot_price_timestamp=self.spot_price_timestamp)


def get_spot_price(availability_zone: Optional[str] = None,
                   filters: Optional[Sequence[pulumi.InputType['GetSpotPriceFilterArgs']]] = None,
                   instance_type: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpotPriceResult:
    """
    Information about most recent Spot Price for a given EC2 instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_spot_price(availability_zone="us-west-2a",
        filters=[aws.ec2.GetSpotPriceFilterArgs(
            name="product-description",
            values=["Linux/UNIX"],
        )],
        instance_type="t3.medium")
    ```


    :param str availability_zone: Availability zone in which to query Spot price information.
    :param Sequence[pulumi.InputType['GetSpotPriceFilterArgs']] filters: One or more configuration blocks containing name-values filters. See the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotPriceHistory.html) for supported filters. Detailed below.
    :param str instance_type: Type of instance for which to query Spot Price information.
    """
    __args__ = dict()
    __args__['availabilityZone'] = availability_zone
    __args__['filters'] = filters
    __args__['instanceType'] = instance_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ec2/getSpotPrice:getSpotPrice', __args__, opts=opts, typ=GetSpotPriceResult).value

    return AwaitableGetSpotPriceResult(
        availability_zone=__ret__.availability_zone,
        filters=__ret__.filters,
        id=__ret__.id,
        instance_type=__ret__.instance_type,
        spot_price=__ret__.spot_price,
        spot_price_timestamp=__ret__.spot_price_timestamp)


@_utilities.lift_output_func(get_spot_price)
def get_spot_price_output(availability_zone: Optional[pulumi.Input[Optional[str]]] = None,
                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSpotPriceFilterArgs']]]]] = None,
                          instance_type: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSpotPriceResult]:
    """
    Information about most recent Spot Price for a given EC2 instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_spot_price(availability_zone="us-west-2a",
        filters=[aws.ec2.GetSpotPriceFilterArgs(
            name="product-description",
            values=["Linux/UNIX"],
        )],
        instance_type="t3.medium")
    ```


    :param str availability_zone: Availability zone in which to query Spot price information.
    :param Sequence[pulumi.InputType['GetSpotPriceFilterArgs']] filters: One or more configuration blocks containing name-values filters. See the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotPriceHistory.html) for supported filters. Detailed below.
    :param str instance_type: Type of instance for which to query Spot Price information.
    """
    ...
