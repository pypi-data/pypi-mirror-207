# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FastApplicationArgs', 'FastApplication']

@pulumi.input_type
class FastApplicationArgs:
    def __init__(__self__, *,
                 fast_json: pulumi.Input[str],
                 template: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FastApplication resource.
        :param pulumi.Input[str] fast_json: Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        :param pulumi.Input[str] template: Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        """
        pulumi.set(__self__, "fast_json", fast_json)
        if template is not None:
            pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter(name="fastJson")
    def fast_json(self) -> pulumi.Input[str]:
        """
        Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        """
        return pulumi.get(self, "fast_json")

    @fast_json.setter
    def fast_json(self, value: pulumi.Input[str]):
        pulumi.set(self, "fast_json", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[str]]:
        """
        Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template", value)


@pulumi.input_type
class _FastApplicationState:
    def __init__(__self__, *,
                 application: Optional[pulumi.Input[str]] = None,
                 fast_json: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 tenant: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FastApplication resources.
        :param pulumi.Input[str] application: A FAST application name.
        :param pulumi.Input[str] fast_json: Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        :param pulumi.Input[str] template: Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        :param pulumi.Input[str] tenant: A FAST tenant name on which you want to manage application.
        """
        if application is not None:
            pulumi.set(__self__, "application", application)
        if fast_json is not None:
            pulumi.set(__self__, "fast_json", fast_json)
        if template is not None:
            pulumi.set(__self__, "template", template)
        if tenant is not None:
            pulumi.set(__self__, "tenant", tenant)

    @property
    @pulumi.getter
    def application(self) -> Optional[pulumi.Input[str]]:
        """
        A FAST application name.
        """
        return pulumi.get(self, "application")

    @application.setter
    def application(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application", value)

    @property
    @pulumi.getter(name="fastJson")
    def fast_json(self) -> Optional[pulumi.Input[str]]:
        """
        Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        """
        return pulumi.get(self, "fast_json")

    @fast_json.setter
    def fast_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fast_json", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[str]]:
        """
        Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter
    def tenant(self) -> Optional[pulumi.Input[str]]:
        """
        A FAST tenant name on which you want to manage application.
        """
        return pulumi.get(self, "tenant")

    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant", value)


class FastApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fast_json: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `FastApplication` This resource will create and manage FAST applications on BIG-IP from provided JSON declaration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        foo_app = f5bigip.FastApplication("foo-app",
            fast_json=(lambda path: open(path).read())("new_fast_app.json"),
            template="examples/simple_http")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fast_json: Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        :param pulumi.Input[str] template: Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FastApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `FastApplication` This resource will create and manage FAST applications on BIG-IP from provided JSON declaration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        foo_app = f5bigip.FastApplication("foo-app",
            fast_json=(lambda path: open(path).read())("new_fast_app.json"),
            template="examples/simple_http")
        ```

        :param str resource_name: The name of the resource.
        :param FastApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FastApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fast_json: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FastApplicationArgs.__new__(FastApplicationArgs)

            if fast_json is None and not opts.urn:
                raise TypeError("Missing required property 'fast_json'")
            __props__.__dict__["fast_json"] = fast_json
            __props__.__dict__["template"] = template
            __props__.__dict__["application"] = None
            __props__.__dict__["tenant"] = None
        super(FastApplication, __self__).__init__(
            'f5bigip:index/fastApplication:FastApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application: Optional[pulumi.Input[str]] = None,
            fast_json: Optional[pulumi.Input[str]] = None,
            template: Optional[pulumi.Input[str]] = None,
            tenant: Optional[pulumi.Input[str]] = None) -> 'FastApplication':
        """
        Get an existing FastApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application: A FAST application name.
        :param pulumi.Input[str] fast_json: Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        :param pulumi.Input[str] template: Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        :param pulumi.Input[str] tenant: A FAST tenant name on which you want to manage application.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FastApplicationState.__new__(_FastApplicationState)

        __props__.__dict__["application"] = application
        __props__.__dict__["fast_json"] = fast_json
        __props__.__dict__["template"] = template
        __props__.__dict__["tenant"] = tenant
        return FastApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def application(self) -> pulumi.Output[str]:
        """
        A FAST application name.
        """
        return pulumi.get(self, "application")

    @property
    @pulumi.getter(name="fastJson")
    def fast_json(self) -> pulumi.Output[str]:
        """
        Path/Filename of Declarative FAST JSON which is a json file used with builtin ```file``` function
        """
        return pulumi.get(self, "fast_json")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional[str]]:
        """
        Name of installed FAST template used to create FAST application. This parameter is required when creating new resource.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter
    def tenant(self) -> pulumi.Output[str]:
        """
        A FAST tenant name on which you want to manage application.
        """
        return pulumi.get(self, "tenant")

