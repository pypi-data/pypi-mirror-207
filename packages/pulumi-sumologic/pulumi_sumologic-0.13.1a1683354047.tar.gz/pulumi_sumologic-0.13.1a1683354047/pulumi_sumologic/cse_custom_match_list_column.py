# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CseCustomMatchListColumnArgs', 'CseCustomMatchListColumn']

@pulumi.input_type
class CseCustomMatchListColumnArgs:
    def __init__(__self__, *,
                 fields: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CseCustomMatchListColumn resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Custom Match List Column fields.
        :param pulumi.Input[str] name: Custom Match List Column name.
        """
        pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Custom Match List Column fields.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom Match List Column name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CseCustomMatchListColumnState:
    def __init__(__self__, *,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CseCustomMatchListColumn resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Custom Match List Column fields.
        :param pulumi.Input[str] name: Custom Match List Column name.
        """
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Custom Match List Column fields.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom Match List Column name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class CseCustomMatchListColumn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Sumologic CSE Custom Match List Column.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        custom_match_list_column = sumologic.CseCustomMatchListColumn("customMatchListColumn", fields=["srcDevice_ip"])
        ```

        ## Import

        Custom Match List Column can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseCustomMatchListColumn:CseCustomMatchListColumn custom_match_list_column id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Custom Match List Column fields.
        :param pulumi.Input[str] name: Custom Match List Column name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseCustomMatchListColumnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumologic CSE Custom Match List Column.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        custom_match_list_column = sumologic.CseCustomMatchListColumn("customMatchListColumn", fields=["srcDevice_ip"])
        ```

        ## Import

        Custom Match List Column can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseCustomMatchListColumn:CseCustomMatchListColumn custom_match_list_column id
        ```

        :param str resource_name: The name of the resource.
        :param CseCustomMatchListColumnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseCustomMatchListColumnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CseCustomMatchListColumnArgs.__new__(CseCustomMatchListColumnArgs)

            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            __props__.__dict__["name"] = name
        super(CseCustomMatchListColumn, __self__).__init__(
            'sumologic:index/cseCustomMatchListColumn:CseCustomMatchListColumn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'CseCustomMatchListColumn':
        """
        Get an existing CseCustomMatchListColumn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Custom Match List Column fields.
        :param pulumi.Input[str] name: Custom Match List Column name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseCustomMatchListColumnState.__new__(_CseCustomMatchListColumnState)

        __props__.__dict__["fields"] = fields
        __props__.__dict__["name"] = name
        return CseCustomMatchListColumn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[str]]:
        """
        Custom Match List Column fields.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Custom Match List Column name.
        """
        return pulumi.get(self, "name")

