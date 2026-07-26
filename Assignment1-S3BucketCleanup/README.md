Assignment 1 - Automated S3 Bucket Cleanup

# Objective

The objective of this project is to automatically delete objects older than 30 days from an Amazon S3 bucket using AWS Lambda and Boto3.

# AWS Services Used

- AWS Lambda
- Amazon S3
- IAM
- Amazon EventBridge
- Amazon CloudWatch
- Python 3.14
- Boto3

# Architecture

S3 Bucket
        │
        ▼
AWS Lambda
        │
        ▼
Deletes objects older than 30 days
        │
        ▼
CloudWatch Logs

# IAM Permissions

The Lambda execution role contains the following permissions:

- s3:ListBucket
- s3:DeleteObject

These permissions are restricted to the target S3 bucket.

# Implementation Steps

1. Created an S3 bucket.
2. Uploaded sample objects.
3. Created an IAM Role.
4. Attached least-privilege inline policy.
5. Developed the Lambda function using Python and Boto3.
6. Listed objects using a paginator.
7. Compared LastModified timestamp with the current UTC time.
8. Deleted objects older than the configured retention period.
9. Printed deleted object names to CloudWatch Logs.
10. Tested the function manually.

# Testing

The Lambda function was invoked manually from the AWS Console.

Verification:

- Objects older than the configured age were deleted.
- Newer objects remained in the bucket.
- Deleted object names appeared in CloudWatch Logs.

# Discussion

Amazon S3 Lifecycle Rules provide a native solution for deleting old objects with no custom code.

AWS Lambda is preferred when custom business logic is required, such as:

- Filtering objects based on naming patterns
- Cross-service automation
- Conditional deletion
- Sending notifications before deletion

# Result

The Lambda function successfully identified and deleted expired S3 objects while preserving newer objects.