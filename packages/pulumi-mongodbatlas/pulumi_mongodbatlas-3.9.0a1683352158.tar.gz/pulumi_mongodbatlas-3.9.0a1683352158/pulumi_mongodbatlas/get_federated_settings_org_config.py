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
    'GetFederatedSettingsOrgConfigResult',
    'AwaitableGetFederatedSettingsOrgConfigResult',
    'get_federated_settings_org_config',
    'get_federated_settings_org_config_output',
]

@pulumi.output_type
class GetFederatedSettingsOrgConfigResult:
    """
    A collection of values returned by getFederatedSettingsOrgConfig.
    """
    def __init__(__self__, domain_allow_lists=None, domain_restriction_enabled=None, federation_settings_id=None, id=None, identity_provider_id=None, org_id=None, post_auth_role_grants=None, role_mappings=None, user_conflicts=None):
        if domain_allow_lists and not isinstance(domain_allow_lists, list):
            raise TypeError("Expected argument 'domain_allow_lists' to be a list")
        pulumi.set(__self__, "domain_allow_lists", domain_allow_lists)
        if domain_restriction_enabled and not isinstance(domain_restriction_enabled, bool):
            raise TypeError("Expected argument 'domain_restriction_enabled' to be a bool")
        pulumi.set(__self__, "domain_restriction_enabled", domain_restriction_enabled)
        if federation_settings_id and not isinstance(federation_settings_id, str):
            raise TypeError("Expected argument 'federation_settings_id' to be a str")
        pulumi.set(__self__, "federation_settings_id", federation_settings_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_provider_id and not isinstance(identity_provider_id, str):
            raise TypeError("Expected argument 'identity_provider_id' to be a str")
        pulumi.set(__self__, "identity_provider_id", identity_provider_id)
        if org_id and not isinstance(org_id, str):
            raise TypeError("Expected argument 'org_id' to be a str")
        pulumi.set(__self__, "org_id", org_id)
        if post_auth_role_grants and not isinstance(post_auth_role_grants, list):
            raise TypeError("Expected argument 'post_auth_role_grants' to be a list")
        pulumi.set(__self__, "post_auth_role_grants", post_auth_role_grants)
        if role_mappings and not isinstance(role_mappings, list):
            raise TypeError("Expected argument 'role_mappings' to be a list")
        pulumi.set(__self__, "role_mappings", role_mappings)
        if user_conflicts and not isinstance(user_conflicts, list):
            raise TypeError("Expected argument 'user_conflicts' to be a list")
        pulumi.set(__self__, "user_conflicts", user_conflicts)

    @property
    @pulumi.getter(name="domainAllowLists")
    def domain_allow_lists(self) -> Sequence[str]:
        """
        List that contains the approved domains from which organization users can log in.  Note: If the organization uses an identity provider,  `domain_allow_list` includes: any SSO domains associated with organization's identity provider and any custom domains associated with the specific organization.
        """
        return pulumi.get(self, "domain_allow_lists")

    @property
    @pulumi.getter(name="domainRestrictionEnabled")
    def domain_restriction_enabled(self) -> bool:
        """
        Flag that indicates whether domain restriction is enabled for the connected organization.  User Conflicts returns null when `domain_restriction_enabled` is false.
        """
        return pulumi.get(self, "domain_restriction_enabled")

    @property
    @pulumi.getter(name="federationSettingsId")
    def federation_settings_id(self) -> str:
        """
        Unique 24-hexadecimal digit string that identifies the federated authentication configuration.
        """
        return pulumi.get(self, "federation_settings_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityProviderId")
    def identity_provider_id(self) -> str:
        """
        Unique 24-hexadecimal digit string that identifies the federated authentication configuration.
        """
        return pulumi.get(self, "identity_provider_id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="postAuthRoleGrants")
    def post_auth_role_grants(self) -> Sequence[str]:
        """
        List that contains the default [roles](https://www.mongodb.com/docs/atlas/reference/user-roles/#std-label-organization-roles) granted to users who authenticate through the IdP in a connected organization.
        """
        return pulumi.get(self, "post_auth_role_grants")

    @property
    @pulumi.getter(name="roleMappings")
    def role_mappings(self) -> Sequence['outputs.GetFederatedSettingsOrgConfigRoleMappingResult']:
        return pulumi.get(self, "role_mappings")

    @property
    @pulumi.getter(name="userConflicts")
    def user_conflicts(self) -> Sequence['outputs.GetFederatedSettingsOrgConfigUserConflictResult']:
        return pulumi.get(self, "user_conflicts")


class AwaitableGetFederatedSettingsOrgConfigResult(GetFederatedSettingsOrgConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFederatedSettingsOrgConfigResult(
            domain_allow_lists=self.domain_allow_lists,
            domain_restriction_enabled=self.domain_restriction_enabled,
            federation_settings_id=self.federation_settings_id,
            id=self.id,
            identity_provider_id=self.identity_provider_id,
            org_id=self.org_id,
            post_auth_role_grants=self.post_auth_role_grants,
            role_mappings=self.role_mappings,
            user_conflicts=self.user_conflicts)


def get_federated_settings_org_config(federation_settings_id: Optional[str] = None,
                                      org_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFederatedSettingsOrgConfigResult:
    """
    `FederatedSettingsOrgConfig` provides an Federated Settings Identity Providers datasource. Atlas Cloud Federated Settings Organizational configuration provides federated settings outputs for the configured Organizational configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    org_connections = mongodbatlas.FederatedSettingsOrgConfig("orgConnections",
        federation_settings_id="627a9687f7f7f7f774de306f14",
        org_id="627a9683ea7ff7f74de306f14",
        domain_restriction_enabled=False,
        domain_allow_lists=["mydomain.com"],
        post_auth_role_grants=["ORG_MEMBER"])
    org_configs_ds = mongodbatlas.get_federated_settings_org_config_output(federation_settings_id=org_connections.id,
        org_id="627a9683ea7ff7f74de306f14")
    ```


    :param str federation_settings_id: Unique 24-hexadecimal digit string that identifies the federated authentication configuration.
    :param str org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
    """
    __args__ = dict()
    __args__['federationSettingsId'] = federation_settings_id
    __args__['orgId'] = org_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getFederatedSettingsOrgConfig:getFederatedSettingsOrgConfig', __args__, opts=opts, typ=GetFederatedSettingsOrgConfigResult).value

    return AwaitableGetFederatedSettingsOrgConfigResult(
        domain_allow_lists=__ret__.domain_allow_lists,
        domain_restriction_enabled=__ret__.domain_restriction_enabled,
        federation_settings_id=__ret__.federation_settings_id,
        id=__ret__.id,
        identity_provider_id=__ret__.identity_provider_id,
        org_id=__ret__.org_id,
        post_auth_role_grants=__ret__.post_auth_role_grants,
        role_mappings=__ret__.role_mappings,
        user_conflicts=__ret__.user_conflicts)


@_utilities.lift_output_func(get_federated_settings_org_config)
def get_federated_settings_org_config_output(federation_settings_id: Optional[pulumi.Input[str]] = None,
                                             org_id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFederatedSettingsOrgConfigResult]:
    """
    `FederatedSettingsOrgConfig` provides an Federated Settings Identity Providers datasource. Atlas Cloud Federated Settings Organizational configuration provides federated settings outputs for the configured Organizational configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    org_connections = mongodbatlas.FederatedSettingsOrgConfig("orgConnections",
        federation_settings_id="627a9687f7f7f7f774de306f14",
        org_id="627a9683ea7ff7f74de306f14",
        domain_restriction_enabled=False,
        domain_allow_lists=["mydomain.com"],
        post_auth_role_grants=["ORG_MEMBER"])
    org_configs_ds = mongodbatlas.get_federated_settings_org_config_output(federation_settings_id=org_connections.id,
        org_id="627a9683ea7ff7f74de306f14")
    ```


    :param str federation_settings_id: Unique 24-hexadecimal digit string that identifies the federated authentication configuration.
    :param str org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
    """
    ...
