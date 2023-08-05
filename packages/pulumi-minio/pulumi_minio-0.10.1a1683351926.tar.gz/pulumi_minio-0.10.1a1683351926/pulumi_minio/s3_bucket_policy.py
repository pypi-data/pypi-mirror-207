# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['S3BucketPolicyArgs', 'S3BucketPolicy']

@pulumi.input_type
class S3BucketPolicyArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 policy: pulumi.Input[str]):
        """
        The set of arguments for constructing a S3BucketPolicy resource.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)


@pulumi.input_type
class _S3BucketPolicyState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering S3BucketPolicy resources.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)


class S3BucketPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_minio as minio

        bucket_s3_bucket = minio.S3Bucket("bucketS3Bucket", bucket="example-bucket")
        bucket_s3_bucket_policy = minio.S3BucketPolicy("bucketS3BucketPolicy",
            bucket=bucket_s3_bucket.bucket,
            policy=bucket_s3_bucket.bucket.apply(lambda bucket: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Effect": "Allow",
             "Principal": {{"AWS": ["*"]}},
              "Resource": ["arn:aws:s3:::{bucket}"],
             "Action": ["s3:ListBucket"]
            }}
          ]
        }}
        \"\"\"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: S3BucketPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_minio as minio

        bucket_s3_bucket = minio.S3Bucket("bucketS3Bucket", bucket="example-bucket")
        bucket_s3_bucket_policy = minio.S3BucketPolicy("bucketS3BucketPolicy",
            bucket=bucket_s3_bucket.bucket,
            policy=bucket_s3_bucket.bucket.apply(lambda bucket: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Effect": "Allow",
             "Principal": {{"AWS": ["*"]}},
              "Resource": ["arn:aws:s3:::{bucket}"],
             "Action": ["s3:ListBucket"]
            }}
          ]
        }}
        \"\"\"))
        ```

        :param str resource_name: The name of the resource.
        :param S3BucketPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(S3BucketPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = S3BucketPolicyArgs.__new__(S3BucketPolicyArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
        super(S3BucketPolicy, __self__).__init__(
            'minio:index/s3BucketPolicy:S3BucketPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None) -> 'S3BucketPolicy':
        """
        Get an existing S3BucketPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _S3BucketPolicyState.__new__(_S3BucketPolicyState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["policy"] = policy
        return S3BucketPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy")

