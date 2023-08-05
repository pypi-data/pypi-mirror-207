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
    'GetPlacementGroupResult',
    'AwaitableGetPlacementGroupResult',
    'get_placement_group',
    'get_placement_group_output',
]

@pulumi.output_type
class GetPlacementGroupResult:
    """
    A collection of values returned by getPlacementGroup.
    """
    def __init__(__self__, id=None, labels=None, most_recent=None, name=None, servers=None, type=None, with_selector=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if servers and not isinstance(servers, list):
            raise TypeError("Expected argument 'servers' to be a list")
        pulumi.set(__self__, "servers", servers)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        """
        (int) Unique ID of the Placement Group.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, Any]]:
        """
        (map) User-defined labels (key-value pairs)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        (string) Name of the Placement Group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def servers(self) -> Sequence[int]:
        return pulumi.get(self, "servers")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        (string)  Type of the Placement Group.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")


class AwaitableGetPlacementGroupResult(GetPlacementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlacementGroupResult(
            id=self.id,
            labels=self.labels,
            most_recent=self.most_recent,
            name=self.name,
            servers=self.servers,
            type=self.type,
            with_selector=self.with_selector)


def get_placement_group(id: Optional[int] = None,
                        labels: Optional[Mapping[str, Any]] = None,
                        most_recent: Optional[bool] = None,
                        name: Optional[str] = None,
                        type: Optional[str] = None,
                        with_selector: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlacementGroupResult:
    """
    Provides details about a specific Hetzner Cloud Placement Group.

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    sample_placement_group1 = hcloud.get_placement_group(name="sample-placement-group-1")
    sample_placement_group2 = hcloud.get_placement_group(id=4711)
    ```


    :param int id: ID of the placement group.
    :param Mapping[str, Any] labels: (map) User-defined labels (key-value pairs)
    :param bool most_recent: Return most recent placement group if multiple are found.
    :param str name: Name of the placement group.
    :param str type: (string)  Type of the Placement Group.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['labels'] = labels
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['type'] = type
    __args__['withSelector'] = with_selector
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcloud:index/getPlacementGroup:getPlacementGroup', __args__, opts=opts, typ=GetPlacementGroupResult).value

    return AwaitableGetPlacementGroupResult(
        id=__ret__.id,
        labels=__ret__.labels,
        most_recent=__ret__.most_recent,
        name=__ret__.name,
        servers=__ret__.servers,
        type=__ret__.type,
        with_selector=__ret__.with_selector)


@_utilities.lift_output_func(get_placement_group)
def get_placement_group_output(id: Optional[pulumi.Input[Optional[int]]] = None,
                               labels: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                               most_recent: Optional[pulumi.Input[Optional[bool]]] = None,
                               name: Optional[pulumi.Input[Optional[str]]] = None,
                               type: Optional[pulumi.Input[Optional[str]]] = None,
                               with_selector: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlacementGroupResult]:
    """
    Provides details about a specific Hetzner Cloud Placement Group.

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    sample_placement_group1 = hcloud.get_placement_group(name="sample-placement-group-1")
    sample_placement_group2 = hcloud.get_placement_group(id=4711)
    ```


    :param int id: ID of the placement group.
    :param Mapping[str, Any] labels: (map) User-defined labels (key-value pairs)
    :param bool most_recent: Return most recent placement group if multiple are found.
    :param str name: Name of the placement group.
    :param str type: (string)  Type of the Placement Group.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    ...
