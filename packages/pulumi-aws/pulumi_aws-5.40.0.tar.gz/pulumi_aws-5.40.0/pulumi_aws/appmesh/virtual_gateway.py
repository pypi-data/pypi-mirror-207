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

__all__ = ['VirtualGatewayArgs', 'VirtualGateway']

@pulumi.input_type
class VirtualGatewayArgs:
    def __init__(__self__, *,
                 mesh_name: pulumi.Input[str],
                 spec: pulumi.Input['VirtualGatewaySpecArgs'],
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a VirtualGateway resource.
        :param pulumi.Input[str] mesh_name: Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input['VirtualGatewaySpecArgs'] spec: Virtual gateway specification to apply.
        :param pulumi.Input[str] mesh_owner: AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        :param pulumi.Input[str] name: Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        pulumi.set(__self__, "mesh_name", mesh_name)
        pulumi.set(__self__, "spec", spec)
        if mesh_owner is not None:
            pulumi.set(__self__, "mesh_owner", mesh_owner)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> pulumi.Input[str]:
        """
        Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "mesh_name")

    @mesh_name.setter
    def mesh_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mesh_name", value)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['VirtualGatewaySpecArgs']:
        """
        Virtual gateway specification to apply.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['VirtualGatewaySpecArgs']):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        """
        return pulumi.get(self, "mesh_owner")

    @mesh_owner.setter
    def mesh_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_owner", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _VirtualGatewayState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 created_date: Optional[pulumi.Input[str]] = None,
                 last_updated_date: Optional[pulumi.Input[str]] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_owner: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input['VirtualGatewaySpecArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering VirtualGateway resources.
        :param pulumi.Input[str] arn: ARN of the virtual gateway.
        :param pulumi.Input[str] created_date: Creation date of the virtual gateway.
        :param pulumi.Input[str] last_updated_date: Last update date of the virtual gateway.
        :param pulumi.Input[str] mesh_name: Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        :param pulumi.Input[str] name: Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] resource_owner: Resource owner's AWS account ID.
        :param pulumi.Input['VirtualGatewaySpecArgs'] spec: Virtual gateway specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if created_date is not None:
            pulumi.set(__self__, "created_date", created_date)
        if last_updated_date is not None:
            pulumi.set(__self__, "last_updated_date", last_updated_date)
        if mesh_name is not None:
            pulumi.set(__self__, "mesh_name", mesh_name)
        if mesh_owner is not None:
            pulumi.set(__self__, "mesh_owner", mesh_owner)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_owner is not None:
            pulumi.set(__self__, "resource_owner", resource_owner)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the virtual gateway.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[str]]:
        """
        Creation date of the virtual gateway.
        """
        return pulumi.get(self, "created_date")

    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_date", value)

    @property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> Optional[pulumi.Input[str]]:
        """
        Last update date of the virtual gateway.
        """
        return pulumi.get(self, "last_updated_date")

    @last_updated_date.setter
    def last_updated_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_date", value)

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "mesh_name")

    @mesh_name.setter
    def mesh_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_name", value)

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        """
        return pulumi.get(self, "mesh_owner")

    @mesh_owner.setter
    def mesh_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_owner", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> Optional[pulumi.Input[str]]:
        """
        Resource owner's AWS account ID.
        """
        return pulumi.get(self, "resource_owner")

    @resource_owner.setter
    def resource_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_owner", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['VirtualGatewaySpecArgs']]:
        """
        Virtual gateway specification to apply.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['VirtualGatewaySpecArgs']]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class VirtualGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['VirtualGatewaySpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an AWS App Mesh virtual gateway resource.

        ## Example Usage
        ### Access Logs and TLS

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appmesh.VirtualGateway("example",
            mesh_name="example-service-mesh",
            spec=aws.appmesh.VirtualGatewaySpecArgs(
                listener=aws.appmesh.VirtualGatewaySpecListenerArgs(
                    port_mapping=aws.appmesh.VirtualGatewaySpecListenerPortMappingArgs(
                        port=8080,
                        protocol="http",
                    ),
                    tls=aws.appmesh.VirtualGatewaySpecListenerTlsArgs(
                        certificate=aws.appmesh.VirtualGatewaySpecListenerTlsCertificateArgs(
                            acm=aws.appmesh.VirtualGatewaySpecListenerTlsCertificateAcmArgs(
                                certificate_arn=aws_acm_certificate["example"]["arn"],
                            ),
                        ),
                        mode="STRICT",
                    ),
                ),
                logging=aws.appmesh.VirtualGatewaySpecLoggingArgs(
                    access_log=aws.appmesh.VirtualGatewaySpecLoggingAccessLogArgs(
                        file=aws.appmesh.VirtualGatewaySpecLoggingAccessLogFileArgs(
                            path="/var/log/access.log",
                        ),
                    ),
                ),
            ))
        ```

        ## Import

        App Mesh virtual gateway can be imported using `mesh_name` together with the virtual gateway's `name`, e.g.,

        ```sh
         $ pulumi import aws:appmesh/virtualGateway:VirtualGateway example mesh/gw1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mesh_name: Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        :param pulumi.Input[str] name: Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[pulumi.InputType['VirtualGatewaySpecArgs']] spec: Virtual gateway specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS App Mesh virtual gateway resource.

        ## Example Usage
        ### Access Logs and TLS

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appmesh.VirtualGateway("example",
            mesh_name="example-service-mesh",
            spec=aws.appmesh.VirtualGatewaySpecArgs(
                listener=aws.appmesh.VirtualGatewaySpecListenerArgs(
                    port_mapping=aws.appmesh.VirtualGatewaySpecListenerPortMappingArgs(
                        port=8080,
                        protocol="http",
                    ),
                    tls=aws.appmesh.VirtualGatewaySpecListenerTlsArgs(
                        certificate=aws.appmesh.VirtualGatewaySpecListenerTlsCertificateArgs(
                            acm=aws.appmesh.VirtualGatewaySpecListenerTlsCertificateAcmArgs(
                                certificate_arn=aws_acm_certificate["example"]["arn"],
                            ),
                        ),
                        mode="STRICT",
                    ),
                ),
                logging=aws.appmesh.VirtualGatewaySpecLoggingArgs(
                    access_log=aws.appmesh.VirtualGatewaySpecLoggingAccessLogArgs(
                        file=aws.appmesh.VirtualGatewaySpecLoggingAccessLogFileArgs(
                            path="/var/log/access.log",
                        ),
                    ),
                ),
            ))
        ```

        ## Import

        App Mesh virtual gateway can be imported using `mesh_name` together with the virtual gateway's `name`, e.g.,

        ```sh
         $ pulumi import aws:appmesh/virtualGateway:VirtualGateway example mesh/gw1
        ```

        :param str resource_name: The name of the resource.
        :param VirtualGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['VirtualGatewaySpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualGatewayArgs.__new__(VirtualGatewayArgs)

            if mesh_name is None and not opts.urn:
                raise TypeError("Missing required property 'mesh_name'")
            __props__.__dict__["mesh_name"] = mesh_name
            __props__.__dict__["mesh_owner"] = mesh_owner
            __props__.__dict__["name"] = name
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["last_updated_date"] = None
            __props__.__dict__["resource_owner"] = None
        super(VirtualGateway, __self__).__init__(
            'aws:appmesh/virtualGateway:VirtualGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            created_date: Optional[pulumi.Input[str]] = None,
            last_updated_date: Optional[pulumi.Input[str]] = None,
            mesh_name: Optional[pulumi.Input[str]] = None,
            mesh_owner: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_owner: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[pulumi.InputType['VirtualGatewaySpecArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'VirtualGateway':
        """
        Get an existing VirtualGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the virtual gateway.
        :param pulumi.Input[str] created_date: Creation date of the virtual gateway.
        :param pulumi.Input[str] last_updated_date: Last update date of the virtual gateway.
        :param pulumi.Input[str] mesh_name: Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        :param pulumi.Input[str] name: Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] resource_owner: Resource owner's AWS account ID.
        :param pulumi.Input[pulumi.InputType['VirtualGatewaySpecArgs']] spec: Virtual gateway specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualGatewayState.__new__(_VirtualGatewayState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["created_date"] = created_date
        __props__.__dict__["last_updated_date"] = last_updated_date
        __props__.__dict__["mesh_name"] = mesh_name
        __props__.__dict__["mesh_owner"] = mesh_owner
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_owner"] = resource_owner
        __props__.__dict__["spec"] = spec
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return VirtualGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the virtual gateway.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        Creation date of the virtual gateway.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[str]:
        """
        Last update date of the virtual gateway.
        """
        return pulumi.get(self, "last_updated_date")

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> pulumi.Output[str]:
        """
        Name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "mesh_name")

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> pulumi.Output[str]:
        """
        AWS account ID of the service mesh's owner. Defaults to the account ID the AWS provider is currently connected to.
        """
        return pulumi.get(self, "mesh_owner")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name to use for the virtual gateway. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> pulumi.Output[str]:
        """
        Resource owner's AWS account ID.
        """
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.VirtualGatewaySpec']:
        """
        Virtual gateway specification to apply.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

