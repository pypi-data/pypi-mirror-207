# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VirtualAddressArgs', 'VirtualAddress']

@pulumi.input_type
class VirtualAddressArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 advertize_route: Optional[pulumi.Input[str]] = None,
                 arp: Optional[pulumi.Input[bool]] = None,
                 auto_delete: Optional[pulumi.Input[bool]] = None,
                 conn_limit: Optional[pulumi.Input[int]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 icmp_echo: Optional[pulumi.Input[str]] = None,
                 traffic_group: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualAddress resource.
        :param pulumi.Input[str] name: Name of the virtual address
        :param pulumi.Input[str] advertize_route: Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        :param pulumi.Input[bool] arp: Enable or disable ARP for the virtual address
        :param pulumi.Input[bool] auto_delete: Automatically delete the virtual address with the virtual server
        :param pulumi.Input[int] conn_limit: Max number of connections for virtual address
        :param pulumi.Input[bool] enabled: Enable or disable the virtual address
        :param pulumi.Input[str] icmp_echo: Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        :param pulumi.Input[str] traffic_group: Specify the partition and traffic group
        """
        pulumi.set(__self__, "name", name)
        if advertize_route is not None:
            pulumi.set(__self__, "advertize_route", advertize_route)
        if arp is not None:
            pulumi.set(__self__, "arp", arp)
        if auto_delete is not None:
            pulumi.set(__self__, "auto_delete", auto_delete)
        if conn_limit is not None:
            pulumi.set(__self__, "conn_limit", conn_limit)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if icmp_echo is not None:
            pulumi.set(__self__, "icmp_echo", icmp_echo)
        if traffic_group is not None:
            pulumi.set(__self__, "traffic_group", traffic_group)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the virtual address
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="advertizeRoute")
    def advertize_route(self) -> Optional[pulumi.Input[str]]:
        """
        Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        """
        return pulumi.get(self, "advertize_route")

    @advertize_route.setter
    def advertize_route(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "advertize_route", value)

    @property
    @pulumi.getter
    def arp(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable ARP for the virtual address
        """
        return pulumi.get(self, "arp")

    @arp.setter
    def arp(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "arp", value)

    @property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        Automatically delete the virtual address with the virtual server
        """
        return pulumi.get(self, "auto_delete")

    @auto_delete.setter
    def auto_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_delete", value)

    @property
    @pulumi.getter(name="connLimit")
    def conn_limit(self) -> Optional[pulumi.Input[int]]:
        """
        Max number of connections for virtual address
        """
        return pulumi.get(self, "conn_limit")

    @conn_limit.setter
    def conn_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "conn_limit", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable the virtual address
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="icmpEcho")
    def icmp_echo(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        """
        return pulumi.get(self, "icmp_echo")

    @icmp_echo.setter
    def icmp_echo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icmp_echo", value)

    @property
    @pulumi.getter(name="trafficGroup")
    def traffic_group(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the partition and traffic group
        """
        return pulumi.get(self, "traffic_group")

    @traffic_group.setter
    def traffic_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "traffic_group", value)


@pulumi.input_type
class _VirtualAddressState:
    def __init__(__self__, *,
                 advertize_route: Optional[pulumi.Input[str]] = None,
                 arp: Optional[pulumi.Input[bool]] = None,
                 auto_delete: Optional[pulumi.Input[bool]] = None,
                 conn_limit: Optional[pulumi.Input[int]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 icmp_echo: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 traffic_group: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VirtualAddress resources.
        :param pulumi.Input[str] advertize_route: Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        :param pulumi.Input[bool] arp: Enable or disable ARP for the virtual address
        :param pulumi.Input[bool] auto_delete: Automatically delete the virtual address with the virtual server
        :param pulumi.Input[int] conn_limit: Max number of connections for virtual address
        :param pulumi.Input[bool] enabled: Enable or disable the virtual address
        :param pulumi.Input[str] icmp_echo: Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        :param pulumi.Input[str] name: Name of the virtual address
        :param pulumi.Input[str] traffic_group: Specify the partition and traffic group
        """
        if advertize_route is not None:
            pulumi.set(__self__, "advertize_route", advertize_route)
        if arp is not None:
            pulumi.set(__self__, "arp", arp)
        if auto_delete is not None:
            pulumi.set(__self__, "auto_delete", auto_delete)
        if conn_limit is not None:
            pulumi.set(__self__, "conn_limit", conn_limit)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if icmp_echo is not None:
            pulumi.set(__self__, "icmp_echo", icmp_echo)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if traffic_group is not None:
            pulumi.set(__self__, "traffic_group", traffic_group)

    @property
    @pulumi.getter(name="advertizeRoute")
    def advertize_route(self) -> Optional[pulumi.Input[str]]:
        """
        Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        """
        return pulumi.get(self, "advertize_route")

    @advertize_route.setter
    def advertize_route(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "advertize_route", value)

    @property
    @pulumi.getter
    def arp(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable ARP for the virtual address
        """
        return pulumi.get(self, "arp")

    @arp.setter
    def arp(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "arp", value)

    @property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        Automatically delete the virtual address with the virtual server
        """
        return pulumi.get(self, "auto_delete")

    @auto_delete.setter
    def auto_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_delete", value)

    @property
    @pulumi.getter(name="connLimit")
    def conn_limit(self) -> Optional[pulumi.Input[int]]:
        """
        Max number of connections for virtual address
        """
        return pulumi.get(self, "conn_limit")

    @conn_limit.setter
    def conn_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "conn_limit", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable the virtual address
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="icmpEcho")
    def icmp_echo(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        """
        return pulumi.get(self, "icmp_echo")

    @icmp_echo.setter
    def icmp_echo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icmp_echo", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the virtual address
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="trafficGroup")
    def traffic_group(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the partition and traffic group
        """
        return pulumi.get(self, "traffic_group")

    @traffic_group.setter
    def traffic_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "traffic_group", value)


class VirtualAddress(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advertize_route: Optional[pulumi.Input[str]] = None,
                 arp: Optional[pulumi.Input[bool]] = None,
                 auto_delete: Optional[pulumi.Input[bool]] = None,
                 conn_limit: Optional[pulumi.Input[int]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 icmp_echo: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 traffic_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `ltm.VirtualAddress` Configures Virtual Server

        For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/virtual_server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        vs_va = f5bigip.ltm.VirtualAddress("vsVa",
            advertize_route="enabled",
            name="/Common/xxxxx")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] advertize_route: Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        :param pulumi.Input[bool] arp: Enable or disable ARP for the virtual address
        :param pulumi.Input[bool] auto_delete: Automatically delete the virtual address with the virtual server
        :param pulumi.Input[int] conn_limit: Max number of connections for virtual address
        :param pulumi.Input[bool] enabled: Enable or disable the virtual address
        :param pulumi.Input[str] icmp_echo: Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        :param pulumi.Input[str] name: Name of the virtual address
        :param pulumi.Input[str] traffic_group: Specify the partition and traffic group
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualAddressArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `ltm.VirtualAddress` Configures Virtual Server

        For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/virtual_server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        vs_va = f5bigip.ltm.VirtualAddress("vsVa",
            advertize_route="enabled",
            name="/Common/xxxxx")
        ```

        :param str resource_name: The name of the resource.
        :param VirtualAddressArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualAddressArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advertize_route: Optional[pulumi.Input[str]] = None,
                 arp: Optional[pulumi.Input[bool]] = None,
                 auto_delete: Optional[pulumi.Input[bool]] = None,
                 conn_limit: Optional[pulumi.Input[int]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 icmp_echo: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 traffic_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualAddressArgs.__new__(VirtualAddressArgs)

            __props__.__dict__["advertize_route"] = advertize_route
            __props__.__dict__["arp"] = arp
            __props__.__dict__["auto_delete"] = auto_delete
            __props__.__dict__["conn_limit"] = conn_limit
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["icmp_echo"] = icmp_echo
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["traffic_group"] = traffic_group
        super(VirtualAddress, __self__).__init__(
            'f5bigip:ltm/virtualAddress:VirtualAddress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            advertize_route: Optional[pulumi.Input[str]] = None,
            arp: Optional[pulumi.Input[bool]] = None,
            auto_delete: Optional[pulumi.Input[bool]] = None,
            conn_limit: Optional[pulumi.Input[int]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            icmp_echo: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            traffic_group: Optional[pulumi.Input[str]] = None) -> 'VirtualAddress':
        """
        Get an existing VirtualAddress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] advertize_route: Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        :param pulumi.Input[bool] arp: Enable or disable ARP for the virtual address
        :param pulumi.Input[bool] auto_delete: Automatically delete the virtual address with the virtual server
        :param pulumi.Input[int] conn_limit: Max number of connections for virtual address
        :param pulumi.Input[bool] enabled: Enable or disable the virtual address
        :param pulumi.Input[str] icmp_echo: Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        :param pulumi.Input[str] name: Name of the virtual address
        :param pulumi.Input[str] traffic_group: Specify the partition and traffic group
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualAddressState.__new__(_VirtualAddressState)

        __props__.__dict__["advertize_route"] = advertize_route
        __props__.__dict__["arp"] = arp
        __props__.__dict__["auto_delete"] = auto_delete
        __props__.__dict__["conn_limit"] = conn_limit
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["icmp_echo"] = icmp_echo
        __props__.__dict__["name"] = name
        __props__.__dict__["traffic_group"] = traffic_group
        return VirtualAddress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advertizeRoute")
    def advertize_route(self) -> pulumi.Output[Optional[str]]:
        """
        Enabled dynamic routing of the address ( In versions prior to BIG-IP 13.0.0 HF1, you can configure the Route Advertisement option for a virtual address to be either Enabled or Disabled only. Beginning with BIG-IP 13.0.0 HF1, F5 added more settings for the Route Advertisement option. In addition, the Enabled setting is deprecated and replaced by the Selective setting. For more information, please look into KB article https://support.f5.com/csp/article/K85543242 )
        """
        return pulumi.get(self, "advertize_route")

    @property
    @pulumi.getter
    def arp(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable or disable ARP for the virtual address
        """
        return pulumi.get(self, "arp")

    @property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> pulumi.Output[Optional[bool]]:
        """
        Automatically delete the virtual address with the virtual server
        """
        return pulumi.get(self, "auto_delete")

    @property
    @pulumi.getter(name="connLimit")
    def conn_limit(self) -> pulumi.Output[Optional[int]]:
        """
        Max number of connections for virtual address
        """
        return pulumi.get(self, "conn_limit")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable or disable the virtual address
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="icmpEcho")
    def icmp_echo(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies how the system sends responses to ICMP echo requests on a per-virtual address basis.
        """
        return pulumi.get(self, "icmp_echo")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the virtual address
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="trafficGroup")
    def traffic_group(self) -> pulumi.Output[Optional[str]]:
        """
        Specify the partition and traffic group
        """
        return pulumi.get(self, "traffic_group")

