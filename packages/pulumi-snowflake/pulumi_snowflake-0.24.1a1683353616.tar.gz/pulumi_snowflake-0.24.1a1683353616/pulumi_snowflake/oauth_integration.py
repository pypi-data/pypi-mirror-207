# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['OauthIntegrationArgs', 'OauthIntegration']

@pulumi.input_type
class OauthIntegrationArgs:
    def __init__(__self__, *,
                 oauth_client: pulumi.Input[str],
                 blocked_roles_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_client_type: Optional[pulumi.Input[str]] = None,
                 oauth_issue_refresh_tokens: Optional[pulumi.Input[bool]] = None,
                 oauth_redirect_uri: Optional[pulumi.Input[str]] = None,
                 oauth_refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 oauth_use_secondary_roles: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OauthIntegration resource.
        :param pulumi.Input[str] oauth_client: Specifies the OAuth client type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] blocked_roles_lists: List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        :param pulumi.Input[str] comment: Specifies a comment for the OAuth integration.
        :param pulumi.Input[bool] enabled: Specifies whether this OAuth integration is enabled or disabled.
        :param pulumi.Input[str] name: Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        :param pulumi.Input[str] oauth_client_type: Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        :param pulumi.Input[bool] oauth_issue_refresh_tokens: Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        :param pulumi.Input[str] oauth_redirect_uri: Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        :param pulumi.Input[int] oauth_refresh_token_validity: Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        :param pulumi.Input[str] oauth_use_secondary_roles: Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        pulumi.set(__self__, "oauth_client", oauth_client)
        if blocked_roles_lists is not None:
            pulumi.set(__self__, "blocked_roles_lists", blocked_roles_lists)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if oauth_client_type is not None:
            pulumi.set(__self__, "oauth_client_type", oauth_client_type)
        if oauth_issue_refresh_tokens is not None:
            pulumi.set(__self__, "oauth_issue_refresh_tokens", oauth_issue_refresh_tokens)
        if oauth_redirect_uri is not None:
            pulumi.set(__self__, "oauth_redirect_uri", oauth_redirect_uri)
        if oauth_refresh_token_validity is not None:
            pulumi.set(__self__, "oauth_refresh_token_validity", oauth_refresh_token_validity)
        if oauth_use_secondary_roles is not None:
            pulumi.set(__self__, "oauth_use_secondary_roles", oauth_use_secondary_roles)

    @property
    @pulumi.getter(name="oauthClient")
    def oauth_client(self) -> pulumi.Input[str]:
        """
        Specifies the OAuth client type.
        """
        return pulumi.get(self, "oauth_client")

    @oauth_client.setter
    def oauth_client(self, value: pulumi.Input[str]):
        pulumi.set(self, "oauth_client", value)

    @property
    @pulumi.getter(name="blockedRolesLists")
    def blocked_roles_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        """
        return pulumi.get(self, "blocked_roles_lists")

    @blocked_roles_lists.setter
    def blocked_roles_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "blocked_roles_lists", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a comment for the OAuth integration.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether this OAuth integration is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="oauthClientType")
    def oauth_client_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        """
        return pulumi.get(self, "oauth_client_type")

    @oauth_client_type.setter
    def oauth_client_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_client_type", value)

    @property
    @pulumi.getter(name="oauthIssueRefreshTokens")
    def oauth_issue_refresh_tokens(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        """
        return pulumi.get(self, "oauth_issue_refresh_tokens")

    @oauth_issue_refresh_tokens.setter
    def oauth_issue_refresh_tokens(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "oauth_issue_refresh_tokens", value)

    @property
    @pulumi.getter(name="oauthRedirectUri")
    def oauth_redirect_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        """
        return pulumi.get(self, "oauth_redirect_uri")

    @oauth_redirect_uri.setter
    def oauth_redirect_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_redirect_uri", value)

    @property
    @pulumi.getter(name="oauthRefreshTokenValidity")
    def oauth_refresh_token_validity(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        """
        return pulumi.get(self, "oauth_refresh_token_validity")

    @oauth_refresh_token_validity.setter
    def oauth_refresh_token_validity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "oauth_refresh_token_validity", value)

    @property
    @pulumi.getter(name="oauthUseSecondaryRoles")
    def oauth_use_secondary_roles(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        return pulumi.get(self, "oauth_use_secondary_roles")

    @oauth_use_secondary_roles.setter
    def oauth_use_secondary_roles(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_use_secondary_roles", value)


@pulumi.input_type
class _OauthIntegrationState:
    def __init__(__self__, *,
                 blocked_roles_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 created_on: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_client: Optional[pulumi.Input[str]] = None,
                 oauth_client_type: Optional[pulumi.Input[str]] = None,
                 oauth_issue_refresh_tokens: Optional[pulumi.Input[bool]] = None,
                 oauth_redirect_uri: Optional[pulumi.Input[str]] = None,
                 oauth_refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 oauth_use_secondary_roles: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OauthIntegration resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] blocked_roles_lists: List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        :param pulumi.Input[str] comment: Specifies a comment for the OAuth integration.
        :param pulumi.Input[str] created_on: Date and time when the OAuth integration was created.
        :param pulumi.Input[bool] enabled: Specifies whether this OAuth integration is enabled or disabled.
        :param pulumi.Input[str] name: Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        :param pulumi.Input[str] oauth_client: Specifies the OAuth client type.
        :param pulumi.Input[str] oauth_client_type: Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        :param pulumi.Input[bool] oauth_issue_refresh_tokens: Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        :param pulumi.Input[str] oauth_redirect_uri: Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        :param pulumi.Input[int] oauth_refresh_token_validity: Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        :param pulumi.Input[str] oauth_use_secondary_roles: Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        if blocked_roles_lists is not None:
            pulumi.set(__self__, "blocked_roles_lists", blocked_roles_lists)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if created_on is not None:
            pulumi.set(__self__, "created_on", created_on)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if oauth_client is not None:
            pulumi.set(__self__, "oauth_client", oauth_client)
        if oauth_client_type is not None:
            pulumi.set(__self__, "oauth_client_type", oauth_client_type)
        if oauth_issue_refresh_tokens is not None:
            pulumi.set(__self__, "oauth_issue_refresh_tokens", oauth_issue_refresh_tokens)
        if oauth_redirect_uri is not None:
            pulumi.set(__self__, "oauth_redirect_uri", oauth_redirect_uri)
        if oauth_refresh_token_validity is not None:
            pulumi.set(__self__, "oauth_refresh_token_validity", oauth_refresh_token_validity)
        if oauth_use_secondary_roles is not None:
            pulumi.set(__self__, "oauth_use_secondary_roles", oauth_use_secondary_roles)

    @property
    @pulumi.getter(name="blockedRolesLists")
    def blocked_roles_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        """
        return pulumi.get(self, "blocked_roles_lists")

    @blocked_roles_lists.setter
    def blocked_roles_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "blocked_roles_lists", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a comment for the OAuth integration.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time when the OAuth integration was created.
        """
        return pulumi.get(self, "created_on")

    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_on", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether this OAuth integration is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="oauthClient")
    def oauth_client(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the OAuth client type.
        """
        return pulumi.get(self, "oauth_client")

    @oauth_client.setter
    def oauth_client(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_client", value)

    @property
    @pulumi.getter(name="oauthClientType")
    def oauth_client_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        """
        return pulumi.get(self, "oauth_client_type")

    @oauth_client_type.setter
    def oauth_client_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_client_type", value)

    @property
    @pulumi.getter(name="oauthIssueRefreshTokens")
    def oauth_issue_refresh_tokens(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        """
        return pulumi.get(self, "oauth_issue_refresh_tokens")

    @oauth_issue_refresh_tokens.setter
    def oauth_issue_refresh_tokens(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "oauth_issue_refresh_tokens", value)

    @property
    @pulumi.getter(name="oauthRedirectUri")
    def oauth_redirect_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        """
        return pulumi.get(self, "oauth_redirect_uri")

    @oauth_redirect_uri.setter
    def oauth_redirect_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_redirect_uri", value)

    @property
    @pulumi.getter(name="oauthRefreshTokenValidity")
    def oauth_refresh_token_validity(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        """
        return pulumi.get(self, "oauth_refresh_token_validity")

    @oauth_refresh_token_validity.setter
    def oauth_refresh_token_validity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "oauth_refresh_token_validity", value)

    @property
    @pulumi.getter(name="oauthUseSecondaryRoles")
    def oauth_use_secondary_roles(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        return pulumi.get(self, "oauth_use_secondary_roles")

    @oauth_use_secondary_roles.setter
    def oauth_use_secondary_roles(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_use_secondary_roles", value)


class OauthIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blocked_roles_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_client: Optional[pulumi.Input[str]] = None,
                 oauth_client_type: Optional[pulumi.Input[str]] = None,
                 oauth_issue_refresh_tokens: Optional[pulumi.Input[bool]] = None,
                 oauth_redirect_uri: Optional[pulumi.Input[str]] = None,
                 oauth_refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 oauth_use_secondary_roles: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_snowflake as snowflake

        tableau_desktop = snowflake.OauthIntegration("tableauDesktop",
            blocked_roles_lists=["SYSADMIN"],
            enabled=True,
            oauth_client="TABLEAU_DESKTOP",
            oauth_issue_refresh_tokens=True,
            oauth_refresh_token_validity=3600)
        ```

        ## Import

        ```sh
         $ pulumi import snowflake:index/oauthIntegration:OauthIntegration example name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] blocked_roles_lists: List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        :param pulumi.Input[str] comment: Specifies a comment for the OAuth integration.
        :param pulumi.Input[bool] enabled: Specifies whether this OAuth integration is enabled or disabled.
        :param pulumi.Input[str] name: Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        :param pulumi.Input[str] oauth_client: Specifies the OAuth client type.
        :param pulumi.Input[str] oauth_client_type: Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        :param pulumi.Input[bool] oauth_issue_refresh_tokens: Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        :param pulumi.Input[str] oauth_redirect_uri: Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        :param pulumi.Input[int] oauth_refresh_token_validity: Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        :param pulumi.Input[str] oauth_use_secondary_roles: Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OauthIntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_snowflake as snowflake

        tableau_desktop = snowflake.OauthIntegration("tableauDesktop",
            blocked_roles_lists=["SYSADMIN"],
            enabled=True,
            oauth_client="TABLEAU_DESKTOP",
            oauth_issue_refresh_tokens=True,
            oauth_refresh_token_validity=3600)
        ```

        ## Import

        ```sh
         $ pulumi import snowflake:index/oauthIntegration:OauthIntegration example name
        ```

        :param str resource_name: The name of the resource.
        :param OauthIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OauthIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blocked_roles_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth_client: Optional[pulumi.Input[str]] = None,
                 oauth_client_type: Optional[pulumi.Input[str]] = None,
                 oauth_issue_refresh_tokens: Optional[pulumi.Input[bool]] = None,
                 oauth_redirect_uri: Optional[pulumi.Input[str]] = None,
                 oauth_refresh_token_validity: Optional[pulumi.Input[int]] = None,
                 oauth_use_secondary_roles: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OauthIntegrationArgs.__new__(OauthIntegrationArgs)

            __props__.__dict__["blocked_roles_lists"] = blocked_roles_lists
            __props__.__dict__["comment"] = comment
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            if oauth_client is None and not opts.urn:
                raise TypeError("Missing required property 'oauth_client'")
            __props__.__dict__["oauth_client"] = oauth_client
            __props__.__dict__["oauth_client_type"] = oauth_client_type
            __props__.__dict__["oauth_issue_refresh_tokens"] = oauth_issue_refresh_tokens
            __props__.__dict__["oauth_redirect_uri"] = oauth_redirect_uri
            __props__.__dict__["oauth_refresh_token_validity"] = oauth_refresh_token_validity
            __props__.__dict__["oauth_use_secondary_roles"] = oauth_use_secondary_roles
            __props__.__dict__["created_on"] = None
        super(OauthIntegration, __self__).__init__(
            'snowflake:index/oauthIntegration:OauthIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            blocked_roles_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            created_on: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            oauth_client: Optional[pulumi.Input[str]] = None,
            oauth_client_type: Optional[pulumi.Input[str]] = None,
            oauth_issue_refresh_tokens: Optional[pulumi.Input[bool]] = None,
            oauth_redirect_uri: Optional[pulumi.Input[str]] = None,
            oauth_refresh_token_validity: Optional[pulumi.Input[int]] = None,
            oauth_use_secondary_roles: Optional[pulumi.Input[str]] = None) -> 'OauthIntegration':
        """
        Get an existing OauthIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] blocked_roles_lists: List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        :param pulumi.Input[str] comment: Specifies a comment for the OAuth integration.
        :param pulumi.Input[str] created_on: Date and time when the OAuth integration was created.
        :param pulumi.Input[bool] enabled: Specifies whether this OAuth integration is enabled or disabled.
        :param pulumi.Input[str] name: Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        :param pulumi.Input[str] oauth_client: Specifies the OAuth client type.
        :param pulumi.Input[str] oauth_client_type: Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        :param pulumi.Input[bool] oauth_issue_refresh_tokens: Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        :param pulumi.Input[str] oauth_redirect_uri: Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        :param pulumi.Input[int] oauth_refresh_token_validity: Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        :param pulumi.Input[str] oauth_use_secondary_roles: Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OauthIntegrationState.__new__(_OauthIntegrationState)

        __props__.__dict__["blocked_roles_lists"] = blocked_roles_lists
        __props__.__dict__["comment"] = comment
        __props__.__dict__["created_on"] = created_on
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["oauth_client"] = oauth_client
        __props__.__dict__["oauth_client_type"] = oauth_client_type
        __props__.__dict__["oauth_issue_refresh_tokens"] = oauth_issue_refresh_tokens
        __props__.__dict__["oauth_redirect_uri"] = oauth_redirect_uri
        __props__.__dict__["oauth_refresh_token_validity"] = oauth_refresh_token_validity
        __props__.__dict__["oauth_use_secondary_roles"] = oauth_use_secondary_roles
        return OauthIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blockedRolesLists")
    def blocked_roles_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of roles that a user cannot explicitly consent to using after authenticating. Do not include ACCOUNTADMIN, ORGADMIN or SECURITYADMIN as they are already implicitly enforced and will cause in-place updates.
        """
        return pulumi.get(self, "blocked_roles_lists")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies a comment for the OAuth integration.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        Date and time when the OAuth integration was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether this OAuth integration is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the OAuth integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauthClient")
    def oauth_client(self) -> pulumi.Output[str]:
        """
        Specifies the OAuth client type.
        """
        return pulumi.get(self, "oauth_client")

    @property
    @pulumi.getter(name="oauthClientType")
    def oauth_client_type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the type of client being registered. Snowflake supports both confidential and public clients.
        """
        return pulumi.get(self, "oauth_client_type")

    @property
    @pulumi.getter(name="oauthIssueRefreshTokens")
    def oauth_issue_refresh_tokens(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to allow the client to exchange a refresh token for an access token when the current access token has expired.
        """
        return pulumi.get(self, "oauth_issue_refresh_tokens")

    @property
    @pulumi.getter(name="oauthRedirectUri")
    def oauth_redirect_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the client URI. After a user is authenticated, the web browser is redirected to this URI.
        """
        return pulumi.get(self, "oauth_redirect_uri")

    @property
    @pulumi.getter(name="oauthRefreshTokenValidity")
    def oauth_refresh_token_validity(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies how long refresh tokens should be valid (in seconds). OAUTH*ISSUE*REFRESH_TOKENS must be set to TRUE.
        """
        return pulumi.get(self, "oauth_refresh_token_validity")

    @property
    @pulumi.getter(name="oauthUseSecondaryRoles")
    def oauth_use_secondary_roles(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether default secondary roles set in the user properties are activated by default in the session being opened.
        """
        return pulumi.get(self, "oauth_use_secondary_roles")

