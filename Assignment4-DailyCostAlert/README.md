# Assignment 4 – Daily AWS Cost Alert using AWS Lambda

## Objective

The objective of this assignment is to automate AWS cost monitoring by checking the current month's AWS spending using AWS Cost Explorer. If the cost exceeds a predefined threshold, the Lambda function sends an email notification through Amazon SNS.

---

## AWS Services Used

- AWS Lambda
- AWS Cost Explorer
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
       AWS Cost Explorer
                │
      Current Month Cost
                │
         Threshold Check
                │
      ┌─────────┴──────────┐
      ▼                    ▼
 Below Threshold      Above Threshold
      │                    │
      ▼                    ▼
   No Action         Amazon SNS
                           │
                           ▼
                     Email Notification
                           │
                           ▼
                     CloudWatch Logs
```

---

## IAM Permissions

The Lambda execution role includes:

- ce:GetCostAndUsage
- sns:Publish

AWS Managed Policy:

- AWSLambdaBasicExecutionRole

---

## Implementation Steps

1. Created an SNS Topic.
2. Added an email subscription.
3. Confirmed the subscription.
4. Created an IAM Role with Cost Explorer and SNS permissions.
5. Developed a Lambda function using Python and Boto3.
6. Queried AWS Cost Explorer for the current month's cost.
7. Compared the cost against a configurable threshold.
8. Published an SNS notification if the threshold was exceeded.
9. Logged the execution details to CloudWatch.
10. Scheduled daily execution using Amazon EventBridge.

---

## EventBridge Schedule

- Schedule Name: DailyCostAlertSchedule
- Frequency: Every 1 Day
- Target: AWS Lambda

---

## Testing

The Lambda function was tested manually.

Verification included:

- Cost retrieved successfully.
- Current monthly cost displayed.
- SNS notification delivered.
- Email received successfully.
- CloudWatch logs verified.

---

## CloudWatch Logs

CloudWatch logs display:

- Current month's AWS cost
- Alert status
- Execution duration
- Memory usage

---

## Result

The Lambda function successfully retrieves the current AWS account cost every day. When the configured threshold is exceeded, an email notification is sent using Amazon SNS. EventBridge automates daily execution, making the solution suitable for continuous cost monitoring.