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
    'GetObjectStoreResult',
    'AwaitableGetObjectStoreResult',
    'get_object_store',
    'get_object_store_output',
]

@pulumi.output_type
class GetObjectStoreResult:
    """
    A collection of values returned by getObjectStore.
    """
    def __init__(__self__, access_key_id=None, bucket_url=None, id=None, max_size_gb=None, name=None, region=None, status=None):
        if access_key_id and not isinstance(access_key_id, str):
            raise TypeError("Expected argument 'access_key_id' to be a str")
        pulumi.set(__self__, "access_key_id", access_key_id)
        if bucket_url and not isinstance(bucket_url, str):
            raise TypeError("Expected argument 'bucket_url' to be a str")
        pulumi.set(__self__, "bucket_url", bucket_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_size_gb and not isinstance(max_size_gb, int):
            raise TypeError("Expected argument 'max_size_gb' to be a int")
        pulumi.set(__self__, "max_size_gb", max_size_gb)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> str:
        """
        The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        """
        return pulumi.get(self, "access_key_id")

    @property
    @pulumi.getter(name="bucketUrl")
    def bucket_url(self) -> str:
        """
        The endpoint of the Object Store
        """
        return pulumi.get(self, "bucket_url")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the Object Store
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxSizeGb")
    def max_size_gb(self) -> int:
        """
        The maximum size of the Object Store
        """
        return pulumi.get(self, "max_size_gb")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the Object Store
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region of an existing Object Store
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the Object Store
        """
        return pulumi.get(self, "status")


class AwaitableGetObjectStoreResult(GetObjectStoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectStoreResult(
            access_key_id=self.access_key_id,
            bucket_url=self.bucket_url,
            id=self.id,
            max_size_gb=self.max_size_gb,
            name=self.name,
            region=self.region,
            status=self.status)


def get_object_store(id: Optional[str] = None,
                     name: Optional[str] = None,
                     region: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectStoreResult:
    """
    Get information of an Object Store for use in other resources. This data source provides all of the Object Store's properties as configured on your Civo account.

    Note: This data source returns a single Object Store. When specifying a name, an error will be raised if more than one Object Stores with the same name found.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    backup = civo.get_object_store(name="backup-server")
    ```


    :param str id: The ID of the Object Store
    :param str name: The name of the Object Store
    :param str region: The region of an existing Object Store
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getObjectStore:getObjectStore', __args__, opts=opts, typ=GetObjectStoreResult).value

    return AwaitableGetObjectStoreResult(
        access_key_id=__ret__.access_key_id,
        bucket_url=__ret__.bucket_url,
        id=__ret__.id,
        max_size_gb=__ret__.max_size_gb,
        name=__ret__.name,
        region=__ret__.region,
        status=__ret__.status)


@_utilities.lift_output_func(get_object_store)
def get_object_store_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                            name: Optional[pulumi.Input[Optional[str]]] = None,
                            region: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectStoreResult]:
    """
    Get information of an Object Store for use in other resources. This data source provides all of the Object Store's properties as configured on your Civo account.

    Note: This data source returns a single Object Store. When specifying a name, an error will be raised if more than one Object Stores with the same name found.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    backup = civo.get_object_store(name="backup-server")
    ```


    :param str id: The ID of the Object Store
    :param str name: The name of the Object Store
    :param str region: The region of an existing Object Store
    """
    ...
