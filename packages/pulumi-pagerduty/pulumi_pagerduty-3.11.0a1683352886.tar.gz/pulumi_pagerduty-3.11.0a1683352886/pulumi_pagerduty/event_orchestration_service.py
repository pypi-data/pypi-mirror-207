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

__all__ = ['EventOrchestrationServiceArgs', 'EventOrchestrationService']

@pulumi.input_type
class EventOrchestrationServiceArgs:
    def __init__(__self__, *,
                 catch_all: pulumi.Input['EventOrchestrationServiceCatchAllArgs'],
                 service: pulumi.Input[str],
                 sets: pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]],
                 enable_event_orchestration_for_service: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a EventOrchestrationService resource.
        :param pulumi.Input['EventOrchestrationServiceCatchAllArgs'] catch_all: the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        :param pulumi.Input[str] service: ID of the Service to which this Service Orchestration belongs to.
        :param pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]] sets: A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        :param pulumi.Input[bool] enable_event_orchestration_for_service: Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        """
        pulumi.set(__self__, "catch_all", catch_all)
        pulumi.set(__self__, "service", service)
        pulumi.set(__self__, "sets", sets)
        if enable_event_orchestration_for_service is not None:
            pulumi.set(__self__, "enable_event_orchestration_for_service", enable_event_orchestration_for_service)

    @property
    @pulumi.getter(name="catchAll")
    def catch_all(self) -> pulumi.Input['EventOrchestrationServiceCatchAllArgs']:
        """
        the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        """
        return pulumi.get(self, "catch_all")

    @catch_all.setter
    def catch_all(self, value: pulumi.Input['EventOrchestrationServiceCatchAllArgs']):
        pulumi.set(self, "catch_all", value)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        ID of the Service to which this Service Orchestration belongs to.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def sets(self) -> pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]]:
        """
        A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        """
        return pulumi.get(self, "sets")

    @sets.setter
    def sets(self, value: pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]]):
        pulumi.set(self, "sets", value)

    @property
    @pulumi.getter(name="enableEventOrchestrationForService")
    def enable_event_orchestration_for_service(self) -> Optional[pulumi.Input[bool]]:
        """
        Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        """
        return pulumi.get(self, "enable_event_orchestration_for_service")

    @enable_event_orchestration_for_service.setter
    def enable_event_orchestration_for_service(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_event_orchestration_for_service", value)


@pulumi.input_type
class _EventOrchestrationServiceState:
    def __init__(__self__, *,
                 catch_all: Optional[pulumi.Input['EventOrchestrationServiceCatchAllArgs']] = None,
                 enable_event_orchestration_for_service: Optional[pulumi.Input[bool]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 sets: Optional[pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]]] = None):
        """
        Input properties used for looking up and filtering EventOrchestrationService resources.
        :param pulumi.Input['EventOrchestrationServiceCatchAllArgs'] catch_all: the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        :param pulumi.Input[bool] enable_event_orchestration_for_service: Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        :param pulumi.Input[str] service: ID of the Service to which this Service Orchestration belongs to.
        :param pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]] sets: A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        """
        if catch_all is not None:
            pulumi.set(__self__, "catch_all", catch_all)
        if enable_event_orchestration_for_service is not None:
            pulumi.set(__self__, "enable_event_orchestration_for_service", enable_event_orchestration_for_service)
        if service is not None:
            pulumi.set(__self__, "service", service)
        if sets is not None:
            pulumi.set(__self__, "sets", sets)

    @property
    @pulumi.getter(name="catchAll")
    def catch_all(self) -> Optional[pulumi.Input['EventOrchestrationServiceCatchAllArgs']]:
        """
        the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        """
        return pulumi.get(self, "catch_all")

    @catch_all.setter
    def catch_all(self, value: Optional[pulumi.Input['EventOrchestrationServiceCatchAllArgs']]):
        pulumi.set(self, "catch_all", value)

    @property
    @pulumi.getter(name="enableEventOrchestrationForService")
    def enable_event_orchestration_for_service(self) -> Optional[pulumi.Input[bool]]:
        """
        Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        """
        return pulumi.get(self, "enable_event_orchestration_for_service")

    @enable_event_orchestration_for_service.setter
    def enable_event_orchestration_for_service(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_event_orchestration_for_service", value)

    @property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Service to which this Service Orchestration belongs to.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]]]:
        """
        A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        """
        return pulumi.get(self, "sets")

    @sets.setter
    def sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventOrchestrationServiceSetArgs']]]]):
        pulumi.set(self, "sets", value)


class EventOrchestrationService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catch_all: Optional[pulumi.Input[pulumi.InputType['EventOrchestrationServiceCatchAllArgs']]] = None,
                 enable_event_orchestration_for_service: Optional[pulumi.Input[bool]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventOrchestrationServiceSetArgs']]]]] = None,
                 __props__=None):
        """
        ## Import

        Service Orchestration can be imported using the `id` of the Service, e.g.

        ```sh
         $ pulumi import pagerduty:index/eventOrchestrationService:EventOrchestrationService service PFEODA7
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EventOrchestrationServiceCatchAllArgs']] catch_all: the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        :param pulumi.Input[bool] enable_event_orchestration_for_service: Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        :param pulumi.Input[str] service: ID of the Service to which this Service Orchestration belongs to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventOrchestrationServiceSetArgs']]]] sets: A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventOrchestrationServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Service Orchestration can be imported using the `id` of the Service, e.g.

        ```sh
         $ pulumi import pagerduty:index/eventOrchestrationService:EventOrchestrationService service PFEODA7
        ```

        :param str resource_name: The name of the resource.
        :param EventOrchestrationServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventOrchestrationServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catch_all: Optional[pulumi.Input[pulumi.InputType['EventOrchestrationServiceCatchAllArgs']]] = None,
                 enable_event_orchestration_for_service: Optional[pulumi.Input[bool]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventOrchestrationServiceSetArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventOrchestrationServiceArgs.__new__(EventOrchestrationServiceArgs)

            if catch_all is None and not opts.urn:
                raise TypeError("Missing required property 'catch_all'")
            __props__.__dict__["catch_all"] = catch_all
            __props__.__dict__["enable_event_orchestration_for_service"] = enable_event_orchestration_for_service
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
            if sets is None and not opts.urn:
                raise TypeError("Missing required property 'sets'")
            __props__.__dict__["sets"] = sets
        super(EventOrchestrationService, __self__).__init__(
            'pagerduty:index/eventOrchestrationService:EventOrchestrationService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            catch_all: Optional[pulumi.Input[pulumi.InputType['EventOrchestrationServiceCatchAllArgs']]] = None,
            enable_event_orchestration_for_service: Optional[pulumi.Input[bool]] = None,
            service: Optional[pulumi.Input[str]] = None,
            sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventOrchestrationServiceSetArgs']]]]] = None) -> 'EventOrchestrationService':
        """
        Get an existing EventOrchestrationService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EventOrchestrationServiceCatchAllArgs']] catch_all: the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        :param pulumi.Input[bool] enable_event_orchestration_for_service: Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        :param pulumi.Input[str] service: ID of the Service to which this Service Orchestration belongs to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventOrchestrationServiceSetArgs']]]] sets: A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EventOrchestrationServiceState.__new__(_EventOrchestrationServiceState)

        __props__.__dict__["catch_all"] = catch_all
        __props__.__dict__["enable_event_orchestration_for_service"] = enable_event_orchestration_for_service
        __props__.__dict__["service"] = service
        __props__.__dict__["sets"] = sets
        return EventOrchestrationService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catchAll")
    def catch_all(self) -> pulumi.Output['outputs.EventOrchestrationServiceCatchAll']:
        """
        the `catch_all` actions will be applied if an Event reaches the end of any set without matching any rules in that set.
        """
        return pulumi.get(self, "catch_all")

    @property
    @pulumi.getter(name="enableEventOrchestrationForService")
    def enable_event_orchestration_for_service(self) -> pulumi.Output[Optional[bool]]:
        """
        Opt-in/out for switching the Service to [Service Orchestrations](https://support.pagerduty.com/docs/event-orchestration#service-orchestrations).
        """
        return pulumi.get(self, "enable_event_orchestration_for_service")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        ID of the Service to which this Service Orchestration belongs to.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def sets(self) -> pulumi.Output[Sequence['outputs.EventOrchestrationServiceSet']]:
        """
        A Service Orchestration must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph.
        """
        return pulumi.get(self, "sets")

