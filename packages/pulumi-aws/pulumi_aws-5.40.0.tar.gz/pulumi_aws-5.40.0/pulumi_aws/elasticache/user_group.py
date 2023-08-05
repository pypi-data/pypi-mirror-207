# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserGroupArgs', 'UserGroup']

@pulumi.input_type
class UserGroupArgs:
    def __init__(__self__, *,
                 engine: pulumi.Input[str],
                 user_group_id: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a UserGroup resource.
        :param pulumi.Input[str] engine: The current supported value is `REDIS`.
        :param pulumi.Input[str] user_group_id: The ID of the user group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_ids: The list of user IDs that belong to the user group.
        """
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "user_group_id", user_group_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if user_ids is not None:
            pulumi.set(__self__, "user_ids", user_ids)

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Input[str]:
        """
        The current supported value is `REDIS`.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the user group.
        """
        return pulumi.get(self, "user_group_id")

    @user_group_id.setter
    def user_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_group_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="userIds")
    def user_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user IDs that belong to the user group.
        """
        return pulumi.get(self, "user_ids")

    @user_ids.setter
    def user_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_ids", value)


@pulumi.input_type
class _UserGroupState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None,
                 user_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering UserGroup resources.
        :param pulumi.Input[str] arn: The ARN that identifies the user group.
        :param pulumi.Input[str] engine: The current supported value is `REDIS`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] user_group_id: The ID of the user group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_ids: The list of user IDs that belong to the user group.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if user_group_id is not None:
            pulumi.set(__self__, "user_group_id", user_group_id)
        if user_ids is not None:
            pulumi.set(__self__, "user_ids", user_ids)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN that identifies the user group.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[str]]:
        """
        The current supported value is `REDIS`.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the user group.
        """
        return pulumi.get(self, "user_group_id")

    @user_group_id.setter
    def user_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_group_id", value)

    @property
    @pulumi.getter(name="userIds")
    def user_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user IDs that belong to the user group.
        """
        return pulumi.get(self, "user_ids")

    @user_ids.setter
    def user_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_ids", value)


class UserGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None,
                 user_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an ElastiCache user group resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_user = aws.elasticache.User("testUser",
            user_id="testUserId",
            user_name="default",
            access_string="on ~app::* -@all +@read +@hash +@bitmap +@geo -setbit -bitfield -hset -hsetnx -hmset -hincrby -hincrbyfloat -hdel -bitop -geoadd -georadius -georadiusbymember",
            engine="REDIS",
            passwords=["password123456789"])
        test_user_group = aws.elasticache.UserGroup("testUserGroup",
            engine="REDIS",
            user_group_id="userGroupId",
            user_ids=[test_user.user_id])
        ```

        ## Import

        ElastiCache user groups can be imported using the `user_group_id`, e.g.,

        ```sh
         $ pulumi import aws:elasticache/userGroup:UserGroup my_user_group userGoupId1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] engine: The current supported value is `REDIS`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] user_group_id: The ID of the user group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_ids: The list of user IDs that belong to the user group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an ElastiCache user group resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_user = aws.elasticache.User("testUser",
            user_id="testUserId",
            user_name="default",
            access_string="on ~app::* -@all +@read +@hash +@bitmap +@geo -setbit -bitfield -hset -hsetnx -hmset -hincrby -hincrbyfloat -hdel -bitop -geoadd -georadius -georadiusbymember",
            engine="REDIS",
            passwords=["password123456789"])
        test_user_group = aws.elasticache.UserGroup("testUserGroup",
            engine="REDIS",
            user_group_id="userGroupId",
            user_ids=[test_user.user_id])
        ```

        ## Import

        ElastiCache user groups can be imported using the `user_group_id`, e.g.,

        ```sh
         $ pulumi import aws:elasticache/userGroup:UserGroup my_user_group userGoupId1
        ```

        :param str resource_name: The name of the resource.
        :param UserGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None,
                 user_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserGroupArgs.__new__(UserGroupArgs)

            if engine is None and not opts.urn:
                raise TypeError("Missing required property 'engine'")
            __props__.__dict__["engine"] = engine
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            if user_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_group_id'")
            __props__.__dict__["user_group_id"] = user_group_id
            __props__.__dict__["user_ids"] = user_ids
            __props__.__dict__["arn"] = None
        super(UserGroup, __self__).__init__(
            'aws:elasticache/userGroup:UserGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user_group_id: Optional[pulumi.Input[str]] = None,
            user_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'UserGroup':
        """
        Get an existing UserGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN that identifies the user group.
        :param pulumi.Input[str] engine: The current supported value is `REDIS`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] user_group_id: The ID of the user group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_ids: The list of user IDs that belong to the user group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserGroupState.__new__(_UserGroupState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["engine"] = engine
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["user_group_id"] = user_group_id
        __props__.__dict__["user_ids"] = user_ids
        return UserGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN that identifies the user group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        The current supported value is `REDIS`.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the user group.
        """
        return pulumi.get(self, "user_group_id")

    @property
    @pulumi.getter(name="userIds")
    def user_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of user IDs that belong to the user group.
        """
        return pulumi.get(self, "user_ids")

