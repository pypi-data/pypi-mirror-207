# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AuditRequestHeaderArgs', 'AuditRequestHeader']

@pulumi.input_type
class AuditRequestHeaderArgs:
    def __init__(__self__, *,
                 hmac: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AuditRequestHeader resource.
        :param pulumi.Input[bool] hmac: Whether this header's value should be HMAC'd in the audit logs.
        :param pulumi.Input[str] name: The name of the request header to audit.
        :param pulumi.Input[str] namespace: Target namespace. (requires Enterprise)
        """
        if hmac is not None:
            pulumi.set(__self__, "hmac", hmac)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def hmac(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this header's value should be HMAC'd in the audit logs.
        """
        return pulumi.get(self, "hmac")

    @hmac.setter
    def hmac(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hmac", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the request header to audit.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Target namespace. (requires Enterprise)
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class _AuditRequestHeaderState:
    def __init__(__self__, *,
                 hmac: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AuditRequestHeader resources.
        :param pulumi.Input[bool] hmac: Whether this header's value should be HMAC'd in the audit logs.
        :param pulumi.Input[str] name: The name of the request header to audit.
        :param pulumi.Input[str] namespace: Target namespace. (requires Enterprise)
        """
        if hmac is not None:
            pulumi.set(__self__, "hmac", hmac)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def hmac(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this header's value should be HMAC'd in the audit logs.
        """
        return pulumi.get(self, "hmac")

    @hmac.setter
    def hmac(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hmac", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the request header to audit.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Target namespace. (requires Enterprise)
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


class AuditRequestHeader(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hmac: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages additional request headers that appear in audited requests.

        > **Note**
        Because of the way the [sys/config/auditing/request-headers API](https://www.vaultproject.io/api-docs/system/config-auditing)
        is implemented in Vault, this resource will manage existing audited headers with
        matching names without requiring import.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        x_forwarded_for = vault.AuditRequestHeader("xForwardedFor", hmac=False)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] hmac: Whether this header's value should be HMAC'd in the audit logs.
        :param pulumi.Input[str] name: The name of the request header to audit.
        :param pulumi.Input[str] namespace: Target namespace. (requires Enterprise)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AuditRequestHeaderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages additional request headers that appear in audited requests.

        > **Note**
        Because of the way the [sys/config/auditing/request-headers API](https://www.vaultproject.io/api-docs/system/config-auditing)
        is implemented in Vault, this resource will manage existing audited headers with
        matching names without requiring import.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        x_forwarded_for = vault.AuditRequestHeader("xForwardedFor", hmac=False)
        ```

        :param str resource_name: The name of the resource.
        :param AuditRequestHeaderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuditRequestHeaderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hmac: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuditRequestHeaderArgs.__new__(AuditRequestHeaderArgs)

            __props__.__dict__["hmac"] = hmac
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
        super(AuditRequestHeader, __self__).__init__(
            'vault:index/auditRequestHeader:AuditRequestHeader',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            hmac: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None) -> 'AuditRequestHeader':
        """
        Get an existing AuditRequestHeader resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] hmac: Whether this header's value should be HMAC'd in the audit logs.
        :param pulumi.Input[str] name: The name of the request header to audit.
        :param pulumi.Input[str] namespace: Target namespace. (requires Enterprise)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuditRequestHeaderState.__new__(_AuditRequestHeaderState)

        __props__.__dict__["hmac"] = hmac
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        return AuditRequestHeader(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def hmac(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this header's value should be HMAC'd in the audit logs.
        """
        return pulumi.get(self, "hmac")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the request header to audit.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        Target namespace. (requires Enterprise)
        """
        return pulumi.get(self, "namespace")

