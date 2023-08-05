# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ClusterAgentTokenArgs', 'ClusterAgentToken']

@pulumi.input_type
class ClusterAgentTokenArgs:
    def __init__(__self__, *,
                 agent_id: pulumi.Input[int],
                 project: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ClusterAgentToken resource.
        :param pulumi.Input[int] agent_id: The ID of the agent.
        :param pulumi.Input[str] project: ID or full path of the project maintained by the authenticated user.
        :param pulumi.Input[str] description: The Description for the agent.
        :param pulumi.Input[str] name: The Name of the agent.
        """
        pulumi.set(__self__, "agent_id", agent_id)
        pulumi.set(__self__, "project", project)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[int]:
        """
        The ID of the agent.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        ID or full path of the project maintained by the authenticated user.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Description for the agent.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the agent.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ClusterAgentTokenState:
    def __init__(__self__, *,
                 agent_id: Optional[pulumi.Input[int]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by_user_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 last_used_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 token_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ClusterAgentToken resources.
        :param pulumi.Input[int] agent_id: The ID of the agent.
        :param pulumi.Input[str] created_at: The ISO8601 datetime when the agent was created.
        :param pulumi.Input[int] created_by_user_id: The ID of the user who created the agent.
        :param pulumi.Input[str] description: The Description for the agent.
        :param pulumi.Input[str] last_used_at: The ISO8601 datetime when the token was last used.
        :param pulumi.Input[str] name: The Name of the agent.
        :param pulumi.Input[str] project: ID or full path of the project maintained by the authenticated user.
        :param pulumi.Input[str] status: The status of the token. Valid values are `active`, `revoked`.
        :param pulumi.Input[str] token: The secret token for the agent. The `token` is not available in imported resources.
        :param pulumi.Input[int] token_id: The ID of the token.
        """
        if agent_id is not None:
            pulumi.set(__self__, "agent_id", agent_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by_user_id is not None:
            pulumi.set(__self__, "created_by_user_id", created_by_user_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if last_used_at is not None:
            pulumi.set(__self__, "last_used_at", last_used_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if token_id is not None:
            pulumi.set(__self__, "token_id", token_id)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the agent.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The ISO8601 datetime when the agent was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the user who created the agent.
        """
        return pulumi.get(self, "created_by_user_id")

    @created_by_user_id.setter
    def created_by_user_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_by_user_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Description for the agent.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lastUsedAt")
    def last_used_at(self) -> Optional[pulumi.Input[str]]:
        """
        The ISO8601 datetime when the token was last used.
        """
        return pulumi.get(self, "last_used_at")

    @last_used_at.setter
    def last_used_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_used_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the agent.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        ID or full path of the project maintained by the authenticated user.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the token. Valid values are `active`, `revoked`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The secret token for the agent. The `token` is not available in imported resources.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the token.
        """
        return pulumi.get(self, "token_id")

    @token_id.setter
    def token_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "token_id", value)


class ClusterAgentToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `ClusterAgentToken` resource allows to manage the lifecycle of a token for a GitLab Agent for Kubernetes.

        > Requires at least maintainer permissions on the project.

        > Requires at least GitLab 15.0

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/cluster_agents.html#create-an-agent-token)

        ## Import

        A token for a GitLab Agent for Kubernetes can be imported with the following command and the id pattern `<project>:<agent-id>:<token-id>`

        ```sh
         $ pulumi import gitlab:index/clusterAgentToken:ClusterAgentToken example '12345:42:1'
        ```

         ATTENTIONthe `token` resource attribute is not available for imported resources as this information cannot be read from the GitLab API.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] agent_id: The ID of the agent.
        :param pulumi.Input[str] description: The Description for the agent.
        :param pulumi.Input[str] name: The Name of the agent.
        :param pulumi.Input[str] project: ID or full path of the project maintained by the authenticated user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterAgentTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `ClusterAgentToken` resource allows to manage the lifecycle of a token for a GitLab Agent for Kubernetes.

        > Requires at least maintainer permissions on the project.

        > Requires at least GitLab 15.0

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/cluster_agents.html#create-an-agent-token)

        ## Import

        A token for a GitLab Agent for Kubernetes can be imported with the following command and the id pattern `<project>:<agent-id>:<token-id>`

        ```sh
         $ pulumi import gitlab:index/clusterAgentToken:ClusterAgentToken example '12345:42:1'
        ```

         ATTENTIONthe `token` resource attribute is not available for imported resources as this information cannot be read from the GitLab API.

        :param str resource_name: The name of the resource.
        :param ClusterAgentTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterAgentTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterAgentTokenArgs.__new__(ClusterAgentTokenArgs)

            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by_user_id"] = None
            __props__.__dict__["last_used_at"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["token"] = None
            __props__.__dict__["token_id"] = None
        super(ClusterAgentToken, __self__).__init__(
            'gitlab:index/clusterAgentToken:ClusterAgentToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_id: Optional[pulumi.Input[int]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by_user_id: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            last_used_at: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            token_id: Optional[pulumi.Input[int]] = None) -> 'ClusterAgentToken':
        """
        Get an existing ClusterAgentToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] agent_id: The ID of the agent.
        :param pulumi.Input[str] created_at: The ISO8601 datetime when the agent was created.
        :param pulumi.Input[int] created_by_user_id: The ID of the user who created the agent.
        :param pulumi.Input[str] description: The Description for the agent.
        :param pulumi.Input[str] last_used_at: The ISO8601 datetime when the token was last used.
        :param pulumi.Input[str] name: The Name of the agent.
        :param pulumi.Input[str] project: ID or full path of the project maintained by the authenticated user.
        :param pulumi.Input[str] status: The status of the token. Valid values are `active`, `revoked`.
        :param pulumi.Input[str] token: The secret token for the agent. The `token` is not available in imported resources.
        :param pulumi.Input[int] token_id: The ID of the token.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterAgentTokenState.__new__(_ClusterAgentTokenState)

        __props__.__dict__["agent_id"] = agent_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by_user_id"] = created_by_user_id
        __props__.__dict__["description"] = description
        __props__.__dict__["last_used_at"] = last_used_at
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["status"] = status
        __props__.__dict__["token"] = token
        __props__.__dict__["token_id"] = token_id
        return ClusterAgentToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[int]:
        """
        The ID of the agent.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The ISO8601 datetime when the agent was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> pulumi.Output[int]:
        """
        The ID of the user who created the agent.
        """
        return pulumi.get(self, "created_by_user_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The Description for the agent.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUsedAt")
    def last_used_at(self) -> pulumi.Output[str]:
        """
        The ISO8601 datetime when the token was last used.
        """
        return pulumi.get(self, "last_used_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Name of the agent.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        ID or full path of the project maintained by the authenticated user.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the token. Valid values are `active`, `revoked`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The secret token for the agent. The `token` is not available in imported resources.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> pulumi.Output[int]:
        """
        The ID of the token.
        """
        return pulumi.get(self, "token_id")

