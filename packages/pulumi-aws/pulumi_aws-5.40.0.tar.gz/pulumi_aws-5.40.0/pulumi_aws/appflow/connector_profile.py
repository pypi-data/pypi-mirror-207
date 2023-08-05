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

__all__ = ['ConnectorProfileArgs', 'ConnectorProfile']

@pulumi.input_type
class ConnectorProfileArgs:
    def __init__(__self__, *,
                 connection_mode: pulumi.Input[str],
                 connector_profile_config: pulumi.Input['ConnectorProfileConnectorProfileConfigArgs'],
                 connector_type: pulumi.Input[str],
                 connector_label: Optional[pulumi.Input[str]] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectorProfile resource.
        :param pulumi.Input[str] connection_mode: Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        :param pulumi.Input['ConnectorProfileConnectorProfileConfigArgs'] connector_profile_config: Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        :param pulumi.Input[str] connector_type: The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        :param pulumi.Input[str] connector_label: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        :param pulumi.Input[str] kms_arn: ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        pulumi.set(__self__, "connection_mode", connection_mode)
        pulumi.set(__self__, "connector_profile_config", connector_profile_config)
        pulumi.set(__self__, "connector_type", connector_type)
        if connector_label is not None:
            pulumi.set(__self__, "connector_label", connector_label)
        if kms_arn is not None:
            pulumi.set(__self__, "kms_arn", kms_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Input[str]:
        """
        Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        """
        return pulumi.get(self, "connection_mode")

    @connection_mode.setter
    def connection_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_mode", value)

    @property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> pulumi.Input['ConnectorProfileConnectorProfileConfigArgs']:
        """
        Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        """
        return pulumi.get(self, "connector_profile_config")

    @connector_profile_config.setter
    def connector_profile_config(self, value: pulumi.Input['ConnectorProfileConnectorProfileConfigArgs']):
        pulumi.set(self, "connector_profile_config", value)

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[str]:
        """
        The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        """
        return pulumi.get(self, "connector_type")

    @connector_type.setter
    def connector_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "connector_type", value)

    @property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> Optional[pulumi.Input[str]]:
        """
        The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        """
        return pulumi.get(self, "connector_label")

    @connector_label.setter
    def connector_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_label", value)

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        return pulumi.get(self, "kms_arn")

    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConnectorProfileState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 connection_mode: Optional[pulumi.Input[str]] = None,
                 connector_label: Optional[pulumi.Input[str]] = None,
                 connector_profile_config: Optional[pulumi.Input['ConnectorProfileConnectorProfileConfigArgs']] = None,
                 connector_type: Optional[pulumi.Input[str]] = None,
                 credentials_arn: Optional[pulumi.Input[str]] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConnectorProfile resources.
        :param pulumi.Input[str] arn: ARN of the connector profile.
        :param pulumi.Input[str] connection_mode: Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        :param pulumi.Input[str] connector_label: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        :param pulumi.Input['ConnectorProfileConnectorProfileConfigArgs'] connector_profile_config: Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        :param pulumi.Input[str] connector_type: The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        :param pulumi.Input[str] credentials_arn: ARN of the connector profile credentials.
        :param pulumi.Input[str] kms_arn: ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if connection_mode is not None:
            pulumi.set(__self__, "connection_mode", connection_mode)
        if connector_label is not None:
            pulumi.set(__self__, "connector_label", connector_label)
        if connector_profile_config is not None:
            pulumi.set(__self__, "connector_profile_config", connector_profile_config)
        if connector_type is not None:
            pulumi.set(__self__, "connector_type", connector_type)
        if credentials_arn is not None:
            pulumi.set(__self__, "credentials_arn", credentials_arn)
        if kms_arn is not None:
            pulumi.set(__self__, "kms_arn", kms_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the connector profile.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        """
        return pulumi.get(self, "connection_mode")

    @connection_mode.setter
    def connection_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_mode", value)

    @property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> Optional[pulumi.Input[str]]:
        """
        The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        """
        return pulumi.get(self, "connector_label")

    @connector_label.setter
    def connector_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_label", value)

    @property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> Optional[pulumi.Input['ConnectorProfileConnectorProfileConfigArgs']]:
        """
        Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        """
        return pulumi.get(self, "connector_profile_config")

    @connector_profile_config.setter
    def connector_profile_config(self, value: Optional[pulumi.Input['ConnectorProfileConnectorProfileConfigArgs']]):
        pulumi.set(self, "connector_profile_config", value)

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        """
        return pulumi.get(self, "connector_type")

    @connector_type.setter
    def connector_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_type", value)

    @property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the connector profile credentials.
        """
        return pulumi.get(self, "credentials_arn")

    @credentials_arn.setter
    def credentials_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credentials_arn", value)

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        return pulumi.get(self, "kms_arn")

    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ConnectorProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_mode: Optional[pulumi.Input[str]] = None,
                 connector_label: Optional[pulumi.Input[str]] = None,
                 connector_profile_config: Optional[pulumi.Input[pulumi.InputType['ConnectorProfileConnectorProfileConfigArgs']]] = None,
                 connector_type: Optional[pulumi.Input[str]] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an AppFlow connector profile resource.

        For information about AppFlow flows, see the [Amazon AppFlow API Reference](https://docs.aws.amazon.com/appflow/1.0/APIReference/Welcome.html).
        For specific information about creating an AppFlow connector profile, see the
        [CreateConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html) page in the Amazon AppFlow API Reference.

        ## Import

        AppFlow Connector Profile can be imported using the connector profile `arn`, e.g.

        ```sh
         $ pulumi import aws:appflow/connectorProfile:ConnectorProfile profile arn:aws:appflow:us-west-2:123456789012:connectorprofile/example-profile
        ```

         [1]https://docs.aws.amazon.com/appflow/1.0/APIReference/Welcome.html [2]https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_mode: Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        :param pulumi.Input[str] connector_label: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        :param pulumi.Input[pulumi.InputType['ConnectorProfileConnectorProfileConfigArgs']] connector_profile_config: Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        :param pulumi.Input[str] connector_type: The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        :param pulumi.Input[str] kms_arn: ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AppFlow connector profile resource.

        For information about AppFlow flows, see the [Amazon AppFlow API Reference](https://docs.aws.amazon.com/appflow/1.0/APIReference/Welcome.html).
        For specific information about creating an AppFlow connector profile, see the
        [CreateConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html) page in the Amazon AppFlow API Reference.

        ## Import

        AppFlow Connector Profile can be imported using the connector profile `arn`, e.g.

        ```sh
         $ pulumi import aws:appflow/connectorProfile:ConnectorProfile profile arn:aws:appflow:us-west-2:123456789012:connectorprofile/example-profile
        ```

         [1]https://docs.aws.amazon.com/appflow/1.0/APIReference/Welcome.html [2]https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html

        :param str resource_name: The name of the resource.
        :param ConnectorProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_mode: Optional[pulumi.Input[str]] = None,
                 connector_label: Optional[pulumi.Input[str]] = None,
                 connector_profile_config: Optional[pulumi.Input[pulumi.InputType['ConnectorProfileConnectorProfileConfigArgs']]] = None,
                 connector_type: Optional[pulumi.Input[str]] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorProfileArgs.__new__(ConnectorProfileArgs)

            if connection_mode is None and not opts.urn:
                raise TypeError("Missing required property 'connection_mode'")
            __props__.__dict__["connection_mode"] = connection_mode
            __props__.__dict__["connector_label"] = connector_label
            if connector_profile_config is None and not opts.urn:
                raise TypeError("Missing required property 'connector_profile_config'")
            __props__.__dict__["connector_profile_config"] = connector_profile_config
            if connector_type is None and not opts.urn:
                raise TypeError("Missing required property 'connector_type'")
            __props__.__dict__["connector_type"] = connector_type
            __props__.__dict__["kms_arn"] = kms_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["arn"] = None
            __props__.__dict__["credentials_arn"] = None
        super(ConnectorProfile, __self__).__init__(
            'aws:appflow/connectorProfile:ConnectorProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            connection_mode: Optional[pulumi.Input[str]] = None,
            connector_label: Optional[pulumi.Input[str]] = None,
            connector_profile_config: Optional[pulumi.Input[pulumi.InputType['ConnectorProfileConnectorProfileConfigArgs']]] = None,
            connector_type: Optional[pulumi.Input[str]] = None,
            credentials_arn: Optional[pulumi.Input[str]] = None,
            kms_arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ConnectorProfile':
        """
        Get an existing ConnectorProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the connector profile.
        :param pulumi.Input[str] connection_mode: Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        :param pulumi.Input[str] connector_label: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        :param pulumi.Input[pulumi.InputType['ConnectorProfileConnectorProfileConfigArgs']] connector_profile_config: Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        :param pulumi.Input[str] connector_type: The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        :param pulumi.Input[str] credentials_arn: ARN of the connector profile credentials.
        :param pulumi.Input[str] kms_arn: ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectorProfileState.__new__(_ConnectorProfileState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["connection_mode"] = connection_mode
        __props__.__dict__["connector_label"] = connector_label
        __props__.__dict__["connector_profile_config"] = connector_profile_config
        __props__.__dict__["connector_type"] = connector_type
        __props__.__dict__["credentials_arn"] = credentials_arn
        __props__.__dict__["kms_arn"] = kms_arn
        __props__.__dict__["name"] = name
        return ConnectorProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the connector profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Output[str]:
        """
        Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: `Public`, `Private`.
        """
        return pulumi.get(self, "connection_mode")

    @property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> pulumi.Output[Optional[str]]:
        """
        The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for `CustomConnector` connector type.
        """
        return pulumi.get(self, "connector_label")

    @property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> pulumi.Output['outputs.ConnectorProfileConnectorProfileConfig']:
        """
        Defines the connector-specific configuration and credentials. See Connector Profile Config for more details.
        """
        return pulumi.get(self, "connector_profile_config")

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output[str]:
        """
        The type of connector. One of: `Amplitude`, `CustomConnector`, `CustomerProfiles`, `Datadog`, `Dynatrace`, `EventBridge`, `Googleanalytics`, `Honeycode`, `Infornexus`, `LookoutMetrics`, `Marketo`, `Redshift`, `S3`, `Salesforce`, `SAPOData`, `Servicenow`, `Singular`, `Slack`, `Snowflake`, `Trendmicro`, `Upsolver`, `Veeva`, `Zendesk`.
        """
        return pulumi.get(self, "connector_type")

    @property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> pulumi.Output[str]:
        """
        ARN of the connector profile credentials.
        """
        return pulumi.get(self, "credentials_arn")

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> pulumi.Output[str]:
        """
        ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        """
        return pulumi.get(self, "kms_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

