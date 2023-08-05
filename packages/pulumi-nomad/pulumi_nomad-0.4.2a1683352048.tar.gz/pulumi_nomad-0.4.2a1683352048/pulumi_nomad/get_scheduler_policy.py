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
    'GetSchedulerPolicyResult',
    'AwaitableGetSchedulerPolicyResult',
    'get_scheduler_policy',
]

@pulumi.output_type
class GetSchedulerPolicyResult:
    """
    A collection of values returned by getSchedulerPolicy.
    """
    def __init__(__self__, id=None, memory_oversubscription_enabled=None, preemption_config=None, scheduler_algorithm=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if memory_oversubscription_enabled and not isinstance(memory_oversubscription_enabled, bool):
            raise TypeError("Expected argument 'memory_oversubscription_enabled' to be a bool")
        pulumi.set(__self__, "memory_oversubscription_enabled", memory_oversubscription_enabled)
        if preemption_config and not isinstance(preemption_config, dict):
            raise TypeError("Expected argument 'preemption_config' to be a dict")
        pulumi.set(__self__, "preemption_config", preemption_config)
        if scheduler_algorithm and not isinstance(scheduler_algorithm, str):
            raise TypeError("Expected argument 'scheduler_algorithm' to be a str")
        pulumi.set(__self__, "scheduler_algorithm", scheduler_algorithm)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memoryOversubscriptionEnabled")
    def memory_oversubscription_enabled(self) -> bool:
        """
        `(bool: false)` - When `true`, tasks may exceed their reserved memory limit.
        """
        return pulumi.get(self, "memory_oversubscription_enabled")

    @property
    @pulumi.getter(name="preemptionConfig")
    def preemption_config(self) -> Mapping[str, bool]:
        """
        `(map[string]bool)` - Options to enable preemption for various schedulers.
        """
        return pulumi.get(self, "preemption_config")

    @property
    @pulumi.getter(name="schedulerAlgorithm")
    def scheduler_algorithm(self) -> str:
        """
        `(string)` - Specifies whether scheduler binpacks or spreads allocations on available nodes.
        """
        return pulumi.get(self, "scheduler_algorithm")


class AwaitableGetSchedulerPolicyResult(GetSchedulerPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchedulerPolicyResult(
            id=self.id,
            memory_oversubscription_enabled=self.memory_oversubscription_enabled,
            preemption_config=self.preemption_config,
            scheduler_algorithm=self.scheduler_algorithm)


def get_scheduler_policy(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchedulerPolicyResult:
    """
    Retrieve the cluster's [scheduler configuration](https://www.nomadproject.io/api-docs/operator#sample-response-3).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_nomad as nomad

    global_ = nomad.get_scheduler_policy()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('nomad:index/getSchedulerPolicy:getSchedulerPolicy', __args__, opts=opts, typ=GetSchedulerPolicyResult).value

    return AwaitableGetSchedulerPolicyResult(
        id=__ret__.id,
        memory_oversubscription_enabled=__ret__.memory_oversubscription_enabled,
        preemption_config=__ret__.preemption_config,
        scheduler_algorithm=__ret__.scheduler_algorithm)
