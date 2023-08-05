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

__all__ = ['InputArgs', 'Input']

@pulumi.input_type
class InputArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc: Optional[pulumi.Input['InputVpcArgs']] = None):
        """
        The set of arguments for constructing a Input resource.
        :param pulumi.Input[str] type: The different types of inputs that AWS Elemental MediaLive supports.
        :param pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]] destinations: Destination settings for PUSH type inputs. See Destinations for more details.
        :param pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]] input_devices: Settings for the devices. See Input Devices for more details.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_security_groups: List of input security groups.
        :param pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]] media_connect_flows: A list of the MediaConnect Flows. See Media Connect Flows for more details.
        :param pulumi.Input[str] name: Name of the input.
        :param pulumi.Input[str] role_arn: The ARN of the role this input assumes during and after creation.
        :param pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]] sources: The source URLs for a PULL-type input. See Sources for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input['InputVpcArgs'] vpc: Settings for a private VPC Input. See VPC for more details.
        """
        pulumi.set(__self__, "type", type)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if input_devices is not None:
            pulumi.set(__self__, "input_devices", input_devices)
        if input_security_groups is not None:
            pulumi.set(__self__, "input_security_groups", input_security_groups)
        if media_connect_flows is not None:
            pulumi.set(__self__, "media_connect_flows", media_connect_flows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if vpc is not None:
            pulumi.set(__self__, "vpc", vpc)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The different types of inputs that AWS Elemental MediaLive supports.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]]]:
        """
        Destination settings for PUSH type inputs. See Destinations for more details.
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]]]:
        """
        Settings for the devices. See Input Devices for more details.
        """
        return pulumi.get(self, "input_devices")

    @input_devices.setter
    def input_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]]]):
        pulumi.set(self, "input_devices", value)

    @property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of input security groups.
        """
        return pulumi.get(self, "input_security_groups")

    @input_security_groups.setter
    def input_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "input_security_groups", value)

    @property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]]]:
        """
        A list of the MediaConnect Flows. See Media Connect Flows for more details.
        """
        return pulumi.get(self, "media_connect_flows")

    @media_connect_flows.setter
    def media_connect_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]]]):
        pulumi.set(self, "media_connect_flows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the input.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the role this input assumes during and after creation.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]]]:
        """
        The source URLs for a PULL-type input. See Sources for more details.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input['InputVpcArgs']]:
        """
        Settings for a private VPC Input. See VPC for more details.
        """
        return pulumi.get(self, "vpc")

    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input['InputVpcArgs']]):
        pulumi.set(self, "vpc", value)


@pulumi.input_type
class _InputState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 attached_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]]] = None,
                 input_class: Optional[pulumi.Input[str]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]]] = None,
                 input_partner_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 input_source_type: Optional[pulumi.Input[str]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc: Optional[pulumi.Input['InputVpcArgs']] = None):
        """
        Input properties used for looking up and filtering Input resources.
        :param pulumi.Input[str] arn: ARN of the Input.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_channels: Channels attached to Input.
        :param pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]] destinations: Destination settings for PUSH type inputs. See Destinations for more details.
        :param pulumi.Input[str] input_class: The input class.
        :param pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]] input_devices: Settings for the devices. See Input Devices for more details.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_partner_ids: A list of IDs for all Inputs which are partners of this one.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_security_groups: List of input security groups.
        :param pulumi.Input[str] input_source_type: Source type of the input.
        :param pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]] media_connect_flows: A list of the MediaConnect Flows. See Media Connect Flows for more details.
        :param pulumi.Input[str] name: Name of the input.
        :param pulumi.Input[str] role_arn: The ARN of the role this input assumes during and after creation.
        :param pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]] sources: The source URLs for a PULL-type input. See Sources for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] type: The different types of inputs that AWS Elemental MediaLive supports.
        :param pulumi.Input['InputVpcArgs'] vpc: Settings for a private VPC Input. See VPC for more details.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if attached_channels is not None:
            pulumi.set(__self__, "attached_channels", attached_channels)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if input_class is not None:
            pulumi.set(__self__, "input_class", input_class)
        if input_devices is not None:
            pulumi.set(__self__, "input_devices", input_devices)
        if input_partner_ids is not None:
            pulumi.set(__self__, "input_partner_ids", input_partner_ids)
        if input_security_groups is not None:
            pulumi.set(__self__, "input_security_groups", input_security_groups)
        if input_source_type is not None:
            pulumi.set(__self__, "input_source_type", input_source_type)
        if media_connect_flows is not None:
            pulumi.set(__self__, "media_connect_flows", media_connect_flows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vpc is not None:
            pulumi.set(__self__, "vpc", vpc)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the Input.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="attachedChannels")
    def attached_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Channels attached to Input.
        """
        return pulumi.get(self, "attached_channels")

    @attached_channels.setter
    def attached_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attached_channels", value)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]]]:
        """
        Destination settings for PUSH type inputs. See Destinations for more details.
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputDestinationArgs']]]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="inputClass")
    def input_class(self) -> Optional[pulumi.Input[str]]:
        """
        The input class.
        """
        return pulumi.get(self, "input_class")

    @input_class.setter
    def input_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_class", value)

    @property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]]]:
        """
        Settings for the devices. See Input Devices for more details.
        """
        return pulumi.get(self, "input_devices")

    @input_devices.setter
    def input_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputInputDeviceArgs']]]]):
        pulumi.set(self, "input_devices", value)

    @property
    @pulumi.getter(name="inputPartnerIds")
    def input_partner_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IDs for all Inputs which are partners of this one.
        """
        return pulumi.get(self, "input_partner_ids")

    @input_partner_ids.setter
    def input_partner_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "input_partner_ids", value)

    @property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of input security groups.
        """
        return pulumi.get(self, "input_security_groups")

    @input_security_groups.setter
    def input_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "input_security_groups", value)

    @property
    @pulumi.getter(name="inputSourceType")
    def input_source_type(self) -> Optional[pulumi.Input[str]]:
        """
        Source type of the input.
        """
        return pulumi.get(self, "input_source_type")

    @input_source_type.setter
    def input_source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_source_type", value)

    @property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]]]:
        """
        A list of the MediaConnect Flows. See Media Connect Flows for more details.
        """
        return pulumi.get(self, "media_connect_flows")

    @media_connect_flows.setter
    def media_connect_flows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputMediaConnectFlowArgs']]]]):
        pulumi.set(self, "media_connect_flows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the input.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the role this input assumes during and after creation.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]]]:
        """
        The source URLs for a PULL-type input. See Sources for more details.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InputSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The different types of inputs that AWS Elemental MediaLive supports.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input['InputVpcArgs']]:
        """
        Settings for a private VPC Input. See VPC for more details.
        """
        return pulumi.get(self, "vpc")

    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input['InputVpcArgs']]):
        pulumi.set(self, "vpc", value)


class Input(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationArgs']]]]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputInputDeviceArgs']]]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc: Optional[pulumi.Input[pulumi.InputType['InputVpcArgs']]] = None,
                 __props__=None):
        """
        Resource for managing an AWS MediaLive Input.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_input_security_group = aws.medialive.InputSecurityGroup("exampleInputSecurityGroup",
            whitelist_rules=[aws.medialive.InputSecurityGroupWhitelistRuleArgs(
                cidr="10.0.0.8/32",
            )],
            tags={
                "ENVIRONMENT": "prod",
            })
        example_input = aws.medialive.Input("exampleInput",
            input_security_groups=[example_input_security_group.id],
            type="UDP_PUSH",
            tags={
                "ENVIRONMENT": "prod",
            })
        ```

        ## Import

        MediaLive Input can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:medialive/input:Input example 12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationArgs']]]] destinations: Destination settings for PUSH type inputs. See Destinations for more details.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputInputDeviceArgs']]]] input_devices: Settings for the devices. See Input Devices for more details.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_security_groups: List of input security groups.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowArgs']]]] media_connect_flows: A list of the MediaConnect Flows. See Media Connect Flows for more details.
        :param pulumi.Input[str] name: Name of the input.
        :param pulumi.Input[str] role_arn: The ARN of the role this input assumes during and after creation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceArgs']]]] sources: The source URLs for a PULL-type input. See Sources for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] type: The different types of inputs that AWS Elemental MediaLive supports.
        :param pulumi.Input[pulumi.InputType['InputVpcArgs']] vpc: Settings for a private VPC Input. See VPC for more details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InputArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS MediaLive Input.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_input_security_group = aws.medialive.InputSecurityGroup("exampleInputSecurityGroup",
            whitelist_rules=[aws.medialive.InputSecurityGroupWhitelistRuleArgs(
                cidr="10.0.0.8/32",
            )],
            tags={
                "ENVIRONMENT": "prod",
            })
        example_input = aws.medialive.Input("exampleInput",
            input_security_groups=[example_input_security_group.id],
            type="UDP_PUSH",
            tags={
                "ENVIRONMENT": "prod",
            })
        ```

        ## Import

        MediaLive Input can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:medialive/input:Input example 12345678
        ```

        :param str resource_name: The name of the resource.
        :param InputArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InputArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationArgs']]]]] = None,
                 input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputInputDeviceArgs']]]]] = None,
                 input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpc: Optional[pulumi.Input[pulumi.InputType['InputVpcArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InputArgs.__new__(InputArgs)

            __props__.__dict__["destinations"] = destinations
            __props__.__dict__["input_devices"] = input_devices
            __props__.__dict__["input_security_groups"] = input_security_groups
            __props__.__dict__["media_connect_flows"] = media_connect_flows
            __props__.__dict__["name"] = name
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["sources"] = sources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["vpc"] = vpc
            __props__.__dict__["arn"] = None
            __props__.__dict__["attached_channels"] = None
            __props__.__dict__["input_class"] = None
            __props__.__dict__["input_partner_ids"] = None
            __props__.__dict__["input_source_type"] = None
        super(Input, __self__).__init__(
            'aws:medialive/input:Input',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            attached_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationArgs']]]]] = None,
            input_class: Optional[pulumi.Input[str]] = None,
            input_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputInputDeviceArgs']]]]] = None,
            input_partner_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            input_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            input_source_type: Optional[pulumi.Input[str]] = None,
            media_connect_flows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vpc: Optional[pulumi.Input[pulumi.InputType['InputVpcArgs']]] = None) -> 'Input':
        """
        Get an existing Input resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the Input.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_channels: Channels attached to Input.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputDestinationArgs']]]] destinations: Destination settings for PUSH type inputs. See Destinations for more details.
        :param pulumi.Input[str] input_class: The input class.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputInputDeviceArgs']]]] input_devices: Settings for the devices. See Input Devices for more details.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_partner_ids: A list of IDs for all Inputs which are partners of this one.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] input_security_groups: List of input security groups.
        :param pulumi.Input[str] input_source_type: Source type of the input.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputMediaConnectFlowArgs']]]] media_connect_flows: A list of the MediaConnect Flows. See Media Connect Flows for more details.
        :param pulumi.Input[str] name: Name of the input.
        :param pulumi.Input[str] role_arn: The ARN of the role this input assumes during and after creation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InputSourceArgs']]]] sources: The source URLs for a PULL-type input. See Sources for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] type: The different types of inputs that AWS Elemental MediaLive supports.
        :param pulumi.Input[pulumi.InputType['InputVpcArgs']] vpc: Settings for a private VPC Input. See VPC for more details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InputState.__new__(_InputState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["attached_channels"] = attached_channels
        __props__.__dict__["destinations"] = destinations
        __props__.__dict__["input_class"] = input_class
        __props__.__dict__["input_devices"] = input_devices
        __props__.__dict__["input_partner_ids"] = input_partner_ids
        __props__.__dict__["input_security_groups"] = input_security_groups
        __props__.__dict__["input_source_type"] = input_source_type
        __props__.__dict__["media_connect_flows"] = media_connect_flows
        __props__.__dict__["name"] = name
        __props__.__dict__["role_arn"] = role_arn
        __props__.__dict__["sources"] = sources
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["type"] = type
        __props__.__dict__["vpc"] = vpc
        return Input(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the Input.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="attachedChannels")
    def attached_channels(self) -> pulumi.Output[Sequence[str]]:
        """
        Channels attached to Input.
        """
        return pulumi.get(self, "attached_channels")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence['outputs.InputDestination']]]:
        """
        Destination settings for PUSH type inputs. See Destinations for more details.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter(name="inputClass")
    def input_class(self) -> pulumi.Output[str]:
        """
        The input class.
        """
        return pulumi.get(self, "input_class")

    @property
    @pulumi.getter(name="inputDevices")
    def input_devices(self) -> pulumi.Output[Sequence['outputs.InputInputDevice']]:
        """
        Settings for the devices. See Input Devices for more details.
        """
        return pulumi.get(self, "input_devices")

    @property
    @pulumi.getter(name="inputPartnerIds")
    def input_partner_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of IDs for all Inputs which are partners of this one.
        """
        return pulumi.get(self, "input_partner_ids")

    @property
    @pulumi.getter(name="inputSecurityGroups")
    def input_security_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of input security groups.
        """
        return pulumi.get(self, "input_security_groups")

    @property
    @pulumi.getter(name="inputSourceType")
    def input_source_type(self) -> pulumi.Output[str]:
        """
        Source type of the input.
        """
        return pulumi.get(self, "input_source_type")

    @property
    @pulumi.getter(name="mediaConnectFlows")
    def media_connect_flows(self) -> pulumi.Output[Sequence['outputs.InputMediaConnectFlow']]:
        """
        A list of the MediaConnect Flows. See Media Connect Flows for more details.
        """
        return pulumi.get(self, "media_connect_flows")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the input.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the role this input assumes during and after creation.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence['outputs.InputSource']]:
        """
        The source URLs for a PULL-type input. See Sources for more details.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the Input. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The different types of inputs that AWS Elemental MediaLive supports.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vpc(self) -> pulumi.Output[Optional['outputs.InputVpc']]:
        """
        Settings for a private VPC Input. See VPC for more details.
        """
        return pulumi.get(self, "vpc")

