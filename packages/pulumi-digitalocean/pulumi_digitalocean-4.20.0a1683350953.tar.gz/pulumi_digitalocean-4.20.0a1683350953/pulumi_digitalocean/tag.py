# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] name: The name of the tag
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TagState:
    def __init__(__self__, *,
                 databases_count: Optional[pulumi.Input[int]] = None,
                 droplets_count: Optional[pulumi.Input[int]] = None,
                 images_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 total_resource_count: Optional[pulumi.Input[int]] = None,
                 volume_snapshots_count: Optional[pulumi.Input[int]] = None,
                 volumes_count: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Tag resources.
        :param pulumi.Input[int] databases_count: A count of the database clusters that the tag is applied to.
        :param pulumi.Input[int] droplets_count: A count of the Droplets the tag is applied to.
        :param pulumi.Input[int] images_count: A count of the images that the tag is applied to.
        :param pulumi.Input[str] name: The name of the tag
        :param pulumi.Input[int] total_resource_count: A count of the total number of resources that the tag is applied to.
        :param pulumi.Input[int] volume_snapshots_count: A count of the volume snapshots that the tag is applied to.
        :param pulumi.Input[int] volumes_count: A count of the volumes that the tag is applied to.
        """
        if databases_count is not None:
            pulumi.set(__self__, "databases_count", databases_count)
        if droplets_count is not None:
            pulumi.set(__self__, "droplets_count", droplets_count)
        if images_count is not None:
            pulumi.set(__self__, "images_count", images_count)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if total_resource_count is not None:
            pulumi.set(__self__, "total_resource_count", total_resource_count)
        if volume_snapshots_count is not None:
            pulumi.set(__self__, "volume_snapshots_count", volume_snapshots_count)
        if volumes_count is not None:
            pulumi.set(__self__, "volumes_count", volumes_count)

    @property
    @pulumi.getter(name="databasesCount")
    def databases_count(self) -> Optional[pulumi.Input[int]]:
        """
        A count of the database clusters that the tag is applied to.
        """
        return pulumi.get(self, "databases_count")

    @databases_count.setter
    def databases_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "databases_count", value)

    @property
    @pulumi.getter(name="dropletsCount")
    def droplets_count(self) -> Optional[pulumi.Input[int]]:
        """
        A count of the Droplets the tag is applied to.
        """
        return pulumi.get(self, "droplets_count")

    @droplets_count.setter
    def droplets_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "droplets_count", value)

    @property
    @pulumi.getter(name="imagesCount")
    def images_count(self) -> Optional[pulumi.Input[int]]:
        """
        A count of the images that the tag is applied to.
        """
        return pulumi.get(self, "images_count")

    @images_count.setter
    def images_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "images_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="totalResourceCount")
    def total_resource_count(self) -> Optional[pulumi.Input[int]]:
        """
        A count of the total number of resources that the tag is applied to.
        """
        return pulumi.get(self, "total_resource_count")

    @total_resource_count.setter
    def total_resource_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total_resource_count", value)

    @property
    @pulumi.getter(name="volumeSnapshotsCount")
    def volume_snapshots_count(self) -> Optional[pulumi.Input[int]]:
        """
        A count of the volume snapshots that the tag is applied to.
        """
        return pulumi.get(self, "volume_snapshots_count")

    @volume_snapshots_count.setter
    def volume_snapshots_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "volume_snapshots_count", value)

    @property
    @pulumi.getter(name="volumesCount")
    def volumes_count(self) -> Optional[pulumi.Input[int]]:
        """
        A count of the volumes that the tag is applied to.
        """
        return pulumi.get(self, "volumes_count")

    @volumes_count.setter
    def volumes_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "volumes_count", value)


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DigitalOcean Tag resource. A Tag is a label that can be applied to a
        Droplet resource in order to better organize or facilitate the lookups and
        actions on it. Tags created with this resource can be referenced in your Droplet
        configuration via their ID or name.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        # Create a new tag
        foobar = digitalocean.Tag("foobar")
        # Create a new Droplet in nyc3 with the foobar tag
        web = digitalocean.Droplet("web",
            image="ubuntu-18-04-x64",
            region="nyc3",
            size="s-1vcpu-1gb",
            tags=[foobar.id])
        ```

        ## Import

        Tags can be imported using the `name`, e.g.

        ```sh
         $ pulumi import digitalocean:index/tag:Tag mytag tagname
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the tag
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TagArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DigitalOcean Tag resource. A Tag is a label that can be applied to a
        Droplet resource in order to better organize or facilitate the lookups and
        actions on it. Tags created with this resource can be referenced in your Droplet
        configuration via their ID or name.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        # Create a new tag
        foobar = digitalocean.Tag("foobar")
        # Create a new Droplet in nyc3 with the foobar tag
        web = digitalocean.Droplet("web",
            image="ubuntu-18-04-x64",
            region="nyc3",
            size="s-1vcpu-1gb",
            tags=[foobar.id])
        ```

        ## Import

        Tags can be imported using the `name`, e.g.

        ```sh
         $ pulumi import digitalocean:index/tag:Tag mytag tagname
        ```

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["databases_count"] = None
            __props__.__dict__["droplets_count"] = None
            __props__.__dict__["images_count"] = None
            __props__.__dict__["total_resource_count"] = None
            __props__.__dict__["volume_snapshots_count"] = None
            __props__.__dict__["volumes_count"] = None
        super(Tag, __self__).__init__(
            'digitalocean:index/tag:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            databases_count: Optional[pulumi.Input[int]] = None,
            droplets_count: Optional[pulumi.Input[int]] = None,
            images_count: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            total_resource_count: Optional[pulumi.Input[int]] = None,
            volume_snapshots_count: Optional[pulumi.Input[int]] = None,
            volumes_count: Optional[pulumi.Input[int]] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] databases_count: A count of the database clusters that the tag is applied to.
        :param pulumi.Input[int] droplets_count: A count of the Droplets the tag is applied to.
        :param pulumi.Input[int] images_count: A count of the images that the tag is applied to.
        :param pulumi.Input[str] name: The name of the tag
        :param pulumi.Input[int] total_resource_count: A count of the total number of resources that the tag is applied to.
        :param pulumi.Input[int] volume_snapshots_count: A count of the volume snapshots that the tag is applied to.
        :param pulumi.Input[int] volumes_count: A count of the volumes that the tag is applied to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagState.__new__(_TagState)

        __props__.__dict__["databases_count"] = databases_count
        __props__.__dict__["droplets_count"] = droplets_count
        __props__.__dict__["images_count"] = images_count
        __props__.__dict__["name"] = name
        __props__.__dict__["total_resource_count"] = total_resource_count
        __props__.__dict__["volume_snapshots_count"] = volume_snapshots_count
        __props__.__dict__["volumes_count"] = volumes_count
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databasesCount")
    def databases_count(self) -> pulumi.Output[int]:
        """
        A count of the database clusters that the tag is applied to.
        """
        return pulumi.get(self, "databases_count")

    @property
    @pulumi.getter(name="dropletsCount")
    def droplets_count(self) -> pulumi.Output[int]:
        """
        A count of the Droplets the tag is applied to.
        """
        return pulumi.get(self, "droplets_count")

    @property
    @pulumi.getter(name="imagesCount")
    def images_count(self) -> pulumi.Output[int]:
        """
        A count of the images that the tag is applied to.
        """
        return pulumi.get(self, "images_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the tag
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="totalResourceCount")
    def total_resource_count(self) -> pulumi.Output[int]:
        """
        A count of the total number of resources that the tag is applied to.
        """
        return pulumi.get(self, "total_resource_count")

    @property
    @pulumi.getter(name="volumeSnapshotsCount")
    def volume_snapshots_count(self) -> pulumi.Output[int]:
        """
        A count of the volume snapshots that the tag is applied to.
        """
        return pulumi.get(self, "volume_snapshots_count")

    @property
    @pulumi.getter(name="volumesCount")
    def volumes_count(self) -> pulumi.Output[int]:
        """
        A count of the volumes that the tag is applied to.
        """
        return pulumi.get(self, "volumes_count")

