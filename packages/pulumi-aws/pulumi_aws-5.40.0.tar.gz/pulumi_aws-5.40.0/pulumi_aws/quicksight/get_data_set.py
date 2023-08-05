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

__all__ = [
    'GetDataSetResult',
    'AwaitableGetDataSetResult',
    'get_data_set',
    'get_data_set_output',
]

@pulumi.output_type
class GetDataSetResult:
    """
    A collection of values returned by getDataSet.
    """
    def __init__(__self__, arn=None, aws_account_id=None, column_groups=None, column_level_permission_rules=None, data_set_id=None, data_set_usage_configurations=None, field_folders=None, id=None, import_mode=None, logical_table_maps=None, name=None, permissions=None, physical_table_maps=None, row_level_permission_data_sets=None, row_level_permission_tag_configurations=None, tags=None, tags_all=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if aws_account_id and not isinstance(aws_account_id, str):
            raise TypeError("Expected argument 'aws_account_id' to be a str")
        pulumi.set(__self__, "aws_account_id", aws_account_id)
        if column_groups and not isinstance(column_groups, list):
            raise TypeError("Expected argument 'column_groups' to be a list")
        pulumi.set(__self__, "column_groups", column_groups)
        if column_level_permission_rules and not isinstance(column_level_permission_rules, list):
            raise TypeError("Expected argument 'column_level_permission_rules' to be a list")
        pulumi.set(__self__, "column_level_permission_rules", column_level_permission_rules)
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if data_set_usage_configurations and not isinstance(data_set_usage_configurations, list):
            raise TypeError("Expected argument 'data_set_usage_configurations' to be a list")
        pulumi.set(__self__, "data_set_usage_configurations", data_set_usage_configurations)
        if field_folders and not isinstance(field_folders, list):
            raise TypeError("Expected argument 'field_folders' to be a list")
        pulumi.set(__self__, "field_folders", field_folders)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if import_mode and not isinstance(import_mode, str):
            raise TypeError("Expected argument 'import_mode' to be a str")
        pulumi.set(__self__, "import_mode", import_mode)
        if logical_table_maps and not isinstance(logical_table_maps, list):
            raise TypeError("Expected argument 'logical_table_maps' to be a list")
        pulumi.set(__self__, "logical_table_maps", logical_table_maps)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if physical_table_maps and not isinstance(physical_table_maps, list):
            raise TypeError("Expected argument 'physical_table_maps' to be a list")
        pulumi.set(__self__, "physical_table_maps", physical_table_maps)
        if row_level_permission_data_sets and not isinstance(row_level_permission_data_sets, list):
            raise TypeError("Expected argument 'row_level_permission_data_sets' to be a list")
        pulumi.set(__self__, "row_level_permission_data_sets", row_level_permission_data_sets)
        if row_level_permission_tag_configurations and not isinstance(row_level_permission_tag_configurations, list):
            raise TypeError("Expected argument 'row_level_permission_tag_configurations' to be a list")
        pulumi.set(__self__, "row_level_permission_tag_configurations", row_level_permission_tag_configurations)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tags_all and not isinstance(tags_all, dict):
            raise TypeError("Expected argument 'tags_all' to be a dict")
        pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> str:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> Sequence['outputs.GetDataSetColumnGroupResult']:
        return pulumi.get(self, "column_groups")

    @property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(self) -> Optional[Sequence['outputs.GetDataSetColumnLevelPermissionRuleResult']]:
        return pulumi.get(self, "column_level_permission_rules")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataSetUsageConfigurations")
    def data_set_usage_configurations(self) -> Sequence['outputs.GetDataSetDataSetUsageConfigurationResult']:
        return pulumi.get(self, "data_set_usage_configurations")

    @property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> Sequence['outputs.GetDataSetFieldFolderResult']:
        return pulumi.get(self, "field_folders")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> str:
        return pulumi.get(self, "import_mode")

    @property
    @pulumi.getter(name="logicalTableMaps")
    def logical_table_maps(self) -> Sequence['outputs.GetDataSetLogicalTableMapResult']:
        return pulumi.get(self, "logical_table_maps")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Sequence['outputs.GetDataSetPermissionResult']:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="physicalTableMaps")
    def physical_table_maps(self) -> Sequence['outputs.GetDataSetPhysicalTableMapResult']:
        return pulumi.get(self, "physical_table_maps")

    @property
    @pulumi.getter(name="rowLevelPermissionDataSets")
    def row_level_permission_data_sets(self) -> Sequence['outputs.GetDataSetRowLevelPermissionDataSetResult']:
        return pulumi.get(self, "row_level_permission_data_sets")

    @property
    @pulumi.getter(name="rowLevelPermissionTagConfigurations")
    def row_level_permission_tag_configurations(self) -> Sequence['outputs.GetDataSetRowLevelPermissionTagConfigurationResult']:
        return pulumi.get(self, "row_level_permission_tag_configurations")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags_all")


class AwaitableGetDataSetResult(GetDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSetResult(
            arn=self.arn,
            aws_account_id=self.aws_account_id,
            column_groups=self.column_groups,
            column_level_permission_rules=self.column_level_permission_rules,
            data_set_id=self.data_set_id,
            data_set_usage_configurations=self.data_set_usage_configurations,
            field_folders=self.field_folders,
            id=self.id,
            import_mode=self.import_mode,
            logical_table_maps=self.logical_table_maps,
            name=self.name,
            permissions=self.permissions,
            physical_table_maps=self.physical_table_maps,
            row_level_permission_data_sets=self.row_level_permission_data_sets,
            row_level_permission_tag_configurations=self.row_level_permission_tag_configurations,
            tags=self.tags,
            tags_all=self.tags_all)


def get_data_set(aws_account_id: Optional[str] = None,
                 column_level_permission_rules: Optional[Sequence[pulumi.InputType['GetDataSetColumnLevelPermissionRuleArgs']]] = None,
                 data_set_id: Optional[str] = None,
                 tags: Optional[Mapping[str, str]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSetResult:
    """
    Data source for managing a QuickSight Data Set.

    ## Example Usage
    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.quicksight.get_data_set(data_set_id="example-id")
    ```


    :param str aws_account_id: AWS account ID.
    :param str data_set_id: Identifier for the data set.
    """
    __args__ = dict()
    __args__['awsAccountId'] = aws_account_id
    __args__['columnLevelPermissionRules'] = column_level_permission_rules
    __args__['dataSetId'] = data_set_id
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:quicksight/getDataSet:getDataSet', __args__, opts=opts, typ=GetDataSetResult).value

    return AwaitableGetDataSetResult(
        arn=__ret__.arn,
        aws_account_id=__ret__.aws_account_id,
        column_groups=__ret__.column_groups,
        column_level_permission_rules=__ret__.column_level_permission_rules,
        data_set_id=__ret__.data_set_id,
        data_set_usage_configurations=__ret__.data_set_usage_configurations,
        field_folders=__ret__.field_folders,
        id=__ret__.id,
        import_mode=__ret__.import_mode,
        logical_table_maps=__ret__.logical_table_maps,
        name=__ret__.name,
        permissions=__ret__.permissions,
        physical_table_maps=__ret__.physical_table_maps,
        row_level_permission_data_sets=__ret__.row_level_permission_data_sets,
        row_level_permission_tag_configurations=__ret__.row_level_permission_tag_configurations,
        tags=__ret__.tags,
        tags_all=__ret__.tags_all)


@_utilities.lift_output_func(get_data_set)
def get_data_set_output(aws_account_id: Optional[pulumi.Input[Optional[str]]] = None,
                        column_level_permission_rules: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDataSetColumnLevelPermissionRuleArgs']]]]] = None,
                        data_set_id: Optional[pulumi.Input[str]] = None,
                        tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataSetResult]:
    """
    Data source for managing a QuickSight Data Set.

    ## Example Usage
    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.quicksight.get_data_set(data_set_id="example-id")
    ```


    :param str aws_account_id: AWS account ID.
    :param str data_set_id: Identifier for the data set.
    """
    ...
