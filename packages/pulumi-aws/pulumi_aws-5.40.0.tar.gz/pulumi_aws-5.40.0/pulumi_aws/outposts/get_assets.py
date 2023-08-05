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
    'GetAssetsResult',
    'AwaitableGetAssetsResult',
    'get_assets',
    'get_assets_output',
]

@pulumi.output_type
class GetAssetsResult:
    """
    A collection of values returned by getAssets.
    """
    def __init__(__self__, arn=None, asset_ids=None, host_id_filters=None, id=None, status_id_filters=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if asset_ids and not isinstance(asset_ids, list):
            raise TypeError("Expected argument 'asset_ids' to be a list")
        pulumi.set(__self__, "asset_ids", asset_ids)
        if host_id_filters and not isinstance(host_id_filters, list):
            raise TypeError("Expected argument 'host_id_filters' to be a list")
        pulumi.set(__self__, "host_id_filters", host_id_filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if status_id_filters and not isinstance(status_id_filters, list):
            raise TypeError("Expected argument 'status_id_filters' to be a list")
        pulumi.set(__self__, "status_id_filters", status_id_filters)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assetIds")
    def asset_ids(self) -> Sequence[str]:
        """
        List of all the asset ids found. This data source will fail if none are found.
        """
        return pulumi.get(self, "asset_ids")

    @property
    @pulumi.getter(name="hostIdFilters")
    def host_id_filters(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "host_id_filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="statusIdFilters")
    def status_id_filters(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "status_id_filters")


class AwaitableGetAssetsResult(GetAssetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetsResult(
            arn=self.arn,
            asset_ids=self.asset_ids,
            host_id_filters=self.host_id_filters,
            id=self.id,
            status_id_filters=self.status_id_filters)


def get_assets(arn: Optional[str] = None,
               host_id_filters: Optional[Sequence[str]] = None,
               status_id_filters: Optional[Sequence[str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetsResult:
    """
    Information about hardware assets in an Outpost.

    ## Example Usage
    ### Basic

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_assets(arn=data["aws_outposts_outpost"]["example"]["arn"])
    ```
    ### With Host ID Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_assets(arn=data["aws_outposts_outpost"]["example"]["arn"],
        host_id_filters=["h-x38g5n0yd2a0ueb61"])
    ```
    ### With Status ID Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_assets(arn=data["aws_outposts_outpost"]["example"]["arn"],
        status_id_filters=["ACTIVE"])
    ```


    :param str arn: Outpost ARN.
    :param Sequence[str] host_id_filters: Filters by list of Host IDs of a Dedicated Host.
    :param Sequence[str] status_id_filters: Filters by list of state status. Valid values: "ACTIVE", "RETIRING".
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['hostIdFilters'] = host_id_filters
    __args__['statusIdFilters'] = status_id_filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:outposts/getAssets:getAssets', __args__, opts=opts, typ=GetAssetsResult).value

    return AwaitableGetAssetsResult(
        arn=__ret__.arn,
        asset_ids=__ret__.asset_ids,
        host_id_filters=__ret__.host_id_filters,
        id=__ret__.id,
        status_id_filters=__ret__.status_id_filters)


@_utilities.lift_output_func(get_assets)
def get_assets_output(arn: Optional[pulumi.Input[str]] = None,
                      host_id_filters: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      status_id_filters: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssetsResult]:
    """
    Information about hardware assets in an Outpost.

    ## Example Usage
    ### Basic

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_assets(arn=data["aws_outposts_outpost"]["example"]["arn"])
    ```
    ### With Host ID Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_assets(arn=data["aws_outposts_outpost"]["example"]["arn"],
        host_id_filters=["h-x38g5n0yd2a0ueb61"])
    ```
    ### With Status ID Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_assets(arn=data["aws_outposts_outpost"]["example"]["arn"],
        status_id_filters=["ACTIVE"])
    ```


    :param str arn: Outpost ARN.
    :param Sequence[str] host_id_filters: Filters by list of Host IDs of a Dedicated Host.
    :param Sequence[str] status_id_filters: Filters by list of state status. Valid values: "ACTIVE", "RETIRING".
    """
    ...
