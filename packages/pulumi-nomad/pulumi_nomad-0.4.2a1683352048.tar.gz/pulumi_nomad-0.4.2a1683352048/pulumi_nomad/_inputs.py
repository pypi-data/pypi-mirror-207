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
    'AclAuthMethodConfigArgs',
    'AclRolePolicyArgs',
    'AclTokenRoleArgs',
    'ExternalVolumeCapabilityArgs',
    'ExternalVolumeMountOptionsArgs',
    'ExternalVolumeTopologyArgs',
    'ExternalVolumeTopologyRequestArgs',
    'ExternalVolumeTopologyRequestPreferredArgs',
    'ExternalVolumeTopologyRequestPreferredTopologyArgs',
    'ExternalVolumeTopologyRequestRequiredArgs',
    'ExternalVolumeTopologyRequestRequiredTopologyArgs',
    'JobHcl2Args',
    'JobTaskGroupArgs',
    'JobTaskGroupTaskArgs',
    'JobTaskGroupTaskVolumeMountArgs',
    'JobTaskGroupVolumeArgs',
    'NamespaceCapabilitiesArgs',
    'ProviderHeaderArgs',
    'QuoteSpecificationLimitArgs',
    'QuoteSpecificationLimitRegionLimitArgs',
    'VolumeCapabilityArgs',
    'VolumeMountOptionsArgs',
    'VolumeTopologyArgs',
    'VolumeTopologyRequestArgs',
    'VolumeTopologyRequestRequiredArgs',
    'VolumeTopologyRequestRequiredTopologyArgs',
]

@pulumi.input_type
class AclAuthMethodConfigArgs:
    def __init__(__self__, *,
                 allowed_redirect_uris: pulumi.Input[Sequence[pulumi.Input[str]]],
                 oidc_client_id: pulumi.Input[str],
                 oidc_client_secret: pulumi.Input[str],
                 oidc_discovery_url: pulumi.Input[str],
                 bound_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 claim_mappings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 discovery_ca_pems: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 list_claim_mappings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 oidc_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 signing_algs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "allowed_redirect_uris", allowed_redirect_uris)
        pulumi.set(__self__, "oidc_client_id", oidc_client_id)
        pulumi.set(__self__, "oidc_client_secret", oidc_client_secret)
        pulumi.set(__self__, "oidc_discovery_url", oidc_discovery_url)
        if bound_audiences is not None:
            pulumi.set(__self__, "bound_audiences", bound_audiences)
        if claim_mappings is not None:
            pulumi.set(__self__, "claim_mappings", claim_mappings)
        if discovery_ca_pems is not None:
            pulumi.set(__self__, "discovery_ca_pems", discovery_ca_pems)
        if list_claim_mappings is not None:
            pulumi.set(__self__, "list_claim_mappings", list_claim_mappings)
        if oidc_scopes is not None:
            pulumi.set(__self__, "oidc_scopes", oidc_scopes)
        if signing_algs is not None:
            pulumi.set(__self__, "signing_algs", signing_algs)

    @property
    @pulumi.getter(name="allowedRedirectUris")
    def allowed_redirect_uris(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "allowed_redirect_uris")

    @allowed_redirect_uris.setter
    def allowed_redirect_uris(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_redirect_uris", value)

    @property
    @pulumi.getter(name="oidcClientId")
    def oidc_client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "oidc_client_id")

    @oidc_client_id.setter
    def oidc_client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_client_id", value)

    @property
    @pulumi.getter(name="oidcClientSecret")
    def oidc_client_secret(self) -> pulumi.Input[str]:
        return pulumi.get(self, "oidc_client_secret")

    @oidc_client_secret.setter
    def oidc_client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_client_secret", value)

    @property
    @pulumi.getter(name="oidcDiscoveryUrl")
    def oidc_discovery_url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "oidc_discovery_url")

    @oidc_discovery_url.setter
    def oidc_discovery_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "oidc_discovery_url", value)

    @property
    @pulumi.getter(name="boundAudiences")
    def bound_audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "bound_audiences")

    @bound_audiences.setter
    def bound_audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "bound_audiences", value)

    @property
    @pulumi.getter(name="claimMappings")
    def claim_mappings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "claim_mappings")

    @claim_mappings.setter
    def claim_mappings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "claim_mappings", value)

    @property
    @pulumi.getter(name="discoveryCaPems")
    def discovery_ca_pems(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "discovery_ca_pems")

    @discovery_ca_pems.setter
    def discovery_ca_pems(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "discovery_ca_pems", value)

    @property
    @pulumi.getter(name="listClaimMappings")
    def list_claim_mappings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "list_claim_mappings")

    @list_claim_mappings.setter
    def list_claim_mappings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "list_claim_mappings", value)

    @property
    @pulumi.getter(name="oidcScopes")
    def oidc_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "oidc_scopes")

    @oidc_scopes.setter
    def oidc_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "oidc_scopes", value)

    @property
    @pulumi.getter(name="signingAlgs")
    def signing_algs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "signing_algs")

    @signing_algs.setter
    def signing_algs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "signing_algs", value)


@pulumi.input_type
class AclRolePolicyArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: `(string: <required>)` - A human-friendly name for this ACL Role.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - A human-friendly name for this ACL Role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class AclTokenRoleArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: `(string: "")` - A human-friendly name for this token.
        """
        pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: "")` - A human-friendly name for this token.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ExternalVolumeCapabilityArgs:
    def __init__(__self__, *,
                 access_mode: pulumi.Input[str],
                 attachment_mode: pulumi.Input[str]):
        """
        :param pulumi.Input[str] access_mode: `(string: <required>)` - Defines whether a volume should be available concurrently. Possible values are:
               - `single-node-reader-only`
               - `single-node-writer`
               - `multi-node-reader-only`
               - `multi-node-single-writer`
               - `multi-node-multi-writer`
        :param pulumi.Input[str] attachment_mode: `(string: <required>)` - The storage API that will be used by the volume. Possible values are:
               - `block-device`
               - `file-system`
        """
        pulumi.set(__self__, "access_mode", access_mode)
        pulumi.set(__self__, "attachment_mode", attachment_mode)

    @property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - Defines whether a volume should be available concurrently. Possible values are:
        - `single-node-reader-only`
        - `single-node-writer`
        - `multi-node-reader-only`
        - `multi-node-single-writer`
        - `multi-node-multi-writer`
        """
        return pulumi.get(self, "access_mode")

    @access_mode.setter
    def access_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_mode", value)

    @property
    @pulumi.getter(name="attachmentMode")
    def attachment_mode(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - The storage API that will be used by the volume. Possible values are:
        - `block-device`
        - `file-system`
        """
        return pulumi.get(self, "attachment_mode")

    @attachment_mode.setter
    def attachment_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "attachment_mode", value)


@pulumi.input_type
class ExternalVolumeMountOptionsArgs:
    def __init__(__self__, *,
                 fs_type: Optional[pulumi.Input[str]] = None,
                 mount_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] fs_type: `(string: optional)` - The file system type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mount_flags: `[]string: optional` - The flags passed to `mount`.
        """
        if fs_type is not None:
            pulumi.set(__self__, "fs_type", fs_type)
        if mount_flags is not None:
            pulumi.set(__self__, "mount_flags", mount_flags)

    @property
    @pulumi.getter(name="fsType")
    def fs_type(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: optional)` - The file system type.
        """
        return pulumi.get(self, "fs_type")

    @fs_type.setter
    def fs_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fs_type", value)

    @property
    @pulumi.getter(name="mountFlags")
    def mount_flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        `[]string: optional` - The flags passed to `mount`.
        """
        return pulumi.get(self, "mount_flags")

    @mount_flags.setter
    def mount_flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "mount_flags", value)


@pulumi.input_type
class ExternalVolumeTopologyArgs:
    def __init__(__self__, *,
                 segments: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] segments: `(map[string]string)` - Define the attributes for the topology request.
        """
        if segments is not None:
            pulumi.set(__self__, "segments", segments)

    @property
    @pulumi.getter
    def segments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        `(map[string]string)` - Define the attributes for the topology request.
        """
        return pulumi.get(self, "segments")

    @segments.setter
    def segments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "segments", value)


@pulumi.input_type
class ExternalVolumeTopologyRequestArgs:
    def __init__(__self__, *,
                 preferred: Optional[pulumi.Input['ExternalVolumeTopologyRequestPreferredArgs']] = None,
                 required: Optional[pulumi.Input['ExternalVolumeTopologyRequestRequiredArgs']] = None):
        """
        :param pulumi.Input['ExternalVolumeTopologyRequestPreferredArgs'] preferred: `(``Topology``: <optional>)` - Preferred topologies indicate that the volume should be created in a location accessible from some of the listed topologies.
        :param pulumi.Input['ExternalVolumeTopologyRequestRequiredArgs'] required: `(``Topology``: <optional>)` - Required topologies indicate that the volume must be created in a location accessible from all the listed topologies.
        """
        if preferred is not None:
            pulumi.set(__self__, "preferred", preferred)
        if required is not None:
            pulumi.set(__self__, "required", required)

    @property
    @pulumi.getter
    def preferred(self) -> Optional[pulumi.Input['ExternalVolumeTopologyRequestPreferredArgs']]:
        """
        `(``Topology``: <optional>)` - Preferred topologies indicate that the volume should be created in a location accessible from some of the listed topologies.
        """
        return pulumi.get(self, "preferred")

    @preferred.setter
    def preferred(self, value: Optional[pulumi.Input['ExternalVolumeTopologyRequestPreferredArgs']]):
        pulumi.set(self, "preferred", value)

    @property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input['ExternalVolumeTopologyRequestRequiredArgs']]:
        """
        `(``Topology``: <optional>)` - Required topologies indicate that the volume must be created in a location accessible from all the listed topologies.
        """
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: Optional[pulumi.Input['ExternalVolumeTopologyRequestRequiredArgs']]):
        pulumi.set(self, "required", value)


@pulumi.input_type
class ExternalVolumeTopologyRequestPreferredArgs:
    def __init__(__self__, *,
                 topologies: pulumi.Input[Sequence[pulumi.Input['ExternalVolumeTopologyRequestPreferredTopologyArgs']]]):
        pulumi.set(__self__, "topologies", topologies)

    @property
    @pulumi.getter
    def topologies(self) -> pulumi.Input[Sequence[pulumi.Input['ExternalVolumeTopologyRequestPreferredTopologyArgs']]]:
        return pulumi.get(self, "topologies")

    @topologies.setter
    def topologies(self, value: pulumi.Input[Sequence[pulumi.Input['ExternalVolumeTopologyRequestPreferredTopologyArgs']]]):
        pulumi.set(self, "topologies", value)


@pulumi.input_type
class ExternalVolumeTopologyRequestPreferredTopologyArgs:
    def __init__(__self__, *,
                 segments: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] segments: `(map[string]string)` - Define the attributes for the topology request.
        """
        pulumi.set(__self__, "segments", segments)

    @property
    @pulumi.getter
    def segments(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        `(map[string]string)` - Define the attributes for the topology request.
        """
        return pulumi.get(self, "segments")

    @segments.setter
    def segments(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "segments", value)


@pulumi.input_type
class ExternalVolumeTopologyRequestRequiredArgs:
    def __init__(__self__, *,
                 topologies: pulumi.Input[Sequence[pulumi.Input['ExternalVolumeTopologyRequestRequiredTopologyArgs']]]):
        pulumi.set(__self__, "topologies", topologies)

    @property
    @pulumi.getter
    def topologies(self) -> pulumi.Input[Sequence[pulumi.Input['ExternalVolumeTopologyRequestRequiredTopologyArgs']]]:
        return pulumi.get(self, "topologies")

    @topologies.setter
    def topologies(self, value: pulumi.Input[Sequence[pulumi.Input['ExternalVolumeTopologyRequestRequiredTopologyArgs']]]):
        pulumi.set(self, "topologies", value)


@pulumi.input_type
class ExternalVolumeTopologyRequestRequiredTopologyArgs:
    def __init__(__self__, *,
                 segments: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] segments: `(map[string]string)` - Define the attributes for the topology request.
        """
        pulumi.set(__self__, "segments", segments)

    @property
    @pulumi.getter
    def segments(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        `(map[string]string)` - Define the attributes for the topology request.
        """
        return pulumi.get(self, "segments")

    @segments.setter
    def segments(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "segments", value)


@pulumi.input_type
class JobHcl2Args:
    def __init__(__self__, *,
                 allow_fs: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 vars: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        :param pulumi.Input[bool] allow_fs: `(boolean: false)` - Set this to `true` to be able to use
               HCL2 filesystem functions
        :param pulumi.Input[bool] enabled: `(boolean: false)` - Set this to `true` if your jobspec uses the HCL2
               format instead of the default HCL.
        """
        if allow_fs is not None:
            pulumi.set(__self__, "allow_fs", allow_fs)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if vars is not None:
            pulumi.set(__self__, "vars", vars)

    @property
    @pulumi.getter(name="allowFs")
    def allow_fs(self) -> Optional[pulumi.Input[bool]]:
        """
        `(boolean: false)` - Set this to `true` to be able to use
        HCL2 filesystem functions
        """
        return pulumi.get(self, "allow_fs")

    @allow_fs.setter
    def allow_fs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_fs", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        `(boolean: false)` - Set this to `true` if your jobspec uses the HCL2
        format instead of the default HCL.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def vars(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "vars")

    @vars.setter
    def vars(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "vars", value)


@pulumi.input_type
class JobTaskGroupArgs:
    def __init__(__self__, *,
                 count: Optional[pulumi.Input[int]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tasks: Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupTaskArgs']]]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupVolumeArgs']]]] = None):
        if count is not None:
            pulumi.set(__self__, "count", count)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tasks is not None:
            pulumi.set(__self__, "tasks", tasks)
        if volumes is not None:
            pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter
    def meta(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "meta")

    @meta.setter
    def meta(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "meta", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tasks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupTaskArgs']]]]:
        return pulumi.get(self, "tasks")

    @tasks.setter
    def tasks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupTaskArgs']]]]):
        pulumi.set(self, "tasks", value)

    @property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupVolumeArgs']]]]:
        return pulumi.get(self, "volumes")

    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupVolumeArgs']]]]):
        pulumi.set(self, "volumes", value)


@pulumi.input_type
class JobTaskGroupTaskArgs:
    def __init__(__self__, *,
                 driver: Optional[pulumi.Input[str]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupTaskVolumeMountArgs']]]] = None):
        if driver is not None:
            pulumi.set(__self__, "driver", driver)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if volume_mounts is not None:
            pulumi.set(__self__, "volume_mounts", volume_mounts)

    @property
    @pulumi.getter
    def driver(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "driver")

    @driver.setter
    def driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "driver", value)

    @property
    @pulumi.getter
    def meta(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "meta")

    @meta.setter
    def meta(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "meta", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupTaskVolumeMountArgs']]]]:
        return pulumi.get(self, "volume_mounts")

    @volume_mounts.setter
    def volume_mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JobTaskGroupTaskVolumeMountArgs']]]]):
        pulumi.set(self, "volume_mounts", value)


@pulumi.input_type
class JobTaskGroupTaskVolumeMountArgs:
    def __init__(__self__, *,
                 destination: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 volume: Optional[pulumi.Input[str]] = None):
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if volume is not None:
            pulumi.set(__self__, "volume", volume)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "read_only")

    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "read_only", value)

    @property
    @pulumi.getter
    def volume(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume")

    @volume.setter
    def volume(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume", value)


@pulumi.input_type
class JobTaskGroupVolumeArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if name is not None:
            pulumi.set(__self__, "name", name)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "read_only")

    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "read_only", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class NamespaceCapabilitiesArgs:
    def __init__(__self__, *,
                 disabled_task_drivers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled_task_drivers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_task_drivers: `([]string: <optional>)` - Task drivers disabled for the namespace.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_task_drivers: `([]string: <optional>)` - Task drivers enabled for the namespace.
        """
        if disabled_task_drivers is not None:
            pulumi.set(__self__, "disabled_task_drivers", disabled_task_drivers)
        if enabled_task_drivers is not None:
            pulumi.set(__self__, "enabled_task_drivers", enabled_task_drivers)

    @property
    @pulumi.getter(name="disabledTaskDrivers")
    def disabled_task_drivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        `([]string: <optional>)` - Task drivers disabled for the namespace.
        """
        return pulumi.get(self, "disabled_task_drivers")

    @disabled_task_drivers.setter
    def disabled_task_drivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disabled_task_drivers", value)

    @property
    @pulumi.getter(name="enabledTaskDrivers")
    def enabled_task_drivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        `([]string: <optional>)` - Task drivers enabled for the namespace.
        """
        return pulumi.get(self, "enabled_task_drivers")

    @enabled_task_drivers.setter
    def enabled_task_drivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_task_drivers", value)


@pulumi.input_type
class ProviderHeaderArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class QuoteSpecificationLimitArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 region_limit: pulumi.Input['QuoteSpecificationLimitRegionLimitArgs']):
        """
        :param pulumi.Input[str] region: `(string: <required>)` - The region these limits should apply to.
        :param pulumi.Input['QuoteSpecificationLimitRegionLimitArgs'] region_limit: `(block: <required>)` - The limits to enforce. This block
               may only be specified once in the `limits` block. Its structure is
               documented below.
        """
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "region_limit", region_limit)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - The region these limits should apply to.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="regionLimit")
    def region_limit(self) -> pulumi.Input['QuoteSpecificationLimitRegionLimitArgs']:
        """
        `(block: <required>)` - The limits to enforce. This block
        may only be specified once in the `limits` block. Its structure is
        documented below.
        """
        return pulumi.get(self, "region_limit")

    @region_limit.setter
    def region_limit(self, value: pulumi.Input['QuoteSpecificationLimitRegionLimitArgs']):
        pulumi.set(self, "region_limit", value)


@pulumi.input_type
class QuoteSpecificationLimitRegionLimitArgs:
    def __init__(__self__, *,
                 cpu: Optional[pulumi.Input[int]] = None,
                 memory_mb: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] cpu: `(int: 0)` - The amount of CPU to limit allocations to. A value of zero
               is treated as unlimited, and a negative value is treated as fully disallowed.
        :param pulumi.Input[int] memory_mb: `(int: 0)` - The amount of memory (in megabytes) to limit
               allocations to. A value of zero is treated as unlimited, and a negative value
               is treated as fully disallowed.
        """
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if memory_mb is not None:
            pulumi.set(__self__, "memory_mb", memory_mb)

    @property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[int]]:
        """
        `(int: 0)` - The amount of CPU to limit allocations to. A value of zero
        is treated as unlimited, and a negative value is treated as fully disallowed.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter(name="memoryMb")
    def memory_mb(self) -> Optional[pulumi.Input[int]]:
        """
        `(int: 0)` - The amount of memory (in megabytes) to limit
        allocations to. A value of zero is treated as unlimited, and a negative value
        is treated as fully disallowed.
        """
        return pulumi.get(self, "memory_mb")

    @memory_mb.setter
    def memory_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memory_mb", value)


@pulumi.input_type
class VolumeCapabilityArgs:
    def __init__(__self__, *,
                 access_mode: pulumi.Input[str],
                 attachment_mode: pulumi.Input[str]):
        """
        :param pulumi.Input[str] access_mode: `(string: <required>)` - Defines whether a volume should be available concurrently. Possible values are:
               - `single-node-reader-only`
               - `single-node-writer`
               - `multi-node-reader-only`
               - `multi-node-single-writer`
               - `multi-node-multi-writer`
        :param pulumi.Input[str] attachment_mode: `(string: <required>)` - The storage API that will be used by the volume. Possible values are:
               - `block-device`
               - `file-system`
        """
        pulumi.set(__self__, "access_mode", access_mode)
        pulumi.set(__self__, "attachment_mode", attachment_mode)

    @property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - Defines whether a volume should be available concurrently. Possible values are:
        - `single-node-reader-only`
        - `single-node-writer`
        - `multi-node-reader-only`
        - `multi-node-single-writer`
        - `multi-node-multi-writer`
        """
        return pulumi.get(self, "access_mode")

    @access_mode.setter
    def access_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_mode", value)

    @property
    @pulumi.getter(name="attachmentMode")
    def attachment_mode(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - The storage API that will be used by the volume. Possible values are:
        - `block-device`
        - `file-system`
        """
        return pulumi.get(self, "attachment_mode")

    @attachment_mode.setter
    def attachment_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "attachment_mode", value)


@pulumi.input_type
class VolumeMountOptionsArgs:
    def __init__(__self__, *,
                 fs_type: Optional[pulumi.Input[str]] = None,
                 mount_flags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] fs_type: `(string: <optional>)` - The file system type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mount_flags: `([]string: <optional>)` - The flags passed to `mount`.
        """
        if fs_type is not None:
            pulumi.set(__self__, "fs_type", fs_type)
        if mount_flags is not None:
            pulumi.set(__self__, "mount_flags", mount_flags)

    @property
    @pulumi.getter(name="fsType")
    def fs_type(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: <optional>)` - The file system type.
        """
        return pulumi.get(self, "fs_type")

    @fs_type.setter
    def fs_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fs_type", value)

    @property
    @pulumi.getter(name="mountFlags")
    def mount_flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        `([]string: <optional>)` - The flags passed to `mount`.
        """
        return pulumi.get(self, "mount_flags")

    @mount_flags.setter
    def mount_flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "mount_flags", value)


@pulumi.input_type
class VolumeTopologyArgs:
    def __init__(__self__, *,
                 segments: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] segments: `(map[string]string)` - Define the attributes for the topology request.
        """
        if segments is not None:
            pulumi.set(__self__, "segments", segments)

    @property
    @pulumi.getter
    def segments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        `(map[string]string)` - Define the attributes for the topology request.
        """
        return pulumi.get(self, "segments")

    @segments.setter
    def segments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "segments", value)


@pulumi.input_type
class VolumeTopologyRequestArgs:
    def __init__(__self__, *,
                 required: Optional[pulumi.Input['VolumeTopologyRequestRequiredArgs']] = None):
        """
        :param pulumi.Input['VolumeTopologyRequestRequiredArgs'] required: `(``Topology``: <optional>)` - Required topologies indicate that the volume must be created in a location accessible from all the listed topologies.
        """
        if required is not None:
            pulumi.set(__self__, "required", required)

    @property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input['VolumeTopologyRequestRequiredArgs']]:
        """
        `(``Topology``: <optional>)` - Required topologies indicate that the volume must be created in a location accessible from all the listed topologies.
        """
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: Optional[pulumi.Input['VolumeTopologyRequestRequiredArgs']]):
        pulumi.set(self, "required", value)


@pulumi.input_type
class VolumeTopologyRequestRequiredArgs:
    def __init__(__self__, *,
                 topologies: pulumi.Input[Sequence[pulumi.Input['VolumeTopologyRequestRequiredTopologyArgs']]]):
        pulumi.set(__self__, "topologies", topologies)

    @property
    @pulumi.getter
    def topologies(self) -> pulumi.Input[Sequence[pulumi.Input['VolumeTopologyRequestRequiredTopologyArgs']]]:
        return pulumi.get(self, "topologies")

    @topologies.setter
    def topologies(self, value: pulumi.Input[Sequence[pulumi.Input['VolumeTopologyRequestRequiredTopologyArgs']]]):
        pulumi.set(self, "topologies", value)


@pulumi.input_type
class VolumeTopologyRequestRequiredTopologyArgs:
    def __init__(__self__, *,
                 segments: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] segments: `(map[string]string)` - Define the attributes for the topology request.
        """
        pulumi.set(__self__, "segments", segments)

    @property
    @pulumi.getter
    def segments(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        `(map[string]string)` - Define the attributes for the topology request.
        """
        return pulumi.get(self, "segments")

    @segments.setter
    def segments(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "segments", value)


