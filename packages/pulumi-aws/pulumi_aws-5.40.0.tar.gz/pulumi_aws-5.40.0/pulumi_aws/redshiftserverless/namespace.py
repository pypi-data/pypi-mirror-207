# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 db_name: Optional[pulumi.Input[str]] = None,
                 default_iam_role_arn: Optional[pulumi.Input[str]] = None,
                 iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[str] namespace_name: The name of the namespace.
        :param pulumi.Input[str] admin_user_password: The password of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] admin_username: The username of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] db_name: The name of the first database created in the namespace.
        :param pulumi.Input[str] default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] iam_roles: A list of IAM roles to associate with the namespace.
        :param pulumi.Input[str] kms_key_id: The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_exports: The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        if admin_user_password is not None:
            pulumi.set(__self__, "admin_user_password", admin_user_password)
        if admin_username is not None:
            pulumi.set(__self__, "admin_username", admin_username)
        if db_name is not None:
            pulumi.set(__self__, "db_name", db_name)
        if default_iam_role_arn is not None:
            pulumi.set(__self__, "default_iam_role_arn", default_iam_role_arn)
        if iam_roles is not None:
            pulumi.set(__self__, "iam_roles", iam_roles)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if log_exports is not None:
            pulumi.set(__self__, "log_exports", log_exports)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_user_password")

    @admin_user_password.setter
    def admin_user_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_user_password", value)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_username")

    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_username", value)

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the first database created in the namespace.
        """
        return pulumi.get(self, "db_name")

    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_name", value)

    @property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        """
        return pulumi.get(self, "default_iam_role_arn")

    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_iam_role_arn", value)

    @property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IAM roles to associate with the namespace.
        """
        return pulumi.get(self, "iam_roles")

    @iam_roles.setter
    def iam_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "iam_roles", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        """
        return pulumi.get(self, "log_exports")

    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "log_exports", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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
class _NamespaceState:
    def __init__(__self__, *,
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 db_name: Optional[pulumi.Input[str]] = None,
                 default_iam_role_arn: Optional[pulumi.Input[str]] = None,
                 iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Namespace resources.
        :param pulumi.Input[str] admin_user_password: The password of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] admin_username: The username of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the Redshift Serverless Namespace.
        :param pulumi.Input[str] db_name: The name of the first database created in the namespace.
        :param pulumi.Input[str] default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] iam_roles: A list of IAM roles to associate with the namespace.
        :param pulumi.Input[str] kms_key_id: The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_exports: The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        :param pulumi.Input[str] namespace_id: The Redshift Namespace ID.
        :param pulumi.Input[str] namespace_name: The name of the namespace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if admin_user_password is not None:
            pulumi.set(__self__, "admin_user_password", admin_user_password)
        if admin_username is not None:
            pulumi.set(__self__, "admin_username", admin_username)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if db_name is not None:
            pulumi.set(__self__, "db_name", db_name)
        if default_iam_role_arn is not None:
            pulumi.set(__self__, "default_iam_role_arn", default_iam_role_arn)
        if iam_roles is not None:
            pulumi.set(__self__, "iam_roles", iam_roles)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if log_exports is not None:
            pulumi.set(__self__, "log_exports", log_exports)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_user_password")

    @admin_user_password.setter
    def admin_user_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_user_password", value)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_username")

    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_username", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the Redshift Serverless Namespace.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the first database created in the namespace.
        """
        return pulumi.get(self, "db_name")

    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_name", value)

    @property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        """
        return pulumi.get(self, "default_iam_role_arn")

    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_iam_role_arn", value)

    @property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IAM roles to associate with the namespace.
        """
        return pulumi.get(self, "iam_roles")

    @iam_roles.setter
    def iam_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "iam_roles", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        """
        return pulumi.get(self, "log_exports")

    @log_exports.setter
    def log_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "log_exports", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Redshift Namespace ID.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
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


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 db_name: Optional[pulumi.Input[str]] = None,
                 default_iam_role_arn: Optional[pulumi.Input[str]] = None,
                 iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a new Amazon Redshift Serverless Namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.redshiftserverless.Namespace("example", namespace_name="concurrency-scaling")
        ```

        ## Import

        Redshift Serverless Namespaces can be imported using the `namespace_name`, e.g.,

        ```sh
         $ pulumi import aws:redshiftserverless/namespace:Namespace example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_user_password: The password of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] admin_username: The username of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] db_name: The name of the first database created in the namespace.
        :param pulumi.Input[str] default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] iam_roles: A list of IAM roles to associate with the namespace.
        :param pulumi.Input[str] kms_key_id: The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_exports: The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        :param pulumi.Input[str] namespace_name: The name of the namespace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Amazon Redshift Serverless Namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.redshiftserverless.Namespace("example", namespace_name="concurrency-scaling")
        ```

        ## Import

        Redshift Serverless Namespaces can be imported using the `namespace_name`, e.g.,

        ```sh
         $ pulumi import aws:redshiftserverless/namespace:Namespace example example
        ```

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_user_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 db_name: Optional[pulumi.Input[str]] = None,
                 default_iam_role_arn: Optional[pulumi.Input[str]] = None,
                 iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["admin_user_password"] = None if admin_user_password is None else pulumi.Output.secret(admin_user_password)
            __props__.__dict__["admin_username"] = None if admin_username is None else pulumi.Output.secret(admin_username)
            __props__.__dict__["db_name"] = db_name
            __props__.__dict__["default_iam_role_arn"] = default_iam_role_arn
            __props__.__dict__["iam_roles"] = iam_roles
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["log_exports"] = log_exports
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
            __props__.__dict__["namespace_id"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["adminUserPassword", "adminUsername"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Namespace, __self__).__init__(
            'aws:redshiftserverless/namespace:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_user_password: Optional[pulumi.Input[str]] = None,
            admin_username: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            db_name: Optional[pulumi.Input[str]] = None,
            default_iam_role_arn: Optional[pulumi.Input[str]] = None,
            iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            log_exports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            namespace_id: Optional[pulumi.Input[str]] = None,
            namespace_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_user_password: The password of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] admin_username: The username of the administrator for the first database created in the namespace.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the Redshift Serverless Namespace.
        :param pulumi.Input[str] db_name: The name of the first database created in the namespace.
        :param pulumi.Input[str] default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] iam_roles: A list of IAM roles to associate with the namespace.
        :param pulumi.Input[str] kms_key_id: The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] log_exports: The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        :param pulumi.Input[str] namespace_id: The Redshift Namespace ID.
        :param pulumi.Input[str] namespace_name: The name of the namespace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamespaceState.__new__(_NamespaceState)

        __props__.__dict__["admin_user_password"] = admin_user_password
        __props__.__dict__["admin_username"] = admin_username
        __props__.__dict__["arn"] = arn
        __props__.__dict__["db_name"] = db_name
        __props__.__dict__["default_iam_role_arn"] = default_iam_role_arn
        __props__.__dict__["iam_roles"] = iam_roles
        __props__.__dict__["kms_key_id"] = kms_key_id
        __props__.__dict__["log_exports"] = log_exports
        __props__.__dict__["namespace_id"] = namespace_id
        __props__.__dict__["namespace_name"] = namespace_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> pulumi.Output[Optional[str]]:
        """
        The password of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_user_password")

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> pulumi.Output[str]:
        """
        The username of the administrator for the first database created in the namespace.
        """
        return pulumi.get(self, "admin_username")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the Redshift Serverless Namespace.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> pulumi.Output[str]:
        """
        The name of the first database created in the namespace.
        """
        return pulumi.get(self, "db_name")

    @property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. When specifying `default_iam_role_arn`, it also must be part of `iam_roles`.
        """
        return pulumi.get(self, "default_iam_role_arn")

    @property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of IAM roles to associate with the namespace.
        """
        return pulumi.get(self, "iam_roles")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[str]:
        """
        The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
        """
        return pulumi.get(self, "log_exports")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[str]:
        """
        The Redshift Namespace ID.
        """
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[str]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

