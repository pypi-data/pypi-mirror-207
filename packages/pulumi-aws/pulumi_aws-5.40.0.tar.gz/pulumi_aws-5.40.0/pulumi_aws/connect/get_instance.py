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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, arn=None, auto_resolve_best_voices_enabled=None, contact_flow_logs_enabled=None, contact_lens_enabled=None, created_time=None, early_media_enabled=None, id=None, identity_management_type=None, inbound_calls_enabled=None, instance_alias=None, instance_id=None, multi_party_conference_enabled=None, outbound_calls_enabled=None, service_role=None, status=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auto_resolve_best_voices_enabled and not isinstance(auto_resolve_best_voices_enabled, bool):
            raise TypeError("Expected argument 'auto_resolve_best_voices_enabled' to be a bool")
        pulumi.set(__self__, "auto_resolve_best_voices_enabled", auto_resolve_best_voices_enabled)
        if contact_flow_logs_enabled and not isinstance(contact_flow_logs_enabled, bool):
            raise TypeError("Expected argument 'contact_flow_logs_enabled' to be a bool")
        pulumi.set(__self__, "contact_flow_logs_enabled", contact_flow_logs_enabled)
        if contact_lens_enabled and not isinstance(contact_lens_enabled, bool):
            raise TypeError("Expected argument 'contact_lens_enabled' to be a bool")
        pulumi.set(__self__, "contact_lens_enabled", contact_lens_enabled)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if early_media_enabled and not isinstance(early_media_enabled, bool):
            raise TypeError("Expected argument 'early_media_enabled' to be a bool")
        pulumi.set(__self__, "early_media_enabled", early_media_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_management_type and not isinstance(identity_management_type, str):
            raise TypeError("Expected argument 'identity_management_type' to be a str")
        pulumi.set(__self__, "identity_management_type", identity_management_type)
        if inbound_calls_enabled and not isinstance(inbound_calls_enabled, bool):
            raise TypeError("Expected argument 'inbound_calls_enabled' to be a bool")
        pulumi.set(__self__, "inbound_calls_enabled", inbound_calls_enabled)
        if instance_alias and not isinstance(instance_alias, str):
            raise TypeError("Expected argument 'instance_alias' to be a str")
        pulumi.set(__self__, "instance_alias", instance_alias)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if multi_party_conference_enabled and not isinstance(multi_party_conference_enabled, bool):
            raise TypeError("Expected argument 'multi_party_conference_enabled' to be a bool")
        pulumi.set(__self__, "multi_party_conference_enabled", multi_party_conference_enabled)
        if outbound_calls_enabled and not isinstance(outbound_calls_enabled, bool):
            raise TypeError("Expected argument 'outbound_calls_enabled' to be a bool")
        pulumi.set(__self__, "outbound_calls_enabled", outbound_calls_enabled)
        if service_role and not isinstance(service_role, str):
            raise TypeError("Expected argument 'service_role' to be a str")
        pulumi.set(__self__, "service_role", service_role)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the instance.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(self) -> bool:
        return pulumi.get(self, "auto_resolve_best_voices_enabled")

    @property
    @pulumi.getter(name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(self) -> bool:
        """
        Whether contact flow logs are enabled.
        """
        return pulumi.get(self, "contact_flow_logs_enabled")

    @property
    @pulumi.getter(name="contactLensEnabled")
    def contact_lens_enabled(self) -> bool:
        """
        Whether contact lens is enabled.
        """
        return pulumi.get(self, "contact_lens_enabled")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        When the instance was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="earlyMediaEnabled")
    def early_media_enabled(self) -> bool:
        """
        Whether early media for outbound calls is enabled .
        """
        return pulumi.get(self, "early_media_enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityManagementType")
    def identity_management_type(self) -> str:
        """
        Specifies The identity management type attached to the instance.
        """
        return pulumi.get(self, "identity_management_type")

    @property
    @pulumi.getter(name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> bool:
        """
        Whether inbound calls are enabled.
        """
        return pulumi.get(self, "inbound_calls_enabled")

    @property
    @pulumi.getter(name="instanceAlias")
    def instance_alias(self) -> str:
        return pulumi.get(self, "instance_alias")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="multiPartyConferenceEnabled")
    def multi_party_conference_enabled(self) -> bool:
        """
        Whether multi-party calls/conference is enabled.
        """
        return pulumi.get(self, "multi_party_conference_enabled")

    @property
    @pulumi.getter(name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> bool:
        """
        Whether outbound calls are enabled.
        """
        return pulumi.get(self, "outbound_calls_enabled")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> str:
        """
        Service role of the instance.
        """
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        State of the instance.
        """
        return pulumi.get(self, "status")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            arn=self.arn,
            auto_resolve_best_voices_enabled=self.auto_resolve_best_voices_enabled,
            contact_flow_logs_enabled=self.contact_flow_logs_enabled,
            contact_lens_enabled=self.contact_lens_enabled,
            created_time=self.created_time,
            early_media_enabled=self.early_media_enabled,
            id=self.id,
            identity_management_type=self.identity_management_type,
            inbound_calls_enabled=self.inbound_calls_enabled,
            instance_alias=self.instance_alias,
            instance_id=self.instance_id,
            multi_party_conference_enabled=self.multi_party_conference_enabled,
            outbound_calls_enabled=self.outbound_calls_enabled,
            service_role=self.service_role,
            status=self.status)


def get_instance(instance_alias: Optional[str] = None,
                 instance_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Provides details about a specific Amazon Connect Instance.

    ## Example Usage

    By instance_alias

    ```python
    import pulumi
    import pulumi_aws as aws

    foo = aws.connect.get_instance(instance_alias="foo")
    ```

    By instance_id

    ```python
    import pulumi
    import pulumi_aws as aws

    foo = aws.connect.get_instance(instance_id="97afc98d-101a-ba98-ab97-ae114fc115ec")
    ```


    :param str instance_alias: Returns information on a specific connect instance by alias
    :param str instance_id: Returns information on a specific connect instance by id
    """
    __args__ = dict()
    __args__['instanceAlias'] = instance_alias
    __args__['instanceId'] = instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:connect/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        arn=__ret__.arn,
        auto_resolve_best_voices_enabled=__ret__.auto_resolve_best_voices_enabled,
        contact_flow_logs_enabled=__ret__.contact_flow_logs_enabled,
        contact_lens_enabled=__ret__.contact_lens_enabled,
        created_time=__ret__.created_time,
        early_media_enabled=__ret__.early_media_enabled,
        id=__ret__.id,
        identity_management_type=__ret__.identity_management_type,
        inbound_calls_enabled=__ret__.inbound_calls_enabled,
        instance_alias=__ret__.instance_alias,
        instance_id=__ret__.instance_id,
        multi_party_conference_enabled=__ret__.multi_party_conference_enabled,
        outbound_calls_enabled=__ret__.outbound_calls_enabled,
        service_role=__ret__.service_role,
        status=__ret__.status)


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_alias: Optional[pulumi.Input[Optional[str]]] = None,
                        instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Provides details about a specific Amazon Connect Instance.

    ## Example Usage

    By instance_alias

    ```python
    import pulumi
    import pulumi_aws as aws

    foo = aws.connect.get_instance(instance_alias="foo")
    ```

    By instance_id

    ```python
    import pulumi
    import pulumi_aws as aws

    foo = aws.connect.get_instance(instance_id="97afc98d-101a-ba98-ab97-ae114fc115ec")
    ```


    :param str instance_alias: Returns information on a specific connect instance by alias
    :param str instance_id: Returns information on a specific connect instance by id
    """
    ...
