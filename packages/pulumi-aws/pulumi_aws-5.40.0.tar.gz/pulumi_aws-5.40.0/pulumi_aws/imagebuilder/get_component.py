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
    'GetComponentResult',
    'AwaitableGetComponentResult',
    'get_component',
    'get_component_output',
]

@pulumi.output_type
class GetComponentResult:
    """
    A collection of values returned by getComponent.
    """
    def __init__(__self__, arn=None, change_description=None, data=None, date_created=None, description=None, encrypted=None, id=None, kms_key_id=None, name=None, owner=None, platform=None, supported_os_versions=None, tags=None, type=None, version=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if change_description and not isinstance(change_description, str):
            raise TypeError("Expected argument 'change_description' to be a str")
        pulumi.set(__self__, "change_description", change_description)
        if data and not isinstance(data, str):
            raise TypeError("Expected argument 'data' to be a str")
        pulumi.set(__self__, "data", data)
        if date_created and not isinstance(date_created, str):
            raise TypeError("Expected argument 'date_created' to be a str")
        pulumi.set(__self__, "date_created", date_created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encrypted and not isinstance(encrypted, bool):
            raise TypeError("Expected argument 'encrypted' to be a bool")
        pulumi.set(__self__, "encrypted", encrypted)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if supported_os_versions and not isinstance(supported_os_versions, list):
            raise TypeError("Expected argument 'supported_os_versions' to be a list")
        pulumi.set(__self__, "supported_os_versions", supported_os_versions)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="changeDescription")
    def change_description(self) -> str:
        """
        Change description of the component.
        """
        return pulumi.get(self, "change_description")

    @property
    @pulumi.getter
    def data(self) -> str:
        """
        Data of the component.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> str:
        """
        Date the component was created.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the component.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encrypted(self) -> bool:
        """
        Encryption status of the component.
        """
        return pulumi.get(self, "encrypted")

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
        ARN of the Key Management Service (KMS) Key used to encrypt the component.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the component.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> str:
        """
        Owner of the component.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def platform(self) -> str:
        """
        Platform of the component.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="supportedOsVersions")
    def supported_os_versions(self) -> Sequence[str]:
        """
        Operating Systems (OSes) supported by the component.
        """
        return pulumi.get(self, "supported_os_versions")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value map of resource tags for the component.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the component.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the component.
        """
        return pulumi.get(self, "version")


class AwaitableGetComponentResult(GetComponentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComponentResult(
            arn=self.arn,
            change_description=self.change_description,
            data=self.data,
            date_created=self.date_created,
            description=self.description,
            encrypted=self.encrypted,
            id=self.id,
            kms_key_id=self.kms_key_id,
            name=self.name,
            owner=self.owner,
            platform=self.platform,
            supported_os_versions=self.supported_os_versions,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_component(arn: Optional[str] = None,
                  tags: Optional[Mapping[str, str]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComponentResult:
    """
    Provides details about an Image Builder Component.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.imagebuilder.get_component(arn="arn:aws:imagebuilder:us-west-2:aws:component/amazon-cloudwatch-agent-linux/1.0.0")
    ```


    :param str arn: ARN of the component.
    :param Mapping[str, str] tags: Key-value map of resource tags for the component.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:imagebuilder/getComponent:getComponent', __args__, opts=opts, typ=GetComponentResult).value

    return AwaitableGetComponentResult(
        arn=__ret__.arn,
        change_description=__ret__.change_description,
        data=__ret__.data,
        date_created=__ret__.date_created,
        description=__ret__.description,
        encrypted=__ret__.encrypted,
        id=__ret__.id,
        kms_key_id=__ret__.kms_key_id,
        name=__ret__.name,
        owner=__ret__.owner,
        platform=__ret__.platform,
        supported_os_versions=__ret__.supported_os_versions,
        tags=__ret__.tags,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_component)
def get_component_output(arn: Optional[pulumi.Input[str]] = None,
                         tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComponentResult]:
    """
    Provides details about an Image Builder Component.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.imagebuilder.get_component(arn="arn:aws:imagebuilder:us-west-2:aws:component/amazon-cloudwatch-agent-linux/1.0.0")
    ```


    :param str arn: ARN of the component.
    :param Mapping[str, str] tags: Key-value map of resource tags for the component.
    """
    ...
