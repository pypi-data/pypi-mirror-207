# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .get_iam_policy_document import *
from .iam_group import *
from .iam_group_membership import *
from .iam_group_policy import *
from .iam_group_policy_attachment import *
from .iam_group_user_attachment import *
from .iam_policy import *
from .iam_service_account import *
from .iam_user import *
from .iam_user_policy_attachment import *
from .ilm_policy import *
from .provider import *
from .s3_bucket import *
from .s3_bucket_notification import *
from .s3_bucket_policy import *
from .s3_bucket_versioning import *
from .s3_object import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_minio.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_minio.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "minio",
  "mod": "index/iamGroup",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamGroup:IamGroup": "IamGroup"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamGroupMembership",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamGroupMembership:IamGroupMembership": "IamGroupMembership"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamGroupPolicy",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamGroupPolicy:IamGroupPolicy": "IamGroupPolicy"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamGroupPolicyAttachment",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamGroupPolicyAttachment:IamGroupPolicyAttachment": "IamGroupPolicyAttachment"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamGroupUserAttachment",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamGroupUserAttachment:IamGroupUserAttachment": "IamGroupUserAttachment"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamPolicy",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamPolicy:IamPolicy": "IamPolicy"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamServiceAccount",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamServiceAccount:IamServiceAccount": "IamServiceAccount"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamUser",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamUser:IamUser": "IamUser"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/iamUserPolicyAttachment",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/iamUserPolicyAttachment:IamUserPolicyAttachment": "IamUserPolicyAttachment"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/ilmPolicy",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/ilmPolicy:IlmPolicy": "IlmPolicy"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/s3Bucket",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/s3Bucket:S3Bucket": "S3Bucket"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/s3BucketNotification",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/s3BucketNotification:S3BucketNotification": "S3BucketNotification"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/s3BucketPolicy",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/s3BucketPolicy:S3BucketPolicy": "S3BucketPolicy"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/s3BucketVersioning",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/s3BucketVersioning:S3BucketVersioning": "S3BucketVersioning"
  }
 },
 {
  "pkg": "minio",
  "mod": "index/s3Object",
  "fqn": "pulumi_minio",
  "classes": {
   "minio:index/s3Object:S3Object": "S3Object"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "minio",
  "token": "pulumi:providers:minio",
  "fqn": "pulumi_minio",
  "class": "Provider"
 }
]
"""
)
