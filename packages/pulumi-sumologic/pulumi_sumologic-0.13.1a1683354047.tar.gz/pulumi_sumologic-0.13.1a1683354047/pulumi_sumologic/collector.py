# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CollectorArgs', 'Collector']

@pulumi.input_type
class CollectorArgs:
    def __init__(__self__, *,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Collector resource.
        :param pulumi.Input[str] category: The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        :param pulumi.Input[str] description: The description of the collector.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fields: Map containing [key/value pairs][3].
        :param pulumi.Input[str] name: The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        :param pulumi.Input[str] timezone: The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the collector.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map containing [key/value pairs][3].
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


@pulumi.input_type
class _CollectorState:
    def __init__(__self__, *,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Collector resources.
        :param pulumi.Input[str] category: The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        :param pulumi.Input[str] description: The description of the collector.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fields: Map containing [key/value pairs][3].
        :param pulumi.Input[str] name: The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        :param pulumi.Input[str] timezone: The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the collector.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map containing [key/value pairs][3].
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


class Collector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a [Sumologic (Hosted) Collector][1].

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        collector = sumologic.Collector("collector",
            description="Just testing this",
            fields={
                "environment": "production",
            })
        ```

        ## Import

        Collectors can be imported using the collector id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/collector:Collector test 1234567890
        ```

         Collectors can also be imported using the collector name, which is unique per Sumo Logic account, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/collector:Collector test my_test_collector
        ```

         [1]https://help.sumologic.com/docs/send-data/hosted-collectors/ [2]https://en.wikipedia.org/wiki/Tz_database [3]https://help.sumologic.com/Manage/Fields

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        :param pulumi.Input[str] description: The description of the collector.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fields: Map containing [key/value pairs][3].
        :param pulumi.Input[str] name: The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        :param pulumi.Input[str] timezone: The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CollectorArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a [Sumologic (Hosted) Collector][1].

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        collector = sumologic.Collector("collector",
            description="Just testing this",
            fields={
                "environment": "production",
            })
        ```

        ## Import

        Collectors can be imported using the collector id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/collector:Collector test 1234567890
        ```

         Collectors can also be imported using the collector name, which is unique per Sumo Logic account, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/collector:Collector test my_test_collector
        ```

         [1]https://help.sumologic.com/docs/send-data/hosted-collectors/ [2]https://en.wikipedia.org/wiki/Tz_database [3]https://help.sumologic.com/Manage/Fields

        :param str resource_name: The name of the resource.
        :param CollectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CollectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CollectorArgs.__new__(CollectorArgs)

            __props__.__dict__["category"] = category
            __props__.__dict__["description"] = description
            __props__.__dict__["fields"] = fields
            __props__.__dict__["name"] = name
            __props__.__dict__["timezone"] = timezone
        super(Collector, __self__).__init__(
            'sumologic:index/collector:Collector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            category: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            timezone: Optional[pulumi.Input[str]] = None) -> 'Collector':
        """
        Get an existing Collector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        :param pulumi.Input[str] description: The description of the collector.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fields: Map containing [key/value pairs][3].
        :param pulumi.Input[str] name: The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        :param pulumi.Input[str] timezone: The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CollectorState.__new__(_CollectorState)

        __props__.__dict__["category"] = category
        __props__.__dict__["description"] = description
        __props__.__dict__["fields"] = fields
        __props__.__dict__["name"] = name
        __props__.__dict__["timezone"] = timezone
        return Collector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional[str]]:
        """
        The default source category for any source attached to this collector. Can be overridden in the configuration of said sources.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the collector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map containing [key/value pairs][3].
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the collector. This is required, and has to be unique. Changing this will force recreation the collector.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[str]]:
        """
        The time zone to use for this collector. The value follows the [tzdata](https://en.wikipedia.org/wiki/Tz_database) naming convention.
        """
        return pulumi.get(self, "timezone")

