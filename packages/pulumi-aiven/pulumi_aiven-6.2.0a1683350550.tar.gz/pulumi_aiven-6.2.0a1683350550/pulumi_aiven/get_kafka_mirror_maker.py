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
    'GetKafkaMirrorMakerResult',
    'AwaitableGetKafkaMirrorMakerResult',
    'get_kafka_mirror_maker',
    'get_kafka_mirror_maker_output',
]

@pulumi.output_type
class GetKafkaMirrorMakerResult:
    """
    A collection of values returned by getKafkaMirrorMaker.
    """
    def __init__(__self__, additional_disk_space=None, cloud_name=None, components=None, disk_space=None, disk_space_cap=None, disk_space_default=None, disk_space_step=None, disk_space_used=None, id=None, kafka_mirrormaker_user_configs=None, kafka_mirrormakers=None, maintenance_window_dow=None, maintenance_window_time=None, plan=None, project=None, project_vpc_id=None, service_host=None, service_integrations=None, service_name=None, service_password=None, service_port=None, service_type=None, service_uri=None, service_username=None, state=None, static_ips=None, tags=None, termination_protection=None):
        if additional_disk_space and not isinstance(additional_disk_space, str):
            raise TypeError("Expected argument 'additional_disk_space' to be a str")
        pulumi.set(__self__, "additional_disk_space", additional_disk_space)
        if cloud_name and not isinstance(cloud_name, str):
            raise TypeError("Expected argument 'cloud_name' to be a str")
        pulumi.set(__self__, "cloud_name", cloud_name)
        if components and not isinstance(components, list):
            raise TypeError("Expected argument 'components' to be a list")
        pulumi.set(__self__, "components", components)
        if disk_space and not isinstance(disk_space, str):
            raise TypeError("Expected argument 'disk_space' to be a str")
        pulumi.set(__self__, "disk_space", disk_space)
        if disk_space_cap and not isinstance(disk_space_cap, str):
            raise TypeError("Expected argument 'disk_space_cap' to be a str")
        pulumi.set(__self__, "disk_space_cap", disk_space_cap)
        if disk_space_default and not isinstance(disk_space_default, str):
            raise TypeError("Expected argument 'disk_space_default' to be a str")
        pulumi.set(__self__, "disk_space_default", disk_space_default)
        if disk_space_step and not isinstance(disk_space_step, str):
            raise TypeError("Expected argument 'disk_space_step' to be a str")
        pulumi.set(__self__, "disk_space_step", disk_space_step)
        if disk_space_used and not isinstance(disk_space_used, str):
            raise TypeError("Expected argument 'disk_space_used' to be a str")
        pulumi.set(__self__, "disk_space_used", disk_space_used)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kafka_mirrormaker_user_configs and not isinstance(kafka_mirrormaker_user_configs, list):
            raise TypeError("Expected argument 'kafka_mirrormaker_user_configs' to be a list")
        pulumi.set(__self__, "kafka_mirrormaker_user_configs", kafka_mirrormaker_user_configs)
        if kafka_mirrormakers and not isinstance(kafka_mirrormakers, list):
            raise TypeError("Expected argument 'kafka_mirrormakers' to be a list")
        pulumi.set(__self__, "kafka_mirrormakers", kafka_mirrormakers)
        if maintenance_window_dow and not isinstance(maintenance_window_dow, str):
            raise TypeError("Expected argument 'maintenance_window_dow' to be a str")
        pulumi.set(__self__, "maintenance_window_dow", maintenance_window_dow)
        if maintenance_window_time and not isinstance(maintenance_window_time, str):
            raise TypeError("Expected argument 'maintenance_window_time' to be a str")
        pulumi.set(__self__, "maintenance_window_time", maintenance_window_time)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if project_vpc_id and not isinstance(project_vpc_id, str):
            raise TypeError("Expected argument 'project_vpc_id' to be a str")
        pulumi.set(__self__, "project_vpc_id", project_vpc_id)
        if service_host and not isinstance(service_host, str):
            raise TypeError("Expected argument 'service_host' to be a str")
        pulumi.set(__self__, "service_host", service_host)
        if service_integrations and not isinstance(service_integrations, list):
            raise TypeError("Expected argument 'service_integrations' to be a list")
        pulumi.set(__self__, "service_integrations", service_integrations)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if service_password and not isinstance(service_password, str):
            raise TypeError("Expected argument 'service_password' to be a str")
        pulumi.set(__self__, "service_password", service_password)
        if service_port and not isinstance(service_port, int):
            raise TypeError("Expected argument 'service_port' to be a int")
        pulumi.set(__self__, "service_port", service_port)
        if service_type and not isinstance(service_type, str):
            raise TypeError("Expected argument 'service_type' to be a str")
        pulumi.set(__self__, "service_type", service_type)
        if service_uri and not isinstance(service_uri, str):
            raise TypeError("Expected argument 'service_uri' to be a str")
        pulumi.set(__self__, "service_uri", service_uri)
        if service_username and not isinstance(service_username, str):
            raise TypeError("Expected argument 'service_username' to be a str")
        pulumi.set(__self__, "service_username", service_username)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if static_ips and not isinstance(static_ips, list):
            raise TypeError("Expected argument 'static_ips' to be a list")
        pulumi.set(__self__, "static_ips", static_ips)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if termination_protection and not isinstance(termination_protection, bool):
            raise TypeError("Expected argument 'termination_protection' to be a bool")
        pulumi.set(__self__, "termination_protection", termination_protection)

    @property
    @pulumi.getter(name="additionalDiskSpace")
    def additional_disk_space(self) -> str:
        """
        Additional disk space. Possible values depend on the service type, the cloud provider and the project. Therefore, reducing will result in the service rebalancing.
        """
        return pulumi.get(self, "additional_disk_space")

    @property
    @pulumi.getter(name="cloudName")
    def cloud_name(self) -> str:
        """
        Defines where the cloud provider and region where the service is hosted in. This can be changed freely after service is created. Changing the value will trigger a potentially lengthy migration process for the service. Format is cloud provider name (`aws`, `azure`, `do` `google`, `upcloud`, etc.), dash, and the cloud provider specific region name. These are documented on each Cloud provider's own support articles, like [here for Google](https://cloud.google.com/compute/docs/regions-zones/) and [here for AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
        """
        return pulumi.get(self, "cloud_name")

    @property
    @pulumi.getter
    def components(self) -> Sequence['outputs.GetKafkaMirrorMakerComponentResult']:
        """
        Service component information objects
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter(name="diskSpace")
    def disk_space(self) -> str:
        """
        Service disk space. Possible values depend on the service type, the cloud provider and the project. Therefore, reducing will result in the service rebalancing.
        """
        return pulumi.get(self, "disk_space")

    @property
    @pulumi.getter(name="diskSpaceCap")
    def disk_space_cap(self) -> str:
        """
        The maximum disk space of the service, possible values depend on the service type, the cloud provider and the project.
        """
        return pulumi.get(self, "disk_space_cap")

    @property
    @pulumi.getter(name="diskSpaceDefault")
    def disk_space_default(self) -> str:
        """
        The default disk space of the service, possible values depend on the service type, the cloud provider and the project. Its also the minimum value for `disk_space`
        """
        return pulumi.get(self, "disk_space_default")

    @property
    @pulumi.getter(name="diskSpaceStep")
    def disk_space_step(self) -> str:
        """
        The default disk space step of the service, possible values depend on the service type, the cloud provider and the project. `disk_space` needs to increment from `disk_space_default` by increments of this size.
        """
        return pulumi.get(self, "disk_space_step")

    @property
    @pulumi.getter(name="diskSpaceUsed")
    def disk_space_used(self) -> str:
        """
        Disk space that service is currently using
        """
        return pulumi.get(self, "disk_space_used")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kafkaMirrormakerUserConfigs")
    def kafka_mirrormaker_user_configs(self) -> Sequence['outputs.GetKafkaMirrorMakerKafkaMirrormakerUserConfigResult']:
        """
        KafkaMirrormaker user configurable settings
        """
        return pulumi.get(self, "kafka_mirrormaker_user_configs")

    @property
    @pulumi.getter(name="kafkaMirrormakers")
    def kafka_mirrormakers(self) -> Sequence['outputs.GetKafkaMirrorMakerKafkaMirrormakerResult']:
        """
        Kafka MirrorMaker 2 server provided values
        """
        return pulumi.get(self, "kafka_mirrormakers")

    @property
    @pulumi.getter(name="maintenanceWindowDow")
    def maintenance_window_dow(self) -> str:
        """
        Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
        """
        return pulumi.get(self, "maintenance_window_dow")

    @property
    @pulumi.getter(name="maintenanceWindowTime")
    def maintenance_window_time(self) -> str:
        """
        Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
        """
        return pulumi.get(self, "maintenance_window_time")

    @property
    @pulumi.getter
    def plan(self) -> str:
        """
        Defines what kind of computing resources are allocated for the service. It can be changed after creation, though there are some restrictions when going to a smaller plan such as the new plan must have sufficient amount of disk space to store all current data and switching to a plan with fewer nodes might not be supported. The basic plan names are `hobbyist`, `startup-x`, `business-x` and `premium-x` where `x` is (roughly) the amount of memory on each node (also other attributes like number of CPUs and amount of disk space varies but naming is based on memory). The available options can be seem from the [Aiven pricing page](https://aiven.io/pricing).
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="projectVpcId")
    def project_vpc_id(self) -> str:
        """
        Specifies the VPC the service should run in. If the value is not set the service is not run inside a VPC. When set, the value should be given as a reference to set up dependencies correctly and the VPC must be in the same cloud and region as the service itself. Project can be freely moved to and from VPC after creation but doing so triggers migration to new servers so the operation can take significant amount of time to complete if the service has a lot of data.
        """
        return pulumi.get(self, "project_vpc_id")

    @property
    @pulumi.getter(name="serviceHost")
    def service_host(self) -> str:
        """
        The hostname of the service.
        """
        return pulumi.get(self, "service_host")

    @property
    @pulumi.getter(name="serviceIntegrations")
    def service_integrations(self) -> Sequence['outputs.GetKafkaMirrorMakerServiceIntegrationResult']:
        """
        Service integrations to specify when creating a service. Not applied after initial service creation
        """
        return pulumi.get(self, "service_integrations")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Specifies the actual name of the service. The name cannot be changed later without destroying and re-creating the service so name should be picked based on intended service usage rather than current attributes.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="servicePassword")
    def service_password(self) -> str:
        """
        Password used for connecting to the service, if applicable
        """
        return pulumi.get(self, "service_password")

    @property
    @pulumi.getter(name="servicePort")
    def service_port(self) -> int:
        """
        The port of the service
        """
        return pulumi.get(self, "service_port")

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> str:
        """
        Aiven internal service type code
        """
        return pulumi.get(self, "service_type")

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> str:
        """
        URI for connecting to the service. Service specific info is under "kafka", "pg", etc.
        """
        return pulumi.get(self, "service_uri")

    @property
    @pulumi.getter(name="serviceUsername")
    def service_username(self) -> str:
        """
        Username used for connecting to the service, if applicable
        """
        return pulumi.get(self, "service_username")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Service state. One of `POWEROFF`, `REBALANCING`, `REBUILDING` or `RUNNING`
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="staticIps")
    def static_ips(self) -> Sequence[str]:
        """
        Static IPs that are going to be associated with this service. Please assign a value using the 'toset' function. Once a static ip resource is in the 'assigned' state it cannot be unbound from the node again
        """
        return pulumi.get(self, "static_ips")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetKafkaMirrorMakerTagResult']:
        """
        Tags are key-value pairs that allow you to categorize services.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> bool:
        """
        Prevents the service from being deleted. It is recommended to set this to `true` for all production services to prevent unintentional service deletion. This does not shield against deleting databases or topics but for services with backups much of the content can at least be restored from backup in case accidental deletion is done.
        """
        return pulumi.get(self, "termination_protection")


class AwaitableGetKafkaMirrorMakerResult(GetKafkaMirrorMakerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaMirrorMakerResult(
            additional_disk_space=self.additional_disk_space,
            cloud_name=self.cloud_name,
            components=self.components,
            disk_space=self.disk_space,
            disk_space_cap=self.disk_space_cap,
            disk_space_default=self.disk_space_default,
            disk_space_step=self.disk_space_step,
            disk_space_used=self.disk_space_used,
            id=self.id,
            kafka_mirrormaker_user_configs=self.kafka_mirrormaker_user_configs,
            kafka_mirrormakers=self.kafka_mirrormakers,
            maintenance_window_dow=self.maintenance_window_dow,
            maintenance_window_time=self.maintenance_window_time,
            plan=self.plan,
            project=self.project,
            project_vpc_id=self.project_vpc_id,
            service_host=self.service_host,
            service_integrations=self.service_integrations,
            service_name=self.service_name,
            service_password=self.service_password,
            service_port=self.service_port,
            service_type=self.service_type,
            service_uri=self.service_uri,
            service_username=self.service_username,
            state=self.state,
            static_ips=self.static_ips,
            tags=self.tags,
            termination_protection=self.termination_protection)


def get_kafka_mirror_maker(project: Optional[str] = None,
                           service_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaMirrorMakerResult:
    """
    The Kafka MirrorMaker data source provides information about the existing Aiven Kafka MirrorMaker 2 service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mm1 = aiven.get_kafka_mirror_maker(project=data["aiven_project"]["pr1"]["project"],
        service_name="my-mm1")
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the actual name of the service. The name cannot be changed later without destroying and re-creating the service so name should be picked based on intended service usage rather than current attributes.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getKafkaMirrorMaker:getKafkaMirrorMaker', __args__, opts=opts, typ=GetKafkaMirrorMakerResult).value

    return AwaitableGetKafkaMirrorMakerResult(
        additional_disk_space=__ret__.additional_disk_space,
        cloud_name=__ret__.cloud_name,
        components=__ret__.components,
        disk_space=__ret__.disk_space,
        disk_space_cap=__ret__.disk_space_cap,
        disk_space_default=__ret__.disk_space_default,
        disk_space_step=__ret__.disk_space_step,
        disk_space_used=__ret__.disk_space_used,
        id=__ret__.id,
        kafka_mirrormaker_user_configs=__ret__.kafka_mirrormaker_user_configs,
        kafka_mirrormakers=__ret__.kafka_mirrormakers,
        maintenance_window_dow=__ret__.maintenance_window_dow,
        maintenance_window_time=__ret__.maintenance_window_time,
        plan=__ret__.plan,
        project=__ret__.project,
        project_vpc_id=__ret__.project_vpc_id,
        service_host=__ret__.service_host,
        service_integrations=__ret__.service_integrations,
        service_name=__ret__.service_name,
        service_password=__ret__.service_password,
        service_port=__ret__.service_port,
        service_type=__ret__.service_type,
        service_uri=__ret__.service_uri,
        service_username=__ret__.service_username,
        state=__ret__.state,
        static_ips=__ret__.static_ips,
        tags=__ret__.tags,
        termination_protection=__ret__.termination_protection)


@_utilities.lift_output_func(get_kafka_mirror_maker)
def get_kafka_mirror_maker_output(project: Optional[pulumi.Input[str]] = None,
                                  service_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaMirrorMakerResult]:
    """
    The Kafka MirrorMaker data source provides information about the existing Aiven Kafka MirrorMaker 2 service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    mm1 = aiven.get_kafka_mirror_maker(project=data["aiven_project"]["pr1"]["project"],
        service_name="my-mm1")
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the actual name of the service. The name cannot be changed later without destroying and re-creating the service so name should be picked based on intended service usage rather than current attributes.
    """
    ...
