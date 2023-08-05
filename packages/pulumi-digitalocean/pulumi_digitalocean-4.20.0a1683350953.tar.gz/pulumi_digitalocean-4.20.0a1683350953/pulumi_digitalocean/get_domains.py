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
    'GetDomainsResult',
    'AwaitableGetDomainsResult',
    'get_domains',
    'get_domains_output',
]

@pulumi.output_type
class GetDomainsResult:
    """
    A collection of values returned by getDomains.
    """
    def __init__(__self__, domains=None, filters=None, id=None, sorts=None):
        if domains and not isinstance(domains, list):
            raise TypeError("Expected argument 'domains' to be a list")
        pulumi.set(__self__, "domains", domains)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def domains(self) -> Sequence['outputs.GetDomainsDomainResult']:
        """
        A list of domains satisfying any `filter` and `sort` criteria. Each domain has the following attributes:
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDomainsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetDomainsSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetDomainsResult(GetDomainsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsResult(
            domains=self.domains,
            filters=self.filters,
            id=self.id,
            sorts=self.sorts)


def get_domains(filters: Optional[Sequence[pulumi.InputType['GetDomainsFilterArgs']]] = None,
                sorts: Optional[Sequence[pulumi.InputType['GetDomainsSortArgs']]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsResult:
    """
    Get information on domains for use in other resources, with the ability to filter and sort the results.
    If no filters are specified, all domains will be returned.

    This data source is useful if the domains in question are not managed by this provider or you need to
    utilize any of the domains' data.

    Note: You can use the `Domain` data source to obtain metadata
    about a single domain if you already know the `name`.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter domains. (This example
    also uses the regular expression `match_by` mode in order to match domains by suffix.)

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    examples = digitalocean.get_domains(filters=[digitalocean.GetDomainsFilterArgs(
        key="name",
        match_by="re",
        values=["example\\\\.com$"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetDomainsFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetDomainsSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getDomains:getDomains', __args__, opts=opts, typ=GetDomainsResult).value

    return AwaitableGetDomainsResult(
        domains=__ret__.domains,
        filters=__ret__.filters,
        id=__ret__.id,
        sorts=__ret__.sorts)


@_utilities.lift_output_func(get_domains)
def get_domains_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDomainsFilterArgs']]]]] = None,
                       sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDomainsSortArgs']]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsResult]:
    """
    Get information on domains for use in other resources, with the ability to filter and sort the results.
    If no filters are specified, all domains will be returned.

    This data source is useful if the domains in question are not managed by this provider or you need to
    utilize any of the domains' data.

    Note: You can use the `Domain` data source to obtain metadata
    about a single domain if you already know the `name`.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter domains. (This example
    also uses the regular expression `match_by` mode in order to match domains by suffix.)

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    examples = digitalocean.get_domains(filters=[digitalocean.GetDomainsFilterArgs(
        key="name",
        match_by="re",
        values=["example\\\\.com$"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetDomainsFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetDomainsSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    ...
