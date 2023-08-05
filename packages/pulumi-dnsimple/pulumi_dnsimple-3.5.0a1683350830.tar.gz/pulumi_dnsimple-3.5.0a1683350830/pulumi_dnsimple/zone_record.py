# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ZoneRecordArgs', 'ZoneRecord']

@pulumi.input_type
class ZoneRecordArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 value: pulumi.Input[str],
                 zone_name: pulumi.Input[str],
                 priority: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZoneRecord resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "zone_name", zone_name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class _ZoneRecordState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 qualified_name: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZoneRecord resources.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if qualified_name is not None:
            pulumi.set(__self__, "qualified_name", qualified_name)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)
        if zone_name is not None:
            pulumi.set(__self__, "zone_name", zone_name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "qualified_name")

    @qualified_name.setter
    def qualified_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qualified_name", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_name", value)


class ZoneRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZoneRecord resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZoneRecord resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZoneRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneRecordArgs.__new__(ZoneRecordArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["ttl"] = ttl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            if zone_name is None and not opts.urn:
                raise TypeError("Missing required property 'zone_name'")
            __props__.__dict__["zone_name"] = zone_name
            __props__.__dict__["qualified_name"] = None
            __props__.__dict__["zone_id"] = None
        super(ZoneRecord, __self__).__init__(
            'dnsimple:index/zoneRecord:ZoneRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[str]] = None,
            qualified_name: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None,
            zone_name: Optional[pulumi.Input[str]] = None) -> 'ZoneRecord':
        """
        Get an existing ZoneRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneRecordState.__new__(_ZoneRecordState)

        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["qualified_name"] = qualified_name
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["type"] = type
        __props__.__dict__["value"] = value
        __props__.__dict__["zone_id"] = zone_id
        __props__.__dict__["zone_name"] = zone_name
        return ZoneRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[str]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "qualified_name")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "zone_id")

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "zone_name")

