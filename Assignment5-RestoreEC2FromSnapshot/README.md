# Assignment 5 – Restore EC2 Instance from an EBS Snapshot

## Objective

The objective of this assignment is to automate the restoration of an Amazon EC2 instance from the latest available EBS snapshot using AWS Lambda and Boto3. The solution demonstrates automated disaster recovery by creating an Amazon Machine Image (AMI) from a snapshot and launching a new EC2 instance.

---

## AWS Services Used

- AWS Lambda
- Amazon EC2
- Amazon EBS Snapshots
- AWS IAM
- Amazon CloudWatch
- Python 3.14
- Boto3

---

## Architecture

```
AWS Lambda
      │
      ▼
Describe EBS Snapshots
      │
      ▼
Select Latest Snapshot
      │
      ▼
Create AMI
      │
      ▼
Wait Until Available
      │
      ▼
Launch EC2 Instance
      │
      ▼
CloudWatch Logs
```

---

## IAM Permissions

The Lambda execution role includes:

- ec2:DescribeSnapshots
- ec2:RegisterImage
- ec2:DescribeImages
- ec2:RunInstances
- ec2:CreateTags
- ec2:DescribeInstances

AWS Managed Policy:

- AWSLambdaBasicExecutionRole

---

## Implementation Steps

1. Identified the target EBS volume.
2. Retrieved all snapshots belonging to the volume.
3. Selected the most recent completed snapshot.
4. Registered a new AMI using the snapshot.
5. Waited until the AMI became available.
6. Launched a new EC2 instance from the AMI.
7. Logged the AMI ID and Instance ID to CloudWatch.

---

## Testing

The Lambda function was tested manually.

Verification included:

- Latest snapshot detected.
- AMI created successfully.
- EC2 instance launched.
- Instance visible in the EC2 Console.
- CloudWatch logs confirmed successful execution.

---

## CloudWatch Logs

CloudWatch logs display:

- Snapshot ID
- AMI ID
- Instance ID
- Successful Lambda execution
- Execution duration
- Memory usage

---

## Result

The Lambda function successfully automated the recovery of an EC2 instance from the latest EBS snapshot. The workflow demonstrates an automated disaster recovery solution using AWS Lambda, Amazon EC2, and Amazon EBS.