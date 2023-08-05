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
    'GetRepositoryTreeResult',
    'AwaitableGetRepositoryTreeResult',
    'get_repository_tree',
    'get_repository_tree_output',
]

@pulumi.output_type
class GetRepositoryTreeResult:
    """
    A collection of values returned by getRepositoryTree.
    """
    def __init__(__self__, id=None, path=None, project=None, recursive=None, ref=None, trees=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if recursive and not isinstance(recursive, bool):
            raise TypeError("Expected argument 'recursive' to be a bool")
        pulumi.set(__self__, "recursive", recursive)
        if ref and not isinstance(ref, str):
            raise TypeError("Expected argument 'ref' to be a str")
        pulumi.set(__self__, "ref", ref)
        if trees and not isinstance(trees, list):
            raise TypeError("Expected argument 'trees' to be a list")
        pulumi.set(__self__, "trees", trees)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        The path inside repository. Used to get content of subdirectories.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        The ID or full path of the project owned by the authenticated user.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def recursive(self) -> Optional[bool]:
        """
        Boolean value used to get a recursive tree (false by default).
        """
        return pulumi.get(self, "recursive")

    @property
    @pulumi.getter
    def ref(self) -> str:
        """
        The name of a repository branch or tag.
        """
        return pulumi.get(self, "ref")

    @property
    @pulumi.getter
    def trees(self) -> Sequence['outputs.GetRepositoryTreeTreeResult']:
        """
        The list of files/directories returned by the search
        """
        return pulumi.get(self, "trees")


class AwaitableGetRepositoryTreeResult(GetRepositoryTreeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryTreeResult(
            id=self.id,
            path=self.path,
            project=self.project,
            recursive=self.recursive,
            ref=self.ref,
            trees=self.trees)


def get_repository_tree(path: Optional[str] = None,
                        project: Optional[str] = None,
                        recursive: Optional[bool] = None,
                        ref: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryTreeResult:
    """
    The `get_repository_tree` data source allows details of directories and files in a repository to be retrieved.

    **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/repositories.html#list-repository-tree)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gitlab as gitlab

    this = gitlab.get_repository_tree(path="ExampleSubFolder",
        project="example",
        recursive=True,
        ref="main")
    ```


    :param str path: The path inside repository. Used to get content of subdirectories.
    :param str project: The ID or full path of the project owned by the authenticated user.
    :param bool recursive: Boolean value used to get a recursive tree (false by default).
    :param str ref: The name of a repository branch or tag.
    """
    __args__ = dict()
    __args__['path'] = path
    __args__['project'] = project
    __args__['recursive'] = recursive
    __args__['ref'] = ref
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gitlab:index/getRepositoryTree:getRepositoryTree', __args__, opts=opts, typ=GetRepositoryTreeResult).value

    return AwaitableGetRepositoryTreeResult(
        id=__ret__.id,
        path=__ret__.path,
        project=__ret__.project,
        recursive=__ret__.recursive,
        ref=__ret__.ref,
        trees=__ret__.trees)


@_utilities.lift_output_func(get_repository_tree)
def get_repository_tree_output(path: Optional[pulumi.Input[Optional[str]]] = None,
                               project: Optional[pulumi.Input[str]] = None,
                               recursive: Optional[pulumi.Input[Optional[bool]]] = None,
                               ref: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryTreeResult]:
    """
    The `get_repository_tree` data source allows details of directories and files in a repository to be retrieved.

    **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/repositories.html#list-repository-tree)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gitlab as gitlab

    this = gitlab.get_repository_tree(path="ExampleSubFolder",
        project="example",
        recursive=True,
        ref="main")
    ```


    :param str path: The path inside repository. Used to get content of subdirectories.
    :param str project: The ID or full path of the project owned by the authenticated user.
    :param bool recursive: Boolean value used to get a recursive tree (false by default).
    :param str ref: The name of a repository branch or tag.
    """
    ...
