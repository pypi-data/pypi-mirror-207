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
    'LanguageModelInputDataConfigArgs',
]

@pulumi.input_type
class LanguageModelInputDataConfigArgs:
    def __init__(__self__, *,
                 data_access_role_arn: pulumi.Input[str],
                 s3_uri: pulumi.Input[str],
                 tuning_data_s3_uri: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] data_access_role_arn: IAM role with access to S3 bucket.
        :param pulumi.Input[str] s3_uri: S3 URI where training data is located.
        :param pulumi.Input[str] tuning_data_s3_uri: S3 URI where tuning data is located.
        """
        pulumi.set(__self__, "data_access_role_arn", data_access_role_arn)
        pulumi.set(__self__, "s3_uri", s3_uri)
        if tuning_data_s3_uri is not None:
            pulumi.set(__self__, "tuning_data_s3_uri", tuning_data_s3_uri)

    @property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Input[str]:
        """
        IAM role with access to S3 bucket.
        """
        return pulumi.get(self, "data_access_role_arn")

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_access_role_arn", value)

    @property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[str]:
        """
        S3 URI where training data is located.
        """
        return pulumi.get(self, "s3_uri")

    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "s3_uri", value)

    @property
    @pulumi.getter(name="tuningDataS3Uri")
    def tuning_data_s3_uri(self) -> Optional[pulumi.Input[str]]:
        """
        S3 URI where tuning data is located.
        """
        return pulumi.get(self, "tuning_data_s3_uri")

    @tuning_data_s3_uri.setter
    def tuning_data_s3_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tuning_data_s3_uri", value)


