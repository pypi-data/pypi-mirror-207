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
    'GetWafSignaturesResult',
    'AwaitableGetWafSignaturesResult',
    'get_waf_signatures',
    'get_waf_signatures_output',
]

@pulumi.output_type
class GetWafSignaturesResult:
    """
    A collection of values returned by getWafSignatures.
    """
    def __init__(__self__, accuracy=None, description=None, enabled=None, id=None, json=None, name=None, perform_staging=None, risk=None, signature_id=None, system_signature_id=None, tag=None, type=None):
        if accuracy and not isinstance(accuracy, str):
            raise TypeError("Expected argument 'accuracy' to be a str")
        pulumi.set(__self__, "accuracy", accuracy)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if perform_staging and not isinstance(perform_staging, bool):
            raise TypeError("Expected argument 'perform_staging' to be a bool")
        pulumi.set(__self__, "perform_staging", perform_staging)
        if risk and not isinstance(risk, str):
            raise TypeError("Expected argument 'risk' to be a str")
        pulumi.set(__self__, "risk", risk)
        if signature_id and not isinstance(signature_id, int):
            raise TypeError("Expected argument 'signature_id' to be a int")
        pulumi.set(__self__, "signature_id", signature_id)
        if system_signature_id and not isinstance(system_signature_id, str):
            raise TypeError("Expected argument 'system_signature_id' to be a str")
        pulumi.set(__self__, "system_signature_id", system_signature_id)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def accuracy(self) -> str:
        """
        The relative detection accuracy of the signature.
        """
        return pulumi.get(self, "accuracy")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the signature.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        return pulumi.get(self, "json")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the signature as configured on the system.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="performStaging")
    def perform_staging(self) -> Optional[bool]:
        return pulumi.get(self, "perform_staging")

    @property
    @pulumi.getter
    def risk(self) -> str:
        """
        The relative risk level of the attack that matches this signature.
        """
        return pulumi.get(self, "risk")

    @property
    @pulumi.getter(name="signatureId")
    def signature_id(self) -> int:
        """
        ID of the signature in the database.
        """
        return pulumi.get(self, "signature_id")

    @property
    @pulumi.getter(name="systemSignatureId")
    def system_signature_id(self) -> str:
        """
        System generated ID of the signature.
        """
        return pulumi.get(self, "system_signature_id")

    @property
    @pulumi.getter
    def tag(self) -> str:
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the signature.
        """
        return pulumi.get(self, "type")


class AwaitableGetWafSignaturesResult(GetWafSignaturesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWafSignaturesResult(
            accuracy=self.accuracy,
            description=self.description,
            enabled=self.enabled,
            id=self.id,
            json=self.json,
            name=self.name,
            perform_staging=self.perform_staging,
            risk=self.risk,
            signature_id=self.signature_id,
            system_signature_id=self.system_signature_id,
            tag=self.tag,
            type=self.type)


def get_waf_signatures(accuracy: Optional[str] = None,
                       description: Optional[str] = None,
                       enabled: Optional[bool] = None,
                       name: Optional[str] = None,
                       perform_staging: Optional[bool] = None,
                       risk: Optional[str] = None,
                       signature_id: Optional[int] = None,
                       system_signature_id: Optional[str] = None,
                       tag: Optional[str] = None,
                       type: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWafSignaturesResult:
    """
    Use this data source (`ssl_get_waf_signatures`) to get the details of attack signatures available on BIG-IP WAF

    ## Example Usage

    ```python
    import pulumi
    import pulumi_f5bigip as f5bigip

    w_afsig1 = f5bigip.ssl.get_waf_signatures(signature_id=200104004)
    ```


    :param str accuracy: The relative detection accuracy of the signature.
    :param str description: Description of the signature.
    :param str name: Name of the signature as configured on the system.
    :param str risk: The relative risk level of the attack that matches this signature.
    :param int signature_id: ID of the signature in the BIG-IP WAF database.
    :param str system_signature_id: System generated ID of the signature.
    :param str type: Type of the signature.
    """
    __args__ = dict()
    __args__['accuracy'] = accuracy
    __args__['description'] = description
    __args__['enabled'] = enabled
    __args__['name'] = name
    __args__['performStaging'] = perform_staging
    __args__['risk'] = risk
    __args__['signatureId'] = signature_id
    __args__['systemSignatureId'] = system_signature_id
    __args__['tag'] = tag
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('f5bigip:ssl/getWafSignatures:getWafSignatures', __args__, opts=opts, typ=GetWafSignaturesResult).value

    return AwaitableGetWafSignaturesResult(
        accuracy=__ret__.accuracy,
        description=__ret__.description,
        enabled=__ret__.enabled,
        id=__ret__.id,
        json=__ret__.json,
        name=__ret__.name,
        perform_staging=__ret__.perform_staging,
        risk=__ret__.risk,
        signature_id=__ret__.signature_id,
        system_signature_id=__ret__.system_signature_id,
        tag=__ret__.tag,
        type=__ret__.type)


@_utilities.lift_output_func(get_waf_signatures)
def get_waf_signatures_output(accuracy: Optional[pulumi.Input[Optional[str]]] = None,
                              description: Optional[pulumi.Input[Optional[str]]] = None,
                              enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              perform_staging: Optional[pulumi.Input[Optional[bool]]] = None,
                              risk: Optional[pulumi.Input[Optional[str]]] = None,
                              signature_id: Optional[pulumi.Input[int]] = None,
                              system_signature_id: Optional[pulumi.Input[Optional[str]]] = None,
                              tag: Optional[pulumi.Input[Optional[str]]] = None,
                              type: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWafSignaturesResult]:
    """
    Use this data source (`ssl_get_waf_signatures`) to get the details of attack signatures available on BIG-IP WAF

    ## Example Usage

    ```python
    import pulumi
    import pulumi_f5bigip as f5bigip

    w_afsig1 = f5bigip.ssl.get_waf_signatures(signature_id=200104004)
    ```


    :param str accuracy: The relative detection accuracy of the signature.
    :param str description: Description of the signature.
    :param str name: Name of the signature as configured on the system.
    :param str risk: The relative risk level of the attack that matches this signature.
    :param int signature_id: ID of the signature in the BIG-IP WAF database.
    :param str system_signature_id: System generated ID of the signature.
    :param str type: Type of the signature.
    """
    ...
