# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EnvironmentEC2Args', 'EnvironmentEC2']

@pulumi.input_type
class EnvironmentEC2Args:
    def __init__(__self__, *,
                 instance_type: pulumi.Input[str],
                 automatic_stop_time_minutes: Optional[pulumi.Input[int]] = None,
                 connection_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_arn: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a EnvironmentEC2 resource.
        :param pulumi.Input[str] instance_type: The type of instance to connect to the environment, e.g., `t2.micro`.
        :param pulumi.Input[int] automatic_stop_time_minutes: The number of minutes until the running instance is shut down after the environment has last been used.
        :param pulumi.Input[str] connection_type: The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        :param pulumi.Input[str] description: The description of the environment.
        :param pulumi.Input[str] image_id: The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
               * `amazonlinux-1-x86_64`
               * `amazonlinux-2-x86_64`
               * `ubuntu-18.04-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input[str] owner_arn: The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        :param pulumi.Input[str] subnet_id: The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        pulumi.set(__self__, "instance_type", instance_type)
        if automatic_stop_time_minutes is not None:
            pulumi.set(__self__, "automatic_stop_time_minutes", automatic_stop_time_minutes)
        if connection_type is not None:
            pulumi.set(__self__, "connection_type", connection_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if image_id is not None:
            pulumi.set(__self__, "image_id", image_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner_arn is not None:
            pulumi.set(__self__, "owner_arn", owner_arn)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        The type of instance to connect to the environment, e.g., `t2.micro`.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of minutes until the running instance is shut down after the environment has last been used.
        """
        return pulumi.get(self, "automatic_stop_time_minutes")

    @automatic_stop_time_minutes.setter
    def automatic_stop_time_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatic_stop_time_minutes", value)

    @property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[str]]:
        """
        The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        """
        return pulumi.get(self, "connection_type")

    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
        * `amazonlinux-1-x86_64`
        * `amazonlinux-2-x86_64`
        * `ubuntu-18.04-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        """
        return pulumi.get(self, "image_id")

    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerArn")
    def owner_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        """
        return pulumi.get(self, "owner_arn")

    @owner_arn.setter
    def owner_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_arn", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _EnvironmentEC2State:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 automatic_stop_time_minutes: Optional[pulumi.Input[int]] = None,
                 connection_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_arn: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EnvironmentEC2 resources.
        :param pulumi.Input[str] arn: The ARN of the environment.
        :param pulumi.Input[int] automatic_stop_time_minutes: The number of minutes until the running instance is shut down after the environment has last been used.
        :param pulumi.Input[str] connection_type: The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        :param pulumi.Input[str] description: The description of the environment.
        :param pulumi.Input[str] image_id: The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
               * `amazonlinux-1-x86_64`
               * `amazonlinux-2-x86_64`
               * `ubuntu-18.04-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        :param pulumi.Input[str] instance_type: The type of instance to connect to the environment, e.g., `t2.micro`.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input[str] owner_arn: The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        :param pulumi.Input[str] subnet_id: The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] type: The type of the environment (e.g., `ssh` or `ec2`)
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if automatic_stop_time_minutes is not None:
            pulumi.set(__self__, "automatic_stop_time_minutes", automatic_stop_time_minutes)
        if connection_type is not None:
            pulumi.set(__self__, "connection_type", connection_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if image_id is not None:
            pulumi.set(__self__, "image_id", image_id)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner_arn is not None:
            pulumi.set(__self__, "owner_arn", owner_arn)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the environment.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of minutes until the running instance is shut down after the environment has last been used.
        """
        return pulumi.get(self, "automatic_stop_time_minutes")

    @automatic_stop_time_minutes.setter
    def automatic_stop_time_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "automatic_stop_time_minutes", value)

    @property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[str]]:
        """
        The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        """
        return pulumi.get(self, "connection_type")

    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
        * `amazonlinux-1-x86_64`
        * `amazonlinux-2-x86_64`
        * `ubuntu-18.04-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        """
        return pulumi.get(self, "image_id")

    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_id", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of instance to connect to the environment, e.g., `t2.micro`.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerArn")
    def owner_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        """
        return pulumi.get(self, "owner_arn")

    @owner_arn.setter
    def owner_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_arn", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the environment (e.g., `ssh` or `ec2`)
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class EnvironmentEC2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic_stop_time_minutes: Optional[pulumi.Input[int]] = None,
                 connection_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_arn: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Cloud9 EC2 Development Environment.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloud9.EnvironmentEC2("example", instance_type="t2.micro")
        ```

        Get the URL of the Cloud9 environment after creation:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloud9.EnvironmentEC2("example", instance_type="t2.micro")
        cloud9_instance = aws.ec2.get_instance_output(filters=[aws.ec2.GetInstanceFilterArgs(
            name="tag:aws:cloud9:environment",
            values=[example.id],
        )])
        pulumi.export("cloud9Url", example.id.apply(lambda id: f"https://{var['region']}.console.aws.amazon.com/cloud9/ide/{id}"))
        ```

        Allocate a static IP to the Cloud9 environment:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloud9.EnvironmentEC2("example", instance_type="t2.micro")
        cloud9_instance = aws.ec2.get_instance_output(filters=[aws.ec2.GetInstanceFilterArgs(
            name="tag:aws:cloud9:environment",
            values=[example.id],
        )])
        cloud9_eip = aws.ec2.Eip("cloud9Eip",
            instance=cloud9_instance.id,
            vpc=True)
        pulumi.export("cloud9PublicIp", cloud9_eip.public_ip)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] automatic_stop_time_minutes: The number of minutes until the running instance is shut down after the environment has last been used.
        :param pulumi.Input[str] connection_type: The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        :param pulumi.Input[str] description: The description of the environment.
        :param pulumi.Input[str] image_id: The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
               * `amazonlinux-1-x86_64`
               * `amazonlinux-2-x86_64`
               * `ubuntu-18.04-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        :param pulumi.Input[str] instance_type: The type of instance to connect to the environment, e.g., `t2.micro`.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input[str] owner_arn: The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        :param pulumi.Input[str] subnet_id: The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentEC2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud9 EC2 Development Environment.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloud9.EnvironmentEC2("example", instance_type="t2.micro")
        ```

        Get the URL of the Cloud9 environment after creation:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloud9.EnvironmentEC2("example", instance_type="t2.micro")
        cloud9_instance = aws.ec2.get_instance_output(filters=[aws.ec2.GetInstanceFilterArgs(
            name="tag:aws:cloud9:environment",
            values=[example.id],
        )])
        pulumi.export("cloud9Url", example.id.apply(lambda id: f"https://{var['region']}.console.aws.amazon.com/cloud9/ide/{id}"))
        ```

        Allocate a static IP to the Cloud9 environment:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloud9.EnvironmentEC2("example", instance_type="t2.micro")
        cloud9_instance = aws.ec2.get_instance_output(filters=[aws.ec2.GetInstanceFilterArgs(
            name="tag:aws:cloud9:environment",
            values=[example.id],
        )])
        cloud9_eip = aws.ec2.Eip("cloud9Eip",
            instance=cloud9_instance.id,
            vpc=True)
        pulumi.export("cloud9PublicIp", cloud9_eip.public_ip)
        ```

        :param str resource_name: The name of the resource.
        :param EnvironmentEC2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentEC2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic_stop_time_minutes: Optional[pulumi.Input[int]] = None,
                 connection_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_arn: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentEC2Args.__new__(EnvironmentEC2Args)

            __props__.__dict__["automatic_stop_time_minutes"] = automatic_stop_time_minutes
            __props__.__dict__["connection_type"] = connection_type
            __props__.__dict__["description"] = description
            __props__.__dict__["image_id"] = image_id
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["name"] = name
            __props__.__dict__["owner_arn"] = owner_arn
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
            __props__.__dict__["type"] = None
        super(EnvironmentEC2, __self__).__init__(
            'aws:cloud9/environmentEC2:EnvironmentEC2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            automatic_stop_time_minutes: Optional[pulumi.Input[int]] = None,
            connection_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            image_id: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner_arn: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'EnvironmentEC2':
        """
        Get an existing EnvironmentEC2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the environment.
        :param pulumi.Input[int] automatic_stop_time_minutes: The number of minutes until the running instance is shut down after the environment has last been used.
        :param pulumi.Input[str] connection_type: The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        :param pulumi.Input[str] description: The description of the environment.
        :param pulumi.Input[str] image_id: The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
               * `amazonlinux-1-x86_64`
               * `amazonlinux-2-x86_64`
               * `ubuntu-18.04-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
               * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        :param pulumi.Input[str] instance_type: The type of instance to connect to the environment, e.g., `t2.micro`.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input[str] owner_arn: The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        :param pulumi.Input[str] subnet_id: The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] type: The type of the environment (e.g., `ssh` or `ec2`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnvironmentEC2State.__new__(_EnvironmentEC2State)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["automatic_stop_time_minutes"] = automatic_stop_time_minutes
        __props__.__dict__["connection_type"] = connection_type
        __props__.__dict__["description"] = description
        __props__.__dict__["image_id"] = image_id
        __props__.__dict__["instance_type"] = instance_type
        __props__.__dict__["name"] = name
        __props__.__dict__["owner_arn"] = owner_arn
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["type"] = type
        return EnvironmentEC2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the environment.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        The number of minutes until the running instance is shut down after the environment has last been used.
        """
        return pulumi.get(self, "automatic_stop_time_minutes")

    @property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Output[Optional[str]]:
        """
        The connection type used for connecting to an Amazon EC2 environment. Valid values are `CONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
        """
        return pulumi.get(self, "connection_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. Valid values are
        * `amazonlinux-1-x86_64`
        * `amazonlinux-2-x86_64`
        * `ubuntu-18.04-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-1-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`
        * `resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        """
        The type of instance to connect to the environment, e.g., `t2.micro`.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerArn")
    def owner_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment's creator.
        """
        return pulumi.get(self, "owner_arn")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the environment (e.g., `ssh` or `ec2`)
        """
        return pulumi.get(self, "type")

