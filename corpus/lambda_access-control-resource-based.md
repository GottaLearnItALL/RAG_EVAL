

# Working with resource-based policies in Lambda
<a name="access-control-resource-based"></a>

With resource-based permissions policies, you can grant other AWS accounts, users, organizations, and AWS services access to your Lambda functions. A resource-based policy is a JSON document that contains one or more *statements*. Each statement defines the following:
+ `Principal`: The entity you want to grant permissions to (another AWS service, an IAM role or user, or another AWS account)
+ `Action`: A list of the API actions you want to allow or deny for the specified principal
+ `Effect`: Whether you want to allow or deny the principal the ability to use the chosen API actions
+ `Resource`: The Lambda function, version, or alias you want the statement to apply to (you can also use a wildcard character to specify all of your function's versions and aliases)

You can also use optional elements such as `Sid` (a statement identifier) and `Condition` (logical conditions for fine-grained access control). For a full list of supported policy elements, refer to [IAM JSON policy element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *AWS Identity and Access Management User Guide*.

## Adding resource-based permissions to a Lambda function
<a name="access-control-resource-based-add"></a>

You can add resource-based permissions to your Lambda function using two methods:
+ **Full JSON policy** – Use the Lambda console, AWS CLI, or the [PutResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_PutResourcePolicy.html) API action to add a complete JSON policy document. With a full JSON policy, you can use the complete range of [IAM global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html), add multiple statements with multiple principals, and create explicit `Deny` statements. The maximum size for a JSON resource-based policy is 20 KB.
+ **Individual permissions** – Use the console or [AddPermission](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html) API action to add single `Allow` statements. Individual permissions support only a limited set of condition keys (`aws:SourceArn`, `aws:SourceAccount`, and `aws:PrincipalOrgID`).

We recommend that you define complete JSON policies to add resource-based permissions to your function. Creating a complete JSON policy gives you more flexibility and fine-grained control over your permissions.

**Important**  
Using `put-resource-policy` replaces any existing resource-based policy on the resource. If the resource already has permissions defined with `add-permission`, `put-resource-policy` overwrites them. Use `get-resource-policy` to retrieve the existing policy before making changes.

### Required permissions
<a name="access-control-resource-based-permissions"></a>

To use the `PutResourcePolicy`, `GetResourcePolicy`, and `DeleteResourcePolicy` API actions, you need the following IAM permissions:


| API action | Required permissions | 
| --- | --- | 
| PutResourcePolicy | lambda:PutResourcePolicy, lambda:AddPermission, and lambda:RemovePermission | 
| GetResourcePolicy | lambda:GetResourcePolicy and lambda:GetPolicy | 
| DeleteResourcePolicy | lambda:DeleteResourcePolicy and lambda:RemovePermission | 

------
#### [ Console ]

**To create a full JSON resource-based policy**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function you want to grant access to and then select the **Configuration** tab.

1. Select **Permissions**.

1. In the **Resource-based policy statements** pane, choose **Edit**. This action opens the JSON policy editor.

1. Add statements to your function's policy. You can select API actions, add principals of different types (services, accounts, IAM roles), and add condition keys to control access.

1. Choose **Save**.

You can also edit your function's resource-based policy directly in the **Policy** pane.

------
#### [ AWS CLI ]

**To add a full JSON resource-based policy**  
To add a full JSON policy to your function, use the `put-resource-policy` AWS CLI command.

The following example command adds a resource-based policy to your function using a policy defined in a file named `policy.json` on your local machine. Run the command from the directory that contains the file. The `resource-arn` can specify a function version or alias, or you can use the unqualified function ARN to apply the policy to the entire function.

```
aws lambda put-resource-policy --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}} \
--policy file://policy.json
```

------
#### [ Lambda APIs ]

To add a full JSON permissions policy to your function, use the [PutResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_PutResourcePolicy.html) API action. You can also delete a function's policy using the [DeleteResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteResourcePolicy.html) action, or retrieve the policy currently attached to a function using the [GetResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetResourcePolicy.html) action.

To add individual permissions to a function's policy, use the [AddPermission](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html) API action.

------

## Viewing a function's resource-based policy
<a name="access-control-resource-based-view"></a>

------
#### [ Console ]

**To view a function's resource-based policy**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose a function.

1. Choose **Configuration** and then choose **Permissions**.

1. Scroll down to **Resource-based policy statements** to see the policy.

------
#### [ AWS CLI ]

To view a function's resource-based policy, use the `get-resource-policy` command. You can use your function's unqualified ARN, or specify a version or alias.

```
aws lambda get-resource-policy --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}}
```

You can also use the `get-policy` command:

```
aws lambda get-policy \
  --function-name my-function \
  --output text
```

------
#### [ Lambda APIs ]

To retrieve a function's resource-based policy, use the [GetResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetResourcePolicy.html) API action. You can use your function's unqualified ARN, or specify a version or alias ARN.

You can also use the [GetPolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetPolicy.html) API action.

------

## Deleting a function's resource-based policy
<a name="access-control-resource-based-delete"></a>

------
#### [ Console ]

**To delete a function's resource-based policy**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function you want to delete the permissions policy for.

1. Select the **Configuration** tab, then **Permissions**.

1. In the **Resource-based policy statements** pane, choose **Delete**.

------
#### [ AWS CLI ]

To delete your function's policy, use the `delete-resource-policy` command and specify the ARN of the function, version, or alias you want to delete the policy from.

```
aws lambda delete-resource-policy --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}}
```

To remove individual statements, use `remove-permission`.

```
aws lambda remove-permission \
  --function-name example \
  --statement-id sns
```

------
#### [ Lambda APIs ]

To delete the resource-based policy attached to a function, function version, or function alias, use the [DeleteResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteResourcePolicy.html) API action.

To remove individual statements from a policy, use the [RemovePermission](https://docs.aws.amazon.com/lambda/latest/api/API_RemovePermission.html) API action.

------

## Updating existing policies
<a name="access-control-resource-based-update"></a>

When you update a function's existing resource-based permissions, the behavior depends on the method you use:
+ `put-resource-policy` / [PutResourcePolicy](https://docs.aws.amazon.com/lambda/latest/api/API_PutResourcePolicy.html) – Replaces the entire existing policy. Any previously added individual permissions are overwritten.
+ `add-permission` / [AddPermission](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html) – Adds a statement to the existing policy without overwriting. If you call `add-permission` after `put-resource-policy`, the new statement appends to the existing JSON policy.

To avoid unintentionally overwriting existing permissions when using `put-resource-policy`, retrieve your function's existing policy first. The `get-resource-policy` output includes a `RevisionId` field.

```
aws lambda get-resource-policy --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}}
```

When you attach a new policy, provide the `RevisionId` value with the `--revision-id` parameter to ensure that you are updating the latest version. If you provide an older revision ID, Lambda does not update your function's policy.

```
aws lambda put-resource-policy \
  --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}} \
  --policy file://policy.json \
  --revision-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```

**Note**  
Existing resource-based policies created with `AddPermission` continue to work without modification. No changes to your function code are required to use the new `PutResourcePolicy` API.

## Security best practices
<a name="access-control-resource-based-security"></a>

With JSON resource-based policies, you can follow least-privilege access patterns. You can also meet regulatory requirements for explicit denials. With full JSON policies, you can:
+ Create explicit `Deny` statements to block specific principals or conditions.
+ Use organizational conditions (`aws:PrincipalOrgID`, `aws:PrincipalOrgPaths`) to restrict access to your Organizations without enumerating individual accounts.
+ Scope permissions to specific source accounts or ARNs using the full range of IAM global condition keys.

## Example resource-based policies
<a name="access-control-resource-based-examples"></a>

**Example Granting permission to Amazon S3 with a deny statement**  
The following policy grants all Amazon S3 buckets in an account permission to invoke a function, except for one bucket that is explicitly denied.  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-s3",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "deny-s3-bucket",
            "Effect": "Deny",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": [
                "arn:aws:lambda:us-east-2:111122223333:function:my-function",
                "arn:aws:lambda:us-east-2:111122223333:function:my-function:*"
            ],
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::amzn-s3-demo-bucket"
                }
            }
        }
    ]
}
```

**Example Granting permission to accounts in an organization**  
The following policy grants invoke access to all AWS accounts in an organization.  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "org-access",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Principal": "*",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-a1b2c3d4e5f"
                }
            }
        }
    ]
}
```

**Example Granting permission to multiple IAM roles with conditions**  
The following policy grants permission to two IAM roles to use the CreateAlias action from a specified IP address.  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-roles",
            "Effect": "Allow",
            "Action": "lambda:CreateAlias",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::444455556666:role/role-name",
                    "arn:aws:iam::444455556666:role/role-name2"
                ]
            },
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "192.0.2.0"
                }
            }
        }
    ]
}
```

**Example Denying access unless the caller is part of a specified organization**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "deny-access",
            "Effect": "Deny",
            "Action": "lambda:InvokeFunction",
            "Principal": "*",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "ForAllValues:StringNotLike": {
                    "aws:PrincipalOrgPaths": [
                        "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/*"
                    ]
                }
            }
        },
        {
            "Sid": "allow-access",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Principal": "*",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "ForAnyValue:StringLike": {
                    "aws:PrincipalOrgPaths": [
                        "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/*"
                    ]
                }
            }
        }
    ]
}
```

## Supported API actions
<a name="permissions-resource-api"></a>

The following Lambda API actions support resource-based policies:
+ [CreateAlias](https://docs.aws.amazon.com/lambda/latest/api/API_CreateAlias.html)
+ [DeleteAlias](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteAlias.html)
+ [DeleteFunction](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunction.html)
+ [DeleteFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunctionConcurrency.html)
+ [DeleteFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunctionEventInvokeConfig.html)
+ [DeleteProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteProvisionedConcurrencyConfig.html)
+ [GetAlias](https://docs.aws.amazon.com/lambda/latest/api/API_GetAlias.html)
+ [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html)
+ [GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConcurrency.html)
+ [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConfiguration.html)
+ [GetFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionEventInvokeConfig.html)
+ [GetPolicy](https://docs.aws.amazon.com/lambda/latest/api/API_GetPolicy.html)
+ [GetProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/api/API_GetProvisionedConcurrencyConfig.html)
+ [Invoke](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html)
+ [InvokeFunctionUrl](urls-auth.md) (permission only)
+ [ListAliases](https://docs.aws.amazon.com/lambda/latest/api/API_ListAliases.html)
+ [ListFunctionEventInvokeConfigs](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctionEventInvokeConfigs.html)
+ [ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/api/API_ListProvisionedConcurrencyConfigs.html)
+ [ListTags](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html)
+ [ListVersionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListVersionsByFunction.html)
+ [PublishVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html)
+ [PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionConcurrency.html)
+ [PutFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionEventInvokeConfig.html)
+ [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutProvisionedConcurrencyConfig.html)
+ [TagResource](https://docs.aws.amazon.com/lambda/latest/api/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/lambda/latest/api/API_UntagResource.html)
+ [UpdateAlias](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateAlias.html)
+ [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html)
+ [UpdateFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionEventInvokeConfig.html)