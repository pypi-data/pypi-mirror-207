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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 add_account_owners_admin_access: Optional[pulumi.Input[bool]] = None,
                 available_credits: Optional[pulumi.Input[str]] = None,
                 billing_group: Optional[pulumi.Input[str]] = None,
                 copy_from_project: Optional[pulumi.Input[str]] = None,
                 default_cloud: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]] = None,
                 technical_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_source_project_billing_group: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] project: Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        :param pulumi.Input[str] account_id: An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[bool] add_account_owners_admin_access: If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        :param pulumi.Input[str] available_credits: The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        :param pulumi.Input[str] billing_group: The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] copy_from_project: is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] default_cloud: Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        :param pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]] tags: Tags are key-value pairs that allow you to categorize projects.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] technical_emails: Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        :param pulumi.Input[bool] use_source_project_billing_group: Use the same billing group that is used in source project.
        """
        pulumi.set(__self__, "project", project)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if add_account_owners_admin_access is not None:
            pulumi.set(__self__, "add_account_owners_admin_access", add_account_owners_admin_access)
        if available_credits is not None:
            pulumi.set(__self__, "available_credits", available_credits)
        if billing_group is not None:
            pulumi.set(__self__, "billing_group", billing_group)
        if copy_from_project is not None:
            pulumi.set(__self__, "copy_from_project", copy_from_project)
        if default_cloud is not None:
            pulumi.set(__self__, "default_cloud", default_cloud)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if technical_emails is not None:
            pulumi.set(__self__, "technical_emails", technical_emails)
        if use_source_project_billing_group is not None:
            pulumi.set(__self__, "use_source_project_billing_group", use_source_project_billing_group)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="addAccountOwnersAdminAccess")
    def add_account_owners_admin_access(self) -> Optional[pulumi.Input[bool]]:
        """
        If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        """
        return pulumi.get(self, "add_account_owners_admin_access")

    @add_account_owners_admin_access.setter
    def add_account_owners_admin_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "add_account_owners_admin_access", value)

    @property
    @pulumi.getter(name="availableCredits")
    def available_credits(self) -> Optional[pulumi.Input[str]]:
        """
        The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        """
        return pulumi.get(self, "available_credits")

    @available_credits.setter
    def available_credits(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "available_credits", value)

    @property
    @pulumi.getter(name="billingGroup")
    def billing_group(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "billing_group")

    @billing_group.setter
    def billing_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_group", value)

    @property
    @pulumi.getter(name="copyFromProject")
    def copy_from_project(self) -> Optional[pulumi.Input[str]]:
        """
        is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "copy_from_project")

    @copy_from_project.setter
    def copy_from_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "copy_from_project", value)

    @property
    @pulumi.getter(name="defaultCloud")
    def default_cloud(self) -> Optional[pulumi.Input[str]]:
        """
        Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        """
        return pulumi.get(self, "default_cloud")

    @default_cloud.setter
    def default_cloud(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_cloud", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]]:
        """
        Tags are key-value pairs that allow you to categorize projects.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="technicalEmails")
    def technical_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        """
        return pulumi.get(self, "technical_emails")

    @technical_emails.setter
    def technical_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "technical_emails", value)

    @property
    @pulumi.getter(name="useSourceProjectBillingGroup")
    def use_source_project_billing_group(self) -> Optional[pulumi.Input[bool]]:
        """
        Use the same billing group that is used in source project.
        """
        return pulumi.get(self, "use_source_project_billing_group")

    @use_source_project_billing_group.setter
    def use_source_project_billing_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_source_project_billing_group", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 add_account_owners_admin_access: Optional[pulumi.Input[bool]] = None,
                 available_credits: Optional[pulumi.Input[str]] = None,
                 billing_group: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 copy_from_project: Optional[pulumi.Input[str]] = None,
                 default_cloud: Optional[pulumi.Input[str]] = None,
                 estimated_balance: Optional[pulumi.Input[str]] = None,
                 payment_method: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]] = None,
                 technical_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_source_project_billing_group: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        :param pulumi.Input[str] account_id: An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[bool] add_account_owners_admin_access: If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        :param pulumi.Input[str] available_credits: The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        :param pulumi.Input[str] billing_group: The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] ca_cert: The CA certificate of the project. This is required for configuring clients that connect to certain services like Kafka.
        :param pulumi.Input[str] copy_from_project: is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] default_cloud: Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        :param pulumi.Input[str] estimated_balance: The current accumulated bill for this project in the current billing period.
        :param pulumi.Input[str] payment_method: The method of invoicing used for payments for this project, e.g. `card`.
        :param pulumi.Input[str] project: Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        :param pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]] tags: Tags are key-value pairs that allow you to categorize projects.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] technical_emails: Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        :param pulumi.Input[bool] use_source_project_billing_group: Use the same billing group that is used in source project.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if add_account_owners_admin_access is not None:
            pulumi.set(__self__, "add_account_owners_admin_access", add_account_owners_admin_access)
        if available_credits is not None:
            pulumi.set(__self__, "available_credits", available_credits)
        if billing_group is not None:
            pulumi.set(__self__, "billing_group", billing_group)
        if ca_cert is not None:
            pulumi.set(__self__, "ca_cert", ca_cert)
        if copy_from_project is not None:
            pulumi.set(__self__, "copy_from_project", copy_from_project)
        if default_cloud is not None:
            pulumi.set(__self__, "default_cloud", default_cloud)
        if estimated_balance is not None:
            pulumi.set(__self__, "estimated_balance", estimated_balance)
        if payment_method is not None:
            pulumi.set(__self__, "payment_method", payment_method)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if technical_emails is not None:
            pulumi.set(__self__, "technical_emails", technical_emails)
        if use_source_project_billing_group is not None:
            pulumi.set(__self__, "use_source_project_billing_group", use_source_project_billing_group)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="addAccountOwnersAdminAccess")
    def add_account_owners_admin_access(self) -> Optional[pulumi.Input[bool]]:
        """
        If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        """
        return pulumi.get(self, "add_account_owners_admin_access")

    @add_account_owners_admin_access.setter
    def add_account_owners_admin_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "add_account_owners_admin_access", value)

    @property
    @pulumi.getter(name="availableCredits")
    def available_credits(self) -> Optional[pulumi.Input[str]]:
        """
        The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        """
        return pulumi.get(self, "available_credits")

    @available_credits.setter
    def available_credits(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "available_credits", value)

    @property
    @pulumi.getter(name="billingGroup")
    def billing_group(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "billing_group")

    @billing_group.setter
    def billing_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_group", value)

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> Optional[pulumi.Input[str]]:
        """
        The CA certificate of the project. This is required for configuring clients that connect to certain services like Kafka.
        """
        return pulumi.get(self, "ca_cert")

    @ca_cert.setter
    def ca_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_cert", value)

    @property
    @pulumi.getter(name="copyFromProject")
    def copy_from_project(self) -> Optional[pulumi.Input[str]]:
        """
        is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "copy_from_project")

    @copy_from_project.setter
    def copy_from_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "copy_from_project", value)

    @property
    @pulumi.getter(name="defaultCloud")
    def default_cloud(self) -> Optional[pulumi.Input[str]]:
        """
        Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        """
        return pulumi.get(self, "default_cloud")

    @default_cloud.setter
    def default_cloud(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_cloud", value)

    @property
    @pulumi.getter(name="estimatedBalance")
    def estimated_balance(self) -> Optional[pulumi.Input[str]]:
        """
        The current accumulated bill for this project in the current billing period.
        """
        return pulumi.get(self, "estimated_balance")

    @estimated_balance.setter
    def estimated_balance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "estimated_balance", value)

    @property
    @pulumi.getter(name="paymentMethod")
    def payment_method(self) -> Optional[pulumi.Input[str]]:
        """
        The method of invoicing used for payments for this project, e.g. `card`.
        """
        return pulumi.get(self, "payment_method")

    @payment_method.setter
    def payment_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payment_method", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]]:
        """
        Tags are key-value pairs that allow you to categorize projects.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="technicalEmails")
    def technical_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        """
        return pulumi.get(self, "technical_emails")

    @technical_emails.setter
    def technical_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "technical_emails", value)

    @property
    @pulumi.getter(name="useSourceProjectBillingGroup")
    def use_source_project_billing_group(self) -> Optional[pulumi.Input[bool]]:
        """
        Use the same billing group that is used in source project.
        """
        return pulumi.get(self, "use_source_project_billing_group")

    @use_source_project_billing_group.setter
    def use_source_project_billing_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_source_project_billing_group", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 add_account_owners_admin_access: Optional[pulumi.Input[bool]] = None,
                 available_credits: Optional[pulumi.Input[str]] = None,
                 billing_group: Optional[pulumi.Input[str]] = None,
                 copy_from_project: Optional[pulumi.Input[str]] = None,
                 default_cloud: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]]] = None,
                 technical_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_source_project_billing_group: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The Project resource allows the creation and management of Aiven Projects.

        ## Import

        ```sh
         $ pulumi import aiven:index/project:Project myproject project
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[bool] add_account_owners_admin_access: If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        :param pulumi.Input[str] available_credits: The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        :param pulumi.Input[str] billing_group: The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] copy_from_project: is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] default_cloud: Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        :param pulumi.Input[str] project: Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]] tags: Tags are key-value pairs that allow you to categorize projects.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] technical_emails: Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        :param pulumi.Input[bool] use_source_project_billing_group: Use the same billing group that is used in source project.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Project resource allows the creation and management of Aiven Projects.

        ## Import

        ```sh
         $ pulumi import aiven:index/project:Project myproject project
        ```

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 add_account_owners_admin_access: Optional[pulumi.Input[bool]] = None,
                 available_credits: Optional[pulumi.Input[str]] = None,
                 billing_group: Optional[pulumi.Input[str]] = None,
                 copy_from_project: Optional[pulumi.Input[str]] = None,
                 default_cloud: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]]] = None,
                 technical_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_source_project_billing_group: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["add_account_owners_admin_access"] = add_account_owners_admin_access
            __props__.__dict__["available_credits"] = available_credits
            __props__.__dict__["billing_group"] = billing_group
            __props__.__dict__["copy_from_project"] = copy_from_project
            __props__.__dict__["default_cloud"] = default_cloud
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["tags"] = tags
            __props__.__dict__["technical_emails"] = technical_emails
            __props__.__dict__["use_source_project_billing_group"] = use_source_project_billing_group
            __props__.__dict__["ca_cert"] = None
            __props__.__dict__["estimated_balance"] = None
            __props__.__dict__["payment_method"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["caCert"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Project, __self__).__init__(
            'aiven:index/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            add_account_owners_admin_access: Optional[pulumi.Input[bool]] = None,
            available_credits: Optional[pulumi.Input[str]] = None,
            billing_group: Optional[pulumi.Input[str]] = None,
            ca_cert: Optional[pulumi.Input[str]] = None,
            copy_from_project: Optional[pulumi.Input[str]] = None,
            default_cloud: Optional[pulumi.Input[str]] = None,
            estimated_balance: Optional[pulumi.Input[str]] = None,
            payment_method: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]]] = None,
            technical_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            use_source_project_billing_group: Optional[pulumi.Input[bool]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[bool] add_account_owners_admin_access: If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        :param pulumi.Input[str] available_credits: The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        :param pulumi.Input[str] billing_group: The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] ca_cert: The CA certificate of the project. This is required for configuring clients that connect to certain services like Kafka.
        :param pulumi.Input[str] copy_from_project: is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        :param pulumi.Input[str] default_cloud: Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        :param pulumi.Input[str] estimated_balance: The current accumulated bill for this project in the current billing period.
        :param pulumi.Input[str] payment_method: The method of invoicing used for payments for this project, e.g. `card`.
        :param pulumi.Input[str] project: Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]] tags: Tags are key-value pairs that allow you to categorize projects.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] technical_emails: Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        :param pulumi.Input[bool] use_source_project_billing_group: Use the same billing group that is used in source project.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["add_account_owners_admin_access"] = add_account_owners_admin_access
        __props__.__dict__["available_credits"] = available_credits
        __props__.__dict__["billing_group"] = billing_group
        __props__.__dict__["ca_cert"] = ca_cert
        __props__.__dict__["copy_from_project"] = copy_from_project
        __props__.__dict__["default_cloud"] = default_cloud
        __props__.__dict__["estimated_balance"] = estimated_balance
        __props__.__dict__["payment_method"] = payment_method
        __props__.__dict__["project"] = project
        __props__.__dict__["tags"] = tags
        __props__.__dict__["technical_emails"] = technical_emails
        __props__.__dict__["use_source_project_billing_group"] = use_source_project_billing_group
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        An optional property to link a project to already an existing account by using account ID. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="addAccountOwnersAdminAccess")
    def add_account_owners_admin_access(self) -> pulumi.Output[Optional[bool]]:
        """
        If account_id is set, grant account owner team admin access to the new project. The default value is `true`.
        """
        return pulumi.get(self, "add_account_owners_admin_access")

    @property
    @pulumi.getter(name="availableCredits")
    def available_credits(self) -> pulumi.Output[str]:
        """
        The amount of platform credits available to the project. This could be your free trial or other promotional credits.
        """
        return pulumi.get(self, "available_credits")

    @property
    @pulumi.getter(name="billingGroup")
    def billing_group(self) -> pulumi.Output[Optional[str]]:
        """
        The id of the billing group that is linked to this project. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "billing_group")

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> pulumi.Output[str]:
        """
        The CA certificate of the project. This is required for configuring clients that connect to certain services like Kafka.
        """
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter(name="copyFromProject")
    def copy_from_project(self) -> pulumi.Output[Optional[str]]:
        """
        is the name of another project used to copy billing information and some other project attributes like technical contacts from. This is mostly relevant when an existing project has billing type set to invoice and that needs to be copied over to a new project. (Setting billing is otherwise not allowed over the API.) This only has effect when the project is created. To set up proper dependencies please refer to this variable as a reference.
        """
        return pulumi.get(self, "copy_from_project")

    @property
    @pulumi.getter(name="defaultCloud")
    def default_cloud(self) -> pulumi.Output[Optional[str]]:
        """
        Defines the default cloud provider and region where services are hosted. This can be changed freely after the project is created. This will not affect existing services.
        """
        return pulumi.get(self, "default_cloud")

    @property
    @pulumi.getter(name="estimatedBalance")
    def estimated_balance(self) -> pulumi.Output[str]:
        """
        The current accumulated bill for this project in the current billing period.
        """
        return pulumi.get(self, "estimated_balance")

    @property
    @pulumi.getter(name="paymentMethod")
    def payment_method(self) -> pulumi.Output[str]:
        """
        The method of invoicing used for payments for this project, e.g. `card`.
        """
        return pulumi.get(self, "payment_method")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        Defines the name of the project. Name must be globally unique (between all Aiven customers) and cannot be changed later without destroying and re-creating the project, including all sub-resources.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ProjectTag']]]:
        """
        Tags are key-value pairs that allow you to categorize projects.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="technicalEmails")
    def technical_emails(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Defines the email addresses that will receive alerts about upcoming maintenance updates or warnings about service instability. It is  good practice to keep this up-to-date to be aware of any potential issues with your project.
        """
        return pulumi.get(self, "technical_emails")

    @property
    @pulumi.getter(name="useSourceProjectBillingGroup")
    def use_source_project_billing_group(self) -> pulumi.Output[Optional[bool]]:
        """
        Use the same billing group that is used in source project.
        """
        return pulumi.get(self, "use_source_project_billing_group")

