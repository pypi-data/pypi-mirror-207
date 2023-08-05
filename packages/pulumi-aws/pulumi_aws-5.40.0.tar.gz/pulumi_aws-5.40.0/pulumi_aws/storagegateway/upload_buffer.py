# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UploadBufferArgs', 'UploadBuffer']

@pulumi.input_type
class UploadBufferArgs:
    def __init__(__self__, *,
                 gateway_arn: pulumi.Input[str],
                 disk_id: Optional[pulumi.Input[str]] = None,
                 disk_path: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UploadBuffer resource.
        :param pulumi.Input[str] gateway_arn: The Amazon Resource Name (ARN) of the gateway.
        :param pulumi.Input[str] disk_id: Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        :param pulumi.Input[str] disk_path: Local disk path. For example, `/dev/nvme1n1`.
        """
        pulumi.set(__self__, "gateway_arn", gateway_arn)
        if disk_id is not None:
            pulumi.set(__self__, "disk_id", disk_id)
        if disk_path is not None:
            pulumi.set(__self__, "disk_path", disk_path)

    @property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the gateway.
        """
        return pulumi.get(self, "gateway_arn")

    @gateway_arn.setter
    def gateway_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_arn", value)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[str]]:
        """
        Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> Optional[pulumi.Input[str]]:
        """
        Local disk path. For example, `/dev/nvme1n1`.
        """
        return pulumi.get(self, "disk_path")

    @disk_path.setter
    def disk_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_path", value)


@pulumi.input_type
class _UploadBufferState:
    def __init__(__self__, *,
                 disk_id: Optional[pulumi.Input[str]] = None,
                 disk_path: Optional[pulumi.Input[str]] = None,
                 gateway_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UploadBuffer resources.
        :param pulumi.Input[str] disk_id: Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        :param pulumi.Input[str] disk_path: Local disk path. For example, `/dev/nvme1n1`.
        :param pulumi.Input[str] gateway_arn: The Amazon Resource Name (ARN) of the gateway.
        """
        if disk_id is not None:
            pulumi.set(__self__, "disk_id", disk_id)
        if disk_path is not None:
            pulumi.set(__self__, "disk_path", disk_path)
        if gateway_arn is not None:
            pulumi.set(__self__, "gateway_arn", gateway_arn)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[str]]:
        """
        Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> Optional[pulumi.Input[str]]:
        """
        Local disk path. For example, `/dev/nvme1n1`.
        """
        return pulumi.get(self, "disk_path")

    @disk_path.setter
    def disk_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_path", value)

    @property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the gateway.
        """
        return pulumi.get(self, "gateway_arn")

    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_arn", value)


class UploadBuffer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_id: Optional[pulumi.Input[str]] = None,
                 disk_path: Optional[pulumi.Input[str]] = None,
                 gateway_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an AWS Storage Gateway upload buffer.

        > **NOTE:** The Storage Gateway API provides no method to remove an upload buffer disk. Destroying this resource does not perform any Storage Gateway actions.

        ## Example Usage
        ### Cached and VTL Gateway Type

        ```python
        import pulumi
        import pulumi_aws as aws

        test_local_disk = aws.storagegateway.get_local_disk(disk_node=aws_volume_attachment["test"]["device_name"],
            gateway_arn=aws_storagegateway_gateway["test"]["arn"])
        test_upload_buffer = aws.storagegateway.UploadBuffer("testUploadBuffer",
            disk_path=test_local_disk.disk_path,
            gateway_arn=aws_storagegateway_gateway["test"]["arn"])
        ```
        ### Stored Gateway Type

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.storagegateway.get_local_disk(disk_node=aws_volume_attachment["test"]["device_name"],
            gateway_arn=aws_storagegateway_gateway["test"]["arn"])
        example = aws.storagegateway.UploadBuffer("example",
            disk_id=data["aws_storagegateway_local_disk"]["example"]["id"],
            gateway_arn=aws_storagegateway_gateway["example"]["arn"])
        ```

        ## Import

        `aws_storagegateway_upload_buffer` can be imported by using the gateway Amazon Resource Name (ARN) and local disk identifier separated with a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:storagegateway/uploadBuffer:UploadBuffer example arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678:pci-0000:03:00.0-scsi-0:0:0:0
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk_id: Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        :param pulumi.Input[str] disk_path: Local disk path. For example, `/dev/nvme1n1`.
        :param pulumi.Input[str] gateway_arn: The Amazon Resource Name (ARN) of the gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UploadBufferArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an AWS Storage Gateway upload buffer.

        > **NOTE:** The Storage Gateway API provides no method to remove an upload buffer disk. Destroying this resource does not perform any Storage Gateway actions.

        ## Example Usage
        ### Cached and VTL Gateway Type

        ```python
        import pulumi
        import pulumi_aws as aws

        test_local_disk = aws.storagegateway.get_local_disk(disk_node=aws_volume_attachment["test"]["device_name"],
            gateway_arn=aws_storagegateway_gateway["test"]["arn"])
        test_upload_buffer = aws.storagegateway.UploadBuffer("testUploadBuffer",
            disk_path=test_local_disk.disk_path,
            gateway_arn=aws_storagegateway_gateway["test"]["arn"])
        ```
        ### Stored Gateway Type

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.storagegateway.get_local_disk(disk_node=aws_volume_attachment["test"]["device_name"],
            gateway_arn=aws_storagegateway_gateway["test"]["arn"])
        example = aws.storagegateway.UploadBuffer("example",
            disk_id=data["aws_storagegateway_local_disk"]["example"]["id"],
            gateway_arn=aws_storagegateway_gateway["example"]["arn"])
        ```

        ## Import

        `aws_storagegateway_upload_buffer` can be imported by using the gateway Amazon Resource Name (ARN) and local disk identifier separated with a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:storagegateway/uploadBuffer:UploadBuffer example arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678:pci-0000:03:00.0-scsi-0:0:0:0
        ```

        :param str resource_name: The name of the resource.
        :param UploadBufferArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UploadBufferArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_id: Optional[pulumi.Input[str]] = None,
                 disk_path: Optional[pulumi.Input[str]] = None,
                 gateway_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UploadBufferArgs.__new__(UploadBufferArgs)

            __props__.__dict__["disk_id"] = disk_id
            __props__.__dict__["disk_path"] = disk_path
            if gateway_arn is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_arn'")
            __props__.__dict__["gateway_arn"] = gateway_arn
        super(UploadBuffer, __self__).__init__(
            'aws:storagegateway/uploadBuffer:UploadBuffer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disk_id: Optional[pulumi.Input[str]] = None,
            disk_path: Optional[pulumi.Input[str]] = None,
            gateway_arn: Optional[pulumi.Input[str]] = None) -> 'UploadBuffer':
        """
        Get an existing UploadBuffer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk_id: Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        :param pulumi.Input[str] disk_path: Local disk path. For example, `/dev/nvme1n1`.
        :param pulumi.Input[str] gateway_arn: The Amazon Resource Name (ARN) of the gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UploadBufferState.__new__(_UploadBufferState)

        __props__.__dict__["disk_id"] = disk_id
        __props__.__dict__["disk_path"] = disk_path
        __props__.__dict__["gateway_arn"] = gateway_arn
        return UploadBuffer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Output[str]:
        """
        Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
        """
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> pulumi.Output[str]:
        """
        Local disk path. For example, `/dev/nvme1n1`.
        """
        return pulumi.get(self, "disk_path")

    @property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the gateway.
        """
        return pulumi.get(self, "gateway_arn")

