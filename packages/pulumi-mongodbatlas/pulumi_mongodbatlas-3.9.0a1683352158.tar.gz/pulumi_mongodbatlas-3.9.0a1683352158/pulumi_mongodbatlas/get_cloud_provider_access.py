# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetCloudProviderAccessResult',
    'AwaitableGetCloudProviderAccessResult',
    'get_cloud_provider_access',
    'get_cloud_provider_access_output',
]

@pulumi.output_type
class GetCloudProviderAccessResult:
    """
    A collection of values returned by getCloudProviderAccess.
    """
    def __init__(__self__, aws_iam_roles=None, id=None, project_id=None):
        if aws_iam_roles and not isinstance(aws_iam_roles, list):
            raise TypeError("Expected argument 'aws_iam_roles' to be a list")
        pulumi.set(__self__, "aws_iam_roles", aws_iam_roles)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="awsIamRoles")
    def aws_iam_roles(self) -> Sequence['outputs.GetCloudProviderAccessAwsIamRoleResult']:
        """
        A list where each represents a Cloud Provider Access Role.
        """
        return pulumi.get(self, "aws_iam_roles")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")


class AwaitableGetCloudProviderAccessResult(GetCloudProviderAccessResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudProviderAccessResult(
            aws_iam_roles=self.aws_iam_roles,
            id=self.id,
            project_id=self.project_id)


def get_cloud_provider_access(project_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudProviderAccessResult:
    """
    `CloudProviderAccess` allows you to get the list of cloud provider access roles, currently only AWS is supported.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    test_role = mongodbatlas.CloudProviderAccess("testRole",
        project_id="<PROJECT-ID>",
        provider_name="AWS")
    all = mongodbatlas.get_cloud_provider_access_output(project_id=test_role.project_id)
    ```


    :param str project_id: The unique ID for the project to get all Cloud Provider Access
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getCloudProviderAccess:getCloudProviderAccess', __args__, opts=opts, typ=GetCloudProviderAccessResult).value

    return AwaitableGetCloudProviderAccessResult(
        aws_iam_roles=__ret__.aws_iam_roles,
        id=__ret__.id,
        project_id=__ret__.project_id)


@_utilities.lift_output_func(get_cloud_provider_access)
def get_cloud_provider_access_output(project_id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudProviderAccessResult]:
    """
    `CloudProviderAccess` allows you to get the list of cloud provider access roles, currently only AWS is supported.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    test_role = mongodbatlas.CloudProviderAccess("testRole",
        project_id="<PROJECT-ID>",
        provider_name="AWS")
    all = mongodbatlas.get_cloud_provider_access_output(project_id=test_role.project_id)
    ```


    :param str project_id: The unique ID for the project to get all Cloud Provider Access
    """
    ...
