# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'SchemaArrayOneOf',
    'SchemaMasterOverridePriority',
    'SchemaOneOf',
    'UserPasswordHash',
    'GetUserSearchResult',
    'GetUsersSearchResult',
    'GetUsersUserResult',
]

@pulumi.output_type
class SchemaArrayOneOf(dict):
    def __init__(__self__, *,
                 const: str,
                 title: str):
        """
        :param str const: value mapping to member of `enum`.
        :param str title: display name for the enum value.
        """
        pulumi.set(__self__, "const", const)
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def const(self) -> str:
        """
        value mapping to member of `enum`.
        """
        return pulumi.get(self, "const")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        display name for the enum value.
        """
        return pulumi.get(self, "title")


@pulumi.output_type
class SchemaMasterOverridePriority(dict):
    def __init__(__self__, *,
                 value: str,
                 type: Optional[str] = None):
        """
        :param str value: ID of profile source.
        :param str type: Type of profile source.
        """
        pulumi.set(__self__, "value", value)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        ID of profile source.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of profile source.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class SchemaOneOf(dict):
    def __init__(__self__, *,
                 const: str,
                 title: str):
        """
        :param str const: value mapping to member of `enum`.
        :param str title: display name for the enum value.
        """
        pulumi.set(__self__, "const", const)
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def const(self) -> str:
        """
        value mapping to member of `enum`.
        """
        return pulumi.get(self, "const")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        display name for the enum value.
        """
        return pulumi.get(self, "title")


@pulumi.output_type
class UserPasswordHash(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "saltOrder":
            suggest = "salt_order"
        elif key == "workFactor":
            suggest = "work_factor"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserPasswordHash. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserPasswordHash.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserPasswordHash.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 algorithm: str,
                 value: str,
                 salt: Optional[str] = None,
                 salt_order: Optional[str] = None,
                 work_factor: Optional[int] = None):
        """
        :param str value: For SHA-512, SHA-256, SHA-1, MD5, this is the actual base64-encoded hash of the password (and salt, if used).
               This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing
               the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be
               the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password.
        :param str salt: Only required for salted hashes. For BCRYPT, this specifies the radix64-encoded salt used to generate
               the hash, which must be 22 characters long. For other salted hashes, this specifies the base64-encoded salt used to generate the hash.
        :param str salt_order: Specifies whether salt was pre- or postfixed to the password before hashing. Only required for salted algorithms.
        :param int work_factor: Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm. Minimum value is 1, and maximum is 20.
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "value", value)
        if salt is not None:
            pulumi.set(__self__, "salt", salt)
        if salt_order is not None:
            pulumi.set(__self__, "salt_order", salt_order)
        if work_factor is not None:
            pulumi.set(__self__, "work_factor", work_factor)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        For SHA-512, SHA-256, SHA-1, MD5, this is the actual base64-encoded hash of the password (and salt, if used).
        This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing
        the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be
        the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def salt(self) -> Optional[str]:
        """
        Only required for salted hashes. For BCRYPT, this specifies the radix64-encoded salt used to generate
        the hash, which must be 22 characters long. For other salted hashes, this specifies the base64-encoded salt used to generate the hash.
        """
        return pulumi.get(self, "salt")

    @property
    @pulumi.getter(name="saltOrder")
    def salt_order(self) -> Optional[str]:
        """
        Specifies whether salt was pre- or postfixed to the password before hashing. Only required for salted algorithms.
        """
        return pulumi.get(self, "salt_order")

    @property
    @pulumi.getter(name="workFactor")
    def work_factor(self) -> Optional[int]:
        """
        Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm. Minimum value is 1, and maximum is 20.
        """
        return pulumi.get(self, "work_factor")


@pulumi.output_type
class GetUserSearchResult(dict):
    def __init__(__self__, *,
                 comparison: Optional[str] = None,
                 expression: Optional[str] = None,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str comparison: Comparison to use. Comparitors for strings: [`eq`, `ge`, `gt`, `le`, `lt`, `ne`, `pr`, `sw`](https://developer.okta.com/docs/reference/core-okta-api/#operators).
        :param str expression: A raw search expression string. If present it will override name/comparison/value.
        :param str name: Name of property to search against.
        :param str value: Value to compare with.
        """
        if comparison is not None:
            pulumi.set(__self__, "comparison", comparison)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def comparison(self) -> Optional[str]:
        """
        Comparison to use. Comparitors for strings: [`eq`, `ge`, `gt`, `le`, `lt`, `ne`, `pr`, `sw`](https://developer.okta.com/docs/reference/core-okta-api/#operators).
        """
        return pulumi.get(self, "comparison")

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        A raw search expression string. If present it will override name/comparison/value.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of property to search against.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value to compare with.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetUsersSearchResult(dict):
    def __init__(__self__, *,
                 comparison: Optional[str] = None,
                 expression: Optional[str] = None,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str comparison: Comparison to use. Comparitors for strings: [`eq`, `ge`, `gt`, `le`, `lt`, `ne`, `pr`, `sw`](https://developer.okta.com/docs/reference/core-okta-api/#operators).
        :param str expression: A raw search expression string. If present it will override name/comparison/value.
        :param str name: Name of property to search against.
        :param str value: Value to compare with.
        """
        if comparison is not None:
            pulumi.set(__self__, "comparison", comparison)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def comparison(self) -> Optional[str]:
        """
        Comparison to use. Comparitors for strings: [`eq`, `ge`, `gt`, `le`, `lt`, `ne`, `pr`, `sw`](https://developer.okta.com/docs/reference/core-okta-api/#operators).
        """
        return pulumi.get(self, "comparison")

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        A raw search expression string. If present it will override name/comparison/value.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of property to search against.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value to compare with.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetUsersUserResult(dict):
    def __init__(__self__, *,
                 admin_roles: Sequence[str],
                 city: str,
                 cost_center: str,
                 country_code: str,
                 custom_profile_attributes: str,
                 department: str,
                 display_name: str,
                 division: str,
                 email: str,
                 employee_number: str,
                 first_name: str,
                 group_memberships: Sequence[str],
                 honorific_prefix: str,
                 honorific_suffix: str,
                 id: str,
                 last_name: str,
                 locale: str,
                 login: str,
                 manager: str,
                 manager_id: str,
                 middle_name: str,
                 mobile_phone: str,
                 nick_name: str,
                 organization: str,
                 postal_address: str,
                 preferred_language: str,
                 primary_phone: str,
                 profile_url: str,
                 roles: Sequence[str],
                 second_email: str,
                 state: str,
                 status: str,
                 street_address: str,
                 timezone: str,
                 title: str,
                 user_type: str,
                 zip_code: str):
        """
        :param Sequence[str] admin_roles: Administrator roles assigned to user.
        :param str city: City or locality component of user's address.
        :param str cost_center: Name of a cost center assigned to user.
        :param str country_code: Country name component of user's address.
        :param str custom_profile_attributes: Raw JSON containing all custom profile attributes.
        :param str department: Name of user's department.
        :param str display_name: Name of the user, suitable for display to end users.
        :param str division: Name of user's division.
        :param str email: Primary email address of user.
        :param str employee_number: Organization or company assigned unique identifier for the user.
        :param str first_name: Given name of the user.
        :param Sequence[str] group_memberships: Groups user belongs to.
        :param str honorific_prefix: Honorific prefix(es) of the user, or title in most Western languages.
        :param str honorific_suffix: Honorific suffix(es) of the user.
        :param str last_name: Family name of the user.
        :param str locale: User's default location for purposes of localizing items such as currency, date time format, numerical representations, etc.
        :param str login: Unique identifier for the user.
        :param str manager: Display name of the user's manager.
        :param str manager_id: `id` of a user's manager.
        :param str middle_name: Middle name(s) of the user.
        :param str mobile_phone: Mobile phone number of user.
        :param str nick_name: Casual way to address the user in real life.
        :param str organization: Name of user's organization.
        :param str postal_address: Mailing address component of user's address.
        :param str preferred_language: User's preferred written or spoken languages.
        :param str primary_phone: Primary phone number of user such as home number.
        :param str profile_url: URL of user's online profile (e.g. a web page).
        :param str second_email: Secondary email address of user typically used for account recovery.
        :param str state: State or region component of user's address (region).
        :param str status: Current status of user.
        :param str street_address: Full street address component of user's address.
        :param str timezone: User's time zone.
        :param str title: User's title, such as "Vice President".
        :param str user_type: Used to describe the organization to user relationship such as "Employee" or "Contractor".
        :param str zip_code: Zipcode or postal code component of user's address (postalCode)
        """
        pulumi.set(__self__, "admin_roles", admin_roles)
        pulumi.set(__self__, "city", city)
        pulumi.set(__self__, "cost_center", cost_center)
        pulumi.set(__self__, "country_code", country_code)
        pulumi.set(__self__, "custom_profile_attributes", custom_profile_attributes)
        pulumi.set(__self__, "department", department)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "division", division)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "employee_number", employee_number)
        pulumi.set(__self__, "first_name", first_name)
        pulumi.set(__self__, "group_memberships", group_memberships)
        pulumi.set(__self__, "honorific_prefix", honorific_prefix)
        pulumi.set(__self__, "honorific_suffix", honorific_suffix)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "last_name", last_name)
        pulumi.set(__self__, "locale", locale)
        pulumi.set(__self__, "login", login)
        pulumi.set(__self__, "manager", manager)
        pulumi.set(__self__, "manager_id", manager_id)
        pulumi.set(__self__, "middle_name", middle_name)
        pulumi.set(__self__, "mobile_phone", mobile_phone)
        pulumi.set(__self__, "nick_name", nick_name)
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "postal_address", postal_address)
        pulumi.set(__self__, "preferred_language", preferred_language)
        pulumi.set(__self__, "primary_phone", primary_phone)
        pulumi.set(__self__, "profile_url", profile_url)
        pulumi.set(__self__, "roles", roles)
        pulumi.set(__self__, "second_email", second_email)
        pulumi.set(__self__, "state", state)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "street_address", street_address)
        pulumi.set(__self__, "timezone", timezone)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "user_type", user_type)
        pulumi.set(__self__, "zip_code", zip_code)

    @property
    @pulumi.getter(name="adminRoles")
    def admin_roles(self) -> Sequence[str]:
        """
        Administrator roles assigned to user.
        """
        return pulumi.get(self, "admin_roles")

    @property
    @pulumi.getter
    def city(self) -> str:
        """
        City or locality component of user's address.
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter(name="costCenter")
    def cost_center(self) -> str:
        """
        Name of a cost center assigned to user.
        """
        return pulumi.get(self, "cost_center")

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> str:
        """
        Country name component of user's address.
        """
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter(name="customProfileAttributes")
    def custom_profile_attributes(self) -> str:
        """
        Raw JSON containing all custom profile attributes.
        """
        return pulumi.get(self, "custom_profile_attributes")

    @property
    @pulumi.getter
    def department(self) -> str:
        """
        Name of user's department.
        """
        return pulumi.get(self, "department")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Name of the user, suitable for display to end users.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def division(self) -> str:
        """
        Name of user's division.
        """
        return pulumi.get(self, "division")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Primary email address of user.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="employeeNumber")
    def employee_number(self) -> str:
        """
        Organization or company assigned unique identifier for the user.
        """
        return pulumi.get(self, "employee_number")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        Given name of the user.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="groupMemberships")
    def group_memberships(self) -> Sequence[str]:
        """
        Groups user belongs to.
        """
        return pulumi.get(self, "group_memberships")

    @property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> str:
        """
        Honorific prefix(es) of the user, or title in most Western languages.
        """
        return pulumi.get(self, "honorific_prefix")

    @property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> str:
        """
        Honorific suffix(es) of the user.
        """
        return pulumi.get(self, "honorific_suffix")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        Family name of the user.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def locale(self) -> str:
        """
        User's default location for purposes of localizing items such as currency, date time format, numerical representations, etc.
        """
        return pulumi.get(self, "locale")

    @property
    @pulumi.getter
    def login(self) -> str:
        """
        Unique identifier for the user.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def manager(self) -> str:
        """
        Display name of the user's manager.
        """
        return pulumi.get(self, "manager")

    @property
    @pulumi.getter(name="managerId")
    def manager_id(self) -> str:
        """
        `id` of a user's manager.
        """
        return pulumi.get(self, "manager_id")

    @property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> str:
        """
        Middle name(s) of the user.
        """
        return pulumi.get(self, "middle_name")

    @property
    @pulumi.getter(name="mobilePhone")
    def mobile_phone(self) -> str:
        """
        Mobile phone number of user.
        """
        return pulumi.get(self, "mobile_phone")

    @property
    @pulumi.getter(name="nickName")
    def nick_name(self) -> str:
        """
        Casual way to address the user in real life.
        """
        return pulumi.get(self, "nick_name")

    @property
    @pulumi.getter
    def organization(self) -> str:
        """
        Name of user's organization.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter(name="postalAddress")
    def postal_address(self) -> str:
        """
        Mailing address component of user's address.
        """
        return pulumi.get(self, "postal_address")

    @property
    @pulumi.getter(name="preferredLanguage")
    def preferred_language(self) -> str:
        """
        User's preferred written or spoken languages.
        """
        return pulumi.get(self, "preferred_language")

    @property
    @pulumi.getter(name="primaryPhone")
    def primary_phone(self) -> str:
        """
        Primary phone number of user such as home number.
        """
        return pulumi.get(self, "primary_phone")

    @property
    @pulumi.getter(name="profileUrl")
    def profile_url(self) -> str:
        """
        URL of user's online profile (e.g. a web page).
        """
        return pulumi.get(self, "profile_url")

    @property
    @pulumi.getter
    def roles(self) -> Sequence[str]:
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="secondEmail")
    def second_email(self) -> str:
        """
        Secondary email address of user typically used for account recovery.
        """
        return pulumi.get(self, "second_email")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State or region component of user's address (region).
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current status of user.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> str:
        """
        Full street address component of user's address.
        """
        return pulumi.get(self, "street_address")

    @property
    @pulumi.getter
    def timezone(self) -> str:
        """
        User's time zone.
        """
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        User's title, such as "Vice President".
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> str:
        """
        Used to describe the organization to user relationship such as "Employee" or "Contractor".
        """
        return pulumi.get(self, "user_type")

    @property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> str:
        """
        Zipcode or postal code component of user's address (postalCode)
        """
        return pulumi.get(self, "zip_code")


