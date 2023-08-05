# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ResourceGroupArgs', 'ResourceGroup']

@pulumi.input_type
class ResourceGroupArgs:
    def __init__(__self__, *,
                 tags: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        """
        The set of arguments for constructing a ResourceGroup resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ResourceGroupState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ResourceGroup resources.
        :param pulumi.Input[str] arn: The resource group ARN.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The resource group ARN.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ResourceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an Amazon Inspector Classic Resource Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.inspector.ResourceGroup("example", tags={
            "Env": "bar",
            "Name": "foo",
        })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Amazon Inspector Classic Resource Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.inspector.ResourceGroup("example", tags={
            "Env": "bar",
            "Name": "foo",
        })
        ```

        :param str resource_name: The name of the resource.
        :param ResourceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceGroupArgs.__new__(ResourceGroupArgs)

            if tags is None and not opts.urn:
                raise TypeError("Missing required property 'tags'")
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(ResourceGroup, __self__).__init__(
            'aws:inspector/resourceGroup:ResourceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ResourceGroup':
        """
        Get an existing ResourceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The resource group ARN.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResourceGroupState.__new__(_ResourceGroupState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["tags"] = tags
        return ResourceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The resource group ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Key-value map of tags that are used to select the EC2 instances to be included in an Amazon Inspector assessment target.
        """
        return pulumi.get(self, "tags")

