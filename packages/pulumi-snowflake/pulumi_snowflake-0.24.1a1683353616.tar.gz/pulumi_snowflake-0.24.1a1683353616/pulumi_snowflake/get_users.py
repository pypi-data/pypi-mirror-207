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
    def __init__(__self__, id=None, pattern=None, users=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if pattern and not isinstance(pattern, str):
            raise TypeError("Expected argument 'pattern' to be a str")
        pulumi.set(__self__, "pattern", pattern)
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
    @pulumi.getter
    def pattern(self) -> str:
        """
        Users pattern for which to return metadata. Please refer to LIKE keyword from snowflake documentation : https://docs.snowflake.com/en/sql-reference/sql/show-users.html#parameters
        """
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetUsersUserResult']:
        """
        The users in the database
        """
        return pulumi.get(self, "users")


class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            id=self.id,
            pattern=self.pattern,
            users=self.users)


def get_users(pattern: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsersResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_snowflake as snowflake

    current = snowflake.get_users(pattern="user1")
    ```


    :param str pattern: Users pattern for which to return metadata. Please refer to LIKE keyword from snowflake documentation : https://docs.snowflake.com/en/sql-reference/sql/show-users.html#parameters
    """
    __args__ = dict()
    __args__['pattern'] = pattern
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('snowflake:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult).value

    return AwaitableGetUsersResult(
        id=__ret__.id,
        pattern=__ret__.pattern,
        users=__ret__.users)


@_utilities.lift_output_func(get_users)
def get_users_output(pattern: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUsersResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_snowflake as snowflake

    current = snowflake.get_users(pattern="user1")
    ```


    :param str pattern: Users pattern for which to return metadata. Please refer to LIKE keyword from snowflake documentation : https://docs.snowflake.com/en/sql-reference/sql/show-users.html#parameters
    """
    ...
