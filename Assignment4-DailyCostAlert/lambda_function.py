import boto3
from datetime import datetime

ce = boto3.client("ce")
sns = boto3.client("sns")

# Change this to your SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:627917841032:CostAlertTopic"

# Low threshold for testing. Change to 50.0 after testing.
THRESHOLD = 50.0

def lambda_handler(event, context):

    today = datetime.utcnow().date()

    start = today.replace(day=1).strftime("%Y-%m-%d")
    end = today.strftime("%Y-%m-%d")

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = float(
        response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    )

    print(f"Current Month Cost: ${amount:.2f}")

    if amount >= THRESHOLD:

        message = f"""
AWS Cost Alert

Current Month Spend: ${amount:.2f}

Threshold: ${THRESHOLD:.2f}

Please review your AWS resources.
"""

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Cost Alert",
            Message=message
        )

        print("Alert sent.")

    else:
        print("Threshold not exceeded.")

    return {
        "statusCode": 200,
        "current_cost": amount
    }