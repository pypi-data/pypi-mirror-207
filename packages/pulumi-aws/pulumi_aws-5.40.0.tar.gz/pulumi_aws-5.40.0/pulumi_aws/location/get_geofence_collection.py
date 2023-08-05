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
    'GetGeofenceCollectionResult',
    'AwaitableGetGeofenceCollectionResult',
    'get_geofence_collection',
    'get_geofence_collection_output',
]

@pulumi.output_type
class GetGeofenceCollectionResult:
    """
    A collection of values returned by getGeofenceCollection.
    """
    def __init__(__self__, collection_arn=None, collection_name=None, create_time=None, description=None, id=None, kms_key_id=None, tags=None, update_time=None):
        if collection_arn and not isinstance(collection_arn, str):
            raise TypeError("Expected argument 'collection_arn' to be a str")
        pulumi.set(__self__, "collection_arn", collection_arn)
        if collection_name and not isinstance(collection_name, str):
            raise TypeError("Expected argument 'collection_name' to be a str")
        pulumi.set(__self__, "collection_name", collection_name)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="collectionArn")
    def collection_arn(self) -> str:
        """
        ARN for the geofence collection resource. Used when you need to specify a resource across all AWS.
        """
        return pulumi.get(self, "collection_arn")

    @property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> str:
        return pulumi.get(self, "collection_name")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Timestamp for when the geofence collection resource was created in ISO 8601 format.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional description of the geofence collection resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        Key identifier for an AWS KMS customer managed key assigned to the Amazon Location resource.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value map of resource tags for the geofence collection.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Timestamp for when the geofence collection resource was last updated in ISO 8601 format.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetGeofenceCollectionResult(GetGeofenceCollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGeofenceCollectionResult(
            collection_arn=self.collection_arn,
            collection_name=self.collection_name,
            create_time=self.create_time,
            description=self.description,
            id=self.id,
            kms_key_id=self.kms_key_id,
            tags=self.tags,
            update_time=self.update_time)


def get_geofence_collection(collection_name: Optional[str] = None,
                            kms_key_id: Optional[str] = None,
                            tags: Optional[Mapping[str, str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGeofenceCollectionResult:
    """
    Retrieve information about a Location Service Geofence Collection.

    ## Example Usage
    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.location.get_geofence_collection(collection_name="example")
    ```


    :param str collection_name: Name of the geofence collection.
    :param str kms_key_id: Key identifier for an AWS KMS customer managed key assigned to the Amazon Location resource.
    :param Mapping[str, str] tags: Key-value map of resource tags for the geofence collection.
    """
    __args__ = dict()
    __args__['collectionName'] = collection_name
    __args__['kmsKeyId'] = kms_key_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:location/getGeofenceCollection:getGeofenceCollection', __args__, opts=opts, typ=GetGeofenceCollectionResult).value

    return AwaitableGetGeofenceCollectionResult(
        collection_arn=__ret__.collection_arn,
        collection_name=__ret__.collection_name,
        create_time=__ret__.create_time,
        description=__ret__.description,
        id=__ret__.id,
        kms_key_id=__ret__.kms_key_id,
        tags=__ret__.tags,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_geofence_collection)
def get_geofence_collection_output(collection_name: Optional[pulumi.Input[str]] = None,
                                   kms_key_id: Optional[pulumi.Input[Optional[str]]] = None,
                                   tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGeofenceCollectionResult]:
    """
    Retrieve information about a Location Service Geofence Collection.

    ## Example Usage
    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.location.get_geofence_collection(collection_name="example")
    ```


    :param str collection_name: Name of the geofence collection.
    :param str kms_key_id: Key identifier for an AWS KMS customer managed key assigned to the Amazon Location resource.
    :param Mapping[str, str] tags: Key-value map of resource tags for the geofence collection.
    """
    ...
