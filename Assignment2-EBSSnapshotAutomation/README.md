# Assignment 2 – Automated EBS Snapshot Creation and Cleanup

## Objective

The objective of this assignment is to automate the creation of Amazon EBS snapshots using AWS Lambda and Boto3. The Lambda function also removes old snapshots based on a retention policy, ensuring efficient backup management and reducing unnecessary storage costs.

---

## AWS Services Used

- AWS Lambda
- Amazon EC2 (EBS Volumes & Snapshots)
- AWS IAM
- Amazon EventBridge
- Amazon CloudWatch
- Python 3.14
- Boto3

---

## Architecture

```
Amazon EventBridge (Weekly Schedule)
                │
                ▼
          AWS Lambda
                │
      ┌─────────┴─────────┐
      ▼                   ▼
Create EBS Snapshot   Delete Old Snapshots
      │                   │
      └─────────┬─────────┘
                ▼
         CloudWatch Logs
```

---

## IAM Permissions

The Lambda execution role uses least-privilege permissions with the following actions:

- ec2:CreateSnapshot
- ec2:DescribeSnapshots
- ec2:DeleteSnapshot
- ec2:CreateTags

Additionally:

- AWSLambdaBasicExecutionRole

---

## Implementation Steps

1. Identified the EBS volume to back up.
2. Created an IAM Role with the required EC2 permissions.
3. Developed a Python Lambda function using Boto3.
4. Created a snapshot of the specified EBS volume.
5. Tagged the snapshot with:

   - CreatedBy = Lambda-Backup

6. Retrieved all snapshots created by the Lambda.
7. Compared snapshot creation dates with the retention period.
8. Deleted snapshots older than the configured retention period.
9. Logged created and deleted snapshot IDs in CloudWatch.
10. Configured Amazon EventBridge to run the Lambda every week.

---

## EventBridge Schedule

- Schedule Type: Recurring
- Frequency: Weekly
- Target: AWS Lambda
- Lambda Function: EBSSnapshotAutomation

---

## Testing

The Lambda function was tested manually using the AWS Lambda Test feature.

Verification included:

- Successful creation of a new EBS snapshot.
- Snapshot visible in the EC2 Console.
- Snapshot tagged correctly.
- Old snapshots deleted according to the retention policy.
- Snapshot IDs displayed in CloudWatch Logs.

---

## CloudWatch Logs

CloudWatch logs confirmed:

- Snapshot creation
- Snapshot deletion (if applicable)
- Snapshot IDs
- Successful Lambda execution
- Execution duration and memory usage

---

## Discussion

Amazon Data Lifecycle Manager (DLM) is AWS's managed service for automating EBS snapshot creation and retention.

AWS Lambda is preferred when:

- Custom retention policies are required.
- Cross-account snapshot management is needed.
- Notifications must be sent after snapshot creation.
- Additional automation or business logic is required.

---

## Result

The Lambda function successfully automated the creation of EBS snapshots and removed expired snapshots based on the configured retention period.

This implementation demonstrates an automated backup solution using AWS Lambda, Boto3, EventBridge, and CloudWatch while following IAM least-privilege best practices.