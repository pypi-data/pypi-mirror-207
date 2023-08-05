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
    'GetOidcResult',
    'AwaitableGetOidcResult',
    'get_oidc',
    'get_oidc_output',
]

@pulumi.output_type
class GetOidcResult:
    """
    A collection of values returned by getOidc.
    """
    def __init__(__self__, authorization_binding=None, authorization_url=None, client_id=None, client_secret=None, id=None, issuer_mode=None, issuer_url=None, jwks_binding=None, jwks_url=None, max_clock_skew=None, name=None, protocol_type=None, scopes=None, token_binding=None, token_url=None, type=None, user_info_binding=None, user_info_url=None):
        if authorization_binding and not isinstance(authorization_binding, str):
            raise TypeError("Expected argument 'authorization_binding' to be a str")
        pulumi.set(__self__, "authorization_binding", authorization_binding)
        if authorization_url and not isinstance(authorization_url, str):
            raise TypeError("Expected argument 'authorization_url' to be a str")
        pulumi.set(__self__, "authorization_url", authorization_url)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issuer_mode and not isinstance(issuer_mode, str):
            raise TypeError("Expected argument 'issuer_mode' to be a str")
        pulumi.set(__self__, "issuer_mode", issuer_mode)
        if issuer_url and not isinstance(issuer_url, str):
            raise TypeError("Expected argument 'issuer_url' to be a str")
        pulumi.set(__self__, "issuer_url", issuer_url)
        if jwks_binding and not isinstance(jwks_binding, str):
            raise TypeError("Expected argument 'jwks_binding' to be a str")
        pulumi.set(__self__, "jwks_binding", jwks_binding)
        if jwks_url and not isinstance(jwks_url, str):
            raise TypeError("Expected argument 'jwks_url' to be a str")
        pulumi.set(__self__, "jwks_url", jwks_url)
        if max_clock_skew and not isinstance(max_clock_skew, int):
            raise TypeError("Expected argument 'max_clock_skew' to be a int")
        pulumi.set(__self__, "max_clock_skew", max_clock_skew)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if protocol_type and not isinstance(protocol_type, str):
            raise TypeError("Expected argument 'protocol_type' to be a str")
        pulumi.set(__self__, "protocol_type", protocol_type)
        if scopes and not isinstance(scopes, list):
            raise TypeError("Expected argument 'scopes' to be a list")
        pulumi.set(__self__, "scopes", scopes)
        if token_binding and not isinstance(token_binding, str):
            raise TypeError("Expected argument 'token_binding' to be a str")
        pulumi.set(__self__, "token_binding", token_binding)
        if token_url and not isinstance(token_url, str):
            raise TypeError("Expected argument 'token_url' to be a str")
        pulumi.set(__self__, "token_url", token_url)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_info_binding and not isinstance(user_info_binding, str):
            raise TypeError("Expected argument 'user_info_binding' to be a str")
        pulumi.set(__self__, "user_info_binding", user_info_binding)
        if user_info_url and not isinstance(user_info_url, str):
            raise TypeError("Expected argument 'user_info_url' to be a str")
        pulumi.set(__self__, "user_info_url", user_info_url)

    @property
    @pulumi.getter(name="authorizationBinding")
    def authorization_binding(self) -> str:
        """
        The method of making an authorization request.
        """
        return pulumi.get(self, "authorization_binding")

    @property
    @pulumi.getter(name="authorizationUrl")
    def authorization_url(self) -> str:
        """
        IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.
        """
        return pulumi.get(self, "authorization_url")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Unique identifier issued by AS for the Okta IdP instance.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        """
        Client secret issued by AS for the Okta IdP instance.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        id of idp.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="issuerMode")
    def issuer_mode(self) -> str:
        """
        Indicates whether Okta uses the original Okta org domain URL, a custom domain URL, or dynamic.
        """
        return pulumi.get(self, "issuer_mode")

    @property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> str:
        """
        URI that identifies the issuer.
        """
        return pulumi.get(self, "issuer_url")

    @property
    @pulumi.getter(name="jwksBinding")
    def jwks_binding(self) -> str:
        """
        The method of making a request for the OIDC JWKS.
        """
        return pulumi.get(self, "jwks_binding")

    @property
    @pulumi.getter(name="jwksUrl")
    def jwks_url(self) -> str:
        """
        Endpoint where the keys signer publishes its keys in a JWK Set.
        """
        return pulumi.get(self, "jwks_url")

    @property
    @pulumi.getter(name="maxClockSkew")
    def max_clock_skew(self) -> int:
        """
        Maximum allowable clock-skew when processing messages from the IdP.
        """
        return pulumi.get(self, "max_clock_skew")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        name of the idp.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> str:
        """
        The type of protocol to use.
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter
    def scopes(self) -> Sequence[str]:
        """
        The scopes of the IdP.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter(name="tokenBinding")
    def token_binding(self) -> str:
        """
        The method of making a token request.
        """
        return pulumi.get(self, "token_binding")

    @property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> str:
        """
        IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.
        """
        return pulumi.get(self, "token_url")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        type of idp.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userInfoBinding")
    def user_info_binding(self) -> str:
        """
        The method of making a user info request.
        """
        return pulumi.get(self, "user_info_binding")

    @property
    @pulumi.getter(name="userInfoUrl")
    def user_info_url(self) -> str:
        """
        Protected resource endpoint that returns claims about the authenticated user.
        """
        return pulumi.get(self, "user_info_url")


class AwaitableGetOidcResult(GetOidcResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOidcResult(
            authorization_binding=self.authorization_binding,
            authorization_url=self.authorization_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            id=self.id,
            issuer_mode=self.issuer_mode,
            issuer_url=self.issuer_url,
            jwks_binding=self.jwks_binding,
            jwks_url=self.jwks_url,
            max_clock_skew=self.max_clock_skew,
            name=self.name,
            protocol_type=self.protocol_type,
            scopes=self.scopes,
            token_binding=self.token_binding,
            token_url=self.token_url,
            type=self.type,
            user_info_binding=self.user_info_binding,
            user_info_url=self.user_info_url)


def get_oidc(id: Optional[str] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOidcResult:
    """
    Use this data source to retrieve a OIDC IdP from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_oidc(name="Example Provider")
    ```


    :param str id: The id of the idp to retrieve, conflicts with `name`.
    :param str name: The name of the idp to retrieve, conflicts with `id`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:idp/getOidc:getOidc', __args__, opts=opts, typ=GetOidcResult).value

    return AwaitableGetOidcResult(
        authorization_binding=__ret__.authorization_binding,
        authorization_url=__ret__.authorization_url,
        client_id=__ret__.client_id,
        client_secret=__ret__.client_secret,
        id=__ret__.id,
        issuer_mode=__ret__.issuer_mode,
        issuer_url=__ret__.issuer_url,
        jwks_binding=__ret__.jwks_binding,
        jwks_url=__ret__.jwks_url,
        max_clock_skew=__ret__.max_clock_skew,
        name=__ret__.name,
        protocol_type=__ret__.protocol_type,
        scopes=__ret__.scopes,
        token_binding=__ret__.token_binding,
        token_url=__ret__.token_url,
        type=__ret__.type,
        user_info_binding=__ret__.user_info_binding,
        user_info_url=__ret__.user_info_url)


@_utilities.lift_output_func(get_oidc)
def get_oidc_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                    name: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOidcResult]:
    """
    Use this data source to retrieve a OIDC IdP from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_oidc(name="Example Provider")
    ```


    :param str id: The id of the idp to retrieve, conflicts with `name`.
    :param str name: The name of the idp to retrieve, conflicts with `id`.
    """
    ...
