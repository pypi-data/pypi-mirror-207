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
    'SnapshotImportClientData',
    'SnapshotImportDiskContainer',
    'SnapshotImportDiskContainerUserBucket',
    'GetEbsVolumesFilterResult',
    'GetSnapshotFilterResult',
    'GetSnapshotIdsFilterResult',
    'GetVolumeFilterResult',
]

@pulumi.output_type
class SnapshotImportClientData(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "uploadEnd":
            suggest = "upload_end"
        elif key == "uploadSize":
            suggest = "upload_size"
        elif key == "uploadStart":
            suggest = "upload_start"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SnapshotImportClientData. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SnapshotImportClientData.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SnapshotImportClientData.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 comment: Optional[str] = None,
                 upload_end: Optional[str] = None,
                 upload_size: Optional[float] = None,
                 upload_start: Optional[str] = None):
        """
        :param str comment: A user-defined comment about the disk upload.
        :param str upload_end: The time that the disk upload ends.
        :param float upload_size: The size of the uploaded disk image, in GiB.
        :param str upload_start: The time that the disk upload starts.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if upload_end is not None:
            pulumi.set(__self__, "upload_end", upload_end)
        if upload_size is not None:
            pulumi.set(__self__, "upload_size", upload_size)
        if upload_start is not None:
            pulumi.set(__self__, "upload_start", upload_start)

    @property
    @pulumi.getter
    def comment(self) -> Optional[str]:
        """
        A user-defined comment about the disk upload.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="uploadEnd")
    def upload_end(self) -> Optional[str]:
        """
        The time that the disk upload ends.
        """
        return pulumi.get(self, "upload_end")

    @property
    @pulumi.getter(name="uploadSize")
    def upload_size(self) -> Optional[float]:
        """
        The size of the uploaded disk image, in GiB.
        """
        return pulumi.get(self, "upload_size")

    @property
    @pulumi.getter(name="uploadStart")
    def upload_start(self) -> Optional[str]:
        """
        The time that the disk upload starts.
        """
        return pulumi.get(self, "upload_start")


@pulumi.output_type
class SnapshotImportDiskContainer(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "userBucket":
            suggest = "user_bucket"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SnapshotImportDiskContainer. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SnapshotImportDiskContainer.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SnapshotImportDiskContainer.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 format: str,
                 description: Optional[str] = None,
                 url: Optional[str] = None,
                 user_bucket: Optional['outputs.SnapshotImportDiskContainerUserBucket'] = None):
        """
        :param str format: The format of the disk image being imported. One of `VHD` or `VMDK`.
        :param str description: The description of the disk image being imported.
        :param str url: The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..). One of `url` or `user_bucket` must be set.
        :param 'SnapshotImportDiskContainerUserBucketArgs' user_bucket: The Amazon S3 bucket for the disk image. One of `url` or `user_bucket` must be set. Detailed below.
        """
        pulumi.set(__self__, "format", format)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if user_bucket is not None:
            pulumi.set(__self__, "user_bucket", user_bucket)

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        The format of the disk image being imported. One of `VHD` or `VMDK`.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the disk image being imported.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..). One of `url` or `user_bucket` must be set.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="userBucket")
    def user_bucket(self) -> Optional['outputs.SnapshotImportDiskContainerUserBucket']:
        """
        The Amazon S3 bucket for the disk image. One of `url` or `user_bucket` must be set. Detailed below.
        """
        return pulumi.get(self, "user_bucket")


@pulumi.output_type
class SnapshotImportDiskContainerUserBucket(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "s3Bucket":
            suggest = "s3_bucket"
        elif key == "s3Key":
            suggest = "s3_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SnapshotImportDiskContainerUserBucket. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SnapshotImportDiskContainerUserBucket.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SnapshotImportDiskContainerUserBucket.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 s3_bucket: str,
                 s3_key: str):
        """
        :param str s3_bucket: The name of the Amazon S3 bucket where the disk image is located.
        :param str s3_key: The file name of the disk image.
        """
        pulumi.set(__self__, "s3_bucket", s3_bucket)
        pulumi.set(__self__, "s3_key", s3_key)

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> str:
        """
        The name of the Amazon S3 bucket where the disk image is located.
        """
        return pulumi.get(self, "s3_bucket")

    @property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> str:
        """
        The file name of the disk image.
        """
        return pulumi.get(self, "s3_key")


@pulumi.output_type
class GetEbsVolumesFilterResult(dict):
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        """
        :param str name: Name of the field to filter by, as defined by
               [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html).
               For example, if matching against the `size` filter, use:
        :param Sequence[str] values: Set of values that are accepted for the given field.
               EBS Volume IDs will be selected if any one of the given values match.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the field to filter by, as defined by
        [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html).
        For example, if matching against the `size` filter, use:
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Set of values that are accepted for the given field.
        EBS Volume IDs will be selected if any one of the given values match.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetSnapshotFilterResult(dict):
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
class GetSnapshotIdsFilterResult(dict):
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
class GetVolumeFilterResult(dict):
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


