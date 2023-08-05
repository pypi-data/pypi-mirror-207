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
    'GetResourceShareFilterResult',
]

@pulumi.output_type
class GetResourceShareFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the tag key to filter on.
        :param Sequence[str] values: Value of the tag key.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the tag key to filter on.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Value of the tag key.
        """
        return pulumi.get(self, "values")


