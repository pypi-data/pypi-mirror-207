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
from ._inputs import *

__all__ = [
    'GetTeamResult',
    'AwaitableGetTeamResult',
    'get_team',
    'get_team_output',
]

@pulumi.output_type
class GetTeamResult:
    """
    A collection of values returned by getTeam.
    """
    def __init__(__self__, description=None, id=None, members=None, name=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def members(self) -> Optional[Sequence['outputs.GetTeamMemberResult']]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetTeamResult(GetTeamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTeamResult(
            description=self.description,
            id=self.id,
            members=self.members,
            name=self.name)


def get_team(description: Optional[str] = None,
             members: Optional[Sequence[pulumi.InputType['GetTeamMemberArgs']]] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTeamResult:
    """
    Manages existing Team within Opsgenie.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_opsgenie as opsgenie

    sre_team = opsgenie.get_team(name="sre-team")
    ```


    :param str description: A description for this team.
    :param Sequence[pulumi.InputType['GetTeamMemberArgs']] members: A Member block as documented below.
    :param str name: The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['members'] = members
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('opsgenie:index/getTeam:getTeam', __args__, opts=opts, typ=GetTeamResult).value

    return AwaitableGetTeamResult(
        description=__ret__.description,
        id=__ret__.id,
        members=__ret__.members,
        name=__ret__.name)


@_utilities.lift_output_func(get_team)
def get_team_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                    members: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTeamMemberArgs']]]]] = None,
                    name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTeamResult]:
    """
    Manages existing Team within Opsgenie.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_opsgenie as opsgenie

    sre_team = opsgenie.get_team(name="sre-team")
    ```


    :param str description: A description for this team.
    :param Sequence[pulumi.InputType['GetTeamMemberArgs']] members: A Member block as documented below.
    :param str name: The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.
    """
    ...
