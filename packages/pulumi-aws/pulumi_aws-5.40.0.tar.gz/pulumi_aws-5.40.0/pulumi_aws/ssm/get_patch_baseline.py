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

__all__ = [
    'GetPatchBaselineResult',
    'AwaitableGetPatchBaselineResult',
    'get_patch_baseline',
    'get_patch_baseline_output',
]

@pulumi.output_type
class GetPatchBaselineResult:
    """
    A collection of values returned by getPatchBaseline.
    """
    def __init__(__self__, approval_rules=None, approved_patches=None, approved_patches_compliance_level=None, approved_patches_enable_non_security=None, default_baseline=None, description=None, global_filters=None, id=None, name=None, name_prefix=None, operating_system=None, owner=None, rejected_patches=None, rejected_patches_action=None, sources=None):
        if approval_rules and not isinstance(approval_rules, list):
            raise TypeError("Expected argument 'approval_rules' to be a list")
        pulumi.set(__self__, "approval_rules", approval_rules)
        if approved_patches and not isinstance(approved_patches, list):
            raise TypeError("Expected argument 'approved_patches' to be a list")
        pulumi.set(__self__, "approved_patches", approved_patches)
        if approved_patches_compliance_level and not isinstance(approved_patches_compliance_level, str):
            raise TypeError("Expected argument 'approved_patches_compliance_level' to be a str")
        pulumi.set(__self__, "approved_patches_compliance_level", approved_patches_compliance_level)
        if approved_patches_enable_non_security and not isinstance(approved_patches_enable_non_security, bool):
            raise TypeError("Expected argument 'approved_patches_enable_non_security' to be a bool")
        pulumi.set(__self__, "approved_patches_enable_non_security", approved_patches_enable_non_security)
        if default_baseline and not isinstance(default_baseline, bool):
            raise TypeError("Expected argument 'default_baseline' to be a bool")
        pulumi.set(__self__, "default_baseline", default_baseline)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if global_filters and not isinstance(global_filters, list):
            raise TypeError("Expected argument 'global_filters' to be a list")
        pulumi.set(__self__, "global_filters", global_filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_prefix and not isinstance(name_prefix, str):
            raise TypeError("Expected argument 'name_prefix' to be a str")
        pulumi.set(__self__, "name_prefix", name_prefix)
        if operating_system and not isinstance(operating_system, str):
            raise TypeError("Expected argument 'operating_system' to be a str")
        pulumi.set(__self__, "operating_system", operating_system)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if rejected_patches and not isinstance(rejected_patches, list):
            raise TypeError("Expected argument 'rejected_patches' to be a list")
        pulumi.set(__self__, "rejected_patches", rejected_patches)
        if rejected_patches_action and not isinstance(rejected_patches_action, str):
            raise TypeError("Expected argument 'rejected_patches_action' to be a str")
        pulumi.set(__self__, "rejected_patches_action", rejected_patches_action)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter(name="approvalRules")
    def approval_rules(self) -> Sequence['outputs.GetPatchBaselineApprovalRuleResult']:
        """
        List of rules used to include patches in the baseline.
        """
        return pulumi.get(self, "approval_rules")

    @property
    @pulumi.getter(name="approvedPatches")
    def approved_patches(self) -> Sequence[str]:
        """
        List of explicitly approved patches for the baseline.
        """
        return pulumi.get(self, "approved_patches")

    @property
    @pulumi.getter(name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> str:
        """
        The compliance level for approved patches.
        """
        return pulumi.get(self, "approved_patches_compliance_level")

    @property
    @pulumi.getter(name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(self) -> bool:
        """
        Indicates whether the list of approved patches includes non-security updates that should be applied to the instances.
        """
        return pulumi.get(self, "approved_patches_enable_non_security")

    @property
    @pulumi.getter(name="defaultBaseline")
    def default_baseline(self) -> Optional[bool]:
        return pulumi.get(self, "default_baseline")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the baseline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="globalFilters")
    def global_filters(self) -> Sequence['outputs.GetPatchBaselineGlobalFilterResult']:
        """
        Set of global filters used to exclude patches from the baseline.
        """
        return pulumi.get(self, "global_filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name specified to identify the patch source.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[str]:
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[str]:
        return pulumi.get(self, "operating_system")

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="rejectedPatches")
    def rejected_patches(self) -> Sequence[str]:
        """
        List of rejected patches.
        """
        return pulumi.get(self, "rejected_patches")

    @property
    @pulumi.getter(name="rejectedPatchesAction")
    def rejected_patches_action(self) -> str:
        """
        The action specified to take on patches included in the `rejected_patches` list.
        """
        return pulumi.get(self, "rejected_patches_action")

    @property
    @pulumi.getter
    def sources(self) -> Sequence['outputs.GetPatchBaselineSourceResult']:
        """
        Information about the patches to use to update the managed nodes, including target operating systems and source repositories.
        """
        return pulumi.get(self, "sources")


class AwaitableGetPatchBaselineResult(GetPatchBaselineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPatchBaselineResult(
            approval_rules=self.approval_rules,
            approved_patches=self.approved_patches,
            approved_patches_compliance_level=self.approved_patches_compliance_level,
            approved_patches_enable_non_security=self.approved_patches_enable_non_security,
            default_baseline=self.default_baseline,
            description=self.description,
            global_filters=self.global_filters,
            id=self.id,
            name=self.name,
            name_prefix=self.name_prefix,
            operating_system=self.operating_system,
            owner=self.owner,
            rejected_patches=self.rejected_patches,
            rejected_patches_action=self.rejected_patches_action,
            sources=self.sources)


def get_patch_baseline(default_baseline: Optional[bool] = None,
                       name_prefix: Optional[str] = None,
                       operating_system: Optional[str] = None,
                       owner: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPatchBaselineResult:
    """
    Provides an SSM Patch Baseline data source. Useful if you wish to reuse the default baselines provided.

    ## Example Usage

    To retrieve a baseline provided by AWS:

    ```python
    import pulumi
    import pulumi_aws as aws

    centos = aws.ssm.get_patch_baseline(name_prefix="AWS-",
        operating_system="CENTOS",
        owner="AWS")
    ```

    To retrieve a baseline on your account:

    ```python
    import pulumi
    import pulumi_aws as aws

    default_custom = aws.ssm.get_patch_baseline(default_baseline=True,
        name_prefix="MyCustomBaseline",
        operating_system="WINDOWS",
        owner="Self")
    ```


    :param bool default_baseline: Filters the results against the baselines default_baseline field.
    :param str name_prefix: Filter results by the baseline name prefix.
    :param str operating_system: Specified OS for the baseline. Valid values: `AMAZON_LINUX`, `AMAZON_LINUX_2`, `UBUNTU`, `REDHAT_ENTERPRISE_LINUX`, `SUSE`, `CENTOS`, `ORACLE_LINUX`, `DEBIAN`, `MACOS`, `RASPBIAN` and `ROCKY_LINUX`.
    :param str owner: Owner of the baseline. Valid values: `All`, `AWS`, `Self` (the current account).
    """
    __args__ = dict()
    __args__['defaultBaseline'] = default_baseline
    __args__['namePrefix'] = name_prefix
    __args__['operatingSystem'] = operating_system
    __args__['owner'] = owner
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:ssm/getPatchBaseline:getPatchBaseline', __args__, opts=opts, typ=GetPatchBaselineResult).value

    return AwaitableGetPatchBaselineResult(
        approval_rules=__ret__.approval_rules,
        approved_patches=__ret__.approved_patches,
        approved_patches_compliance_level=__ret__.approved_patches_compliance_level,
        approved_patches_enable_non_security=__ret__.approved_patches_enable_non_security,
        default_baseline=__ret__.default_baseline,
        description=__ret__.description,
        global_filters=__ret__.global_filters,
        id=__ret__.id,
        name=__ret__.name,
        name_prefix=__ret__.name_prefix,
        operating_system=__ret__.operating_system,
        owner=__ret__.owner,
        rejected_patches=__ret__.rejected_patches,
        rejected_patches_action=__ret__.rejected_patches_action,
        sources=__ret__.sources)


@_utilities.lift_output_func(get_patch_baseline)
def get_patch_baseline_output(default_baseline: Optional[pulumi.Input[Optional[bool]]] = None,
                              name_prefix: Optional[pulumi.Input[Optional[str]]] = None,
                              operating_system: Optional[pulumi.Input[Optional[str]]] = None,
                              owner: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPatchBaselineResult]:
    """
    Provides an SSM Patch Baseline data source. Useful if you wish to reuse the default baselines provided.

    ## Example Usage

    To retrieve a baseline provided by AWS:

    ```python
    import pulumi
    import pulumi_aws as aws

    centos = aws.ssm.get_patch_baseline(name_prefix="AWS-",
        operating_system="CENTOS",
        owner="AWS")
    ```

    To retrieve a baseline on your account:

    ```python
    import pulumi
    import pulumi_aws as aws

    default_custom = aws.ssm.get_patch_baseline(default_baseline=True,
        name_prefix="MyCustomBaseline",
        operating_system="WINDOWS",
        owner="Self")
    ```


    :param bool default_baseline: Filters the results against the baselines default_baseline field.
    :param str name_prefix: Filter results by the baseline name prefix.
    :param str operating_system: Specified OS for the baseline. Valid values: `AMAZON_LINUX`, `AMAZON_LINUX_2`, `UBUNTU`, `REDHAT_ENTERPRISE_LINUX`, `SUSE`, `CENTOS`, `ORACLE_LINUX`, `DEBIAN`, `MACOS`, `RASPBIAN` and `ROCKY_LINUX`.
    :param str owner: Owner of the baseline. Valid values: `All`, `AWS`, `Self` (the current account).
    """
    ...
