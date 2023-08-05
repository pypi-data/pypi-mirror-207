# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SnmpArgs', 'Snmp']

@pulumi.input_type
class SnmpArgs:
    def __init__(__self__, *,
                 allowedaddresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sys_contact: Optional[pulumi.Input[str]] = None,
                 sys_location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Snmp resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowedaddresses: Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        :param pulumi.Input[str] sys_contact: Specifies the contact information for the system administrator.
        :param pulumi.Input[str] sys_location: Describes the system's physical location.
        """
        if allowedaddresses is not None:
            pulumi.set(__self__, "allowedaddresses", allowedaddresses)
        if sys_contact is not None:
            pulumi.set(__self__, "sys_contact", sys_contact)
        if sys_location is not None:
            pulumi.set(__self__, "sys_location", sys_location)

    @property
    @pulumi.getter
    def allowedaddresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        """
        return pulumi.get(self, "allowedaddresses")

    @allowedaddresses.setter
    def allowedaddresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowedaddresses", value)

    @property
    @pulumi.getter(name="sysContact")
    def sys_contact(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the contact information for the system administrator.
        """
        return pulumi.get(self, "sys_contact")

    @sys_contact.setter
    def sys_contact(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sys_contact", value)

    @property
    @pulumi.getter(name="sysLocation")
    def sys_location(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the system's physical location.
        """
        return pulumi.get(self, "sys_location")

    @sys_location.setter
    def sys_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sys_location", value)


@pulumi.input_type
class _SnmpState:
    def __init__(__self__, *,
                 allowedaddresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sys_contact: Optional[pulumi.Input[str]] = None,
                 sys_location: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Snmp resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowedaddresses: Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        :param pulumi.Input[str] sys_contact: Specifies the contact information for the system administrator.
        :param pulumi.Input[str] sys_location: Describes the system's physical location.
        """
        if allowedaddresses is not None:
            pulumi.set(__self__, "allowedaddresses", allowedaddresses)
        if sys_contact is not None:
            pulumi.set(__self__, "sys_contact", sys_contact)
        if sys_location is not None:
            pulumi.set(__self__, "sys_location", sys_location)

    @property
    @pulumi.getter
    def allowedaddresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        """
        return pulumi.get(self, "allowedaddresses")

    @allowedaddresses.setter
    def allowedaddresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowedaddresses", value)

    @property
    @pulumi.getter(name="sysContact")
    def sys_contact(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the contact information for the system administrator.
        """
        return pulumi.get(self, "sys_contact")

    @sys_contact.setter
    def sys_contact(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sys_contact", value)

    @property
    @pulumi.getter(name="sysLocation")
    def sys_location(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the system's physical location.
        """
        return pulumi.get(self, "sys_location")

    @sys_location.setter
    def sys_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sys_location", value)


class Snmp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowedaddresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sys_contact: Optional[pulumi.Input[str]] = None,
                 sys_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `sys.Snmp` provides details bout how to enable "ilx", "asm" "apm" resource on BIG-IP
        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        snmp = f5bigip.sys.Snmp("snmp",
            allowedaddresses=["202.10.10.2"],
            sys_contact=" NetOPsAdmin s.shitole@f5.com",
            sys_location="SeattleHQ")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowedaddresses: Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        :param pulumi.Input[str] sys_contact: Specifies the contact information for the system administrator.
        :param pulumi.Input[str] sys_location: Describes the system's physical location.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SnmpArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `sys.Snmp` provides details bout how to enable "ilx", "asm" "apm" resource on BIG-IP
        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        snmp = f5bigip.sys.Snmp("snmp",
            allowedaddresses=["202.10.10.2"],
            sys_contact=" NetOPsAdmin s.shitole@f5.com",
            sys_location="SeattleHQ")
        ```

        :param str resource_name: The name of the resource.
        :param SnmpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnmpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowedaddresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sys_contact: Optional[pulumi.Input[str]] = None,
                 sys_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SnmpArgs.__new__(SnmpArgs)

            __props__.__dict__["allowedaddresses"] = allowedaddresses
            __props__.__dict__["sys_contact"] = sys_contact
            __props__.__dict__["sys_location"] = sys_location
        super(Snmp, __self__).__init__(
            'f5bigip:sys/snmp:Snmp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowedaddresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            sys_contact: Optional[pulumi.Input[str]] = None,
            sys_location: Optional[pulumi.Input[str]] = None) -> 'Snmp':
        """
        Get an existing Snmp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowedaddresses: Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        :param pulumi.Input[str] sys_contact: Specifies the contact information for the system administrator.
        :param pulumi.Input[str] sys_location: Describes the system's physical location.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SnmpState.__new__(_SnmpState)

        __props__.__dict__["allowedaddresses"] = allowedaddresses
        __props__.__dict__["sys_contact"] = sys_contact
        __props__.__dict__["sys_location"] = sys_location
        return Snmp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def allowedaddresses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.
        """
        return pulumi.get(self, "allowedaddresses")

    @property
    @pulumi.getter(name="sysContact")
    def sys_contact(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the contact information for the system administrator.
        """
        return pulumi.get(self, "sys_contact")

    @property
    @pulumi.getter(name="sysLocation")
    def sys_location(self) -> pulumi.Output[Optional[str]]:
        """
        Describes the system's physical location.
        """
        return pulumi.get(self, "sys_location")

