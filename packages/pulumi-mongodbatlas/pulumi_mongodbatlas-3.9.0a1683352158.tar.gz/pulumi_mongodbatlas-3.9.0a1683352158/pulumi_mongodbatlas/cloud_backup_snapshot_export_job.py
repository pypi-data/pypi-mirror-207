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

__all__ = ['CloudBackupSnapshotExportJobArgs', 'CloudBackupSnapshotExportJob']

@pulumi.input_type
class CloudBackupSnapshotExportJobArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 custom_datas: pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]],
                 export_bucket_id: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 snapshot_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a CloudBackupSnapshotExportJob resource.
        :param pulumi.Input[str] cluster_name: Name of the Atlas cluster whose snapshot you want to export.
        :param pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]] custom_datas: Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        :param pulumi.Input[str] project_id: Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "custom_datas", custom_datas)
        pulumi.set(__self__, "export_bucket_id", export_bucket_id)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "snapshot_id", snapshot_id)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        Name of the Atlas cluster whose snapshot you want to export.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="customDatas")
    def custom_datas(self) -> pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]]:
        """
        Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        """
        return pulumi.get(self, "custom_datas")

    @custom_datas.setter
    def custom_datas(self, value: pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]]):
        pulumi.set(self, "custom_datas", value)

    @property
    @pulumi.getter(name="exportBucketId")
    def export_bucket_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "export_bucket_id")

    @export_bucket_id.setter
    def export_bucket_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "export_bucket_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "snapshot_id", value)


@pulumi.input_type
class _CloudBackupSnapshotExportJobState:
    def __init__(__self__, *,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 components: Optional[pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobComponentArgs']]]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 custom_datas: Optional[pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]]] = None,
                 err_msg: Optional[pulumi.Input[str]] = None,
                 export_bucket_id: Optional[pulumi.Input[str]] = None,
                 export_job_id: Optional[pulumi.Input[str]] = None,
                 export_status_exported_collections: Optional[pulumi.Input[int]] = None,
                 export_status_total_collections: Optional[pulumi.Input[int]] = None,
                 finished_at: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudBackupSnapshotExportJob resources.
        :param pulumi.Input[str] cluster_name: Name of the Atlas cluster whose snapshot you want to export.
        :param pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobComponentArgs']]] components: _Returned for sharded clusters only._ Export job details for each replica set in the sharded cluster.
        :param pulumi.Input[str] created_at: Timestamp in ISO 8601 date and time format in UTC when the export job was created.
        :param pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]] custom_datas: Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        :param pulumi.Input[str] err_msg: Error message, only if the export job failed.
        :param pulumi.Input[str] export_job_id: Unique identifier of the export job.
               * `prefix ` - Full path on the cloud provider bucket to the folder where the snapshot is exported. The path is in the following format:`/exported_snapshots/{ORG-NAME}/{PROJECT-NAME}/{CLUSTER-NAME}/{SNAPSHOT-INITIATION-DATE}/{TIMESTAMP}`
        :param pulumi.Input[str] finished_at: Timestamp in ISO 8601 date and time format in UTC when the export job completes.
        :param pulumi.Input[str] project_id: Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        :param pulumi.Input[str] state: Status of the export job. Value can be one of the following:
        """
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if components is not None:
            pulumi.set(__self__, "components", components)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if custom_datas is not None:
            pulumi.set(__self__, "custom_datas", custom_datas)
        if err_msg is not None:
            pulumi.set(__self__, "err_msg", err_msg)
        if export_bucket_id is not None:
            pulumi.set(__self__, "export_bucket_id", export_bucket_id)
        if export_job_id is not None:
            pulumi.set(__self__, "export_job_id", export_job_id)
        if export_status_exported_collections is not None:
            pulumi.set(__self__, "export_status_exported_collections", export_status_exported_collections)
        if export_status_total_collections is not None:
            pulumi.set(__self__, "export_status_total_collections", export_status_total_collections)
        if finished_at is not None:
            pulumi.set(__self__, "finished_at", finished_at)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Atlas cluster whose snapshot you want to export.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobComponentArgs']]]]:
        """
        _Returned for sharded clusters only._ Export job details for each replica set in the sharded cluster.
        """
        return pulumi.get(self, "components")

    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobComponentArgs']]]]):
        pulumi.set(self, "components", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp in ISO 8601 date and time format in UTC when the export job was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="customDatas")
    def custom_datas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]]]:
        """
        Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        """
        return pulumi.get(self, "custom_datas")

    @custom_datas.setter
    def custom_datas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudBackupSnapshotExportJobCustomDataArgs']]]]):
        pulumi.set(self, "custom_datas", value)

    @property
    @pulumi.getter(name="errMsg")
    def err_msg(self) -> Optional[pulumi.Input[str]]:
        """
        Error message, only if the export job failed.
        """
        return pulumi.get(self, "err_msg")

    @err_msg.setter
    def err_msg(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "err_msg", value)

    @property
    @pulumi.getter(name="exportBucketId")
    def export_bucket_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "export_bucket_id")

    @export_bucket_id.setter
    def export_bucket_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_bucket_id", value)

    @property
    @pulumi.getter(name="exportJobId")
    def export_job_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the export job.
        * `prefix ` - Full path on the cloud provider bucket to the folder where the snapshot is exported. The path is in the following format:`/exported_snapshots/{ORG-NAME}/{PROJECT-NAME}/{CLUSTER-NAME}/{SNAPSHOT-INITIATION-DATE}/{TIMESTAMP}`
        """
        return pulumi.get(self, "export_job_id")

    @export_job_id.setter
    def export_job_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_job_id", value)

    @property
    @pulumi.getter(name="exportStatusExportedCollections")
    def export_status_exported_collections(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "export_status_exported_collections")

    @export_status_exported_collections.setter
    def export_status_exported_collections(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "export_status_exported_collections", value)

    @property
    @pulumi.getter(name="exportStatusTotalCollections")
    def export_status_total_collections(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "export_status_total_collections")

    @export_status_total_collections.setter
    def export_status_total_collections(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "export_status_total_collections", value)

    @property
    @pulumi.getter(name="finishedAt")
    def finished_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp in ISO 8601 date and time format in UTC when the export job completes.
        """
        return pulumi.get(self, "finished_at")

    @finished_at.setter
    def finished_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "finished_at", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the export job. Value can be one of the following:
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class CloudBackupSnapshotExportJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 custom_datas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobCustomDataArgs']]]]] = None,
                 export_bucket_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test_cloud_backup_snapshot_export_bucket = mongodbatlas.CloudBackupSnapshotExportBucket("testCloudBackupSnapshotExportBucket",
            project_id="{PROJECT_ID}",
            iam_role_id="{IAM_ROLE_ID}",
            bucket_name="example_bucket",
            cloud_provider="AWS")
        test_cloud_backup_snapshot_export_job = mongodbatlas.CloudBackupSnapshotExportJob("testCloudBackupSnapshotExportJob",
            project_id="{PROJECT_ID}",
            cluster_name="{CLUSTER_NAME}",
            snapshot_id="{SNAPSHOT_ID}",
            export_bucket_id=test_cloud_backup_snapshot_export_bucket.export_bucket_id,
            custom_datas=[mongodbatlas.CloudBackupSnapshotExportJobCustomDataArgs(
                key="exported by",
                value="myName",
            )])
        ```

        ## Import

        Cloud Backup Snapshot Export Backup entries can be imported using project project_id, cluster_name and export_job_id (Unique identifier of the snapshot export job), in the format `PROJECTID-CLUSTERNAME-EXPORTJOBID`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/cloudBackupSnapshotExportJob:CloudBackupSnapshotExportJob test 5d0f1f73cf09a29120e173cf-5d116d82014b764445b2f9b5-5d116d82014b764445b2f9b5
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/cloud-backup/export/create-one-export-job/)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Name of the Atlas cluster whose snapshot you want to export.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobCustomDataArgs']]]] custom_datas: Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        :param pulumi.Input[str] project_id: Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudBackupSnapshotExportJobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test_cloud_backup_snapshot_export_bucket = mongodbatlas.CloudBackupSnapshotExportBucket("testCloudBackupSnapshotExportBucket",
            project_id="{PROJECT_ID}",
            iam_role_id="{IAM_ROLE_ID}",
            bucket_name="example_bucket",
            cloud_provider="AWS")
        test_cloud_backup_snapshot_export_job = mongodbatlas.CloudBackupSnapshotExportJob("testCloudBackupSnapshotExportJob",
            project_id="{PROJECT_ID}",
            cluster_name="{CLUSTER_NAME}",
            snapshot_id="{SNAPSHOT_ID}",
            export_bucket_id=test_cloud_backup_snapshot_export_bucket.export_bucket_id,
            custom_datas=[mongodbatlas.CloudBackupSnapshotExportJobCustomDataArgs(
                key="exported by",
                value="myName",
            )])
        ```

        ## Import

        Cloud Backup Snapshot Export Backup entries can be imported using project project_id, cluster_name and export_job_id (Unique identifier of the snapshot export job), in the format `PROJECTID-CLUSTERNAME-EXPORTJOBID`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/cloudBackupSnapshotExportJob:CloudBackupSnapshotExportJob test 5d0f1f73cf09a29120e173cf-5d116d82014b764445b2f9b5-5d116d82014b764445b2f9b5
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/cloud-backup/export/create-one-export-job/)

        :param str resource_name: The name of the resource.
        :param CloudBackupSnapshotExportJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudBackupSnapshotExportJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 custom_datas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobCustomDataArgs']]]]] = None,
                 export_bucket_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudBackupSnapshotExportJobArgs.__new__(CloudBackupSnapshotExportJobArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if custom_datas is None and not opts.urn:
                raise TypeError("Missing required property 'custom_datas'")
            __props__.__dict__["custom_datas"] = custom_datas
            if export_bucket_id is None and not opts.urn:
                raise TypeError("Missing required property 'export_bucket_id'")
            __props__.__dict__["export_bucket_id"] = export_bucket_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if snapshot_id is None and not opts.urn:
                raise TypeError("Missing required property 'snapshot_id'")
            __props__.__dict__["snapshot_id"] = snapshot_id
            __props__.__dict__["components"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["err_msg"] = None
            __props__.__dict__["export_job_id"] = None
            __props__.__dict__["export_status_exported_collections"] = None
            __props__.__dict__["export_status_total_collections"] = None
            __props__.__dict__["finished_at"] = None
            __props__.__dict__["prefix"] = None
            __props__.__dict__["state"] = None
        super(CloudBackupSnapshotExportJob, __self__).__init__(
            'mongodbatlas:index/cloudBackupSnapshotExportJob:CloudBackupSnapshotExportJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            components: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobComponentArgs']]]]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            custom_datas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobCustomDataArgs']]]]] = None,
            err_msg: Optional[pulumi.Input[str]] = None,
            export_bucket_id: Optional[pulumi.Input[str]] = None,
            export_job_id: Optional[pulumi.Input[str]] = None,
            export_status_exported_collections: Optional[pulumi.Input[int]] = None,
            export_status_total_collections: Optional[pulumi.Input[int]] = None,
            finished_at: Optional[pulumi.Input[str]] = None,
            prefix: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            snapshot_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'CloudBackupSnapshotExportJob':
        """
        Get an existing CloudBackupSnapshotExportJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Name of the Atlas cluster whose snapshot you want to export.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobComponentArgs']]]] components: _Returned for sharded clusters only._ Export job details for each replica set in the sharded cluster.
        :param pulumi.Input[str] created_at: Timestamp in ISO 8601 date and time format in UTC when the export job was created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudBackupSnapshotExportJobCustomDataArgs']]]] custom_datas: Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        :param pulumi.Input[str] err_msg: Error message, only if the export job failed.
        :param pulumi.Input[str] export_job_id: Unique identifier of the export job.
               * `prefix ` - Full path on the cloud provider bucket to the folder where the snapshot is exported. The path is in the following format:`/exported_snapshots/{ORG-NAME}/{PROJECT-NAME}/{CLUSTER-NAME}/{SNAPSHOT-INITIATION-DATE}/{TIMESTAMP}`
        :param pulumi.Input[str] finished_at: Timestamp in ISO 8601 date and time format in UTC when the export job completes.
        :param pulumi.Input[str] project_id: Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        :param pulumi.Input[str] state: Status of the export job. Value can be one of the following:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudBackupSnapshotExportJobState.__new__(_CloudBackupSnapshotExportJobState)

        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["components"] = components
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["custom_datas"] = custom_datas
        __props__.__dict__["err_msg"] = err_msg
        __props__.__dict__["export_bucket_id"] = export_bucket_id
        __props__.__dict__["export_job_id"] = export_job_id
        __props__.__dict__["export_status_exported_collections"] = export_status_exported_collections
        __props__.__dict__["export_status_total_collections"] = export_status_total_collections
        __props__.__dict__["finished_at"] = finished_at
        __props__.__dict__["prefix"] = prefix
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["snapshot_id"] = snapshot_id
        __props__.__dict__["state"] = state
        return CloudBackupSnapshotExportJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Name of the Atlas cluster whose snapshot you want to export.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter
    def components(self) -> pulumi.Output[Sequence['outputs.CloudBackupSnapshotExportJobComponent']]:
        """
        _Returned for sharded clusters only._ Export job details for each replica set in the sharded cluster.
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Timestamp in ISO 8601 date and time format in UTC when the export job was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="customDatas")
    def custom_datas(self) -> pulumi.Output[Sequence['outputs.CloudBackupSnapshotExportJobCustomData']]:
        """
        Custom data to include in the metadata file named `.complete` that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs.
        """
        return pulumi.get(self, "custom_datas")

    @property
    @pulumi.getter(name="errMsg")
    def err_msg(self) -> pulumi.Output[str]:
        """
        Error message, only if the export job failed.
        """
        return pulumi.get(self, "err_msg")

    @property
    @pulumi.getter(name="exportBucketId")
    def export_bucket_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "export_bucket_id")

    @property
    @pulumi.getter(name="exportJobId")
    def export_job_id(self) -> pulumi.Output[str]:
        """
        Unique identifier of the export job.
        * `prefix ` - Full path on the cloud provider bucket to the folder where the snapshot is exported. The path is in the following format:`/exported_snapshots/{ORG-NAME}/{PROJECT-NAME}/{CLUSTER-NAME}/{SNAPSHOT-INITIATION-DATE}/{TIMESTAMP}`
        """
        return pulumi.get(self, "export_job_id")

    @property
    @pulumi.getter(name="exportStatusExportedCollections")
    def export_status_exported_collections(self) -> pulumi.Output[int]:
        return pulumi.get(self, "export_status_exported_collections")

    @property
    @pulumi.getter(name="exportStatusTotalCollections")
    def export_status_total_collections(self) -> pulumi.Output[int]:
        return pulumi.get(self, "export_status_total_collections")

    @property
    @pulumi.getter(name="finishedAt")
    def finished_at(self) -> pulumi.Output[str]:
        """
        Timestamp in ISO 8601 date and time format in UTC when the export job completes.
        """
        return pulumi.get(self, "finished_at")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[str]:
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        Unique 24-hexadecimal digit string that identifies the project which contains the Atlas cluster whose snapshot you want to export.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Status of the export job. Value can be one of the following:
        """
        return pulumi.get(self, "state")

