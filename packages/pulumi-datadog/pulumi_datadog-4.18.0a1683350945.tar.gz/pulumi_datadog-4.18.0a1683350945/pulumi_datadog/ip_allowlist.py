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
from ._inputs import *

__all__ = ['IpAllowlistArgs', 'IpAllowlist']

@pulumi.input_type
class IpAllowlistArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]]] = None):
        """
        The set of arguments for constructing a IpAllowlist resource.
        :param pulumi.Input[bool] enabled: Whether the IP Allowlist is enabled.
        :param pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]] entries: Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        pulumi.set(__self__, "enabled", enabled)
        if entries is not None:
            pulumi.set(__self__, "entries", entries)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Whether the IP Allowlist is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]]]:
        """
        Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]]]):
        pulumi.set(self, "entries", value)


@pulumi.input_type
class _IpAllowlistState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]]] = None):
        """
        Input properties used for looking up and filtering IpAllowlist resources.
        :param pulumi.Input[bool] enabled: Whether the IP Allowlist is enabled.
        :param pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]] entries: Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if entries is not None:
            pulumi.set(__self__, "entries", entries)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the IP Allowlist is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]]]:
        """
        Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpAllowlistEntryArgs']]]]):
        pulumi.set(self, "entries", value)


class IpAllowlist(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAllowlistEntryArgs']]]]] = None,
                 __props__=None):
        """
        Provides the Datadog IP allowlist resource. This can be used to manage the Datadog IP allowlist

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Whether the IP Allowlist is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAllowlistEntryArgs']]]] entries: Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpAllowlistArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides the Datadog IP allowlist resource. This can be used to manage the Datadog IP allowlist

        :param str resource_name: The name of the resource.
        :param IpAllowlistArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpAllowlistArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAllowlistEntryArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpAllowlistArgs.__new__(IpAllowlistArgs)

            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["entries"] = entries
        super(IpAllowlist, __self__).__init__(
            'datadog:index/ipAllowlist:IpAllowlist',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAllowlistEntryArgs']]]]] = None) -> 'IpAllowlist':
        """
        Get an existing IpAllowlist resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Whether the IP Allowlist is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAllowlistEntryArgs']]]] entries: Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IpAllowlistState.__new__(_IpAllowlistState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["entries"] = entries
        return IpAllowlist(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether the IP Allowlist is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def entries(self) -> pulumi.Output[Optional[Sequence['outputs.IpAllowlistEntry']]]:
        """
        Set of objects containing an IP address or range of IP addresses in the allowlist and an accompanying note.
        """
        return pulumi.get(self, "entries")

