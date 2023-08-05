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

__all__ = [
    'GroupExternalId',
    'UserAddresses',
    'UserEmails',
    'UserExternalId',
    'UserName',
    'UserPhoneNumbers',
    'GetGroupAlternateIdentifierResult',
    'GetGroupAlternateIdentifierExternalIdResult',
    'GetGroupAlternateIdentifierUniqueAttributeResult',
    'GetGroupExternalIdResult',
    'GetGroupFilterResult',
    'GetUserAddressResult',
    'GetUserAlternateIdentifierResult',
    'GetUserAlternateIdentifierExternalIdResult',
    'GetUserAlternateIdentifierUniqueAttributeResult',
    'GetUserEmailResult',
    'GetUserExternalIdResult',
    'GetUserFilterResult',
    'GetUserNameResult',
    'GetUserPhoneNumberResult',
]

@pulumi.output_type
class GroupExternalId(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 issuer: Optional[str] = None):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> Optional[str]:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")


@pulumi.output_type
class UserAddresses(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "postalCode":
            suggest = "postal_code"
        elif key == "streetAddress":
            suggest = "street_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAddresses. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAddresses.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAddresses.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 country: Optional[str] = None,
                 formatted: Optional[str] = None,
                 locality: Optional[str] = None,
                 postal_code: Optional[str] = None,
                 primary: Optional[bool] = None,
                 region: Optional[str] = None,
                 street_address: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str country: The country that this address is in.
        :param str formatted: The name that is typically displayed when the address is shown for display.
        :param str locality: The address locality.
        :param str postal_code: The postal code of the address.
        :param bool primary: When `true`, this is the primary address associated with the user.
        :param str region: The region of the address.
        :param str street_address: The street of the address.
        :param str type: The type of address.
        """
        if country is not None:
            pulumi.set(__self__, "country", country)
        if formatted is not None:
            pulumi.set(__self__, "formatted", formatted)
        if locality is not None:
            pulumi.set(__self__, "locality", locality)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if street_address is not None:
            pulumi.set(__self__, "street_address", street_address)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def country(self) -> Optional[str]:
        """
        The country that this address is in.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def formatted(self) -> Optional[str]:
        """
        The name that is typically displayed when the address is shown for display.
        """
        return pulumi.get(self, "formatted")

    @property
    @pulumi.getter
    def locality(self) -> Optional[str]:
        """
        The address locality.
        """
        return pulumi.get(self, "locality")

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[str]:
        """
        The postal code of the address.
        """
        return pulumi.get(self, "postal_code")

    @property
    @pulumi.getter
    def primary(self) -> Optional[bool]:
        """
        When `true`, this is the primary address associated with the user.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region of the address.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[str]:
        """
        The street of the address.
        """
        return pulumi.get(self, "street_address")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of address.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class UserEmails(dict):
    def __init__(__self__, *,
                 primary: Optional[bool] = None,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param bool primary: When `true`, this is the primary email associated with the user.
        :param str type: The type of email.
        :param str value: The email address. This value must be unique across the identity store.
        """
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[bool]:
        """
        When `true`, this is the primary email associated with the user.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of email.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The email address. This value must be unique across the identity store.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class UserExternalId(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 issuer: Optional[str] = None):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> Optional[str]:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")


@pulumi.output_type
class UserName(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "familyName":
            suggest = "family_name"
        elif key == "givenName":
            suggest = "given_name"
        elif key == "honorificPrefix":
            suggest = "honorific_prefix"
        elif key == "honorificSuffix":
            suggest = "honorific_suffix"
        elif key == "middleName":
            suggest = "middle_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserName. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserName.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserName.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 family_name: str,
                 given_name: str,
                 formatted: Optional[str] = None,
                 honorific_prefix: Optional[str] = None,
                 honorific_suffix: Optional[str] = None,
                 middle_name: Optional[str] = None):
        """
        :param str family_name: The family name of the user.
        :param str given_name: The given name of the user.
        :param str formatted: The name that is typically displayed when the name is shown for display.
        :param str honorific_prefix: The honorific prefix of the user.
        :param str honorific_suffix: The honorific suffix of the user.
        :param str middle_name: The middle name of the user.
        """
        pulumi.set(__self__, "family_name", family_name)
        pulumi.set(__self__, "given_name", given_name)
        if formatted is not None:
            pulumi.set(__self__, "formatted", formatted)
        if honorific_prefix is not None:
            pulumi.set(__self__, "honorific_prefix", honorific_prefix)
        if honorific_suffix is not None:
            pulumi.set(__self__, "honorific_suffix", honorific_suffix)
        if middle_name is not None:
            pulumi.set(__self__, "middle_name", middle_name)

    @property
    @pulumi.getter(name="familyName")
    def family_name(self) -> str:
        """
        The family name of the user.
        """
        return pulumi.get(self, "family_name")

    @property
    @pulumi.getter(name="givenName")
    def given_name(self) -> str:
        """
        The given name of the user.
        """
        return pulumi.get(self, "given_name")

    @property
    @pulumi.getter
    def formatted(self) -> Optional[str]:
        """
        The name that is typically displayed when the name is shown for display.
        """
        return pulumi.get(self, "formatted")

    @property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> Optional[str]:
        """
        The honorific prefix of the user.
        """
        return pulumi.get(self, "honorific_prefix")

    @property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> Optional[str]:
        """
        The honorific suffix of the user.
        """
        return pulumi.get(self, "honorific_suffix")

    @property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[str]:
        """
        The middle name of the user.
        """
        return pulumi.get(self, "middle_name")


@pulumi.output_type
class UserPhoneNumbers(dict):
    def __init__(__self__, *,
                 primary: Optional[bool] = None,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param bool primary: When `true`, this is the primary phone number associated with the user.
        :param str type: The type of phone number.
        :param str value: The user's phone number.
        """
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[bool]:
        """
        When `true`, this is the primary phone number associated with the user.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of phone number.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The user's phone number.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetGroupAlternateIdentifierResult(dict):
    def __init__(__self__, *,
                 external_id: Optional['outputs.GetGroupAlternateIdentifierExternalIdResult'] = None,
                 unique_attribute: Optional['outputs.GetGroupAlternateIdentifierUniqueAttributeResult'] = None):
        """
        :param 'GetGroupAlternateIdentifierExternalIdArgs' external_id: Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        :param 'GetGroupAlternateIdentifierUniqueAttributeArgs' unique_attribute: An entity attribute that's unique to a specific entity. Detailed below.
        """
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if unique_attribute is not None:
            pulumi.set(__self__, "unique_attribute", unique_attribute)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional['outputs.GetGroupAlternateIdentifierExternalIdResult']:
        """
        Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(self) -> Optional['outputs.GetGroupAlternateIdentifierUniqueAttributeResult']:
        """
        An entity attribute that's unique to a specific entity. Detailed below.
        """
        return pulumi.get(self, "unique_attribute")


@pulumi.output_type
class GetGroupAlternateIdentifierExternalIdResult(dict):
    def __init__(__self__, *,
                 id: str,
                 issuer: str):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")


@pulumi.output_type
class GetGroupAlternateIdentifierUniqueAttributeResult(dict):
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. For example: `DisplayName`. Refer to the [Group data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html).
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. For example: `DisplayName`. Refer to the [Group data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html).
        """
        return pulumi.get(self, "attribute_path")

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")


@pulumi.output_type
class GetGroupExternalIdResult(dict):
    def __init__(__self__, *,
                 id: str,
                 issuer: str):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")


@pulumi.output_type
class GetGroupFilterResult(dict):
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        """
        return pulumi.get(self, "attribute_path")

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")


@pulumi.output_type
class GetUserAddressResult(dict):
    def __init__(__self__, *,
                 country: str,
                 formatted: str,
                 locality: str,
                 postal_code: str,
                 primary: bool,
                 region: str,
                 street_address: str,
                 type: str):
        """
        :param str country: The country that this address is in.
        :param str formatted: The name that is typically displayed when the name is shown for display.
        :param str locality: The address locality.
        :param str postal_code: The postal code of the address.
        :param bool primary: When `true`, this is the primary phone number associated with the user.
        :param str region: The region of the address.
        :param str street_address: The street of the address.
        :param str type: The type of phone number.
        """
        pulumi.set(__self__, "country", country)
        pulumi.set(__self__, "formatted", formatted)
        pulumi.set(__self__, "locality", locality)
        pulumi.set(__self__, "postal_code", postal_code)
        pulumi.set(__self__, "primary", primary)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "street_address", street_address)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        The country that this address is in.
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def formatted(self) -> str:
        """
        The name that is typically displayed when the name is shown for display.
        """
        return pulumi.get(self, "formatted")

    @property
    @pulumi.getter
    def locality(self) -> str:
        """
        The address locality.
        """
        return pulumi.get(self, "locality")

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> str:
        """
        The postal code of the address.
        """
        return pulumi.get(self, "postal_code")

    @property
    @pulumi.getter
    def primary(self) -> bool:
        """
        When `true`, this is the primary phone number associated with the user.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region of the address.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> str:
        """
        The street of the address.
        """
        return pulumi.get(self, "street_address")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of phone number.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetUserAlternateIdentifierResult(dict):
    def __init__(__self__, *,
                 external_id: Optional['outputs.GetUserAlternateIdentifierExternalIdResult'] = None,
                 unique_attribute: Optional['outputs.GetUserAlternateIdentifierUniqueAttributeResult'] = None):
        """
        :param 'GetUserAlternateIdentifierExternalIdArgs' external_id: Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        :param 'GetUserAlternateIdentifierUniqueAttributeArgs' unique_attribute: An entity attribute that's unique to a specific entity. Detailed below.
        """
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if unique_attribute is not None:
            pulumi.set(__self__, "unique_attribute", unique_attribute)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional['outputs.GetUserAlternateIdentifierExternalIdResult']:
        """
        Configuration block for filtering by the identifier issued by an external identity provider. Detailed below.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(self) -> Optional['outputs.GetUserAlternateIdentifierUniqueAttributeResult']:
        """
        An entity attribute that's unique to a specific entity. Detailed below.
        """
        return pulumi.get(self, "unique_attribute")


@pulumi.output_type
class GetUserAlternateIdentifierExternalIdResult(dict):
    def __init__(__self__, *,
                 id: str,
                 issuer: str):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")


@pulumi.output_type
class GetUserAlternateIdentifierUniqueAttributeResult(dict):
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. For example: `UserName`. Refer to the [User data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html).
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. For example: `UserName`. Refer to the [User data type](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html).
        """
        return pulumi.get(self, "attribute_path")

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")


@pulumi.output_type
class GetUserEmailResult(dict):
    def __init__(__self__, *,
                 primary: bool,
                 type: str,
                 value: str):
        """
        :param bool primary: When `true`, this is the primary phone number associated with the user.
        :param str type: The type of phone number.
        :param str value: The user's phone number.
        """
        pulumi.set(__self__, "primary", primary)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def primary(self) -> bool:
        """
        When `true`, this is the primary phone number associated with the user.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of phone number.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The user's phone number.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetUserExternalIdResult(dict):
    def __init__(__self__, *,
                 id: str,
                 issuer: str):
        """
        :param str id: The identifier issued to this resource by an external identity provider.
        :param str issuer: The issuer for an external identifier.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier issued to this resource by an external identity provider.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The issuer for an external identifier.
        """
        return pulumi.get(self, "issuer")


@pulumi.output_type
class GetUserFilterResult(dict):
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: Attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        :param str attribute_value: Value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        Attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        """
        return pulumi.get(self, "attribute_path")

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        Value for an attribute.
        """
        return pulumi.get(self, "attribute_value")


@pulumi.output_type
class GetUserNameResult(dict):
    def __init__(__self__, *,
                 family_name: str,
                 formatted: str,
                 given_name: str,
                 honorific_prefix: str,
                 honorific_suffix: str,
                 middle_name: str):
        """
        :param str family_name: The family name of the user.
        :param str formatted: The name that is typically displayed when the name is shown for display.
        :param str given_name: The given name of the user.
        :param str honorific_prefix: The honorific prefix of the user.
        :param str honorific_suffix: The honorific suffix of the user.
        :param str middle_name: The middle name of the user.
        """
        pulumi.set(__self__, "family_name", family_name)
        pulumi.set(__self__, "formatted", formatted)
        pulumi.set(__self__, "given_name", given_name)
        pulumi.set(__self__, "honorific_prefix", honorific_prefix)
        pulumi.set(__self__, "honorific_suffix", honorific_suffix)
        pulumi.set(__self__, "middle_name", middle_name)

    @property
    @pulumi.getter(name="familyName")
    def family_name(self) -> str:
        """
        The family name of the user.
        """
        return pulumi.get(self, "family_name")

    @property
    @pulumi.getter
    def formatted(self) -> str:
        """
        The name that is typically displayed when the name is shown for display.
        """
        return pulumi.get(self, "formatted")

    @property
    @pulumi.getter(name="givenName")
    def given_name(self) -> str:
        """
        The given name of the user.
        """
        return pulumi.get(self, "given_name")

    @property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> str:
        """
        The honorific prefix of the user.
        """
        return pulumi.get(self, "honorific_prefix")

    @property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> str:
        """
        The honorific suffix of the user.
        """
        return pulumi.get(self, "honorific_suffix")

    @property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> str:
        """
        The middle name of the user.
        """
        return pulumi.get(self, "middle_name")


@pulumi.output_type
class GetUserPhoneNumberResult(dict):
    def __init__(__self__, *,
                 primary: bool,
                 type: str,
                 value: str):
        """
        :param bool primary: When `true`, this is the primary phone number associated with the user.
        :param str type: The type of phone number.
        :param str value: The user's phone number.
        """
        pulumi.set(__self__, "primary", primary)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def primary(self) -> bool:
        """
        When `true`, this is the primary phone number associated with the user.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of phone number.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The user's phone number.
        """
        return pulumi.get(self, "value")


