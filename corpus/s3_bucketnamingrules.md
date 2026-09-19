

# General purpose bucket naming rules
<a name="bucketnamingrules"></a>

When you create a general purpose bucket, make sure that you consider the length, valid characters, formatting, and uniqueness of bucket names. The following sections provide information about general purpose bucket naming, including naming rules, best practices, and an example for how you can create buckets in your account regional namespace. an example for creating a general purpose bucket with a name that includes a globally unique identifier (GUID). 

For information about object key names, see [Creating object key names](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html).

To create a general purpose bucket, see [Creating a general purpose bucket](create-bucket-overview.md).

**Topics**
+ [General purpose buckets naming rules](#general-purpose-bucket-names)
+ [Account regional namespace naming rules](#account-regional-naming-rules)
+ [Example general purpose bucket names](#bucket-names)
+ [Best practices](#automatically-created-buckets)
+ [Creating a bucket that uses a GUID in the bucket name](#create-bucket-name-guid)
+ [Creating a bucket in your account regional namespace](#create-account-regional-naming)

## General purpose buckets naming rules
<a name="general-purpose-bucket-names"></a>

The following naming rules apply for general purpose buckets.
+ Bucket names must be between 3 (min) and 63 (max) characters long.
+ Bucket names can consist only of lowercase letters, numbers, periods (`.`), and hyphens (`-`).
+ Bucket names must begin and end with a letter or number.
+ Bucket names must not contain two adjacent periods.
+ Bucket names must not be formatted as an IP address (for example, `192.168.5.4`).
+ Bucket names must not start with the prefix `xn--`.
+ Bucket names must not start with the prefix `sthree-`.
+ Bucket names must not start with the prefix `amzn-s3-demo-`.
+ Bucket names must not end with the suffix `-s3alias`. This suffix is reserved for access point alias names. For more information, see [Access point aliases](access-points-naming.md#access-points-alias).
+ Bucket names must not end with the suffix `--ol-s3`. This suffix is reserved for Object Lambda Access Point alias names. For more information, see [How to use a bucket-style alias for your S3 bucket Object Lambda Access Point](olap-use.md#ol-access-points-alias).
+ Bucket names must not end with the suffix `.mrap`. This suffix is reserved for Multi-Region Access Point names. For more information, see [Rules for naming Amazon S3 Multi-Region Access Points](multi-region-access-point-naming.md).
+ Bucket names must not end with the suffix `--x-s3`. This suffix is reserved for directory buckets. For more information, see [Directory bucket naming rules](directory-bucket-naming-rules.md).
+ Bucket names must not end with the suffix `--table-s3`. This suffix is reserved for S3 Tables buckets. For more information, see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md).
+ Bucket names can only end with the suffix `-an` when you are creating buckets in your account regional namespace. For more information, see [Namespaces for general purpose buckets](gpbucketnamespaces.md).
+ Buckets used with Amazon S3 Transfer Acceleration can't have periods (`.`) in their names. For more information about Transfer Acceleration, see [Configuring fast, secure file transfers using Amazon S3 Transfer Acceleration](transfer-acceleration.md).

**Important**  
General purpose buckets exist in a global namespace, which means that each bucket name must be unique across all AWS accounts in all the AWS Regions within a partition. A partition is a grouping of Regions. AWS currently has four partitions: `aws` (Standard Regions), `aws-cn` (China Regions), `aws-us-gov` (AWS GovCloud (US)), and `aws-eusc` (European Sovereign Cloud). After creating a general purpose bucket in the shared global namespace, that bucket name is unavailable for anyone else to create within a partition. When a bucket owner deletes their bucket, the bucket name might become available again in the global namespace for anyone to re-create. However, the name might not become available immediately, and in some cases might not become available again at all.
A bucket name in the shared global namespace can't be used by another AWS account in the same partition until the bucket is deleted. **After you delete a bucket in the shared global namespace, be aware that another AWS account in the same partition can use the same bucket name for a new bucket and can therefore potentially receive requests intended for the deleted bucket.** If you want to prevent this, or if you want to continue to use the same bucket name, don't delete the bucket. We recommend that you empty the bucket and keep it, and instead, block any bucket requests as needed. For buckets no longer in active use, we recommend emptying the bucket of all objects to minimize costs while retaining the bucket itself.
We recommend creating buckets in your account regional namespace for assurance that only your account can ever own these bucket names.
When you create a general purpose bucket, you choose its name and the AWS Region to create it in. After you create a general purpose bucket, you can't change its name or Region. 
Don't include sensitive information in the bucket name. The bucket name is visible in the URLs that point to the objects in the bucket.

**Note**  
Before March 1, 2018, buckets created in the US East (N. Virginia) Region could have names that were up to 255 characters long and included uppercase letters and underscores. Beginning March 1, 2018, new buckets in US East (N. Virginia) must conform to the same rules applied in all other Regions.

## Account regional namespace naming rules
<a name="account-regional-naming-rules"></a>

Although Amazon S3 general purpose buckets exist in a shared global namespace, you can optionally create buckets in your account regional namespace. The account regional namespace is a reserved subdivision of the global bucket namespace where only your account can create general purpose buckets. New general purpose buckets created in your account regional namespace are unique to your account and can never be re-created by another account. These buckets support all the S3 features and AWS services that general purpose buckets in the shared global namespace already support, your applications require no change to interact with buckets in your account regional namespace.

General purpose buckets in your account regional namespace must follow a specific naming convention. These buckets consist of a bucket name prefix that you create, and a suffix that contains your 12-digit AWS account ID, the AWS Region code, and ends with `-an`.

```
{{bucket-name-prefix}}-accountId-region-an
```

For example, the following general purpose bucket exists in the account regional namespace for AWS account 111122223333 in the us-west-2 Region:

```
{{amzn-s3-demo-bucket}}-111122223333-us-west-2-an
```

To create bucket in your account regional namespace, you make a `CreateBucket` request and specify the `x-amz-bucket-namespace` request header with the value set to `account-regional` along with specifying an account regional namespace formatted bucket name: `{{customer-chosen-name}}-AWS-Account-ID-AWS-Region-an`. For example, you could specify to create a bucket named: `{{amzn-s3-demo-bucket}}-111122223333-us-east-1-an` where your account regional suffix is `-111122223333-us-east-1-an`. For more information on account regional namespaces, see [Namespaces for general purpose buckets](gpbucketnamespaces.md).

## Example general purpose bucket names
<a name="bucket-names"></a>

The following bucket names show examples of which characters are allowed in general purpose bucket names: a-z, 0-9, and hyphens (`-`). The `amzn-s3-demo-` reserved prefix is used here only for illustration. Because it's a reserved prefix, you can't create bucket names that start with `amzn-s3-demo-`.
+ `amzn-s3-demo-bucket1-a1b2c3d4-5678-90ab-cdef-example11111`
+ `amzn-s3-demo-bucket`

The following examples shows bucket names in your account regional namespace. These buckets must adhere to the specific account regional namespace naming convention: `{{customer-chosen-name}}-AWS-Account-ID-AWS-Region-an`
+ `amzn-s3-demo-bucket-111122223333-us-west-2-an`
+ `amzn-s3-demo-bucket-012345678910-ap-southeast-2-an`

The following example bucket names are valid but not recommended for uses other than static website hosting because they contain periods (`.`):
+ `example.com`
+ `www.example.com`
+ `my.example.s3.bucket`

The following example bucket names are *not* valid:
+ `amzn_s3_demo_bucket` (contains underscores)
+ `AmznS3DemoBucket` (contains uppercase letters)
+ `amzn-s3-demo-bucket-` (starts with `amzn-s3-demo-` prefix and ends with a hyphen)
+ `example..com` (contains two periods in a row)
+ `192.168.5.4` (matches format of an IP address)

## Best practices
<a name="automatically-created-buckets"></a>

When naming your general purpose buckets, consider the following bucket naming best practices.

**Create buckets in your account regional namespace**  
We recommend creating buckets in your account regional namespace for assurance that only your account can ever own these bucket names. With account regional namespaces, you can create predictable bucket names across multiple AWS Regions with assurance that no other account can create bucket names in your namespace.

**Choose a bucket naming scheme that's unlikely to cause naming conflicts**  
If your application automatically creates buckets, choose a bucket naming scheme that's unlikely to cause naming conflicts. Ensure that your application logic will choose a different bucket name if a bucket name is already taken.

**Append globally unique identifiers (GUIDs) to bucket names**  
We recommend that you create bucket names that aren't predictable. Don't write code assuming your chosen bucket name is available unless you have already created the bucket. One method for creating bucket names that aren't predictable is to append a Globally Unique Identifier (GUID) to your bucket name, for example, `amzn-s3-demo-bucket-a1b2c3d4-5678-90ab-cdef-example11111`. For more information, see [Creating a bucket that uses a GUID in the bucket name](#create-bucket-name-guid).

**Avoid using periods (`.`) in bucket names**  
For best compatibility, we recommend that you avoid using periods (`.`) in bucket names, except for buckets that are used only for static website hosting. If you include periods in a bucket's name, you can't use virtual-host-style addressing over HTTPS, unless you perform your own certificate validation. The security certificates used for virtual hosting of buckets don't work for buckets with periods in their names. 

This limitation doesn't affect buckets used for static website hosting, because static website hosting is available only over HTTP. For more information about virtual-host-style addressing, see [Virtual hosting of general purpose buckets](VirtualHosting.md). For more information about static website hosting, see [Hosting a static website using Amazon S3](WebsiteHosting.md).

**Choose a relevant name**  
When you name a bucket, we recommend that you choose a name that's relevant to you or your business. Avoid using names associated with others. For example, avoid using `AWS` or `Amazon` in your bucket name.

**Don't delete buckets so that you can reuse bucket names**  
If a bucket is empty, you can delete it. After a bucket is deleted, the name becomes available for reuse. However, you aren't guaranteed to be able to reuse the name right away, or at all. After you delete a bucket in the shared global namespace, some time might pass before you can reuse the name. In addition, another AWS account might create a bucket with the same name before you can reuse the name. 

**After you delete a general purpose bucket in the shared global namespace, be aware that another AWS account in the same partition can use the same general purpose bucket name for a new bucket and can therefore potentially receive requests intended for the deleted general purpose bucket.** If you want to prevent this, or if you want to continue to use the same general purpose bucket name, don't delete the general purpose bucket. We recommend that you empty the bucket and keep it, and instead, block any bucket requests as needed.

## Creating a bucket that uses a GUID in the bucket name
<a name="create-bucket-name-guid"></a>

The following examples show you how to create a general purpose bucket that uses a GUID at the end of the bucket name.

### Using the AWS CLI
<a name="guid-cli-bucket-name"></a>

The following AWS CLI example creates a general purpose bucket in the US West (N. California) Region (`us-west-1`) Region with an example bucket name that uses a globally unique identifier (GUID). To use this example command, replace the `{{user input placeholders}}` with your own information.

```
aws s3api create-bucket \
    --bucket {{amzn-s3-demo-bucket1}}$(uuidgen | tr -d - | tr '[:upper:]' '[:lower:]' ) \
    --region {{us-west-1}} \
    --create-bucket-configuration LocationConstraint={{us-west-1}}
```

### Using the AWS SDK for Java
<a name="guid-sdk-bucket-name"></a>

The following example shows you how to create a with a GUID at the end of the bucket name in US East (N. Virginia) Region (`us-east-1`) by using the AWS SDK for Java. To use this example, replace the `{{user input placeholders}}` with your own information. For information about other AWS SDKs, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/).

```
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.Bucket;
import com.amazonaws.services.s3.model.CreateBucketRequest;

import java.util.List;
import java.util.UUID;

public class CreateBucketWithUUID {
    public static void main(String[] args) {
        final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.{{US_EAST_1}}).build();
        String bucketName = "{{amzn-s3-demo-bucket}}" +  UUID.randomUUID().toString().replace("-", "");
        CreateBucketRequest createRequest = new CreateBucketRequest(bucketName);
        System.out.println(bucketName);
        s3.createBucket(createRequest);
    }
}
```

## Creating a bucket in your account regional namespace
<a name="create-account-regional-naming"></a>

The following examples show you how to create a general purpose bucket in your account regional namespace.

### Using the AWS CLI
<a name="account-regional-cli-naming"></a>

The following AWS CLI example creates a general purpose bucket in the account regional namespace for AWS account 012345678910 in the US West (N. California) Region (`us-west-1`) Region. To use this example command, replace the {{user input placeholders}} with your own information.

```
aws s3api create-bucket \
    --bucket {{amzn-s3-demo-bucket-012345678910-us-west-1-an}} \
    --bucket-namespace account-regional
    --region {{us-west-1}} \
    --create-bucket-configuration LocationConstraint={{us-west-1}}
```