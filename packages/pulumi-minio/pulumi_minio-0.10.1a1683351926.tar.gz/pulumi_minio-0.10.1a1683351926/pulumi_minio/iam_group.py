# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IamGroupArgs', 'IamGroup']

@pulumi.input_type
class IamGroupArgs:
    def __init__(__self__, *,
                 disable_group: Optional[pulumi.Input[bool]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IamGroup resource.
        :param pulumi.Input[bool] disable_group: Disable group
        :param pulumi.Input[bool] force_destroy: Delete group even if it has non-Terraform-managed members
        """
        if disable_group is not None:
            pulumi.set(__self__, "disable_group", disable_group)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="disableGroup")
    def disable_group(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable group
        """
        return pulumi.get(self, "disable_group")

    @disable_group.setter
    def disable_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_group", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete group even if it has non-Terraform-managed members
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _IamGroupState:
    def __init__(__self__, *,
                 disable_group: Optional[pulumi.Input[bool]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IamGroup resources.
        :param pulumi.Input[bool] disable_group: Disable group
        :param pulumi.Input[bool] force_destroy: Delete group even if it has non-Terraform-managed members
        """
        if disable_group is not None:
            pulumi.set(__self__, "disable_group", disable_group)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="disableGroup")
    def disable_group(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable group
        """
        return pulumi.get(self, "disable_group")

    @disable_group.setter
    def disable_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_group", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete group even if it has non-Terraform-managed members
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class IamGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_group: Optional[pulumi.Input[bool]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_minio as minio

        developer = minio.IamGroup("developer")
        pulumi.export("minioUserGroup", developer.group_name)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_group: Disable group
        :param pulumi.Input[bool] force_destroy: Delete group even if it has non-Terraform-managed members
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[IamGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_minio as minio

        developer = minio.IamGroup("developer")
        pulumi.export("minioUserGroup", developer.group_name)
        ```

        :param str resource_name: The name of the resource.
        :param IamGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IamGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_group: Optional[pulumi.Input[bool]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IamGroupArgs.__new__(IamGroupArgs)

            __props__.__dict__["disable_group"] = disable_group
            __props__.__dict__["force_destroy"] = force_destroy
            __props__.__dict__["name"] = name
            __props__.__dict__["group_name"] = None
        super(IamGroup, __self__).__init__(
            'minio:index/iamGroup:IamGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disable_group: Optional[pulumi.Input[bool]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            group_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'IamGroup':
        """
        Get an existing IamGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_group: Disable group
        :param pulumi.Input[bool] force_destroy: Delete group even if it has non-Terraform-managed members
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IamGroupState.__new__(_IamGroupState)

        __props__.__dict__["disable_group"] = disable_group
        __props__.__dict__["force_destroy"] = force_destroy
        __props__.__dict__["group_name"] = group_name
        __props__.__dict__["name"] = name
        return IamGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disableGroup")
    def disable_group(self) -> pulumi.Output[Optional[bool]]:
        """
        Disable group
        """
        return pulumi.get(self, "disable_group")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        Delete group even if it has non-Terraform-managed members
        """
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

