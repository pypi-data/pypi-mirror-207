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

__all__ = ['ListenerArgs', 'Listener']

@pulumi.input_type
class ListenerArgs:
    def __init__(__self__, *,
                 accelerator_arn: pulumi.Input[str],
                 port_ranges: pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]],
                 protocol: pulumi.Input[str],
                 client_affinity: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Listener resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        :param pulumi.Input[str] protocol: The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        :param pulumi.Input[str] client_affinity: Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        """
        pulumi.set(__self__, "accelerator_arn", accelerator_arn)
        pulumi.set(__self__, "port_ranges", port_ranges)
        pulumi.set(__self__, "protocol", protocol)
        if client_affinity is not None:
            pulumi.set(__self__, "client_affinity", client_affinity)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of your accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @accelerator_arn.setter
    def accelerator_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_arn", value)

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]]:
        """
        The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        return pulumi.get(self, "port_ranges")

    @port_ranges.setter
    def port_ranges(self, value: pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]]):
        pulumi.set(self, "port_ranges", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> Optional[pulumi.Input[str]]:
        """
        Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        """
        return pulumi.get(self, "client_affinity")

    @client_affinity.setter
    def client_affinity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_affinity", value)


@pulumi.input_type
class _ListenerState:
    def __init__(__self__, *,
                 accelerator_arn: Optional[pulumi.Input[str]] = None,
                 client_affinity: Optional[pulumi.Input[str]] = None,
                 port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Listener resources.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param pulumi.Input[str] client_affinity: Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        :param pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        :param pulumi.Input[str] protocol: The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        if accelerator_arn is not None:
            pulumi.set(__self__, "accelerator_arn", accelerator_arn)
        if client_affinity is not None:
            pulumi.set(__self__, "client_affinity", client_affinity)
        if port_ranges is not None:
            pulumi.set(__self__, "port_ranges", port_ranges)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of your accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @accelerator_arn.setter
    def accelerator_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_arn", value)

    @property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> Optional[pulumi.Input[str]]:
        """
        Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        """
        return pulumi.get(self, "client_affinity")

    @client_affinity.setter
    def client_affinity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_affinity", value)

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]]]:
        """
        The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        return pulumi.get(self, "port_ranges")

    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerPortRangeArgs']]]]):
        pulumi.set(self, "port_ranges", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)


class Listener(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_arn: Optional[pulumi.Input[str]] = None,
                 client_affinity: Optional[pulumi.Input[str]] = None,
                 port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerPortRangeArgs']]]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator listener.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_accelerator = aws.globalaccelerator.Accelerator("exampleAccelerator",
            ip_address_type="IPV4",
            enabled=True,
            attributes=aws.globalaccelerator.AcceleratorAttributesArgs(
                flow_logs_enabled=True,
                flow_logs_s3_bucket="example-bucket",
                flow_logs_s3_prefix="flow-logs/",
            ))
        example_listener = aws.globalaccelerator.Listener("exampleListener",
            accelerator_arn=example_accelerator.id,
            client_affinity="SOURCE_IP",
            protocol="TCP",
            port_ranges=[aws.globalaccelerator.ListenerPortRangeArgs(
                from_port=80,
                to_port=80,
            )])
        ```

        ## Import

        Global Accelerator listeners can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:globalaccelerator/listener:Listener example arn:aws:globalaccelerator::111111111111:accelerator/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/listener/xxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param pulumi.Input[str] client_affinity: Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerPortRangeArgs']]]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        :param pulumi.Input[str] protocol: The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ListenerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator listener.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_accelerator = aws.globalaccelerator.Accelerator("exampleAccelerator",
            ip_address_type="IPV4",
            enabled=True,
            attributes=aws.globalaccelerator.AcceleratorAttributesArgs(
                flow_logs_enabled=True,
                flow_logs_s3_bucket="example-bucket",
                flow_logs_s3_prefix="flow-logs/",
            ))
        example_listener = aws.globalaccelerator.Listener("exampleListener",
            accelerator_arn=example_accelerator.id,
            client_affinity="SOURCE_IP",
            protocol="TCP",
            port_ranges=[aws.globalaccelerator.ListenerPortRangeArgs(
                from_port=80,
                to_port=80,
            )])
        ```

        ## Import

        Global Accelerator listeners can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:globalaccelerator/listener:Listener example arn:aws:globalaccelerator::111111111111:accelerator/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/listener/xxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param ListenerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ListenerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_arn: Optional[pulumi.Input[str]] = None,
                 client_affinity: Optional[pulumi.Input[str]] = None,
                 port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerPortRangeArgs']]]]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ListenerArgs.__new__(ListenerArgs)

            if accelerator_arn is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_arn'")
            __props__.__dict__["accelerator_arn"] = accelerator_arn
            __props__.__dict__["client_affinity"] = client_affinity
            if port_ranges is None and not opts.urn:
                raise TypeError("Missing required property 'port_ranges'")
            __props__.__dict__["port_ranges"] = port_ranges
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
        super(Listener, __self__).__init__(
            'aws:globalaccelerator/listener:Listener',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerator_arn: Optional[pulumi.Input[str]] = None,
            client_affinity: Optional[pulumi.Input[str]] = None,
            port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerPortRangeArgs']]]]] = None,
            protocol: Optional[pulumi.Input[str]] = None) -> 'Listener':
        """
        Get an existing Listener resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param pulumi.Input[str] client_affinity: Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerPortRangeArgs']]]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        :param pulumi.Input[str] protocol: The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ListenerState.__new__(_ListenerState)

        __props__.__dict__["accelerator_arn"] = accelerator_arn
        __props__.__dict__["client_affinity"] = client_affinity
        __props__.__dict__["port_ranges"] = port_ranges
        __props__.__dict__["protocol"] = protocol
        return Listener(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of your accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @property
    @pulumi.getter(name="clientAffinity")
    def client_affinity(self) -> pulumi.Output[Optional[str]]:
        """
        Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        """
        return pulumi.get(self, "client_affinity")

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Output[Sequence['outputs.ListenerPortRange']]:
        """
        The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        return pulumi.get(self, "port_ranges")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        return pulumi.get(self, "protocol")

