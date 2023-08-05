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
    'GetVmfsDisksResult',
    'AwaitableGetVmfsDisksResult',
    'get_vmfs_disks',
    'get_vmfs_disks_output',
]

@pulumi.output_type
class GetVmfsDisksResult:
    """
    A collection of values returned by getVmfsDisks.
    """
    def __init__(__self__, disks=None, filter=None, host_system_id=None, id=None, rescan=None):
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        pulumi.set(__self__, "disks", disks)
        if filter and not isinstance(filter, str):
            raise TypeError("Expected argument 'filter' to be a str")
        pulumi.set(__self__, "filter", filter)
        if host_system_id and not isinstance(host_system_id, str):
            raise TypeError("Expected argument 'host_system_id' to be a str")
        pulumi.set(__self__, "host_system_id", host_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rescan and not isinstance(rescan, bool):
            raise TypeError("Expected argument 'rescan' to be a bool")
        pulumi.set(__self__, "rescan", rescan)

    @property
    @pulumi.getter
    def disks(self) -> Sequence[str]:
        """
        A lexicographically sorted list of devices discovered by the
        operation, matching the supplied `filter`, if provided.
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def filter(self) -> Optional[str]:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="hostSystemId")
    def host_system_id(self) -> str:
        return pulumi.get(self, "host_system_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rescan(self) -> Optional[bool]:
        return pulumi.get(self, "rescan")


class AwaitableGetVmfsDisksResult(GetVmfsDisksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVmfsDisksResult(
            disks=self.disks,
            filter=self.filter,
            host_system_id=self.host_system_id,
            id=self.id,
            rescan=self.rescan)


def get_vmfs_disks(filter: Optional[str] = None,
                   host_system_id: Optional[str] = None,
                   rescan: Optional[bool] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVmfsDisksResult:
    """
    The _get_vmfs_disks_ data source can be used to discover the storage
    devices available on an ESXi host. This data source can be combined with the
    `VmfsDatastore` resource to create VMFS
    datastores based off a set of discovered disks.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    datacenter = vsphere.get_datacenter(name="dc-01")
    host = vsphere.get_host(name="esxi-01.example.com",
        datacenter_id=datacenter.id)
    vmfs_disks = vsphere.get_vmfs_disks(host_system_id=host.id,
        rescan=True,
        filter="mpx.vmhba1:C0:T[12]:L0")
    ```


    :param str filter: A regular expression to filter the disks against. Only
           disks with canonical names that match will be included.
    :param str host_system_id: The managed object ID of
           the host to look for disks on.
    :param bool rescan: Whether or not to rescan storage adapters before
           searching for disks. This may lengthen the time it takes to perform the
           search. Default: `false`.
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['hostSystemId'] = host_system_id
    __args__['rescan'] = rescan
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('vsphere:index/getVmfsDisks:getVmfsDisks', __args__, opts=opts, typ=GetVmfsDisksResult).value

    return AwaitableGetVmfsDisksResult(
        disks=__ret__.disks,
        filter=__ret__.filter,
        host_system_id=__ret__.host_system_id,
        id=__ret__.id,
        rescan=__ret__.rescan)


@_utilities.lift_output_func(get_vmfs_disks)
def get_vmfs_disks_output(filter: Optional[pulumi.Input[Optional[str]]] = None,
                          host_system_id: Optional[pulumi.Input[str]] = None,
                          rescan: Optional[pulumi.Input[Optional[bool]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVmfsDisksResult]:
    """
    The _get_vmfs_disks_ data source can be used to discover the storage
    devices available on an ESXi host. This data source can be combined with the
    `VmfsDatastore` resource to create VMFS
    datastores based off a set of discovered disks.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    datacenter = vsphere.get_datacenter(name="dc-01")
    host = vsphere.get_host(name="esxi-01.example.com",
        datacenter_id=datacenter.id)
    vmfs_disks = vsphere.get_vmfs_disks(host_system_id=host.id,
        rescan=True,
        filter="mpx.vmhba1:C0:T[12]:L0")
    ```


    :param str filter: A regular expression to filter the disks against. Only
           disks with canonical names that match will be included.
    :param str host_system_id: The managed object ID of
           the host to look for disks on.
    :param bool rescan: Whether or not to rescan storage adapters before
           searching for disks. This may lengthen the time it takes to perform the
           search. Default: `false`.
    """
    ...
