# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 resource_arn: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] key: Tag name.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the ECS resource to tag.
        :param pulumi.Input[str] value: Tag value.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "resource_arn", resource_arn)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Tag name.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) of the ECS resource to tag.
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Tag value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class _TagState:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Tag resources.
        :param pulumi.Input[str] key: Tag name.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the ECS resource to tag.
        :param pulumi.Input[str] value: Tag value.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if resource_arn is not None:
            pulumi.set(__self__, "resource_arn", resource_arn)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Tag name.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the ECS resource to tag.
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Tag value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an individual ECS resource tag. This resource should only be used in cases where ECS resources are created outside the provider (e.g., ECS Clusters implicitly created by Batch Compute Environments).

        > **NOTE:** This tagging resource should not be combined with the resource for managing the parent resource. For example, using `ecs.Cluster` and `ecs.Tag` to manage tags of the same ECS Cluster will cause a perpetual difference where the `ecs.Cluster` resource will try to remove the tag being added by the `ecs.Tag` resource.

        > **NOTE:** This tagging resource does not use the provider `ignore_tags` configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_compute_environment = aws.batch.ComputeEnvironment("exampleComputeEnvironment",
            compute_environment_name="example",
            service_role=aws_iam_role["example"]["arn"],
            type="UNMANAGED")
        example_tag = aws.ecs.Tag("exampleTag",
            resource_arn=example_compute_environment.ecs_cluster_arn,
            key="Name",
            value="Hello World")
        ```

        ## Import

        `aws_ecs_tag` can be imported by using the ECS resource identifier and key, separated by a comma (`,`), e.g.,

        ```sh
         $ pulumi import aws:ecs/tag:Tag example arn:aws:ecs:us-east-1:123456789012:cluster/example,Name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: Tag name.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the ECS resource to tag.
        :param pulumi.Input[str] value: Tag value.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an individual ECS resource tag. This resource should only be used in cases where ECS resources are created outside the provider (e.g., ECS Clusters implicitly created by Batch Compute Environments).

        > **NOTE:** This tagging resource should not be combined with the resource for managing the parent resource. For example, using `ecs.Cluster` and `ecs.Tag` to manage tags of the same ECS Cluster will cause a perpetual difference where the `ecs.Cluster` resource will try to remove the tag being added by the `ecs.Tag` resource.

        > **NOTE:** This tagging resource does not use the provider `ignore_tags` configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_compute_environment = aws.batch.ComputeEnvironment("exampleComputeEnvironment",
            compute_environment_name="example",
            service_role=aws_iam_role["example"]["arn"],
            type="UNMANAGED")
        example_tag = aws.ecs.Tag("exampleTag",
            resource_arn=example_compute_environment.ecs_cluster_arn,
            key="Name",
            value="Hello World")
        ```

        ## Import

        `aws_ecs_tag` can be imported by using the ECS resource identifier and key, separated by a comma (`,`), e.g.,

        ```sh
         $ pulumi import aws:ecs/tag:Tag example arn:aws:ecs:us-east-1:123456789012:cluster/example,Name
        ```

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if resource_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_arn'")
            __props__.__dict__["resource_arn"] = resource_arn
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
        super(Tag, __self__).__init__(
            'aws:ecs/tag:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key: Optional[pulumi.Input[str]] = None,
            resource_arn: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: Tag name.
        :param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the ECS resource to tag.
        :param pulumi.Input[str] value: Tag value.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagState.__new__(_TagState)

        __props__.__dict__["key"] = key
        __props__.__dict__["resource_arn"] = resource_arn
        __props__.__dict__["value"] = value
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Tag name.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the ECS resource to tag.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        Tag value.
        """
        return pulumi.get(self, "value")

