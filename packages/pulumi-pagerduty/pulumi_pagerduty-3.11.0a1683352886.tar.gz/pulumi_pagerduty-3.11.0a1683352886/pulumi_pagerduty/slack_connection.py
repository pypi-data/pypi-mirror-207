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

__all__ = ['SlackConnectionArgs', 'SlackConnection']

@pulumi.input_type
class SlackConnectionArgs:
    def __init__(__self__, *,
                 channel_id: pulumi.Input[str],
                 configs: pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]],
                 notification_type: pulumi.Input[str],
                 source_id: pulumi.Input[str],
                 source_type: pulumi.Input[str],
                 workspace_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a SlackConnection resource.
        :param pulumi.Input[str] channel_id: The ID of a Slack channel in the workspace.
        :param pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]] configs: Configuration options for the Slack connection that provide options to filter events.
        :param pulumi.Input[str] notification_type: Type of notification. Either `responder` or `stakeholder`.
        :param pulumi.Input[str] source_id: The ID of the source in PagerDuty. Valid sources are services or teams.
        :param pulumi.Input[str] source_type: The type of the source. Either `team_reference` or `service_reference`.
        :param pulumi.Input[str] workspace_id: The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        pulumi.set(__self__, "channel_id", channel_id)
        pulumi.set(__self__, "configs", configs)
        pulumi.set(__self__, "notification_type", notification_type)
        pulumi.set(__self__, "source_id", source_id)
        pulumi.set(__self__, "source_type", source_type)
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Input[str]:
        """
        The ID of a Slack channel in the workspace.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter
    def configs(self) -> pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]]:
        """
        Configuration options for the Slack connection that provide options to filter events.
        """
        return pulumi.get(self, "configs")

    @configs.setter
    def configs(self, value: pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]]):
        pulumi.set(self, "configs", value)

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Input[str]:
        """
        Type of notification. Either `responder` or `stakeholder`.
        """
        return pulumi.get(self, "notification_type")

    @notification_type.setter
    def notification_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "notification_type", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[str]:
        """
        The ID of the source in PagerDuty. Valid sources are services or teams.
        """
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[str]:
        """
        The type of the source. Either `team_reference` or `service_reference`.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)


@pulumi.input_type
class _SlackConnectionState:
    def __init__(__self__, *,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]]] = None,
                 notification_type: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 source_name: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SlackConnection resources.
        :param pulumi.Input[str] channel_id: The ID of a Slack channel in the workspace.
        :param pulumi.Input[str] channel_name: Name of the Slack channel in Slack connection.
        :param pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]] configs: Configuration options for the Slack connection that provide options to filter events.
        :param pulumi.Input[str] notification_type: Type of notification. Either `responder` or `stakeholder`.
        :param pulumi.Input[str] source_id: The ID of the source in PagerDuty. Valid sources are services or teams.
        :param pulumi.Input[str] source_name: Name of the source (team or service) in Slack connection.
        :param pulumi.Input[str] source_type: The type of the source. Either `team_reference` or `service_reference`.
        :param pulumi.Input[str] workspace_id: The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if configs is not None:
            pulumi.set(__self__, "configs", configs)
        if notification_type is not None:
            pulumi.set(__self__, "notification_type", notification_type)
        if source_id is not None:
            pulumi.set(__self__, "source_id", source_id)
        if source_name is not None:
            pulumi.set(__self__, "source_name", source_name)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a Slack channel in the workspace.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Slack channel in Slack connection.
        """
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter
    def configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]]]:
        """
        Configuration options for the Slack connection that provide options to filter events.
        """
        return pulumi.get(self, "configs")

    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SlackConnectionConfigArgs']]]]):
        pulumi.set(self, "configs", value)

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of notification. Either `responder` or `stakeholder`.
        """
        return pulumi.get(self, "notification_type")

    @notification_type.setter
    def notification_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_type", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the source in PagerDuty. Valid sources are services or teams.
        """
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the source (team or service) in Slack connection.
        """
        return pulumi.get(self, "source_name")

    @source_name.setter
    def source_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_name", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the source. Either `team_reference` or `service_reference`.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class SlackConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SlackConnectionConfigArgs']]]]] = None,
                 notification_type: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A [slack connection](https://developer.pagerduty.com/api-reference/YXBpOjExMjA5NTQ0-pager-duty-slack-integration-api) allows you to connect a workspace in Slack to a PagerDuty service or team which allows you to acknowledge and resolve PagerDuty incidents from the Slack user interface.

        **NOTES for using this resource:**
        * To first use this resource you will need to [map your PagerDuty account to a valid Slack Workspace](https://support.pagerduty.com/docs/slack-integration-guide#integration-walkthrough). *This can only be done through the PagerDuty UI.*
        * This resource requires a PagerDuty [user-level API key](https://support.pagerduty.com/docs/generating-api-keys#section-generating-a-personal-rest-api-key). This can be set as the `user_token` on the provider tag or as the `PAGERDUTY_USER_TOKEN` environment variable.
        * This resource is for configuring Slack V2 Next Generation connections. If you configured your Slack integration (V1 or V2) prior to August 10, 2021, you may migrate to the Slack V2 Next Generation update using this [migration instructions](https://support.pagerduty.com/docs/slack-integration-guide#migrate-to-slack-v2-next-generation), but if you configured your Slack integration after that date, you will have access to the update out of the box.
        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        foo_team = pagerduty.Team("fooTeam")
        p1 = pagerduty.get_priority(name="P1")
        foo_slack_connection = pagerduty.SlackConnection("fooSlackConnection",
            source_id=foo_team.id,
            source_type="team_reference",
            workspace_id="T02A123LV1A",
            channel_id="C02CABCDAC9",
            notification_type="responder",
            configs=[pagerduty.SlackConnectionConfigArgs(
                events=[
                    "incident.triggered",
                    "incident.acknowledged",
                    "incident.escalated",
                    "incident.resolved",
                    "incident.reassigned",
                    "incident.annotated",
                    "incident.unacknowledged",
                    "incident.delegated",
                    "incident.priority_updated",
                    "incident.responder.added",
                    "incident.responder.replied",
                    "incident.status_update_published",
                    "incident.reopened",
                ],
                priorities=[p1.id],
            )])
        ```

        ## Import

        Slack connections can be imported using the related `workspace` ID and the `slack_connection` ID separated by a dot, e.g.

        ```sh
         $ pulumi import pagerduty:index/slackConnection:SlackConnection main T02A123LV1A.PUABCDL
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] channel_id: The ID of a Slack channel in the workspace.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SlackConnectionConfigArgs']]]] configs: Configuration options for the Slack connection that provide options to filter events.
        :param pulumi.Input[str] notification_type: Type of notification. Either `responder` or `stakeholder`.
        :param pulumi.Input[str] source_id: The ID of the source in PagerDuty. Valid sources are services or teams.
        :param pulumi.Input[str] source_type: The type of the source. Either `team_reference` or `service_reference`.
        :param pulumi.Input[str] workspace_id: The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SlackConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A [slack connection](https://developer.pagerduty.com/api-reference/YXBpOjExMjA5NTQ0-pager-duty-slack-integration-api) allows you to connect a workspace in Slack to a PagerDuty service or team which allows you to acknowledge and resolve PagerDuty incidents from the Slack user interface.

        **NOTES for using this resource:**
        * To first use this resource you will need to [map your PagerDuty account to a valid Slack Workspace](https://support.pagerduty.com/docs/slack-integration-guide#integration-walkthrough). *This can only be done through the PagerDuty UI.*
        * This resource requires a PagerDuty [user-level API key](https://support.pagerduty.com/docs/generating-api-keys#section-generating-a-personal-rest-api-key). This can be set as the `user_token` on the provider tag or as the `PAGERDUTY_USER_TOKEN` environment variable.
        * This resource is for configuring Slack V2 Next Generation connections. If you configured your Slack integration (V1 or V2) prior to August 10, 2021, you may migrate to the Slack V2 Next Generation update using this [migration instructions](https://support.pagerduty.com/docs/slack-integration-guide#migrate-to-slack-v2-next-generation), but if you configured your Slack integration after that date, you will have access to the update out of the box.
        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        foo_team = pagerduty.Team("fooTeam")
        p1 = pagerduty.get_priority(name="P1")
        foo_slack_connection = pagerduty.SlackConnection("fooSlackConnection",
            source_id=foo_team.id,
            source_type="team_reference",
            workspace_id="T02A123LV1A",
            channel_id="C02CABCDAC9",
            notification_type="responder",
            configs=[pagerduty.SlackConnectionConfigArgs(
                events=[
                    "incident.triggered",
                    "incident.acknowledged",
                    "incident.escalated",
                    "incident.resolved",
                    "incident.reassigned",
                    "incident.annotated",
                    "incident.unacknowledged",
                    "incident.delegated",
                    "incident.priority_updated",
                    "incident.responder.added",
                    "incident.responder.replied",
                    "incident.status_update_published",
                    "incident.reopened",
                ],
                priorities=[p1.id],
            )])
        ```

        ## Import

        Slack connections can be imported using the related `workspace` ID and the `slack_connection` ID separated by a dot, e.g.

        ```sh
         $ pulumi import pagerduty:index/slackConnection:SlackConnection main T02A123LV1A.PUABCDL
        ```

        :param str resource_name: The name of the resource.
        :param SlackConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SlackConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SlackConnectionConfigArgs']]]]] = None,
                 notification_type: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SlackConnectionArgs.__new__(SlackConnectionArgs)

            if channel_id is None and not opts.urn:
                raise TypeError("Missing required property 'channel_id'")
            __props__.__dict__["channel_id"] = channel_id
            if configs is None and not opts.urn:
                raise TypeError("Missing required property 'configs'")
            __props__.__dict__["configs"] = configs
            if notification_type is None and not opts.urn:
                raise TypeError("Missing required property 'notification_type'")
            __props__.__dict__["notification_type"] = notification_type
            if source_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_id'")
            __props__.__dict__["source_id"] = source_id
            if source_type is None and not opts.urn:
                raise TypeError("Missing required property 'source_type'")
            __props__.__dict__["source_type"] = source_type
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["channel_name"] = None
            __props__.__dict__["source_name"] = None
        super(SlackConnection, __self__).__init__(
            'pagerduty:index/slackConnection:SlackConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            channel_id: Optional[pulumi.Input[str]] = None,
            channel_name: Optional[pulumi.Input[str]] = None,
            configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SlackConnectionConfigArgs']]]]] = None,
            notification_type: Optional[pulumi.Input[str]] = None,
            source_id: Optional[pulumi.Input[str]] = None,
            source_name: Optional[pulumi.Input[str]] = None,
            source_type: Optional[pulumi.Input[str]] = None,
            workspace_id: Optional[pulumi.Input[str]] = None) -> 'SlackConnection':
        """
        Get an existing SlackConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] channel_id: The ID of a Slack channel in the workspace.
        :param pulumi.Input[str] channel_name: Name of the Slack channel in Slack connection.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SlackConnectionConfigArgs']]]] configs: Configuration options for the Slack connection that provide options to filter events.
        :param pulumi.Input[str] notification_type: Type of notification. Either `responder` or `stakeholder`.
        :param pulumi.Input[str] source_id: The ID of the source in PagerDuty. Valid sources are services or teams.
        :param pulumi.Input[str] source_name: Name of the source (team or service) in Slack connection.
        :param pulumi.Input[str] source_type: The type of the source. Either `team_reference` or `service_reference`.
        :param pulumi.Input[str] workspace_id: The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SlackConnectionState.__new__(_SlackConnectionState)

        __props__.__dict__["channel_id"] = channel_id
        __props__.__dict__["channel_name"] = channel_name
        __props__.__dict__["configs"] = configs
        __props__.__dict__["notification_type"] = notification_type
        __props__.__dict__["source_id"] = source_id
        __props__.__dict__["source_name"] = source_name
        __props__.__dict__["source_type"] = source_type
        __props__.__dict__["workspace_id"] = workspace_id
        return SlackConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[str]:
        """
        The ID of a Slack channel in the workspace.
        """
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Output[str]:
        """
        Name of the Slack channel in Slack connection.
        """
        return pulumi.get(self, "channel_name")

    @property
    @pulumi.getter
    def configs(self) -> pulumi.Output[Sequence['outputs.SlackConnectionConfig']]:
        """
        Configuration options for the Slack connection that provide options to filter events.
        """
        return pulumi.get(self, "configs")

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Output[str]:
        """
        Type of notification. Either `responder` or `stakeholder`.
        """
        return pulumi.get(self, "notification_type")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Output[str]:
        """
        The ID of the source in PagerDuty. Valid sources are services or teams.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Output[str]:
        """
        Name of the source (team or service) in Slack connection.
        """
        return pulumi.get(self, "source_name")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[str]:
        """
        The type of the source. Either `team_reference` or `service_reference`.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the connected Slack workspace. Can also be defined by the `SLACK_CONNECTION_WORKSPACE_ID` environment variable.
        """
        return pulumi.get(self, "workspace_id")

