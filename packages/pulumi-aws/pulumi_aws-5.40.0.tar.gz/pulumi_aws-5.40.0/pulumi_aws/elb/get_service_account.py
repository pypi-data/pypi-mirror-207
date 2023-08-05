# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetServiceAccountResult',
    'AwaitableGetServiceAccountResult',
    'get_service_account',
    'get_service_account_output',
]

@pulumi.output_type
class GetServiceAccountResult:
    """
    A collection of values returned by getServiceAccount.
    """
    def __init__(__self__, arn=None, id=None, region=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the AWS ELB service account in the selected region.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")


class AwaitableGetServiceAccountResult(GetServiceAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceAccountResult(
            arn=self.arn,
            id=self.id,
            region=self.region)


def get_service_account(region: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceAccountResult:
    """
    Use this data source to get the Account ID of the [AWS Elastic Load Balancing Service Account](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html#attach-bucket-policy)
    in a given region for the purpose of permitting in S3 bucket policy.

    > **Note:** For AWS Regions opened since Jakarta (`ap-southeast-3`) in December 2021, AWS [documents that](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html#attach-bucket-policy) a [service principal name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) should be used instead of an AWS account ID in any relevant IAM policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    main = aws.elb.get_service_account()
    elb_logs = aws.s3.BucketV2("elbLogs")
    elb_logs_acl = aws.s3.BucketAclV2("elbLogsAcl",
        bucket=elb_logs.id,
        acl="private")
    allow_elb_logging_policy_document = elb_logs.arn.apply(lambda arn: aws.iam.get_policy_document_output(statements=[aws.iam.GetPolicyDocumentStatementArgs(
        effect="Allow",
        principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
            type="AWS",
            identifiers=[main.arn],
        )],
        actions=["s3:PutObject"],
        resources=[f"{arn}/AWSLogs/*"],
    )]))
    allow_elb_logging_bucket_policy = aws.s3.BucketPolicy("allowElbLoggingBucketPolicy",
        bucket=elb_logs.id,
        policy=allow_elb_logging_policy_document.json)
    bar = aws.elb.LoadBalancer("bar",
        availability_zones=["us-west-2a"],
        access_logs=aws.elb.LoadBalancerAccessLogsArgs(
            bucket=elb_logs.id,
            interval=5,
        ),
        listeners=[aws.elb.LoadBalancerListenerArgs(
            instance_port=8000,
            instance_protocol="http",
            lb_port=80,
            lb_protocol="http",
        )])
    ```


    :param str region: Name of the region whose AWS ELB account ID is desired.
           Defaults to the region from the AWS provider configuration.
    """
    __args__ = dict()
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:elb/getServiceAccount:getServiceAccount', __args__, opts=opts, typ=GetServiceAccountResult).value

    return AwaitableGetServiceAccountResult(
        arn=__ret__.arn,
        id=__ret__.id,
        region=__ret__.region)


@_utilities.lift_output_func(get_service_account)
def get_service_account_output(region: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceAccountResult]:
    """
    Use this data source to get the Account ID of the [AWS Elastic Load Balancing Service Account](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html#attach-bucket-policy)
    in a given region for the purpose of permitting in S3 bucket policy.

    > **Note:** For AWS Regions opened since Jakarta (`ap-southeast-3`) in December 2021, AWS [documents that](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html#attach-bucket-policy) a [service principal name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) should be used instead of an AWS account ID in any relevant IAM policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    main = aws.elb.get_service_account()
    elb_logs = aws.s3.BucketV2("elbLogs")
    elb_logs_acl = aws.s3.BucketAclV2("elbLogsAcl",
        bucket=elb_logs.id,
        acl="private")
    allow_elb_logging_policy_document = elb_logs.arn.apply(lambda arn: aws.iam.get_policy_document_output(statements=[aws.iam.GetPolicyDocumentStatementArgs(
        effect="Allow",
        principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
            type="AWS",
            identifiers=[main.arn],
        )],
        actions=["s3:PutObject"],
        resources=[f"{arn}/AWSLogs/*"],
    )]))
    allow_elb_logging_bucket_policy = aws.s3.BucketPolicy("allowElbLoggingBucketPolicy",
        bucket=elb_logs.id,
        policy=allow_elb_logging_policy_document.json)
    bar = aws.elb.LoadBalancer("bar",
        availability_zones=["us-west-2a"],
        access_logs=aws.elb.LoadBalancerAccessLogsArgs(
            bucket=elb_logs.id,
            interval=5,
        ),
        listeners=[aws.elb.LoadBalancerListenerArgs(
            instance_port=8000,
            instance_protocol="http",
            lb_port=80,
            lb_protocol="http",
        )])
    ```


    :param str region: Name of the region whose AWS ELB account ID is desired.
           Defaults to the region from the AWS provider configuration.
    """
    ...
