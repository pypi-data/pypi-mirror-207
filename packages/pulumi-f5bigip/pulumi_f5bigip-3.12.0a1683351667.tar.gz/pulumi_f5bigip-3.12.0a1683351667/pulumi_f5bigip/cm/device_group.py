# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DeviceGroupArgs', 'DeviceGroup']

@pulumi.input_type
class DeviceGroupArgs:
    def __init__(__self__, *,
                 auto_sync: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 devices: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]]] = None,
                 full_load_on_sync: Optional[pulumi.Input[str]] = None,
                 incremental_config: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_failover: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 save_on_auto_sync: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DeviceGroup resource.
        :param pulumi.Input[str] auto_sync: Specifies if the device-group will automatically sync configuration data to its members
        :param pulumi.Input[str] description: Description of Device group
        :param pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]] devices: Name of the device to be included in device group, this need to be configured before using devicegroup resource
        :param pulumi.Input[str] full_load_on_sync: Specifies if the device-group will perform a full-load upon sync
        :param pulumi.Input[int] incremental_config: Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        :param pulumi.Input[str] name: Is the name of the device Group
        :param pulumi.Input[str] network_failover: Specifies if the device-group will use a network connection for failover
        :param pulumi.Input[str] partition: Device administrative partition
        :param pulumi.Input[str] save_on_auto_sync: Specifies whether the configuration should be saved upon auto-sync.
        :param pulumi.Input[str] type: Specifies if the device-group will be used for failover or resource syncing
        """
        if auto_sync is not None:
            pulumi.set(__self__, "auto_sync", auto_sync)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if devices is not None:
            pulumi.set(__self__, "devices", devices)
        if full_load_on_sync is not None:
            pulumi.set(__self__, "full_load_on_sync", full_load_on_sync)
        if incremental_config is not None:
            pulumi.set(__self__, "incremental_config", incremental_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_failover is not None:
            pulumi.set(__self__, "network_failover", network_failover)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if save_on_auto_sync is not None:
            pulumi.set(__self__, "save_on_auto_sync", save_on_auto_sync)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will automatically sync configuration data to its members
        """
        return pulumi.get(self, "auto_sync")

    @auto_sync.setter
    def auto_sync(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_sync", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of Device group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]]]:
        """
        Name of the device to be included in device group, this need to be configured before using devicegroup resource
        """
        return pulumi.get(self, "devices")

    @devices.setter
    def devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]]]):
        pulumi.set(self, "devices", value)

    @property
    @pulumi.getter(name="fullLoadOnSync")
    def full_load_on_sync(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will perform a full-load upon sync
        """
        return pulumi.get(self, "full_load_on_sync")

    @full_load_on_sync.setter
    def full_load_on_sync(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "full_load_on_sync", value)

    @property
    @pulumi.getter(name="incrementalConfig")
    def incremental_config(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        """
        return pulumi.get(self, "incremental_config")

    @incremental_config.setter
    def incremental_config(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "incremental_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Is the name of the device Group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkFailover")
    def network_failover(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will use a network connection for failover
        """
        return pulumi.get(self, "network_failover")

    @network_failover.setter
    def network_failover(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_failover", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Device administrative partition
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter(name="saveOnAutoSync")
    def save_on_auto_sync(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the configuration should be saved upon auto-sync.
        """
        return pulumi.get(self, "save_on_auto_sync")

    @save_on_auto_sync.setter
    def save_on_auto_sync(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "save_on_auto_sync", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will be used for failover or resource syncing
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _DeviceGroupState:
    def __init__(__self__, *,
                 auto_sync: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 devices: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]]] = None,
                 full_load_on_sync: Optional[pulumi.Input[str]] = None,
                 incremental_config: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_failover: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 save_on_auto_sync: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeviceGroup resources.
        :param pulumi.Input[str] auto_sync: Specifies if the device-group will automatically sync configuration data to its members
        :param pulumi.Input[str] description: Description of Device group
        :param pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]] devices: Name of the device to be included in device group, this need to be configured before using devicegroup resource
        :param pulumi.Input[str] full_load_on_sync: Specifies if the device-group will perform a full-load upon sync
        :param pulumi.Input[int] incremental_config: Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        :param pulumi.Input[str] name: Is the name of the device Group
        :param pulumi.Input[str] network_failover: Specifies if the device-group will use a network connection for failover
        :param pulumi.Input[str] partition: Device administrative partition
        :param pulumi.Input[str] save_on_auto_sync: Specifies whether the configuration should be saved upon auto-sync.
        :param pulumi.Input[str] type: Specifies if the device-group will be used for failover or resource syncing
        """
        if auto_sync is not None:
            pulumi.set(__self__, "auto_sync", auto_sync)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if devices is not None:
            pulumi.set(__self__, "devices", devices)
        if full_load_on_sync is not None:
            pulumi.set(__self__, "full_load_on_sync", full_load_on_sync)
        if incremental_config is not None:
            pulumi.set(__self__, "incremental_config", incremental_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_failover is not None:
            pulumi.set(__self__, "network_failover", network_failover)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if save_on_auto_sync is not None:
            pulumi.set(__self__, "save_on_auto_sync", save_on_auto_sync)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will automatically sync configuration data to its members
        """
        return pulumi.get(self, "auto_sync")

    @auto_sync.setter
    def auto_sync(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_sync", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of Device group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]]]:
        """
        Name of the device to be included in device group, this need to be configured before using devicegroup resource
        """
        return pulumi.get(self, "devices")

    @devices.setter
    def devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceGroupDeviceArgs']]]]):
        pulumi.set(self, "devices", value)

    @property
    @pulumi.getter(name="fullLoadOnSync")
    def full_load_on_sync(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will perform a full-load upon sync
        """
        return pulumi.get(self, "full_load_on_sync")

    @full_load_on_sync.setter
    def full_load_on_sync(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "full_load_on_sync", value)

    @property
    @pulumi.getter(name="incrementalConfig")
    def incremental_config(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        """
        return pulumi.get(self, "incremental_config")

    @incremental_config.setter
    def incremental_config(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "incremental_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Is the name of the device Group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkFailover")
    def network_failover(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will use a network connection for failover
        """
        return pulumi.get(self, "network_failover")

    @network_failover.setter
    def network_failover(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_failover", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Device administrative partition
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter(name="saveOnAutoSync")
    def save_on_auto_sync(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the configuration should be saved upon auto-sync.
        """
        return pulumi.get(self, "save_on_auto_sync")

    @save_on_auto_sync.setter
    def save_on_auto_sync(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "save_on_auto_sync", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies if the device-group will be used for failover or resource syncing
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class DeviceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_sync: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceGroupDeviceArgs']]]]] = None,
                 full_load_on_sync: Optional[pulumi.Input[str]] = None,
                 incremental_config: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_failover: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 save_on_auto_sync: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `cm.DeviceGroup` A device group is a collection of BIG-IP devices that are configured to securely synchronize their BIG-IP configuration data, and fail over when needed.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        my_new_devicegroup = f5bigip.cm.DeviceGroup("myNewDevicegroup",
            auto_sync="enabled",
            devices=[
                f5bigip.cm.DeviceGroupDeviceArgs(
                    name="bigip1.cisco.com",
                ),
                f5bigip.cm.DeviceGroupDeviceArgs(
                    name="bigip200.f5.com",
                ),
            ],
            full_load_on_sync="true",
            name="sanjose_devicegroup",
            type="sync-only")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_sync: Specifies if the device-group will automatically sync configuration data to its members
        :param pulumi.Input[str] description: Description of Device group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceGroupDeviceArgs']]]] devices: Name of the device to be included in device group, this need to be configured before using devicegroup resource
        :param pulumi.Input[str] full_load_on_sync: Specifies if the device-group will perform a full-load upon sync
        :param pulumi.Input[int] incremental_config: Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        :param pulumi.Input[str] name: Is the name of the device Group
        :param pulumi.Input[str] network_failover: Specifies if the device-group will use a network connection for failover
        :param pulumi.Input[str] partition: Device administrative partition
        :param pulumi.Input[str] save_on_auto_sync: Specifies whether the configuration should be saved upon auto-sync.
        :param pulumi.Input[str] type: Specifies if the device-group will be used for failover or resource syncing
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DeviceGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `cm.DeviceGroup` A device group is a collection of BIG-IP devices that are configured to securely synchronize their BIG-IP configuration data, and fail over when needed.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        my_new_devicegroup = f5bigip.cm.DeviceGroup("myNewDevicegroup",
            auto_sync="enabled",
            devices=[
                f5bigip.cm.DeviceGroupDeviceArgs(
                    name="bigip1.cisco.com",
                ),
                f5bigip.cm.DeviceGroupDeviceArgs(
                    name="bigip200.f5.com",
                ),
            ],
            full_load_on_sync="true",
            name="sanjose_devicegroup",
            type="sync-only")
        ```

        :param str resource_name: The name of the resource.
        :param DeviceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_sync: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceGroupDeviceArgs']]]]] = None,
                 full_load_on_sync: Optional[pulumi.Input[str]] = None,
                 incremental_config: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_failover: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 save_on_auto_sync: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceGroupArgs.__new__(DeviceGroupArgs)

            __props__.__dict__["auto_sync"] = auto_sync
            __props__.__dict__["description"] = description
            __props__.__dict__["devices"] = devices
            __props__.__dict__["full_load_on_sync"] = full_load_on_sync
            __props__.__dict__["incremental_config"] = incremental_config
            __props__.__dict__["name"] = name
            __props__.__dict__["network_failover"] = network_failover
            __props__.__dict__["partition"] = partition
            __props__.__dict__["save_on_auto_sync"] = save_on_auto_sync
            __props__.__dict__["type"] = type
        super(DeviceGroup, __self__).__init__(
            'f5bigip:cm/deviceGroup:DeviceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_sync: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceGroupDeviceArgs']]]]] = None,
            full_load_on_sync: Optional[pulumi.Input[str]] = None,
            incremental_config: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_failover: Optional[pulumi.Input[str]] = None,
            partition: Optional[pulumi.Input[str]] = None,
            save_on_auto_sync: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'DeviceGroup':
        """
        Get an existing DeviceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_sync: Specifies if the device-group will automatically sync configuration data to its members
        :param pulumi.Input[str] description: Description of Device group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceGroupDeviceArgs']]]] devices: Name of the device to be included in device group, this need to be configured before using devicegroup resource
        :param pulumi.Input[str] full_load_on_sync: Specifies if the device-group will perform a full-load upon sync
        :param pulumi.Input[int] incremental_config: Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        :param pulumi.Input[str] name: Is the name of the device Group
        :param pulumi.Input[str] network_failover: Specifies if the device-group will use a network connection for failover
        :param pulumi.Input[str] partition: Device administrative partition
        :param pulumi.Input[str] save_on_auto_sync: Specifies whether the configuration should be saved upon auto-sync.
        :param pulumi.Input[str] type: Specifies if the device-group will be used for failover or resource syncing
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeviceGroupState.__new__(_DeviceGroupState)

        __props__.__dict__["auto_sync"] = auto_sync
        __props__.__dict__["description"] = description
        __props__.__dict__["devices"] = devices
        __props__.__dict__["full_load_on_sync"] = full_load_on_sync
        __props__.__dict__["incremental_config"] = incremental_config
        __props__.__dict__["name"] = name
        __props__.__dict__["network_failover"] = network_failover
        __props__.__dict__["partition"] = partition
        __props__.__dict__["save_on_auto_sync"] = save_on_auto_sync
        __props__.__dict__["type"] = type
        return DeviceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies if the device-group will automatically sync configuration data to its members
        """
        return pulumi.get(self, "auto_sync")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of Device group
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def devices(self) -> pulumi.Output[Optional[Sequence['outputs.DeviceGroupDevice']]]:
        """
        Name of the device to be included in device group, this need to be configured before using devicegroup resource
        """
        return pulumi.get(self, "devices")

    @property
    @pulumi.getter(name="fullLoadOnSync")
    def full_load_on_sync(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies if the device-group will perform a full-load upon sync
        """
        return pulumi.get(self, "full_load_on_sync")

    @property
    @pulumi.getter(name="incrementalConfig")
    def incremental_config(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.
        """
        return pulumi.get(self, "incremental_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Is the name of the device Group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFailover")
    def network_failover(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies if the device-group will use a network connection for failover
        """
        return pulumi.get(self, "network_failover")

    @property
    @pulumi.getter
    def partition(self) -> pulumi.Output[Optional[str]]:
        """
        Device administrative partition
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter(name="saveOnAutoSync")
    def save_on_auto_sync(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether the configuration should be saved upon auto-sync.
        """
        return pulumi.get(self, "save_on_auto_sync")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies if the device-group will be used for failover or resource syncing
        """
        return pulumi.get(self, "type")

