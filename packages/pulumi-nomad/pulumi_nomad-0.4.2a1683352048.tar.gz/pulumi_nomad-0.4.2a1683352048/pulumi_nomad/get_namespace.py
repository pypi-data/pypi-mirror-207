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
    'GetNamespaceResult',
    'AwaitableGetNamespaceResult',
    'get_namespace',
    'get_namespace_output',
]

@pulumi.output_type
class GetNamespaceResult:
    """
    A collection of values returned by getNamespace.
    """
    def __init__(__self__, capabilities=None, description=None, id=None, meta=None, name=None, quota=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if meta and not isinstance(meta, dict):
            raise TypeError("Expected argument 'meta' to be a dict")
        pulumi.set(__self__, "meta", meta)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if quota and not isinstance(quota, str):
            raise TypeError("Expected argument 'quota' to be a str")
        pulumi.set(__self__, "quota", quota)

    @property
    @pulumi.getter
    def capabilities(self) -> Sequence['outputs.GetNamespaceCapabilityResult']:
        """
        `(block)` - Capabilities of the namespace
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        `(string)` - The description of the namespace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def meta(self) -> Mapping[str, str]:
        """
        `(map[string]string)` -  Arbitrary KV metadata associated with the namespace.
        """
        return pulumi.get(self, "meta")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def quota(self) -> str:
        """
        `(string)` - The quota associated with the namespace.
        """
        return pulumi.get(self, "quota")


class AwaitableGetNamespaceResult(GetNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceResult(
            capabilities=self.capabilities,
            description=self.description,
            id=self.id,
            meta=self.meta,
            name=self.name,
            quota=self.quota)


def get_namespace(name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceResult:
    """
    Get information about a namespace in Nomad.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_nomad as nomad

    namespaces = nomad.get_namespace(name="default")
    ```


    :param str name: `(string)` - The name of the namespace.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('nomad:index/getNamespace:getNamespace', __args__, opts=opts, typ=GetNamespaceResult).value

    return AwaitableGetNamespaceResult(
        capabilities=__ret__.capabilities,
        description=__ret__.description,
        id=__ret__.id,
        meta=__ret__.meta,
        name=__ret__.name,
        quota=__ret__.quota)


@_utilities.lift_output_func(get_namespace)
def get_namespace_output(name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceResult]:
    """
    Get information about a namespace in Nomad.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_nomad as nomad

    namespaces = nomad.get_namespace(name="default")
    ```


    :param str name: `(string)` - The name of the namespace.
    """
    ...
