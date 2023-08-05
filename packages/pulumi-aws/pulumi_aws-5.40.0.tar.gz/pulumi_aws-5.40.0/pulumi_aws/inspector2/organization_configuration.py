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
from ._inputs import *

__all__ = ['OrganizationConfigurationArgs', 'OrganizationConfiguration']

@pulumi.input_type
class OrganizationConfigurationArgs:
    def __init__(__self__, *,
                 auto_enable: pulumi.Input['OrganizationConfigurationAutoEnableArgs']):
        """
        The set of arguments for constructing a OrganizationConfiguration resource.
        :param pulumi.Input['OrganizationConfigurationAutoEnableArgs'] auto_enable: Configuration block for auto enabling. See below.
        """
        pulumi.set(__self__, "auto_enable", auto_enable)

    @property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input['OrganizationConfigurationAutoEnableArgs']:
        """
        Configuration block for auto enabling. See below.
        """
        return pulumi.get(self, "auto_enable")

    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input['OrganizationConfigurationAutoEnableArgs']):
        pulumi.set(self, "auto_enable", value)


@pulumi.input_type
class _OrganizationConfigurationState:
    def __init__(__self__, *,
                 auto_enable: Optional[pulumi.Input['OrganizationConfigurationAutoEnableArgs']] = None,
                 max_account_limit_reached: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering OrganizationConfiguration resources.
        :param pulumi.Input['OrganizationConfigurationAutoEnableArgs'] auto_enable: Configuration block for auto enabling. See below.
        :param pulumi.Input[bool] max_account_limit_reached: Whether your configuration reached the max account limit.
        """
        if auto_enable is not None:
            pulumi.set(__self__, "auto_enable", auto_enable)
        if max_account_limit_reached is not None:
            pulumi.set(__self__, "max_account_limit_reached", max_account_limit_reached)

    @property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> Optional[pulumi.Input['OrganizationConfigurationAutoEnableArgs']]:
        """
        Configuration block for auto enabling. See below.
        """
        return pulumi.get(self, "auto_enable")

    @auto_enable.setter
    def auto_enable(self, value: Optional[pulumi.Input['OrganizationConfigurationAutoEnableArgs']]):
        pulumi.set(self, "auto_enable", value)

    @property
    @pulumi.getter(name="maxAccountLimitReached")
    def max_account_limit_reached(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether your configuration reached the max account limit.
        """
        return pulumi.get(self, "max_account_limit_reached")

    @max_account_limit_reached.setter
    def max_account_limit_reached(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "max_account_limit_reached", value)


class OrganizationConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_enable: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigurationAutoEnableArgs']]] = None,
                 __props__=None):
        """
        Resource for managing an Amazon Inspector Organization Configuration.

        > **NOTE:** In order for this resource to work, the account you use must be an Inspector Delegated Admin Account.

        > **NOTE:** When this resource is deleted, EC2, ECR and Lambda scans will no longer be automatically enabled for new members of your Amazon Inspector organization.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.inspector2.OrganizationConfiguration("example", auto_enable=aws.inspector2.OrganizationConfigurationAutoEnableArgs(
            ec2=True,
            ecr=False,
            lambda_=True,
        ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['OrganizationConfigurationAutoEnableArgs']] auto_enable: Configuration block for auto enabling. See below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an Amazon Inspector Organization Configuration.

        > **NOTE:** In order for this resource to work, the account you use must be an Inspector Delegated Admin Account.

        > **NOTE:** When this resource is deleted, EC2, ECR and Lambda scans will no longer be automatically enabled for new members of your Amazon Inspector organization.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.inspector2.OrganizationConfiguration("example", auto_enable=aws.inspector2.OrganizationConfigurationAutoEnableArgs(
            ec2=True,
            ecr=False,
            lambda_=True,
        ))
        ```

        :param str resource_name: The name of the resource.
        :param OrganizationConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_enable: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigurationAutoEnableArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationConfigurationArgs.__new__(OrganizationConfigurationArgs)

            if auto_enable is None and not opts.urn:
                raise TypeError("Missing required property 'auto_enable'")
            __props__.__dict__["auto_enable"] = auto_enable
            __props__.__dict__["max_account_limit_reached"] = None
        super(OrganizationConfiguration, __self__).__init__(
            'aws:inspector2/organizationConfiguration:OrganizationConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_enable: Optional[pulumi.Input[pulumi.InputType['OrganizationConfigurationAutoEnableArgs']]] = None,
            max_account_limit_reached: Optional[pulumi.Input[bool]] = None) -> 'OrganizationConfiguration':
        """
        Get an existing OrganizationConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['OrganizationConfigurationAutoEnableArgs']] auto_enable: Configuration block for auto enabling. See below.
        :param pulumi.Input[bool] max_account_limit_reached: Whether your configuration reached the max account limit.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrganizationConfigurationState.__new__(_OrganizationConfigurationState)

        __props__.__dict__["auto_enable"] = auto_enable
        __props__.__dict__["max_account_limit_reached"] = max_account_limit_reached
        return OrganizationConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Output['outputs.OrganizationConfigurationAutoEnable']:
        """
        Configuration block for auto enabling. See below.
        """
        return pulumi.get(self, "auto_enable")

    @property
    @pulumi.getter(name="maxAccountLimitReached")
    def max_account_limit_reached(self) -> pulumi.Output[bool]:
        """
        Whether your configuration reached the max account limit.
        """
        return pulumi.get(self, "max_account_limit_reached")

