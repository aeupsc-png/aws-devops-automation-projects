import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = "maahi-s3-cleanup-2026"

# Change this back to 30 for final submission
DAYS = 30

def lambda_handler(event, context):

    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS)

    paginator = s3.get_paginator('list_objects_v2')

    deleted = []

    for page in paginator.paginate(Bucket=BUCKET_NAME):

        if 'Contents' not in page:
            continue

        for obj in page['Contents']:

            if obj['LastModified'] < cutoff:

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=obj['Key']
                )

                print(f"Deleted: {obj['Key']}")
                deleted.append(obj['Key'])

    return {
        "statusCode": 200,
        "deleted_objects": deleted
    }