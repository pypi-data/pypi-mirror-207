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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 service_catalog_provisioning_details: pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs'],
                 project_description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] project_name: The name of the Project.
        :param pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs'] service_catalog_provisioning_details: The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        :param pulumi.Input[str] project_description: A description for the project.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "service_catalog_provisioning_details", service_catalog_provisioning_details)
        if project_description is not None:
            pulumi.set(__self__, "project_description", project_description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        The name of the Project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs']:
        """
        The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        """
        return pulumi.get(self, "service_catalog_provisioning_details")

    @service_catalog_provisioning_details.setter
    def service_catalog_provisioning_details(self, value: pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs']):
        pulumi.set(self, "service_catalog_provisioning_details", value)

    @property
    @pulumi.getter(name="projectDescription")
    def project_description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the project.
        """
        return pulumi.get(self, "project_description")

    @project_description.setter
    def project_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 project_description: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_catalog_provisioning_details: Optional[pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this Project.
        :param pulumi.Input[str] project_description: A description for the project.
        :param pulumi.Input[str] project_id: The ID of the project.
        :param pulumi.Input[str] project_name: The name of the Project.
        :param pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs'] service_catalog_provisioning_details: The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if project_description is not None:
            pulumi.set(__self__, "project_description", project_description)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if service_catalog_provisioning_details is not None:
            pulumi.set(__self__, "service_catalog_provisioning_details", service_catalog_provisioning_details)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this Project.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="projectDescription")
    def project_description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the project.
        """
        return pulumi.get(self, "project_description")

    @project_description.setter
    def project_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_description", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> Optional[pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs']]:
        """
        The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        """
        return pulumi.get(self, "service_catalog_provisioning_details")

    @service_catalog_provisioning_details.setter
    def service_catalog_provisioning_details(self, value: Optional[pulumi.Input['ProjectServiceCatalogProvisioningDetailsArgs']]):
        pulumi.set(self, "service_catalog_provisioning_details", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_description: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_catalog_provisioning_details: Optional[pulumi.Input[pulumi.InputType['ProjectServiceCatalogProvisioningDetailsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a SageMaker Project resource.

         > Note: If you are trying to use SageMaker projects with SageMaker studio you will need to add a tag with the key `sagemaker:studio-visibility` with value `true`. For more on requirements to use projects and permission needed see [AWS Docs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-custom.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.sagemaker.Project("example",
            project_name="example",
            service_catalog_provisioning_details=aws.sagemaker.ProjectServiceCatalogProvisioningDetailsArgs(
                product_id=aws_servicecatalog_product["example"]["id"],
            ))
        ```

        ## Import

        SageMaker Projects can be imported using the `project_name`, e.g.,

        ```sh
         $ pulumi import aws:sagemaker/project:Project example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_description: A description for the project.
        :param pulumi.Input[str] project_name: The name of the Project.
        :param pulumi.Input[pulumi.InputType['ProjectServiceCatalogProvisioningDetailsArgs']] service_catalog_provisioning_details: The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a SageMaker Project resource.

         > Note: If you are trying to use SageMaker projects with SageMaker studio you will need to add a tag with the key `sagemaker:studio-visibility` with value `true`. For more on requirements to use projects and permission needed see [AWS Docs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-custom.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.sagemaker.Project("example",
            project_name="example",
            service_catalog_provisioning_details=aws.sagemaker.ProjectServiceCatalogProvisioningDetailsArgs(
                product_id=aws_servicecatalog_product["example"]["id"],
            ))
        ```

        ## Import

        SageMaker Projects can be imported using the `project_name`, e.g.,

        ```sh
         $ pulumi import aws:sagemaker/project:Project example example
        ```

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_description: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_catalog_provisioning_details: Optional[pulumi.Input[pulumi.InputType['ProjectServiceCatalogProvisioningDetailsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["project_description"] = project_description
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if service_catalog_provisioning_details is None and not opts.urn:
                raise TypeError("Missing required property 'service_catalog_provisioning_details'")
            __props__.__dict__["service_catalog_provisioning_details"] = service_catalog_provisioning_details
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
            __props__.__dict__["project_id"] = None
        super(Project, __self__).__init__(
            'aws:sagemaker/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            project_description: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            project_name: Optional[pulumi.Input[str]] = None,
            service_catalog_provisioning_details: Optional[pulumi.Input[pulumi.InputType['ProjectServiceCatalogProvisioningDetailsArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this Project.
        :param pulumi.Input[str] project_description: A description for the project.
        :param pulumi.Input[str] project_id: The ID of the project.
        :param pulumi.Input[str] project_name: The name of the Project.
        :param pulumi.Input[pulumi.InputType['ProjectServiceCatalogProvisioningDetailsArgs']] service_catalog_provisioning_details: The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["project_description"] = project_description
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["project_name"] = project_name
        __props__.__dict__["service_catalog_provisioning_details"] = service_catalog_provisioning_details
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this Project.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="projectDescription")
    def project_description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the project.
        """
        return pulumi.get(self, "project_description")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Output[str]:
        """
        The name of the Project.
        """
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter(name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> pulumi.Output['outputs.ProjectServiceCatalogProvisioningDetails']:
        """
        The product ID and provisioning artifact ID to provision a service catalog. See Service Catalog Provisioning Details below.
        """
        return pulumi.get(self, "service_catalog_provisioning_details")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

