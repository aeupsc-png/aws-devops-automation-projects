# AWS DevOps Automation Projects

## Overview

This repository contains six AWS automation projects developed using **AWS Lambda**, **Python (Boto3)**, and various AWS services as part of the **Multi Cloud Architecture & DevOps** program.

The projects demonstrate serverless automation, cloud resource management, infrastructure monitoring, disaster recovery, and security auditing using AWS best practices.

---

# Technologies Used

- AWS Lambda
- Python 3.14
- Boto3
- AWS IAM
- Amazon EC2
- Amazon EBS
- Amazon S3
- Amazon SNS
- Amazon EventBridge
- Amazon CloudWatch
- AWS Cost Explorer API

---

# Project Structure

```
aws-devops-automation-projects
│
├── Assignment1-S3BucketCleanup
├── Assignment2-EBSSnapshotAutomation
├── Assignment3-EC2AutoTag
├── Assignment4-DailyCostAlert
├── Assignment5-RestoreEC2FromSnapshot
└── Assignment6-S3PublicBucketAudit
```

---

# Assignment 1 – Automated S3 Bucket Cleanup

### Objective

Automatically delete S3 objects older than the configured retention period.

### AWS Services

- Amazon S3
- AWS Lambda
- IAM
- CloudWatch

### Features

- Lists objects using a paginator
- Deletes expired objects
- Logs deleted object names
- Uses least-privilege IAM permissions

---

# Assignment 2 – Automated EBS Snapshot Creation and Cleanup

### Objective

Automatically create EBS snapshots and delete old snapshots based on a retention policy.

### AWS Services

- Amazon EC2
- Amazon EBS
- AWS Lambda
- EventBridge
- CloudWatch

### Features

- Creates snapshots
- Tags snapshots
- Deletes old snapshots
- Weekly automation using EventBridge

---

# Assignment 3 – EC2 Auto Tagging

### Objective

Automatically tag newly launched EC2 instances.

### AWS Services

- Amazon EC2
- AWS Lambda
- EventBridge
- IAM

### Features

- Detects EC2 Running state
- Automatically adds LaunchDate tag
- Automatically adds Environment tag
- Logs actions to CloudWatch

---

# Assignment 4 – Daily AWS Cost Alert

### Objective

Monitor AWS monthly costs using Cost Explorer and send email alerts.

### AWS Services

- AWS Cost Explorer
- Amazon SNS
- AWS Lambda
- EventBridge

### Features

- Retrieves current monthly cost
- Compares against a threshold
- Sends SNS email alerts
- Daily scheduled execution

---

# Assignment 5 – Restore EC2 Instance from Latest Snapshot

### Objective

Automate disaster recovery by restoring an EC2 instance from the latest EBS snapshot.

### AWS Services

- Amazon EC2
- Amazon EBS
- AWS Lambda
- CloudWatch

### Features

- Finds latest snapshot
- Registers an AMI
- Launches a new EC2 instance
- Tags restored instance

---

# Assignment 6 – Audit S3 Buckets for Public Access

### Objective

Audit Amazon S3 buckets for public access and notify administrators using Amazon SNS.

### AWS Services

- Amazon S3
- Amazon SNS
- AWS Lambda
- EventBridge

### Features

- Checks Block Public Access
- Verifies bucket policy status
- Reviews ACL permissions
- Sends email alerts for public buckets

---

# Skills Demonstrated

- AWS Lambda Development
- Python Automation using Boto3
- IAM Least-Privilege Policies
- Event-Driven Architecture
- Amazon EventBridge Scheduling
- Amazon SNS Notifications
- Amazon S3 Automation
- Amazon EC2 Automation
- Amazon EBS Snapshot Management
- AWS Cost Monitoring
- CloudWatch Logging
- Infrastructure Automation
- Serverless Computing

---

Postgraduate Program in Multi Cloud Architecture & DevOps

---

# License

This project is licensed under the MIT License.