# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetLicenseResult',
    'AwaitableGetLicenseResult',
    'get_license',
    'get_license_output',
]

@pulumi.output_type
class GetLicenseResult:
    """
    A collection of values returned by getLicense.
    """
    def __init__(__self__, allocations_available=None, current_value=None, description=None, html_url=None, id=None, name=None, role_group=None, self=None, summary=None, type=None, valid_roles=None):
        if allocations_available and not isinstance(allocations_available, int):
            raise TypeError("Expected argument 'allocations_available' to be a int")
        pulumi.set(__self__, "allocations_available", allocations_available)
        if current_value and not isinstance(current_value, int):
            raise TypeError("Expected argument 'current_value' to be a int")
        pulumi.set(__self__, "current_value", current_value)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if html_url and not isinstance(html_url, str):
            raise TypeError("Expected argument 'html_url' to be a str")
        pulumi.set(__self__, "html_url", html_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_group and not isinstance(role_group, str):
            raise TypeError("Expected argument 'role_group' to be a str")
        pulumi.set(__self__, "role_group", role_group)
        if self and not isinstance(self, str):
            raise TypeError("Expected argument 'self' to be a str")
        pulumi.set(__self__, "self", self)
        if summary and not isinstance(summary, str):
            raise TypeError("Expected argument 'summary' to be a str")
        pulumi.set(__self__, "summary", summary)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if valid_roles and not isinstance(valid_roles, list):
            raise TypeError("Expected argument 'valid_roles' to be a list")
        pulumi.set(__self__, "valid_roles", valid_roles)

    @property
    @pulumi.getter(name="allocationsAvailable")
    def allocations_available(self) -> int:
        """
        Available allocations to assign to users
        """
        return pulumi.get(self, "allocations_available")

    @property
    @pulumi.getter(name="currentValue")
    def current_value(self) -> int:
        """
        The number of allocations already assigned to users
        """
        return pulumi.get(self, "current_value")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="htmlUrl")
    def html_url(self) -> str:
        return pulumi.get(self, "html_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleGroup")
    def role_group(self) -> str:
        """
        The role group for the license that determines the available `valid_roles`
        """
        return pulumi.get(self, "role_group")

    @property
    @pulumi.getter
    def self(self) -> str:
        return pulumi.get(self, "self")

    @property
    @pulumi.getter
    def summary(self) -> str:
        """
        Summary of the license
        """
        return pulumi.get(self, "summary")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validRoles")
    def valid_roles(self) -> Sequence[str]:
        """
        List of allowed roles that may be assigned to a user with this license
        """
        return pulumi.get(self, "valid_roles")


class AwaitableGetLicenseResult(GetLicenseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicenseResult(
            allocations_available=self.allocations_available,
            current_value=self.current_value,
            description=self.description,
            html_url=self.html_url,
            id=self.id,
            name=self.name,
            role_group=self.role_group,
            self=self.self,
            summary=self.summary,
            type=self.type,
            valid_roles=self.valid_roles)


def get_license(allocations_available: Optional[int] = None,
                current_value: Optional[int] = None,
                description: Optional[str] = None,
                html_url: Optional[str] = None,
                id: Optional[str] = None,
                name: Optional[str] = None,
                role_group: Optional[str] = None,
                self: Optional[str] = None,
                summary: Optional[str] = None,
                type: Optional[str] = None,
                valid_roles: Optional[Sequence[str]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicenseResult:
    """
    Use this data source to use a single purchased [license](https://developer.pagerduty.com/api-reference/4c10cb38f7381-list-licenses) to manage PagerDuty user resources. After applying changes to users' licenses, the `current_value` and `allocations_available` attributes of licenses will change.

    > It is preferred to set the `name` and `description` to their exact values or to set the `id`. However, this will require updating your configuration if the accounts products ever change. To avoid errors when account products change, you may set the `name` of a license to a valid substring such as `"Full User"` or `"Stakeholder"`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    invalid_roles = ["owner"]
    full_user = pagerduty.get_license(name="Full User",
        description="")
    example = pagerduty.User("example",
        email="125.greenholt.earline@graham.name",
        license=full_user.id,
        role="user")
    ```


    :param int allocations_available: Available allocations to assign to users
    :param int current_value: The number of allocations already assigned to users
    :param str description: Used to determine if the data config *description* is a valid substring of a valid license description assigned to the account.
    :param str id: Used to match the data config *id* with an exact match of a valid license ID assigned to the account.
    :param str name: Used to determine if the data config *name* is a valid substring of a valid license name assigned to the account.
    :param str role_group: The role group for the license that determines the available `valid_roles`
    :param str summary: Summary of the license
    :param Sequence[str] valid_roles: List of allowed roles that may be assigned to a user with this license
    """
    __args__ = dict()
    __args__['allocationsAvailable'] = allocations_available
    __args__['currentValue'] = current_value
    __args__['description'] = description
    __args__['htmlUrl'] = html_url
    __args__['id'] = id
    __args__['name'] = name
    __args__['roleGroup'] = role_group
    __args__['self'] = self
    __args__['summary'] = summary
    __args__['type'] = type
    __args__['validRoles'] = valid_roles
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('pagerduty:index/getLicense:getLicense', __args__, opts=opts, typ=GetLicenseResult).value

    return AwaitableGetLicenseResult(
        allocations_available=__ret__.allocations_available,
        current_value=__ret__.current_value,
        description=__ret__.description,
        html_url=__ret__.html_url,
        id=__ret__.id,
        name=__ret__.name,
        role_group=__ret__.role_group,
        self=__ret__.self,
        summary=__ret__.summary,
        type=__ret__.type,
        valid_roles=__ret__.valid_roles)


@_utilities.lift_output_func(get_license)
def get_license_output(allocations_available: Optional[pulumi.Input[Optional[int]]] = None,
                       current_value: Optional[pulumi.Input[Optional[int]]] = None,
                       description: Optional[pulumi.Input[Optional[str]]] = None,
                       html_url: Optional[pulumi.Input[Optional[str]]] = None,
                       id: Optional[pulumi.Input[Optional[str]]] = None,
                       name: Optional[pulumi.Input[Optional[str]]] = None,
                       role_group: Optional[pulumi.Input[Optional[str]]] = None,
                       self: Optional[pulumi.Input[Optional[str]]] = None,
                       summary: Optional[pulumi.Input[Optional[str]]] = None,
                       type: Optional[pulumi.Input[Optional[str]]] = None,
                       valid_roles: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLicenseResult]:
    """
    Use this data source to use a single purchased [license](https://developer.pagerduty.com/api-reference/4c10cb38f7381-list-licenses) to manage PagerDuty user resources. After applying changes to users' licenses, the `current_value` and `allocations_available` attributes of licenses will change.

    > It is preferred to set the `name` and `description` to their exact values or to set the `id`. However, this will require updating your configuration if the accounts products ever change. To avoid errors when account products change, you may set the `name` of a license to a valid substring such as `"Full User"` or `"Stakeholder"`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    invalid_roles = ["owner"]
    full_user = pagerduty.get_license(name="Full User",
        description="")
    example = pagerduty.User("example",
        email="125.greenholt.earline@graham.name",
        license=full_user.id,
        role="user")
    ```


    :param int allocations_available: Available allocations to assign to users
    :param int current_value: The number of allocations already assigned to users
    :param str description: Used to determine if the data config *description* is a valid substring of a valid license description assigned to the account.
    :param str id: Used to match the data config *id* with an exact match of a valid license ID assigned to the account.
    :param str name: Used to determine if the data config *name* is a valid substring of a valid license name assigned to the account.
    :param str role_group: The role group for the license that determines the available `valid_roles`
    :param str summary: Summary of the license
    :param Sequence[str] valid_roles: List of allowed roles that may be assigned to a user with this license
    """
    ...
