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
    'SecretBackendRoleAllowedUserKeyConfigArgs',
]

@pulumi.input_type
class SecretBackendRoleAllowedUserKeyConfigArgs:
    def __init__(__self__, *,
                 lengths: pulumi.Input[Sequence[pulumi.Input[int]]],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[int]]] lengths: A list of allowed key lengths as integers. 
               For key types that do not support setting the length a value of `[0]` should be used.
               Setting multiple lengths is only supported on Vault 1.10+. For prior releases `length`
               must be set to a single element list.
        :param pulumi.Input[str] type: The SSH public key type.  
               *Supported key types are:*
               `rsa`, `ecdsa`, `ec`, `dsa`, `ed25519`, `ssh-rsa`, `ssh-dss`, `ssh-ed25519`,
               `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, `ecdsa-sha2-nistp521`
        """
        pulumi.set(__self__, "lengths", lengths)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def lengths(self) -> pulumi.Input[Sequence[pulumi.Input[int]]]:
        """
        A list of allowed key lengths as integers. 
        For key types that do not support setting the length a value of `[0]` should be used.
        Setting multiple lengths is only supported on Vault 1.10+. For prior releases `length`
        must be set to a single element list.
        """
        return pulumi.get(self, "lengths")

    @lengths.setter
    def lengths(self, value: pulumi.Input[Sequence[pulumi.Input[int]]]):
        pulumi.set(self, "lengths", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The SSH public key type.  
        *Supported key types are:*
        `rsa`, `ecdsa`, `ec`, `dsa`, `ed25519`, `ssh-rsa`, `ssh-dss`, `ssh-ed25519`,
        `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, `ecdsa-sha2-nistp521`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


