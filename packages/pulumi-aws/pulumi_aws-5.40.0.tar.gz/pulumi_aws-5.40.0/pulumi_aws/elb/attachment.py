# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AttachmentArgs', 'Attachment']

@pulumi.input_type
class AttachmentArgs:
    def __init__(__self__, *,
                 elb: pulumi.Input[str],
                 instance: pulumi.Input[str]):
        """
        The set of arguments for constructing a Attachment resource.
        :param pulumi.Input[str] elb: The name of the ELB.
        :param pulumi.Input[str] instance: Instance ID to place in the ELB pool.
        """
        pulumi.set(__self__, "elb", elb)
        pulumi.set(__self__, "instance", instance)

    @property
    @pulumi.getter
    def elb(self) -> pulumi.Input[str]:
        """
        The name of the ELB.
        """
        return pulumi.get(self, "elb")

    @elb.setter
    def elb(self, value: pulumi.Input[str]):
        pulumi.set(self, "elb", value)

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Input[str]:
        """
        Instance ID to place in the ELB pool.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance", value)


@pulumi.input_type
class _AttachmentState:
    def __init__(__self__, *,
                 elb: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Attachment resources.
        :param pulumi.Input[str] elb: The name of the ELB.
        :param pulumi.Input[str] instance: Instance ID to place in the ELB pool.
        """
        if elb is not None:
            pulumi.set(__self__, "elb", elb)
        if instance is not None:
            pulumi.set(__self__, "instance", instance)

    @property
    @pulumi.getter
    def elb(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ELB.
        """
        return pulumi.get(self, "elb")

    @elb.setter
    def elb(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "elb", value)

    @property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[str]]:
        """
        Instance ID to place in the ELB pool.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance", value)


class Attachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elb: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Attaches an EC2 instance to an Elastic Load Balancer (ELB). For attaching resources with Application Load Balancer (ALB) or Network Load Balancer (NLB), see the `lb.TargetGroupAttachment` resource.

        > **NOTE on ELB Instances and ELB Attachments:** This provider currently provides
        both a standalone ELB Attachment resource (describing an instance attached to
        an ELB), and an Elastic Load Balancer resource with
        `instances` defined in-line. At this time you cannot use an ELB with in-line
        instances in conjunction with an ELB Attachment resource. Doing so will cause a
        conflict and will overwrite attachments.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new load balancer attachment
        baz = aws.elb.Attachment("baz",
            elb=aws_elb["bar"]["id"],
            instance=aws_instance["foo"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] elb: The name of the ELB.
        :param pulumi.Input[str] instance: Instance ID to place in the ELB pool.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Attaches an EC2 instance to an Elastic Load Balancer (ELB). For attaching resources with Application Load Balancer (ALB) or Network Load Balancer (NLB), see the `lb.TargetGroupAttachment` resource.

        > **NOTE on ELB Instances and ELB Attachments:** This provider currently provides
        both a standalone ELB Attachment resource (describing an instance attached to
        an ELB), and an Elastic Load Balancer resource with
        `instances` defined in-line. At this time you cannot use an ELB with in-line
        instances in conjunction with an ELB Attachment resource. Doing so will cause a
        conflict and will overwrite attachments.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new load balancer attachment
        baz = aws.elb.Attachment("baz",
            elb=aws_elb["bar"]["id"],
            instance=aws_instance["foo"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param AttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elb: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttachmentArgs.__new__(AttachmentArgs)

            if elb is None and not opts.urn:
                raise TypeError("Missing required property 'elb'")
            __props__.__dict__["elb"] = elb
            if instance is None and not opts.urn:
                raise TypeError("Missing required property 'instance'")
            __props__.__dict__["instance"] = instance
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="aws:elasticloadbalancing/attachment:Attachment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Attachment, __self__).__init__(
            'aws:elb/attachment:Attachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            elb: Optional[pulumi.Input[str]] = None,
            instance: Optional[pulumi.Input[str]] = None) -> 'Attachment':
        """
        Get an existing Attachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] elb: The name of the ELB.
        :param pulumi.Input[str] instance: Instance ID to place in the ELB pool.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AttachmentState.__new__(_AttachmentState)

        __props__.__dict__["elb"] = elb
        __props__.__dict__["instance"] = instance
        return Attachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def elb(self) -> pulumi.Output[str]:
        """
        The name of the ELB.
        """
        return pulumi.get(self, "elb")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        """
        Instance ID to place in the ELB pool.
        """
        return pulumi.get(self, "instance")

