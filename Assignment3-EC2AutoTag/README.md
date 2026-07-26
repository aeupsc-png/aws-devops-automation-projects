# Assignment 3 – Auto-Tagging EC2 Instances on Launch

## Objective

The objective of this assignment is to automatically tag Amazon EC2 instances when they enter the **Running** state using AWS Lambda, Amazon EventBridge, and Boto3. Automatic tagging helps with resource management, cost allocation, ownership tracking, and operational governance.

---

## AWS Services Used

- AWS Lambda
- Amazon EC2
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch
- Python 3.14
- Boto3

---

## Architecture

```
EC2 Instance Launch
          │
          ▼
EC2 Instance State = Running
          │
          ▼
Amazon EventBridge Rule
          │
          ▼
AWS Lambda
          │
          ▼
Add Tags to EC2 Instance
          │
          ▼
CloudWatch Logs
```

---

## IAM Permissions

The Lambda execution role follows the principle of least privilege and includes the following permissions:

- ec2:CreateTags
- ec2:DescribeInstances

Additionally:

- AWSLambdaBasicExecutionRole

---

## EventBridge Configuration

Event Pattern:

- Source: aws.ec2
- Detail Type: EC2 Instance State-change Notification
- State: running

Target:

- AWS Lambda
- Function Name: EC2AutoTag

---

## Implementation Steps

1. Created an IAM Role with EC2 tagging permissions.
2. Developed the Lambda function using Python and Boto3.
3. Extracted the EC2 Instance ID from the EventBridge event.
4. Generated the current date.
5. Added the following tags automatically:
   - LaunchDate
   - Environment
6. Logged the tagged instance details to CloudWatch.
7. Configured an EventBridge rule to trigger the Lambda whenever an EC2 instance enters the **Running** state.
8. Verified that the tags appeared on the EC2 instance.

---

## Automatic Tags Applied

Example:

| Tag Key | Tag Value |
|----------|-----------|
| LaunchDate | 2026-07-26 |
| Environment | Dev |

---

## Testing

The solution was tested by:

1. Launching a new EC2 instance.
2. Waiting for the instance to reach the **Running** state.
3. Confirming that EventBridge triggered the Lambda.
4. Verifying that the tags were automatically added.
5. Reviewing CloudWatch Logs for successful execution.

---

## CloudWatch Logs

CloudWatch logs displayed:

- Instance ID
- Applied tags
- Successful Lambda execution
- Execution duration
- Memory usage

---

## Discussion

Automatic EC2 tagging provides several operational benefits:

- Resource ownership tracking
- Cost allocation
- Environment identification
- Governance and compliance
- Automation of resource management

This implementation demonstrates how AWS Lambda and EventBridge can automate routine infrastructure management tasks without manual intervention.

---

## Result

The Lambda function successfully detected newly launched EC2 instances and automatically applied the required tags. The EventBridge rule invoked the Lambda whenever an EC2 instance entered the **Running** state, and the applied tags were verified in the EC2 console.