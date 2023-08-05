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
    'AuthBackendCustomEndpoint',
    'SecretRolesetBinding',
    'SecretStaticAccountBinding',
]

@pulumi.output_type
class AuthBackendCustomEndpoint(dict):
    def __init__(__self__, *,
                 api: Optional[str] = None,
                 compute: Optional[str] = None,
                 crm: Optional[str] = None,
                 iam: Optional[str] = None):
        """
        :param str api: Replaces the service endpoint used in API requests to `https://www.googleapis.com`.
        :param str compute: Replaces the service endpoint used in API requests to `https://compute.googleapis.com`.
        :param str crm: Replaces the service endpoint used in API requests to `https://cloudresourcemanager.googleapis.com`.
        :param str iam: Replaces the service endpoint used in API requests to `https://iam.googleapis.com`.
        """
        if api is not None:
            pulumi.set(__self__, "api", api)
        if compute is not None:
            pulumi.set(__self__, "compute", compute)
        if crm is not None:
            pulumi.set(__self__, "crm", crm)
        if iam is not None:
            pulumi.set(__self__, "iam", iam)

    @property
    @pulumi.getter
    def api(self) -> Optional[str]:
        """
        Replaces the service endpoint used in API requests to `https://www.googleapis.com`.
        """
        return pulumi.get(self, "api")

    @property
    @pulumi.getter
    def compute(self) -> Optional[str]:
        """
        Replaces the service endpoint used in API requests to `https://compute.googleapis.com`.
        """
        return pulumi.get(self, "compute")

    @property
    @pulumi.getter
    def crm(self) -> Optional[str]:
        """
        Replaces the service endpoint used in API requests to `https://cloudresourcemanager.googleapis.com`.
        """
        return pulumi.get(self, "crm")

    @property
    @pulumi.getter
    def iam(self) -> Optional[str]:
        """
        Replaces the service endpoint used in API requests to `https://iam.googleapis.com`.
        """
        return pulumi.get(self, "iam")


@pulumi.output_type
class SecretRolesetBinding(dict):
    def __init__(__self__, *,
                 resource: str,
                 roles: Sequence[str]):
        """
        :param str resource: Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings).
        :param Sequence[str] roles: List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        pulumi.set(__self__, "resource", resource)
        pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings).
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def roles(self) -> Sequence[str]:
        """
        List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        return pulumi.get(self, "roles")


@pulumi.output_type
class SecretStaticAccountBinding(dict):
    def __init__(__self__, *,
                 resource: str,
                 roles: Sequence[str]):
        """
        :param str resource: Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#bindings).
        :param Sequence[str] roles: List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        pulumi.set(__self__, "resource", resource)
        pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#bindings).
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def roles(self) -> Sequence[str]:
        """
        List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        return pulumi.get(self, "roles")


