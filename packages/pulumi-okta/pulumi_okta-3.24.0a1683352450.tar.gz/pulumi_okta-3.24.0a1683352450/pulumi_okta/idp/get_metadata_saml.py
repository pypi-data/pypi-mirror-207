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
    'GetMetadataSamlResult',
    'AwaitableGetMetadataSamlResult',
    'get_metadata_saml',
    'get_metadata_saml_output',
]

@pulumi.output_type
class GetMetadataSamlResult:
    """
    A collection of values returned by getMetadataSaml.
    """
    def __init__(__self__, assertions_signed=None, authn_request_signed=None, encryption_certificate=None, entity_id=None, http_post_binding=None, http_redirect_binding=None, id=None, idp_id=None, metadata=None, signing_certificate=None):
        if assertions_signed and not isinstance(assertions_signed, bool):
            raise TypeError("Expected argument 'assertions_signed' to be a bool")
        pulumi.set(__self__, "assertions_signed", assertions_signed)
        if authn_request_signed and not isinstance(authn_request_signed, bool):
            raise TypeError("Expected argument 'authn_request_signed' to be a bool")
        pulumi.set(__self__, "authn_request_signed", authn_request_signed)
        if encryption_certificate and not isinstance(encryption_certificate, str):
            raise TypeError("Expected argument 'encryption_certificate' to be a str")
        pulumi.set(__self__, "encryption_certificate", encryption_certificate)
        if entity_id and not isinstance(entity_id, str):
            raise TypeError("Expected argument 'entity_id' to be a str")
        pulumi.set(__self__, "entity_id", entity_id)
        if http_post_binding and not isinstance(http_post_binding, str):
            raise TypeError("Expected argument 'http_post_binding' to be a str")
        pulumi.set(__self__, "http_post_binding", http_post_binding)
        if http_redirect_binding and not isinstance(http_redirect_binding, str):
            raise TypeError("Expected argument 'http_redirect_binding' to be a str")
        pulumi.set(__self__, "http_redirect_binding", http_redirect_binding)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idp_id and not isinstance(idp_id, str):
            raise TypeError("Expected argument 'idp_id' to be a str")
        pulumi.set(__self__, "idp_id", idp_id)
        if metadata and not isinstance(metadata, str):
            raise TypeError("Expected argument 'metadata' to be a str")
        pulumi.set(__self__, "metadata", metadata)
        if signing_certificate and not isinstance(signing_certificate, str):
            raise TypeError("Expected argument 'signing_certificate' to be a str")
        pulumi.set(__self__, "signing_certificate", signing_certificate)

    @property
    @pulumi.getter(name="assertionsSigned")
    def assertions_signed(self) -> bool:
        """
        whether assertions are signed.
        """
        return pulumi.get(self, "assertions_signed")

    @property
    @pulumi.getter(name="authnRequestSigned")
    def authn_request_signed(self) -> bool:
        """
        whether authn requests are signed.
        """
        return pulumi.get(self, "authn_request_signed")

    @property
    @pulumi.getter(name="encryptionCertificate")
    def encryption_certificate(self) -> str:
        """
        SAML request encryption certificate.
        """
        return pulumi.get(self, "encryption_certificate")

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> str:
        """
        Entity URL for instance `https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf`.
        """
        return pulumi.get(self, "entity_id")

    @property
    @pulumi.getter(name="httpPostBinding")
    def http_post_binding(self) -> str:
        """
        urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post location from the SAML metadata.
        """
        return pulumi.get(self, "http_post_binding")

    @property
    @pulumi.getter(name="httpRedirectBinding")
    def http_redirect_binding(self) -> str:
        """
        urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect location from the SAML metadata.
        """
        return pulumi.get(self, "http_redirect_binding")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idpId")
    def idp_id(self) -> Optional[str]:
        return pulumi.get(self, "idp_id")

    @property
    @pulumi.getter
    def metadata(self) -> str:
        """
        raw IdP metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="signingCertificate")
    def signing_certificate(self) -> str:
        """
        SAML request signing certificate.
        """
        return pulumi.get(self, "signing_certificate")


class AwaitableGetMetadataSamlResult(GetMetadataSamlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetadataSamlResult(
            assertions_signed=self.assertions_signed,
            authn_request_signed=self.authn_request_signed,
            encryption_certificate=self.encryption_certificate,
            entity_id=self.entity_id,
            http_post_binding=self.http_post_binding,
            http_redirect_binding=self.http_redirect_binding,
            id=self.id,
            idp_id=self.idp_id,
            metadata=self.metadata,
            signing_certificate=self.signing_certificate)


def get_metadata_saml(idp_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetadataSamlResult:
    """
    Use this data source to retrieve SAML IdP metadata from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_metadata_saml(idp_id="<idp id>")
    ```


    :param str idp_id: The id of the IdP to retrieve metadata for.
    """
    __args__ = dict()
    __args__['idpId'] = idp_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:idp/getMetadataSaml:getMetadataSaml', __args__, opts=opts, typ=GetMetadataSamlResult).value

    return AwaitableGetMetadataSamlResult(
        assertions_signed=__ret__.assertions_signed,
        authn_request_signed=__ret__.authn_request_signed,
        encryption_certificate=__ret__.encryption_certificate,
        entity_id=__ret__.entity_id,
        http_post_binding=__ret__.http_post_binding,
        http_redirect_binding=__ret__.http_redirect_binding,
        id=__ret__.id,
        idp_id=__ret__.idp_id,
        metadata=__ret__.metadata,
        signing_certificate=__ret__.signing_certificate)


@_utilities.lift_output_func(get_metadata_saml)
def get_metadata_saml_output(idp_id: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetadataSamlResult]:
    """
    Use this data source to retrieve SAML IdP metadata from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_metadata_saml(idp_id="<idp id>")
    ```


    :param str idp_id: The id of the IdP to retrieve metadata for.
    """
    ...
