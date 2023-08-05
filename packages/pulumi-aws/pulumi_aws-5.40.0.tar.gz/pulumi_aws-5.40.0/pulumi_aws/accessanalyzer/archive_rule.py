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

__all__ = ['ArchiveRuleArgs', 'ArchiveRule']

@pulumi.input_type
class ArchiveRuleArgs:
    def __init__(__self__, *,
                 analyzer_name: pulumi.Input[str],
                 filters: pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]],
                 rule_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ArchiveRule resource.
        :param pulumi.Input[str] analyzer_name: Analyzer name.
        :param pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]] filters: Filter criteria for the archive rule. See Filter for more details.
        :param pulumi.Input[str] rule_name: Rule name.
        """
        pulumi.set(__self__, "analyzer_name", analyzer_name)
        pulumi.set(__self__, "filters", filters)
        pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> pulumi.Input[str]:
        """
        Analyzer name.
        """
        return pulumi.get(self, "analyzer_name")

    @analyzer_name.setter
    def analyzer_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "analyzer_name", value)

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]]:
        """
        Filter criteria for the archive rule. See Filter for more details.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[str]:
        """
        Rule name.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_name", value)


@pulumi.input_type
class _ArchiveRuleState:
    def __init__(__self__, *,
                 analyzer_name: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ArchiveRule resources.
        :param pulumi.Input[str] analyzer_name: Analyzer name.
        :param pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]] filters: Filter criteria for the archive rule. See Filter for more details.
        :param pulumi.Input[str] rule_name: Rule name.
        """
        if analyzer_name is not None:
            pulumi.set(__self__, "analyzer_name", analyzer_name)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> Optional[pulumi.Input[str]]:
        """
        Analyzer name.
        """
        return pulumi.get(self, "analyzer_name")

    @analyzer_name.setter
    def analyzer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "analyzer_name", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]]]:
        """
        Filter criteria for the archive rule. See Filter for more details.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ArchiveRuleFilterArgs']]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Rule name.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)


class ArchiveRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analyzer_name: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArchiveRuleFilterArgs']]]]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing an AWS AccessAnalyzer Archive Rule.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.accessanalyzer.ArchiveRule("example",
            analyzer_name="example-analyzer",
            filters=[
                aws.accessanalyzer.ArchiveRuleFilterArgs(
                    criteria="condition.aws:UserId",
                    eqs=["userid"],
                ),
                aws.accessanalyzer.ArchiveRuleFilterArgs(
                    criteria="error",
                    exists="true",
                ),
                aws.accessanalyzer.ArchiveRuleFilterArgs(
                    criteria="isPublic",
                    eqs=["false"],
                ),
            ],
            rule_name="example-rule")
        ```

        ## Import

        AccessAnalyzer ArchiveRule can be imported using the `analyzer_name/rule_name`, e.g.,

        ```sh
         $ pulumi import aws:accessanalyzer/archiveRule:ArchiveRule example example-analyzer/example-rule
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] analyzer_name: Analyzer name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArchiveRuleFilterArgs']]]] filters: Filter criteria for the archive rule. See Filter for more details.
        :param pulumi.Input[str] rule_name: Rule name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ArchiveRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing an AWS AccessAnalyzer Archive Rule.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.accessanalyzer.ArchiveRule("example",
            analyzer_name="example-analyzer",
            filters=[
                aws.accessanalyzer.ArchiveRuleFilterArgs(
                    criteria="condition.aws:UserId",
                    eqs=["userid"],
                ),
                aws.accessanalyzer.ArchiveRuleFilterArgs(
                    criteria="error",
                    exists="true",
                ),
                aws.accessanalyzer.ArchiveRuleFilterArgs(
                    criteria="isPublic",
                    eqs=["false"],
                ),
            ],
            rule_name="example-rule")
        ```

        ## Import

        AccessAnalyzer ArchiveRule can be imported using the `analyzer_name/rule_name`, e.g.,

        ```sh
         $ pulumi import aws:accessanalyzer/archiveRule:ArchiveRule example example-analyzer/example-rule
        ```

        :param str resource_name: The name of the resource.
        :param ArchiveRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ArchiveRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analyzer_name: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArchiveRuleFilterArgs']]]]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ArchiveRuleArgs.__new__(ArchiveRuleArgs)

            if analyzer_name is None and not opts.urn:
                raise TypeError("Missing required property 'analyzer_name'")
            __props__.__dict__["analyzer_name"] = analyzer_name
            if filters is None and not opts.urn:
                raise TypeError("Missing required property 'filters'")
            __props__.__dict__["filters"] = filters
            if rule_name is None and not opts.urn:
                raise TypeError("Missing required property 'rule_name'")
            __props__.__dict__["rule_name"] = rule_name
        super(ArchiveRule, __self__).__init__(
            'aws:accessanalyzer/archiveRule:ArchiveRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            analyzer_name: Optional[pulumi.Input[str]] = None,
            filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArchiveRuleFilterArgs']]]]] = None,
            rule_name: Optional[pulumi.Input[str]] = None) -> 'ArchiveRule':
        """
        Get an existing ArchiveRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] analyzer_name: Analyzer name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArchiveRuleFilterArgs']]]] filters: Filter criteria for the archive rule. See Filter for more details.
        :param pulumi.Input[str] rule_name: Rule name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ArchiveRuleState.__new__(_ArchiveRuleState)

        __props__.__dict__["analyzer_name"] = analyzer_name
        __props__.__dict__["filters"] = filters
        __props__.__dict__["rule_name"] = rule_name
        return ArchiveRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> pulumi.Output[str]:
        """
        Analyzer name.
        """
        return pulumi.get(self, "analyzer_name")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Sequence['outputs.ArchiveRuleFilter']]:
        """
        Filter criteria for the archive rule. See Filter for more details.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[str]:
        """
        Rule name.
        """
        return pulumi.get(self, "rule_name")

