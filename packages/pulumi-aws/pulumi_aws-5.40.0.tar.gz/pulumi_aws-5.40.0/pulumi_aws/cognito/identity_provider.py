# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IdentityProviderArgs', 'IdentityProvider']

@pulumi.input_type
class IdentityProviderArgs:
    def __init__(__self__, *,
                 provider_details: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 provider_name: pulumi.Input[str],
                 provider_type: pulumi.Input[str],
                 user_pool_id: pulumi.Input[str],
                 attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 idp_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IdentityProvider resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] provider_details: The map of identity details, such as access token
        :param pulumi.Input[str] provider_name: The provider name
        :param pulumi.Input[str] provider_type: The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        :param pulumi.Input[str] user_pool_id: The user pool id
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attribute_mapping: The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] idp_identifiers: The list of identity providers.
        """
        pulumi.set(__self__, "provider_details", provider_details)
        pulumi.set(__self__, "provider_name", provider_name)
        pulumi.set(__self__, "provider_type", provider_type)
        pulumi.set(__self__, "user_pool_id", user_pool_id)
        if attribute_mapping is not None:
            pulumi.set(__self__, "attribute_mapping", attribute_mapping)
        if idp_identifiers is not None:
            pulumi.set(__self__, "idp_identifiers", idp_identifiers)

    @property
    @pulumi.getter(name="providerDetails")
    def provider_details(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        The map of identity details, such as access token
        """
        return pulumi.get(self, "provider_details")

    @provider_details.setter
    def provider_details(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "provider_details", value)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[str]:
        """
        The provider name
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Input[str]:
        """
        The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        """
        return pulumi.get(self, "provider_type")

    @provider_type.setter
    def provider_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_type", value)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[str]:
        """
        The user pool id
        """
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_pool_id", value)

    @property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        """
        return pulumi.get(self, "attribute_mapping")

    @attribute_mapping.setter
    def attribute_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "attribute_mapping", value)

    @property
    @pulumi.getter(name="idpIdentifiers")
    def idp_identifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of identity providers.
        """
        return pulumi.get(self, "idp_identifiers")

    @idp_identifiers.setter
    def idp_identifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "idp_identifiers", value)


@pulumi.input_type
class _IdentityProviderState:
    def __init__(__self__, *,
                 attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 idp_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IdentityProvider resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attribute_mapping: The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] idp_identifiers: The list of identity providers.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] provider_details: The map of identity details, such as access token
        :param pulumi.Input[str] provider_name: The provider name
        :param pulumi.Input[str] provider_type: The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        :param pulumi.Input[str] user_pool_id: The user pool id
        """
        if attribute_mapping is not None:
            pulumi.set(__self__, "attribute_mapping", attribute_mapping)
        if idp_identifiers is not None:
            pulumi.set(__self__, "idp_identifiers", idp_identifiers)
        if provider_details is not None:
            pulumi.set(__self__, "provider_details", provider_details)
        if provider_name is not None:
            pulumi.set(__self__, "provider_name", provider_name)
        if provider_type is not None:
            pulumi.set(__self__, "provider_type", provider_type)
        if user_pool_id is not None:
            pulumi.set(__self__, "user_pool_id", user_pool_id)

    @property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        """
        return pulumi.get(self, "attribute_mapping")

    @attribute_mapping.setter
    def attribute_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "attribute_mapping", value)

    @property
    @pulumi.getter(name="idpIdentifiers")
    def idp_identifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of identity providers.
        """
        return pulumi.get(self, "idp_identifiers")

    @idp_identifiers.setter
    def idp_identifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "idp_identifiers", value)

    @property
    @pulumi.getter(name="providerDetails")
    def provider_details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The map of identity details, such as access token
        """
        return pulumi.get(self, "provider_details")

    @provider_details.setter
    def provider_details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "provider_details", value)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The provider name
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[pulumi.Input[str]]:
        """
        The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        """
        return pulumi.get(self, "provider_type")

    @provider_type.setter
    def provider_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_type", value)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The user pool id
        """
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_pool_id", value)


class IdentityProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 idp_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cognito User Identity Provider resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cognito.UserPool("example", auto_verified_attributes=["email"])
        example_provider = aws.cognito.IdentityProvider("exampleProvider",
            user_pool_id=example.id,
            provider_name="Google",
            provider_type="Google",
            provider_details={
                "authorize_scopes": "email",
                "client_id": "your client_id",
                "client_secret": "your client_secret",
            },
            attribute_mapping={
                "email": "email",
                "username": "sub",
            })
        ```

        ## Import

        `aws_cognito_identity_provider` resources can be imported using their User Pool ID and Provider Name, e.g.,

        ```sh
         $ pulumi import aws:cognito/identityProvider:IdentityProvider example us-west-2_abc123:CorpAD
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attribute_mapping: The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] idp_identifiers: The list of identity providers.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] provider_details: The map of identity details, such as access token
        :param pulumi.Input[str] provider_name: The provider name
        :param pulumi.Input[str] provider_type: The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        :param pulumi.Input[str] user_pool_id: The user pool id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cognito User Identity Provider resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cognito.UserPool("example", auto_verified_attributes=["email"])
        example_provider = aws.cognito.IdentityProvider("exampleProvider",
            user_pool_id=example.id,
            provider_name="Google",
            provider_type="Google",
            provider_details={
                "authorize_scopes": "email",
                "client_id": "your client_id",
                "client_secret": "your client_secret",
            },
            attribute_mapping={
                "email": "email",
                "username": "sub",
            })
        ```

        ## Import

        `aws_cognito_identity_provider` resources can be imported using their User Pool ID and Provider Name, e.g.,

        ```sh
         $ pulumi import aws:cognito/identityProvider:IdentityProvider example us-west-2_abc123:CorpAD
        ```

        :param str resource_name: The name of the resource.
        :param IdentityProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 idp_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 provider_type: Optional[pulumi.Input[str]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IdentityProviderArgs.__new__(IdentityProviderArgs)

            __props__.__dict__["attribute_mapping"] = attribute_mapping
            __props__.__dict__["idp_identifiers"] = idp_identifiers
            if provider_details is None and not opts.urn:
                raise TypeError("Missing required property 'provider_details'")
            __props__.__dict__["provider_details"] = provider_details
            if provider_name is None and not opts.urn:
                raise TypeError("Missing required property 'provider_name'")
            __props__.__dict__["provider_name"] = provider_name
            if provider_type is None and not opts.urn:
                raise TypeError("Missing required property 'provider_type'")
            __props__.__dict__["provider_type"] = provider_type
            if user_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__.__dict__["user_pool_id"] = user_pool_id
        super(IdentityProvider, __self__).__init__(
            'aws:cognito/identityProvider:IdentityProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            idp_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            provider_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            provider_name: Optional[pulumi.Input[str]] = None,
            provider_type: Optional[pulumi.Input[str]] = None,
            user_pool_id: Optional[pulumi.Input[str]] = None) -> 'IdentityProvider':
        """
        Get an existing IdentityProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attribute_mapping: The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] idp_identifiers: The list of identity providers.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] provider_details: The map of identity details, such as access token
        :param pulumi.Input[str] provider_name: The provider name
        :param pulumi.Input[str] provider_type: The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        :param pulumi.Input[str] user_pool_id: The user pool id
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityProviderState.__new__(_IdentityProviderState)

        __props__.__dict__["attribute_mapping"] = attribute_mapping
        __props__.__dict__["idp_identifiers"] = idp_identifiers
        __props__.__dict__["provider_details"] = provider_details
        __props__.__dict__["provider_name"] = provider_name
        __props__.__dict__["provider_type"] = provider_type
        __props__.__dict__["user_pool_id"] = user_pool_id
        return IdentityProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)
        """
        return pulumi.get(self, "attribute_mapping")

    @property
    @pulumi.getter(name="idpIdentifiers")
    def idp_identifiers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of identity providers.
        """
        return pulumi.get(self, "idp_identifiers")

    @property
    @pulumi.getter(name="providerDetails")
    def provider_details(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The map of identity details, such as access token
        """
        return pulumi.get(self, "provider_details")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[str]:
        """
        The provider name
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Output[str]:
        """
        The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)
        """
        return pulumi.get(self, "provider_type")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[str]:
        """
        The user pool id
        """
        return pulumi.get(self, "user_pool_id")

