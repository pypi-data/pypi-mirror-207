# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPrivatelinkEndpointServiceServerlessResult',
    'AwaitableGetPrivatelinkEndpointServiceServerlessResult',
    'get_privatelink_endpoint_service_serverless',
    'get_privatelink_endpoint_service_serverless_output',
]

@pulumi.output_type
class GetPrivatelinkEndpointServiceServerlessResult:
    """
    A collection of values returned by getPrivatelinkEndpointServiceServerless.
    """
    def __init__(__self__, cloud_provider_endpoint_id=None, comment=None, endpoint_id=None, endpoint_service_name=None, error_message=None, id=None, instance_name=None, private_endpoint_ip_address=None, private_link_service_resource_id=None, project_id=None, status=None):
        if cloud_provider_endpoint_id and not isinstance(cloud_provider_endpoint_id, str):
            raise TypeError("Expected argument 'cloud_provider_endpoint_id' to be a str")
        pulumi.set(__self__, "cloud_provider_endpoint_id", cloud_provider_endpoint_id)
        if comment and not isinstance(comment, str):
            raise TypeError("Expected argument 'comment' to be a str")
        pulumi.set(__self__, "comment", comment)
        if endpoint_id and not isinstance(endpoint_id, str):
            raise TypeError("Expected argument 'endpoint_id' to be a str")
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        if endpoint_service_name and not isinstance(endpoint_service_name, str):
            raise TypeError("Expected argument 'endpoint_service_name' to be a str")
        pulumi.set(__self__, "endpoint_service_name", endpoint_service_name)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_name and not isinstance(instance_name, str):
            raise TypeError("Expected argument 'instance_name' to be a str")
        pulumi.set(__self__, "instance_name", instance_name)
        if private_endpoint_ip_address and not isinstance(private_endpoint_ip_address, str):
            raise TypeError("Expected argument 'private_endpoint_ip_address' to be a str")
        pulumi.set(__self__, "private_endpoint_ip_address", private_endpoint_ip_address)
        if private_link_service_resource_id and not isinstance(private_link_service_resource_id, str):
            raise TypeError("Expected argument 'private_link_service_resource_id' to be a str")
        pulumi.set(__self__, "private_link_service_resource_id", private_link_service_resource_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="cloudProviderEndpointId")
    def cloud_provider_endpoint_id(self) -> str:
        return pulumi.get(self, "cloud_provider_endpoint_id")

    @property
    @pulumi.getter
    def comment(self) -> str:
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> str:
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> str:
        """
        Unique string that identifies the PrivateLink endpoint service. MongoDB Cloud returns null while it creates the endpoint service.
        """
        return pulumi.get(self, "endpoint_service_name")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> str:
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="privateEndpointIpAddress")
    def private_endpoint_ip_address(self) -> str:
        """
        IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service.
        """
        return pulumi.get(self, "private_endpoint_ip_address")

    @property
    @pulumi.getter(name="privateLinkServiceResourceId")
    def private_link_service_resource_id(self) -> str:
        """
        Root-relative path that identifies the Azure Private Link Service that MongoDB Cloud manages.
        """
        return pulumi.get(self, "private_link_service_resource_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Human-readable label that indicates the current operating status of the private endpoint. Values include: RESERVATION_REQUESTED, RESERVED, INITIATING, AVAILABLE, FAILED, DELETING.
        """
        return pulumi.get(self, "status")


class AwaitableGetPrivatelinkEndpointServiceServerlessResult(GetPrivatelinkEndpointServiceServerlessResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivatelinkEndpointServiceServerlessResult(
            cloud_provider_endpoint_id=self.cloud_provider_endpoint_id,
            comment=self.comment,
            endpoint_id=self.endpoint_id,
            endpoint_service_name=self.endpoint_service_name,
            error_message=self.error_message,
            id=self.id,
            instance_name=self.instance_name,
            private_endpoint_ip_address=self.private_endpoint_ip_address,
            private_link_service_resource_id=self.private_link_service_resource_id,
            project_id=self.project_id,
            status=self.status)


def get_privatelink_endpoint_service_serverless(endpoint_id: Optional[str] = None,
                                                instance_name: Optional[str] = None,
                                                project_id: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivatelinkEndpointServiceServerlessResult:
    """
    Use this data source to access information about an existing resource.

    :param str endpoint_id: Unique 22-character alphanumeric string that identifies the private endpoint. Atlas supports AWS private endpoints using the [AWS PrivateLink](https://aws.amazon.com/privatelink/) feature.
    :param str instance_name: Human-readable label that identifies the serverless instance
    :param str project_id: Unique 24-digit hexadecimal string that identifies the project.
    """
    __args__ = dict()
    __args__['endpointId'] = endpoint_id
    __args__['instanceName'] = instance_name
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getPrivatelinkEndpointServiceServerless:getPrivatelinkEndpointServiceServerless', __args__, opts=opts, typ=GetPrivatelinkEndpointServiceServerlessResult).value

    return AwaitableGetPrivatelinkEndpointServiceServerlessResult(
        cloud_provider_endpoint_id=__ret__.cloud_provider_endpoint_id,
        comment=__ret__.comment,
        endpoint_id=__ret__.endpoint_id,
        endpoint_service_name=__ret__.endpoint_service_name,
        error_message=__ret__.error_message,
        id=__ret__.id,
        instance_name=__ret__.instance_name,
        private_endpoint_ip_address=__ret__.private_endpoint_ip_address,
        private_link_service_resource_id=__ret__.private_link_service_resource_id,
        project_id=__ret__.project_id,
        status=__ret__.status)


@_utilities.lift_output_func(get_privatelink_endpoint_service_serverless)
def get_privatelink_endpoint_service_serverless_output(endpoint_id: Optional[pulumi.Input[str]] = None,
                                                       instance_name: Optional[pulumi.Input[str]] = None,
                                                       project_id: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivatelinkEndpointServiceServerlessResult]:
    """
    Use this data source to access information about an existing resource.

    :param str endpoint_id: Unique 22-character alphanumeric string that identifies the private endpoint. Atlas supports AWS private endpoints using the [AWS PrivateLink](https://aws.amazon.com/privatelink/) feature.
    :param str instance_name: Human-readable label that identifies the serverless instance
    :param str project_id: Unique 24-digit hexadecimal string that identifies the project.
    """
    ...
