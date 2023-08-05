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

__all__ = ['FlinkApplicationVersionArgs', 'FlinkApplicationVersion']

@pulumi.input_type
class FlinkApplicationVersionArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 project: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 statement: pulumi.Input[str],
                 sink: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]] = None,
                 sinks: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]] = None,
                 source: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]] = None):
        """
        The set of arguments for constructing a FlinkApplicationVersion resource.
        :param pulumi.Input[str] application_id: Application ID
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] statement: Job SQL statement
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]] sink: Application sink
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]] sinks: Application sinks
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]] source: Application source
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]] sources: Application sources
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "statement", statement)
        if sink is not None:
            pulumi.set(__self__, "sink", sink)
        if sinks is not None:
            warnings.warn("""This field is deprecated and will be removed in the next major release. Use `sink` instead.""", DeprecationWarning)
            pulumi.log.warn("""sinks is deprecated: This field is deprecated and will be removed in the next major release. Use `sink` instead.""")
        if sinks is not None:
            pulumi.set(__self__, "sinks", sinks)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if sources is not None:
            warnings.warn("""This field is deprecated and will be removed in the next major release. Use `source` instead.""", DeprecationWarning)
            pulumi.log.warn("""sources is deprecated: This field is deprecated and will be removed in the next major release. Use `source` instead.""")
        if sources is not None:
            pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        Application ID
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def statement(self) -> pulumi.Input[str]:
        """
        Job SQL statement
        """
        return pulumi.get(self, "statement")

    @statement.setter
    def statement(self, value: pulumi.Input[str]):
        pulumi.set(self, "statement", value)

    @property
    @pulumi.getter
    def sink(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]:
        """
        Application sink
        """
        return pulumi.get(self, "sink")

    @sink.setter
    def sink(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]):
        pulumi.set(self, "sink", value)

    @property
    @pulumi.getter
    def sinks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]:
        """
        Application sinks
        """
        return pulumi.get(self, "sinks")

    @sinks.setter
    def sinks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]):
        pulumi.set(self, "sinks", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]:
        """
        Application source
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]:
        """
        Application sources
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]):
        pulumi.set(self, "sources", value)


@pulumi.input_type
class _FlinkApplicationVersionState:
    def __init__(__self__, *,
                 application_id: Optional[pulumi.Input[str]] = None,
                 application_version_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sink: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]] = None,
                 sinks: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]] = None,
                 source: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering FlinkApplicationVersion resources.
        :param pulumi.Input[str] application_id: Application ID
        :param pulumi.Input[str] application_version_id: Application version ID
        :param pulumi.Input[str] created_at: Application version creation time
        :param pulumi.Input[str] created_by: Application version creator
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]] sink: Application sink
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]] sinks: Application sinks
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]] source: Application source
        :param pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]] sources: Application sources
        :param pulumi.Input[str] statement: Job SQL statement
        :param pulumi.Input[int] version: Application version number
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if application_version_id is not None:
            pulumi.set(__self__, "application_version_id", application_version_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if sink is not None:
            pulumi.set(__self__, "sink", sink)
        if sinks is not None:
            warnings.warn("""This field is deprecated and will be removed in the next major release. Use `sink` instead.""", DeprecationWarning)
            pulumi.log.warn("""sinks is deprecated: This field is deprecated and will be removed in the next major release. Use `sink` instead.""")
        if sinks is not None:
            pulumi.set(__self__, "sinks", sinks)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if sources is not None:
            warnings.warn("""This field is deprecated and will be removed in the next major release. Use `source` instead.""", DeprecationWarning)
            pulumi.log.warn("""sources is deprecated: This field is deprecated and will be removed in the next major release. Use `source` instead.""")
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if statement is not None:
            pulumi.set(__self__, "statement", statement)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        Application ID
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="applicationVersionId")
    def application_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        Application version ID
        """
        return pulumi.get(self, "application_version_id")

    @application_version_id.setter
    def application_version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_version_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Application version creation time
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        Application version creator
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def sink(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]:
        """
        Application sink
        """
        return pulumi.get(self, "sink")

    @sink.setter
    def sink(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]):
        pulumi.set(self, "sink", value)

    @property
    @pulumi.getter
    def sinks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]:
        """
        Application sinks
        """
        return pulumi.get(self, "sinks")

    @sinks.setter
    def sinks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSinkArgs']]]]):
        pulumi.set(self, "sinks", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]:
        """
        Application source
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]:
        """
        Application sources
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FlinkApplicationVersionSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def statement(self) -> Optional[pulumi.Input[str]]:
        """
        Job SQL statement
        """
        return pulumi.get(self, "statement")

    @statement.setter
    def statement(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "statement", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Application version number
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class FlinkApplicationVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sink: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]]] = None,
                 sinks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]]] = None,
                 source: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Flink Application Version resource allows the creation and management of Aiven Flink Application Versions.

        ## Import

        ```sh
         $ pulumi import aiven:index/flinkApplicationVersion:FlinkApplicationVersion v1 project/service/application_id/application_version_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: Application ID
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]] sink: Application sink
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]] sinks: Application sinks
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]] source: Application source
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]] sources: Application sources
        :param pulumi.Input[str] statement: Job SQL statement
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FlinkApplicationVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Flink Application Version resource allows the creation and management of Aiven Flink Application Versions.

        ## Import

        ```sh
         $ pulumi import aiven:index/flinkApplicationVersion:FlinkApplicationVersion v1 project/service/application_id/application_version_id
        ```

        :param str resource_name: The name of the resource.
        :param FlinkApplicationVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlinkApplicationVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sink: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]]] = None,
                 sinks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]]] = None,
                 source: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlinkApplicationVersionArgs.__new__(FlinkApplicationVersionArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["sink"] = sink
            if sinks is not None and not opts.urn:
                warnings.warn("""This field is deprecated and will be removed in the next major release. Use `sink` instead.""", DeprecationWarning)
                pulumi.log.warn("""sinks is deprecated: This field is deprecated and will be removed in the next major release. Use `sink` instead.""")
            __props__.__dict__["sinks"] = sinks
            __props__.__dict__["source"] = source
            if sources is not None and not opts.urn:
                warnings.warn("""This field is deprecated and will be removed in the next major release. Use `source` instead.""", DeprecationWarning)
                pulumi.log.warn("""sources is deprecated: This field is deprecated and will be removed in the next major release. Use `source` instead.""")
            __props__.__dict__["sources"] = sources
            if statement is None and not opts.urn:
                raise TypeError("Missing required property 'statement'")
            __props__.__dict__["statement"] = statement
            __props__.__dict__["application_version_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["version"] = None
        super(FlinkApplicationVersion, __self__).__init__(
            'aiven:index/flinkApplicationVersion:FlinkApplicationVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            application_version_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            sink: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]]] = None,
            sinks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]]] = None,
            source: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]]] = None,
            statement: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'FlinkApplicationVersion':
        """
        Get an existing FlinkApplicationVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: Application ID
        :param pulumi.Input[str] application_version_id: Application version ID
        :param pulumi.Input[str] created_at: Application version creation time
        :param pulumi.Input[str] created_by: Application version creator
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]] sink: Application sink
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSinkArgs']]]] sinks: Application sinks
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]] source: Application source
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlinkApplicationVersionSourceArgs']]]] sources: Application sources
        :param pulumi.Input[str] statement: Job SQL statement
        :param pulumi.Input[int] version: Application version number
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FlinkApplicationVersionState.__new__(_FlinkApplicationVersionState)

        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["application_version_id"] = application_version_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["project"] = project
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["sink"] = sink
        __props__.__dict__["sinks"] = sinks
        __props__.__dict__["source"] = source
        __props__.__dict__["sources"] = sources
        __props__.__dict__["statement"] = statement
        __props__.__dict__["version"] = version
        return FlinkApplicationVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        Application ID
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="applicationVersionId")
    def application_version_id(self) -> pulumi.Output[str]:
        """
        Application version ID
        """
        return pulumi.get(self, "application_version_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Application version creation time
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        Application version creator
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def sink(self) -> pulumi.Output[Optional[Sequence['outputs.FlinkApplicationVersionSink']]]:
        """
        Application sink
        """
        return pulumi.get(self, "sink")

    @property
    @pulumi.getter
    def sinks(self) -> pulumi.Output[Optional[Sequence['outputs.FlinkApplicationVersionSink']]]:
        """
        Application sinks
        """
        return pulumi.get(self, "sinks")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[Sequence['outputs.FlinkApplicationVersionSource']]]:
        """
        Application source
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence['outputs.FlinkApplicationVersionSource']]]:
        """
        Application sources
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def statement(self) -> pulumi.Output[str]:
        """
        Job SQL statement
        """
        return pulumi.get(self, "statement")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        Application version number
        """
        return pulumi.get(self, "version")

