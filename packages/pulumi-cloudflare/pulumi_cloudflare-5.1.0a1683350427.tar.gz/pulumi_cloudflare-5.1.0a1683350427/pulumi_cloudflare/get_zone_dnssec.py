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
    'GetZoneDnssecResult',
    'AwaitableGetZoneDnssecResult',
    'get_zone_dnssec',
    'get_zone_dnssec_output',
]

@pulumi.output_type
class GetZoneDnssecResult:
    """
    A collection of values returned by getZoneDnssec.
    """
    def __init__(__self__, algorithm=None, digest=None, digest_algorithm=None, digest_type=None, ds=None, flags=None, id=None, key_tag=None, key_type=None, public_key=None, status=None, zone_id=None):
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if digest and not isinstance(digest, str):
            raise TypeError("Expected argument 'digest' to be a str")
        pulumi.set(__self__, "digest", digest)
        if digest_algorithm and not isinstance(digest_algorithm, str):
            raise TypeError("Expected argument 'digest_algorithm' to be a str")
        pulumi.set(__self__, "digest_algorithm", digest_algorithm)
        if digest_type and not isinstance(digest_type, str):
            raise TypeError("Expected argument 'digest_type' to be a str")
        pulumi.set(__self__, "digest_type", digest_type)
        if ds and not isinstance(ds, str):
            raise TypeError("Expected argument 'ds' to be a str")
        pulumi.set(__self__, "ds", ds)
        if flags and not isinstance(flags, int):
            raise TypeError("Expected argument 'flags' to be a int")
        pulumi.set(__self__, "flags", flags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_tag and not isinstance(key_tag, int):
            raise TypeError("Expected argument 'key_tag' to be a int")
        pulumi.set(__self__, "key_tag", key_tag)
        if key_type and not isinstance(key_type, str):
            raise TypeError("Expected argument 'key_type' to be a str")
        pulumi.set(__self__, "key_type", key_type)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        """
        Zone DNSSEC algorithm.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter
    def digest(self) -> str:
        """
        Zone DNSSEC digest.
        """
        return pulumi.get(self, "digest")

    @property
    @pulumi.getter(name="digestAlgorithm")
    def digest_algorithm(self) -> str:
        """
        Digest algorithm use for Zone DNSSEC.
        """
        return pulumi.get(self, "digest_algorithm")

    @property
    @pulumi.getter(name="digestType")
    def digest_type(self) -> str:
        """
        Digest Type for Zone DNSSEC.
        """
        return pulumi.get(self, "digest_type")

    @property
    @pulumi.getter
    def ds(self) -> str:
        """
        DS for the Zone DNSSEC.
        """
        return pulumi.get(self, "ds")

    @property
    @pulumi.getter
    def flags(self) -> int:
        """
        Zone DNSSEC flags.
        """
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> int:
        """
        Key Tag for the Zone DNSSEC.
        """
        return pulumi.get(self, "key_tag")

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> str:
        """
        Key type used for Zone DNSSEC.
        """
        return pulumi.get(self, "key_type")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        Public Key for the Zone DNSSEC.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the Zone DNSSEC.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The zone identifier to target for the resource.
        """
        return pulumi.get(self, "zone_id")


class AwaitableGetZoneDnssecResult(GetZoneDnssecResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneDnssecResult(
            algorithm=self.algorithm,
            digest=self.digest,
            digest_algorithm=self.digest_algorithm,
            digest_type=self.digest_type,
            ds=self.ds,
            flags=self.flags,
            id=self.id,
            key_tag=self.key_tag,
            key_type=self.key_type,
            public_key=self.public_key,
            status=self.status,
            zone_id=self.zone_id)


def get_zone_dnssec(zone_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneDnssecResult:
    """
    Use this data source to look up Zone DNSSEC settings.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudflare as cloudflare

    example = cloudflare.get_zone_dnssec(zone_id="0da42c8d2132a9ddaf714f9e7c920711")
    ```


    :param str zone_id: The zone identifier to target for the resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getZoneDnssec:getZoneDnssec', __args__, opts=opts, typ=GetZoneDnssecResult).value

    return AwaitableGetZoneDnssecResult(
        algorithm=__ret__.algorithm,
        digest=__ret__.digest,
        digest_algorithm=__ret__.digest_algorithm,
        digest_type=__ret__.digest_type,
        ds=__ret__.ds,
        flags=__ret__.flags,
        id=__ret__.id,
        key_tag=__ret__.key_tag,
        key_type=__ret__.key_type,
        public_key=__ret__.public_key,
        status=__ret__.status,
        zone_id=__ret__.zone_id)


@_utilities.lift_output_func(get_zone_dnssec)
def get_zone_dnssec_output(zone_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZoneDnssecResult]:
    """
    Use this data source to look up Zone DNSSEC settings.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudflare as cloudflare

    example = cloudflare.get_zone_dnssec(zone_id="0da42c8d2132a9ddaf714f9e7c920711")
    ```


    :param str zone_id: The zone identifier to target for the resource.
    """
    ...
