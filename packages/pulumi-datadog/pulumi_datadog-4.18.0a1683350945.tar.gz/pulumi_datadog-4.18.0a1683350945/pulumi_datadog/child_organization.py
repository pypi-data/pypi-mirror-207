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

__all__ = ['ChildOrganizationArgs', 'ChildOrganization']

@pulumi.input_type
class ChildOrganizationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ChildOrganization resource.
        :param pulumi.Input[str] name: Name for Child Organization after creation.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name for Child Organization after creation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ChildOrganizationState:
    def __init__(__self__, *,
                 api_keys: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApiKeyArgs']]]] = None,
                 application_keys: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApplicationKeyArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationSettingArgs']]]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationUserArgs']]]] = None):
        """
        Input properties used for looking up and filtering ChildOrganization resources.
        :param pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApiKeyArgs']]] api_keys: Datadog API key.
        :param pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApplicationKeyArgs']]] application_keys: An application key with its associated metadata.
        :param pulumi.Input[str] description: Description of the organization.
        :param pulumi.Input[str] name: Name for Child Organization after creation.
        :param pulumi.Input[str] public_id: The `public_id` of the organization you are operating within.
        :param pulumi.Input[Sequence[pulumi.Input['ChildOrganizationSettingArgs']]] settings: Organization settings
        :param pulumi.Input[Sequence[pulumi.Input['ChildOrganizationUserArgs']]] users: Information about a user
        """
        if api_keys is not None:
            pulumi.set(__self__, "api_keys", api_keys)
        if application_keys is not None:
            pulumi.set(__self__, "application_keys", application_keys)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_id is not None:
            pulumi.set(__self__, "public_id", public_id)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)
        if users is not None:
            pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApiKeyArgs']]]]:
        """
        Datadog API key.
        """
        return pulumi.get(self, "api_keys")

    @api_keys.setter
    def api_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApiKeyArgs']]]]):
        pulumi.set(self, "api_keys", value)

    @property
    @pulumi.getter(name="applicationKeys")
    def application_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApplicationKeyArgs']]]]:
        """
        An application key with its associated metadata.
        """
        return pulumi.get(self, "application_keys")

    @application_keys.setter
    def application_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationApplicationKeyArgs']]]]):
        pulumi.set(self, "application_keys", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the organization.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for Child Organization after creation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicId")
    def public_id(self) -> Optional[pulumi.Input[str]]:
        """
        The `public_id` of the organization you are operating within.
        """
        return pulumi.get(self, "public_id")

    @public_id.setter
    def public_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_id", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationSettingArgs']]]]:
        """
        Organization settings
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationSettingArgs']]]]):
        pulumi.set(self, "settings", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationUserArgs']]]]:
        """
        Information about a user
        """
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChildOrganizationUserArgs']]]]):
        pulumi.set(self, "users", value)


class ChildOrganization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Datadog Child Organization resource. This can be used to create Datadog Child Organizations. To manage created organization use `OrganizationSettings`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        # Create a new Datadog Child Organization
        organization = datadog.ChildOrganization("organization", name="foo-organization")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name for Child Organization after creation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChildOrganizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog Child Organization resource. This can be used to create Datadog Child Organizations. To manage created organization use `OrganizationSettings`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        # Create a new Datadog Child Organization
        organization = datadog.ChildOrganization("organization", name="foo-organization")
        ```

        :param str resource_name: The name of the resource.
        :param ChildOrganizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChildOrganizationArgs, pulumi.ResourceOptions, *args, **kwargs)
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
            __props__ = ChildOrganizationArgs.__new__(ChildOrganizationArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["api_keys"] = None
            __props__.__dict__["application_keys"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["public_id"] = None
            __props__.__dict__["settings"] = None
            __props__.__dict__["users"] = None
        super(ChildOrganization, __self__).__init__(
            'datadog:index/childOrganization:ChildOrganization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationApiKeyArgs']]]]] = None,
            application_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationApplicationKeyArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_id: Optional[pulumi.Input[str]] = None,
            settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationSettingArgs']]]]] = None,
            users: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationUserArgs']]]]] = None) -> 'ChildOrganization':
        """
        Get an existing ChildOrganization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationApiKeyArgs']]]] api_keys: Datadog API key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationApplicationKeyArgs']]]] application_keys: An application key with its associated metadata.
        :param pulumi.Input[str] description: Description of the organization.
        :param pulumi.Input[str] name: Name for Child Organization after creation.
        :param pulumi.Input[str] public_id: The `public_id` of the organization you are operating within.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationSettingArgs']]]] settings: Organization settings
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChildOrganizationUserArgs']]]] users: Information about a user
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChildOrganizationState.__new__(_ChildOrganizationState)

        __props__.__dict__["api_keys"] = api_keys
        __props__.__dict__["application_keys"] = application_keys
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["public_id"] = public_id
        __props__.__dict__["settings"] = settings
        __props__.__dict__["users"] = users
        return ChildOrganization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> pulumi.Output[Sequence['outputs.ChildOrganizationApiKey']]:
        """
        Datadog API key.
        """
        return pulumi.get(self, "api_keys")

    @property
    @pulumi.getter(name="applicationKeys")
    def application_keys(self) -> pulumi.Output[Sequence['outputs.ChildOrganizationApplicationKey']]:
        """
        An application key with its associated metadata.
        """
        return pulumi.get(self, "application_keys")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the organization.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name for Child Organization after creation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicId")
    def public_id(self) -> pulumi.Output[str]:
        """
        The `public_id` of the organization you are operating within.
        """
        return pulumi.get(self, "public_id")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Sequence['outputs.ChildOrganizationSetting']]:
        """
        Organization settings
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Sequence['outputs.ChildOrganizationUser']]:
        """
        Information about a user
        """
        return pulumi.get(self, "users")

