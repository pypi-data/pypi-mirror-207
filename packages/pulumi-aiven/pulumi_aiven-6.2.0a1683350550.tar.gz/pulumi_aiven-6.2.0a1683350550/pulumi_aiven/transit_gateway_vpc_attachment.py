# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TransitGatewayVpcAttachmentArgs', 'TransitGatewayVpcAttachment']

@pulumi.input_type
class TransitGatewayVpcAttachmentArgs:
    def __init__(__self__, *,
                 peer_cloud_account: pulumi.Input[str],
                 peer_region: pulumi.Input[str],
                 peer_vpc: pulumi.Input[str],
                 user_peer_network_cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a TransitGatewayVpcAttachment resource.
        :param pulumi.Input[str] peer_cloud_account: AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] peer_region: AWS region of the peered VPC (if not in the same region as Aiven VPC)
        :param pulumi.Input[str] peer_vpc: Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_peer_network_cidrs: List of private IPv4 ranges to route through the peering connection
        :param pulumi.Input[str] vpc_id: The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        pulumi.set(__self__, "peer_cloud_account", peer_cloud_account)
        pulumi.set(__self__, "peer_region", peer_region)
        pulumi.set(__self__, "peer_vpc", peer_vpc)
        pulumi.set(__self__, "user_peer_network_cidrs", user_peer_network_cidrs)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="peerCloudAccount")
    def peer_cloud_account(self) -> pulumi.Input[str]:
        """
        AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "peer_cloud_account")

    @peer_cloud_account.setter
    def peer_cloud_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_cloud_account", value)

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> pulumi.Input[str]:
        """
        AWS region of the peered VPC (if not in the same region as Aiven VPC)
        """
        return pulumi.get(self, "peer_region")

    @peer_region.setter
    def peer_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_region", value)

    @property
    @pulumi.getter(name="peerVpc")
    def peer_vpc(self) -> pulumi.Input[str]:
        """
        Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "peer_vpc")

    @peer_vpc.setter
    def peer_vpc(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_vpc", value)

    @property
    @pulumi.getter(name="userPeerNetworkCidrs")
    def user_peer_network_cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of private IPv4 ranges to route through the peering connection
        """
        return pulumi.get(self, "user_peer_network_cidrs")

    @user_peer_network_cidrs.setter
    def user_peer_network_cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "user_peer_network_cidrs", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)


@pulumi.input_type
class _TransitGatewayVpcAttachmentState:
    def __init__(__self__, *,
                 peer_cloud_account: Optional[pulumi.Input[str]] = None,
                 peer_region: Optional[pulumi.Input[str]] = None,
                 peer_vpc: Optional[pulumi.Input[str]] = None,
                 peering_connection_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 state_info: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 user_peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TransitGatewayVpcAttachment resources.
        :param pulumi.Input[str] peer_cloud_account: AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] peer_region: AWS region of the peered VPC (if not in the same region as Aiven VPC)
        :param pulumi.Input[str] peer_vpc: Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] peering_connection_id: Cloud provider identifier for the peering connection if available
        :param pulumi.Input[str] state: State of the peering connection
        :param pulumi.Input[Mapping[str, Any]] state_info: State-specific help or error information
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_peer_network_cidrs: List of private IPv4 ranges to route through the peering connection
        :param pulumi.Input[str] vpc_id: The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        if peer_cloud_account is not None:
            pulumi.set(__self__, "peer_cloud_account", peer_cloud_account)
        if peer_region is not None:
            pulumi.set(__self__, "peer_region", peer_region)
        if peer_vpc is not None:
            pulumi.set(__self__, "peer_vpc", peer_vpc)
        if peering_connection_id is not None:
            pulumi.set(__self__, "peering_connection_id", peering_connection_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if state_info is not None:
            pulumi.set(__self__, "state_info", state_info)
        if user_peer_network_cidrs is not None:
            pulumi.set(__self__, "user_peer_network_cidrs", user_peer_network_cidrs)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="peerCloudAccount")
    def peer_cloud_account(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "peer_cloud_account")

    @peer_cloud_account.setter
    def peer_cloud_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_cloud_account", value)

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> Optional[pulumi.Input[str]]:
        """
        AWS region of the peered VPC (if not in the same region as Aiven VPC)
        """
        return pulumi.get(self, "peer_region")

    @peer_region.setter
    def peer_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_region", value)

    @property
    @pulumi.getter(name="peerVpc")
    def peer_vpc(self) -> Optional[pulumi.Input[str]]:
        """
        Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "peer_vpc")

    @peer_vpc.setter
    def peer_vpc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_vpc", value)

    @property
    @pulumi.getter(name="peeringConnectionId")
    def peering_connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud provider identifier for the peering connection if available
        """
        return pulumi.get(self, "peering_connection_id")

    @peering_connection_id.setter
    def peering_connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_connection_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the peering connection
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="stateInfo")
    def state_info(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        State-specific help or error information
        """
        return pulumi.get(self, "state_info")

    @state_info.setter
    def state_info(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "state_info", value)

    @property
    @pulumi.getter(name="userPeerNetworkCidrs")
    def user_peer_network_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of private IPv4 ranges to route through the peering connection
        """
        return pulumi.get(self, "user_peer_network_cidrs")

    @user_peer_network_cidrs.setter
    def user_peer_network_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_peer_network_cidrs", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class TransitGatewayVpcAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 peer_cloud_account: Optional[pulumi.Input[str]] = None,
                 peer_region: Optional[pulumi.Input[str]] = None,
                 peer_vpc: Optional[pulumi.Input[str]] = None,
                 user_peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Transit Gateway VPC Attachment resource allows the creation and management Transit Gateway VPC Attachment VPC peering connection between Aiven and AWS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        attachment = aiven.TransitGatewayVpcAttachment("attachment",
            vpc_id=aiven_project_vpc["bar"]["id"],
            peer_cloud_account="<PEER_ACCOUNT_ID>",
            peer_vpc="google-project1",
            peer_region="aws-eu-west-1",
            user_peer_network_cidrs=["10.0.0.0/24"])
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/transitGatewayVpcAttachment:TransitGatewayVpcAttachment attachment project/vpc_id/peer_cloud_account/peer_vpc/peer_region
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] peer_cloud_account: AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] peer_region: AWS region of the peered VPC (if not in the same region as Aiven VPC)
        :param pulumi.Input[str] peer_vpc: Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_peer_network_cidrs: List of private IPv4 ranges to route through the peering connection
        :param pulumi.Input[str] vpc_id: The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitGatewayVpcAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Transit Gateway VPC Attachment resource allows the creation and management Transit Gateway VPC Attachment VPC peering connection between Aiven and AWS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        attachment = aiven.TransitGatewayVpcAttachment("attachment",
            vpc_id=aiven_project_vpc["bar"]["id"],
            peer_cloud_account="<PEER_ACCOUNT_ID>",
            peer_vpc="google-project1",
            peer_region="aws-eu-west-1",
            user_peer_network_cidrs=["10.0.0.0/24"])
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/transitGatewayVpcAttachment:TransitGatewayVpcAttachment attachment project/vpc_id/peer_cloud_account/peer_vpc/peer_region
        ```

        :param str resource_name: The name of the resource.
        :param TransitGatewayVpcAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitGatewayVpcAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 peer_cloud_account: Optional[pulumi.Input[str]] = None,
                 peer_region: Optional[pulumi.Input[str]] = None,
                 peer_vpc: Optional[pulumi.Input[str]] = None,
                 user_peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransitGatewayVpcAttachmentArgs.__new__(TransitGatewayVpcAttachmentArgs)

            if peer_cloud_account is None and not opts.urn:
                raise TypeError("Missing required property 'peer_cloud_account'")
            __props__.__dict__["peer_cloud_account"] = peer_cloud_account
            if peer_region is None and not opts.urn:
                raise TypeError("Missing required property 'peer_region'")
            __props__.__dict__["peer_region"] = peer_region
            if peer_vpc is None and not opts.urn:
                raise TypeError("Missing required property 'peer_vpc'")
            __props__.__dict__["peer_vpc"] = peer_vpc
            if user_peer_network_cidrs is None and not opts.urn:
                raise TypeError("Missing required property 'user_peer_network_cidrs'")
            __props__.__dict__["user_peer_network_cidrs"] = user_peer_network_cidrs
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["peering_connection_id"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["state_info"] = None
        super(TransitGatewayVpcAttachment, __self__).__init__(
            'aiven:index/transitGatewayVpcAttachment:TransitGatewayVpcAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            peer_cloud_account: Optional[pulumi.Input[str]] = None,
            peer_region: Optional[pulumi.Input[str]] = None,
            peer_vpc: Optional[pulumi.Input[str]] = None,
            peering_connection_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            state_info: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            user_peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'TransitGatewayVpcAttachment':
        """
        Get an existing TransitGatewayVpcAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] peer_cloud_account: AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] peer_region: AWS region of the peered VPC (if not in the same region as Aiven VPC)
        :param pulumi.Input[str] peer_vpc: Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] peering_connection_id: Cloud provider identifier for the peering connection if available
        :param pulumi.Input[str] state: State of the peering connection
        :param pulumi.Input[Mapping[str, Any]] state_info: State-specific help or error information
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_peer_network_cidrs: List of private IPv4 ranges to route through the peering connection
        :param pulumi.Input[str] vpc_id: The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TransitGatewayVpcAttachmentState.__new__(_TransitGatewayVpcAttachmentState)

        __props__.__dict__["peer_cloud_account"] = peer_cloud_account
        __props__.__dict__["peer_region"] = peer_region
        __props__.__dict__["peer_vpc"] = peer_vpc
        __props__.__dict__["peering_connection_id"] = peering_connection_id
        __props__.__dict__["state"] = state
        __props__.__dict__["state_info"] = state_info
        __props__.__dict__["user_peer_network_cidrs"] = user_peer_network_cidrs
        __props__.__dict__["vpc_id"] = vpc_id
        return TransitGatewayVpcAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="peerCloudAccount")
    def peer_cloud_account(self) -> pulumi.Output[str]:
        """
        AWS account ID or GCP project ID of the peered VPC. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "peer_cloud_account")

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> pulumi.Output[str]:
        """
        AWS region of the peered VPC (if not in the same region as Aiven VPC)
        """
        return pulumi.get(self, "peer_region")

    @property
    @pulumi.getter(name="peerVpc")
    def peer_vpc(self) -> pulumi.Output[str]:
        """
        Transit gateway ID. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "peer_vpc")

    @property
    @pulumi.getter(name="peeringConnectionId")
    def peering_connection_id(self) -> pulumi.Output[str]:
        """
        Cloud provider identifier for the peering connection if available
        """
        return pulumi.get(self, "peering_connection_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the peering connection
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateInfo")
    def state_info(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        State-specific help or error information
        """
        return pulumi.get(self, "state_info")

    @property
    @pulumi.getter(name="userPeerNetworkCidrs")
    def user_peer_network_cidrs(self) -> pulumi.Output[Sequence[str]]:
        """
        List of private IPv4 ranges to route through the peering connection
        """
        return pulumi.get(self, "user_peer_network_cidrs")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The VPC the peering connection belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "vpc_id")

