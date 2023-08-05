# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetUsersResult',
    'AwaitableGetUsersResult',
    'get_users',
    'get_users_output',
]

@pulumi.output_type
class GetUsersResult:
    """
    A collection of values returned by getUsers.
    """
    def __init__(__self__, id=None, team_ids=None, users=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if team_ids and not isinstance(team_ids, list):
            raise TypeError("Expected argument 'team_ids' to be a list")
        pulumi.set(__self__, "team_ids", team_ids)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="teamIds")
    def team_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "team_ids")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetUsersUserResult']:
        """
        List of users queried.
        """
        return pulumi.get(self, "users")


class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            id=self.id,
            team_ids=self.team_ids,
            users=self.users)


def get_users(team_ids: Optional[Sequence[str]] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsersResult:
    """
    Use this data source to get information about [list of users](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODIzMw-list-users) that you can use for other PagerDuty resources, optionally filtering by team ids.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    devops = pagerduty.get_team(name="devops")
    me = pagerduty.get_user(email="me@example.com")
    example_w_team = pagerduty.User("exampleWTeam", email="user-with-team@example.com")
    example = pagerduty.TeamMembership("example",
        team_id=pagerduty_team["devops"]["id"],
        user_id=example_w_team.id)
    all_users = pagerduty.get_users()
    from_devops_team = pagerduty.get_users(team_ids=[pagerduty_team["devops"]["id"]])
    ```


    :param Sequence[str] team_ids: List of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.
    """
    __args__ = dict()
    __args__['teamIds'] = team_ids
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('pagerduty:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult).value

    return AwaitableGetUsersResult(
        id=__ret__.id,
        team_ids=__ret__.team_ids,
        users=__ret__.users)


@_utilities.lift_output_func(get_users)
def get_users_output(team_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUsersResult]:
    """
    Use this data source to get information about [list of users](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODIzMw-list-users) that you can use for other PagerDuty resources, optionally filtering by team ids.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    devops = pagerduty.get_team(name="devops")
    me = pagerduty.get_user(email="me@example.com")
    example_w_team = pagerduty.User("exampleWTeam", email="user-with-team@example.com")
    example = pagerduty.TeamMembership("example",
        team_id=pagerduty_team["devops"]["id"],
        user_id=example_w_team.id)
    all_users = pagerduty.get_users()
    from_devops_team = pagerduty.get_users(team_ids=[pagerduty_team["devops"]["id"]])
    ```


    :param Sequence[str] team_ids: List of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.
    """
    ...
