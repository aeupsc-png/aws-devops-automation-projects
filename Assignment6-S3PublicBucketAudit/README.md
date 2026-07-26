# Assignment 6 – Audit S3 Buckets for Public Access and Notify

## Objective

The objective of this assignment is to automatically audit all Amazon S3 buckets for public access using AWS Lambda and Boto3. If a bucket is detected as public, the Lambda function sends an email notification using Amazon SNS.

---

## AWS Services Used

- AWS Lambda
- Amazon S3
- Amazon SNS
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch
- Python 3.14
- Boto3

---

## Architecture

```
Amazon EventBridge (Daily Schedule)
                │
                ▼
          AWS Lambda
                │
                ▼
         List S3 Buckets
                │
                ▼
Check:
- Block Public Access
- Bucket Policy Status
- ACL Permissions
                │
        ┌───────┴────────┐
        ▼                ▼
 Public Bucket      Private Bucket
        │                │
        ▼                ▼
 Amazon SNS         Log Result
        │
        ▼
 Email Notification
```

---

## IAM Permissions

The Lambda execution role includes:

- s3:ListAllMyBuckets
- s3:GetBucketPublicAccessBlock
- s3:GetBucketPolicyStatus
- s3:GetBucketAcl
- sns:Publish

AWS Managed Policy:

- AWSLambdaBasicExecutionRole

---

## Implementation Steps

1. Created an SNS Topic.
2. Added and confirmed an email subscription.
3. Created an IAM Role with S3 audit permissions.
4. Developed a Lambda function using Python and Boto3.
5. Retrieved all S3 buckets.
6. Checked Block Public Access configuration.
7. Checked Bucket Policy Status.
8. Checked Bucket ACLs.
9. Published an SNS notification if a public bucket was detected.
10. Scheduled daily execution using Amazon EventBridge.

---

## EventBridge Schedule

- Schedule Name: S3BucketAuditDaily
- Frequency: Every 1 Day
- Target: AWS Lambda

---

## Testing

The Lambda function was tested manually.

Verification included:

- Bucket list retrieved successfully.
- Public access configuration checked.
- No public buckets detected.
- CloudWatch logs verified.
- EventBridge schedule created successfully.

---

## CloudWatch Logs

CloudWatch logs display:

- Bucket names
- Public access evaluation
- Audit results
- Execution duration
- Memory usage

---

## Discussion

AWS enables **Block Public Access** by default for new buckets, significantly reducing the risk of accidental exposure.

Using AWS Lambda allows organizations to implement custom compliance checks, send notifications, integrate with ticketing systems, and enforce organization-specific security policies beyond the built-in AWS features.

---

## Result

The Lambda function successfully audited all Amazon S3 buckets for public access. No public buckets were detected, confirming that the environment is configured securely. EventBridge automates the daily audit, providing continuous monitoring of S3 bucket security.