# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AliasArgs', 'Alias']

@pulumi.input_type
class AliasArgs:
    def __init__(__self__, *,
                 target_key_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Alias resource.
        :param pulumi.Input[str] target_key_id: Identifier for the key for which the alias is for, can be either an ARN or key_id.
        :param pulumi.Input[str] name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        :param pulumi.Input[str] name_prefix: Creates an unique alias beginning with the specified prefix.
               The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        """
        pulumi.set(__self__, "target_key_id", target_key_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)

    @property
    @pulumi.getter(name="targetKeyId")
    def target_key_id(self) -> pulumi.Input[str]:
        """
        Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        return pulumi.get(self, "target_key_id")

    @target_key_id.setter
    def target_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates an unique alias beginning with the specified prefix.
        The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)


@pulumi.input_type
class _AliasState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 target_key_arn: Optional[pulumi.Input[str]] = None,
                 target_key_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Alias resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the key alias.
        :param pulumi.Input[str] name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        :param pulumi.Input[str] name_prefix: Creates an unique alias beginning with the specified prefix.
               The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        :param pulumi.Input[str] target_key_arn: The Amazon Resource Name (ARN) of the target key identifier.
        :param pulumi.Input[str] target_key_id: Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if target_key_arn is not None:
            pulumi.set(__self__, "target_key_arn", target_key_arn)
        if target_key_id is not None:
            pulumi.set(__self__, "target_key_id", target_key_id)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the key alias.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates an unique alias beginning with the specified prefix.
        The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="targetKeyArn")
    def target_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the target key identifier.
        """
        return pulumi.get(self, "target_key_arn")

    @target_key_arn.setter
    def target_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_key_arn", value)

    @property
    @pulumi.getter(name="targetKeyId")
    def target_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        return pulumi.get(self, "target_key_id")

    @target_key_id.setter
    def target_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_key_id", value)


class Alias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 target_key_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases & keys,
        but API (hence this provider too) allows you to create as many aliases as
        the [account limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) allow you.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.kms.Key("key")
        alias = aws.kms.Alias("alias", target_key_id=key.key_id)
        ```

        ## Import

        KMS aliases can be imported using the `name`, e.g.,

        ```sh
         $ pulumi import aws:kms/alias:Alias a alias/my-key-alias
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        :param pulumi.Input[str] name_prefix: Creates an unique alias beginning with the specified prefix.
               The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        :param pulumi.Input[str] target_key_id: Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases & keys,
        but API (hence this provider too) allows you to create as many aliases as
        the [account limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) allow you.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.kms.Key("key")
        alias = aws.kms.Alias("alias", target_key_id=key.key_id)
        ```

        ## Import

        KMS aliases can be imported using the `name`, e.g.,

        ```sh
         $ pulumi import aws:kms/alias:Alias a alias/my-key-alias
        ```

        :param str resource_name: The name of the resource.
        :param AliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 target_key_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AliasArgs.__new__(AliasArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["name_prefix"] = name_prefix
            if target_key_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_key_id'")
            __props__.__dict__["target_key_id"] = target_key_id
            __props__.__dict__["arn"] = None
            __props__.__dict__["target_key_arn"] = None
        super(Alias, __self__).__init__(
            'aws:kms/alias:Alias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            target_key_arn: Optional[pulumi.Input[str]] = None,
            target_key_id: Optional[pulumi.Input[str]] = None) -> 'Alias':
        """
        Get an existing Alias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the key alias.
        :param pulumi.Input[str] name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        :param pulumi.Input[str] name_prefix: Creates an unique alias beginning with the specified prefix.
               The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        :param pulumi.Input[str] target_key_arn: The Amazon Resource Name (ARN) of the target key identifier.
        :param pulumi.Input[str] target_key_id: Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AliasState.__new__(_AliasState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["name"] = name
        __props__.__dict__["name_prefix"] = name_prefix
        __props__.__dict__["target_key_arn"] = target_key_arn
        __props__.__dict__["target_key_id"] = target_key_id
        return Alias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the key alias.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[str]:
        """
        Creates an unique alias beginning with the specified prefix.
        The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="targetKeyArn")
    def target_key_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the target key identifier.
        """
        return pulumi.get(self, "target_key_arn")

    @property
    @pulumi.getter(name="targetKeyId")
    def target_key_id(self) -> pulumi.Output[str]:
        """
        Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        return pulumi.get(self, "target_key_id")

