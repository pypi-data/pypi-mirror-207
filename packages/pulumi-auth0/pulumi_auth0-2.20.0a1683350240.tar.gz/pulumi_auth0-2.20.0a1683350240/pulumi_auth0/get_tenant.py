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
    'GetTenantResult',
    'AwaitableGetTenantResult',
    'get_tenant',
]

@pulumi.output_type
class GetTenantResult:
    """
    A collection of values returned by getTenant.
    """
    def __init__(__self__, allowed_logout_urls=None, change_passwords=None, default_audience=None, default_directory=None, default_redirection_uri=None, domain=None, enabled_locales=None, error_pages=None, flags=None, friendly_name=None, guardian_mfa_pages=None, id=None, idle_session_lifetime=None, management_api_identifier=None, picture_url=None, sandbox_version=None, session_cookies=None, session_lifetime=None, support_email=None, support_url=None, universal_logins=None):
        if allowed_logout_urls and not isinstance(allowed_logout_urls, list):
            raise TypeError("Expected argument 'allowed_logout_urls' to be a list")
        pulumi.set(__self__, "allowed_logout_urls", allowed_logout_urls)
        if change_passwords and not isinstance(change_passwords, list):
            raise TypeError("Expected argument 'change_passwords' to be a list")
        pulumi.set(__self__, "change_passwords", change_passwords)
        if default_audience and not isinstance(default_audience, str):
            raise TypeError("Expected argument 'default_audience' to be a str")
        pulumi.set(__self__, "default_audience", default_audience)
        if default_directory and not isinstance(default_directory, str):
            raise TypeError("Expected argument 'default_directory' to be a str")
        pulumi.set(__self__, "default_directory", default_directory)
        if default_redirection_uri and not isinstance(default_redirection_uri, str):
            raise TypeError("Expected argument 'default_redirection_uri' to be a str")
        pulumi.set(__self__, "default_redirection_uri", default_redirection_uri)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if enabled_locales and not isinstance(enabled_locales, list):
            raise TypeError("Expected argument 'enabled_locales' to be a list")
        pulumi.set(__self__, "enabled_locales", enabled_locales)
        if error_pages and not isinstance(error_pages, list):
            raise TypeError("Expected argument 'error_pages' to be a list")
        pulumi.set(__self__, "error_pages", error_pages)
        if flags and not isinstance(flags, list):
            raise TypeError("Expected argument 'flags' to be a list")
        pulumi.set(__self__, "flags", flags)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if guardian_mfa_pages and not isinstance(guardian_mfa_pages, list):
            raise TypeError("Expected argument 'guardian_mfa_pages' to be a list")
        pulumi.set(__self__, "guardian_mfa_pages", guardian_mfa_pages)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idle_session_lifetime and not isinstance(idle_session_lifetime, float):
            raise TypeError("Expected argument 'idle_session_lifetime' to be a float")
        pulumi.set(__self__, "idle_session_lifetime", idle_session_lifetime)
        if management_api_identifier and not isinstance(management_api_identifier, str):
            raise TypeError("Expected argument 'management_api_identifier' to be a str")
        pulumi.set(__self__, "management_api_identifier", management_api_identifier)
        if picture_url and not isinstance(picture_url, str):
            raise TypeError("Expected argument 'picture_url' to be a str")
        pulumi.set(__self__, "picture_url", picture_url)
        if sandbox_version and not isinstance(sandbox_version, str):
            raise TypeError("Expected argument 'sandbox_version' to be a str")
        pulumi.set(__self__, "sandbox_version", sandbox_version)
        if session_cookies and not isinstance(session_cookies, list):
            raise TypeError("Expected argument 'session_cookies' to be a list")
        pulumi.set(__self__, "session_cookies", session_cookies)
        if session_lifetime and not isinstance(session_lifetime, float):
            raise TypeError("Expected argument 'session_lifetime' to be a float")
        pulumi.set(__self__, "session_lifetime", session_lifetime)
        if support_email and not isinstance(support_email, str):
            raise TypeError("Expected argument 'support_email' to be a str")
        pulumi.set(__self__, "support_email", support_email)
        if support_url and not isinstance(support_url, str):
            raise TypeError("Expected argument 'support_url' to be a str")
        pulumi.set(__self__, "support_url", support_url)
        if universal_logins and not isinstance(universal_logins, list):
            raise TypeError("Expected argument 'universal_logins' to be a list")
        pulumi.set(__self__, "universal_logins", universal_logins)

    @property
    @pulumi.getter(name="allowedLogoutUrls")
    def allowed_logout_urls(self) -> Sequence[str]:
        """
        URLs that Auth0 may redirect to after logout.
        """
        return pulumi.get(self, "allowed_logout_urls")

    @property
    @pulumi.getter(name="changePasswords")
    def change_passwords(self) -> Sequence['outputs.GetTenantChangePasswordResult']:
        """
        Configuration settings for change password page.
        """
        return pulumi.get(self, "change_passwords")

    @property
    @pulumi.getter(name="defaultAudience")
    def default_audience(self) -> str:
        """
        API Audience to use by default for API Authorization flows. This setting is equivalent to appending the audience to every authorization request made to the tenant for every application.
        """
        return pulumi.get(self, "default_audience")

    @property
    @pulumi.getter(name="defaultDirectory")
    def default_directory(self) -> str:
        """
        Name of the connection to be used for Password Grant exchanges. Options include `auth0-adldap`, `ad`, `auth0`, `email`, `sms`, `waad`, and `adfs`.
        """
        return pulumi.get(self, "default_directory")

    @property
    @pulumi.getter(name="defaultRedirectionUri")
    def default_redirection_uri(self) -> str:
        """
        The default absolute redirection URI. Must be HTTPS or an empty string.
        """
        return pulumi.get(self, "default_redirection_uri")

    @property
    @pulumi.getter
    def domain(self) -> str:
        """
        Your Auth0 domain name.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="enabledLocales")
    def enabled_locales(self) -> Sequence[str]:
        """
        Supported locales for the user interface. The first locale in the list will be used to set the default locale.
        """
        return pulumi.get(self, "enabled_locales")

    @property
    @pulumi.getter(name="errorPages")
    def error_pages(self) -> Sequence['outputs.GetTenantErrorPageResult']:
        """
        Configuration settings for error pages.
        """
        return pulumi.get(self, "error_pages")

    @property
    @pulumi.getter
    def flags(self) -> Sequence['outputs.GetTenantFlagResult']:
        """
        Configuration settings for tenant flags.
        """
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> str:
        """
        Friendly name for the tenant.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="guardianMfaPages")
    def guardian_mfa_pages(self) -> Sequence['outputs.GetTenantGuardianMfaPageResult']:
        """
        Configuration settings for the Guardian MFA page.
        """
        return pulumi.get(self, "guardian_mfa_pages")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idleSessionLifetime")
    def idle_session_lifetime(self) -> float:
        """
        Number of hours during which a session can be inactive before the user must log in again.
        """
        return pulumi.get(self, "idle_session_lifetime")

    @property
    @pulumi.getter(name="managementApiIdentifier")
    def management_api_identifier(self) -> str:
        """
        The identifier value of the built-in Management API resource server, which can be used as an audience when configuring client grants.
        """
        return pulumi.get(self, "management_api_identifier")

    @property
    @pulumi.getter(name="pictureUrl")
    def picture_url(self) -> str:
        """
        URL of logo to be shown for the tenant. Recommended size is 150px x 150px. If no URL is provided, the Auth0 logo will be used.
        """
        return pulumi.get(self, "picture_url")

    @property
    @pulumi.getter(name="sandboxVersion")
    def sandbox_version(self) -> str:
        """
        Selected sandbox version for the extensibility environment, which allows you to use custom scripts to extend parts of Auth0's functionality.
        """
        return pulumi.get(self, "sandbox_version")

    @property
    @pulumi.getter(name="sessionCookies")
    def session_cookies(self) -> Sequence['outputs.GetTenantSessionCookyResult']:
        """
        Alters behavior of tenant's session cookie. Contains a single `mode` property.
        """
        return pulumi.get(self, "session_cookies")

    @property
    @pulumi.getter(name="sessionLifetime")
    def session_lifetime(self) -> float:
        """
        Number of hours during which a session will stay valid.
        """
        return pulumi.get(self, "session_lifetime")

    @property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> str:
        """
        Support email address for authenticating users.
        """
        return pulumi.get(self, "support_email")

    @property
    @pulumi.getter(name="supportUrl")
    def support_url(self) -> str:
        """
        Support URL for authenticating users.
        """
        return pulumi.get(self, "support_url")

    @property
    @pulumi.getter(name="universalLogins")
    def universal_logins(self) -> Sequence['outputs.GetTenantUniversalLoginResult']:
        """
        Configuration settings for Universal Login.
        """
        return pulumi.get(self, "universal_logins")


class AwaitableGetTenantResult(GetTenantResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTenantResult(
            allowed_logout_urls=self.allowed_logout_urls,
            change_passwords=self.change_passwords,
            default_audience=self.default_audience,
            default_directory=self.default_directory,
            default_redirection_uri=self.default_redirection_uri,
            domain=self.domain,
            enabled_locales=self.enabled_locales,
            error_pages=self.error_pages,
            flags=self.flags,
            friendly_name=self.friendly_name,
            guardian_mfa_pages=self.guardian_mfa_pages,
            id=self.id,
            idle_session_lifetime=self.idle_session_lifetime,
            management_api_identifier=self.management_api_identifier,
            picture_url=self.picture_url,
            sandbox_version=self.sandbox_version,
            session_cookies=self.session_cookies,
            session_lifetime=self.session_lifetime,
            support_email=self.support_email,
            support_url=self.support_url,
            universal_logins=self.universal_logins)


def get_tenant(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTenantResult:
    """
    Use this data source to access information about the tenant this provider is configured to access.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_auth0 as auth0

    my_tenant = auth0.get_tenant()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('auth0:index/getTenant:getTenant', __args__, opts=opts, typ=GetTenantResult).value

    return AwaitableGetTenantResult(
        allowed_logout_urls=__ret__.allowed_logout_urls,
        change_passwords=__ret__.change_passwords,
        default_audience=__ret__.default_audience,
        default_directory=__ret__.default_directory,
        default_redirection_uri=__ret__.default_redirection_uri,
        domain=__ret__.domain,
        enabled_locales=__ret__.enabled_locales,
        error_pages=__ret__.error_pages,
        flags=__ret__.flags,
        friendly_name=__ret__.friendly_name,
        guardian_mfa_pages=__ret__.guardian_mfa_pages,
        id=__ret__.id,
        idle_session_lifetime=__ret__.idle_session_lifetime,
        management_api_identifier=__ret__.management_api_identifier,
        picture_url=__ret__.picture_url,
        sandbox_version=__ret__.sandbox_version,
        session_cookies=__ret__.session_cookies,
        session_lifetime=__ret__.session_lifetime,
        support_email=__ret__.support_email,
        support_url=__ret__.support_url,
        universal_logins=__ret__.universal_logins)
