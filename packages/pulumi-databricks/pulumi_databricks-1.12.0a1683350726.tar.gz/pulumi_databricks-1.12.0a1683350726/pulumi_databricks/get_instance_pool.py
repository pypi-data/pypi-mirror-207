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
from ._inputs import *

__all__ = [
    'GetInstancePoolResult',
    'AwaitableGetInstancePoolResult',
    'get_instance_pool',
    'get_instance_pool_output',
]

@pulumi.output_type
class GetInstancePoolResult:
    """
    A collection of values returned by getInstancePool.
    """
    def __init__(__self__, id=None, name=None, pool_info=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pool_info and not isinstance(pool_info, dict):
            raise TypeError("Expected argument 'pool_info' to be a dict")
        pulumi.set(__self__, "pool_info", pool_info)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolInfo")
    def pool_info(self) -> 'outputs.GetInstancePoolPoolInfoResult':
        """
        block describing instance pool and its state. Check documentation for InstancePool for a list of exposed attributes.
        """
        return pulumi.get(self, "pool_info")


class AwaitableGetInstancePoolResult(GetInstancePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancePoolResult(
            id=self.id,
            name=self.name,
            pool_info=self.pool_info)


def get_instance_pool(name: Optional[str] = None,
                      pool_info: Optional[pulumi.InputType['GetInstancePoolPoolInfoArgs']] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancePoolResult:
    """
    ## Example Usage

    Referring to an instance pool by name:

    ```python
    import pulumi
    import pulumi_databricks as databricks

    pool = databricks.get_instance_pool(name="All spot")
    my_cluster = databricks.Cluster("myCluster", instance_pool_id=data["databricks_instance_pool"]["pool"]["id"])
    # ...
    ```


    :param str name: Name of the instance pool. The instance pool must exist before this resource can be planned.
    :param pulumi.InputType['GetInstancePoolPoolInfoArgs'] pool_info: block describing instance pool and its state. Check documentation for InstancePool for a list of exposed attributes.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['poolInfo'] = pool_info
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getInstancePool:getInstancePool', __args__, opts=opts, typ=GetInstancePoolResult).value

    return AwaitableGetInstancePoolResult(
        id=__ret__.id,
        name=__ret__.name,
        pool_info=__ret__.pool_info)


@_utilities.lift_output_func(get_instance_pool)
def get_instance_pool_output(name: Optional[pulumi.Input[str]] = None,
                             pool_info: Optional[pulumi.Input[Optional[pulumi.InputType['GetInstancePoolPoolInfoArgs']]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancePoolResult]:
    """
    ## Example Usage

    Referring to an instance pool by name:

    ```python
    import pulumi
    import pulumi_databricks as databricks

    pool = databricks.get_instance_pool(name="All spot")
    my_cluster = databricks.Cluster("myCluster", instance_pool_id=data["databricks_instance_pool"]["pool"]["id"])
    # ...
    ```


    :param str name: Name of the instance pool. The instance pool must exist before this resource can be planned.
    :param pulumi.InputType['GetInstancePoolPoolInfoArgs'] pool_info: block describing instance pool and its state. Check documentation for InstancePool for a list of exposed attributes.
    """
    ...
