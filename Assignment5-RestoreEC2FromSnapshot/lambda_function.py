import boto3
import time
from datetime import datetime

ec2 = boto3.client("ec2")

VOLUME_ID = "vol-xxxxxxxxxxxxxxxxx"
ROOT_DEVICE = "/dev/xvda"


def lambda_handler(event, context):

    snapshots = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "volume-id",
                "Values": [VOLUME_ID]
            }
        ]
    )["Snapshots"]

    snapshots.sort(
        key=lambda s: s["StartTime"],
        reverse=True
    )

    latest_snapshot = snapshots[0]["SnapshotId"]

    print(f"Latest Snapshot: {latest_snapshot}")

    ami = ec2.register_image(
        Name=f"restore-{int(time.time())}",
        RootDeviceName=ROOT_DEVICE,
        BlockDeviceMappings=[
            {
                "DeviceName": ROOT_DEVICE,
                "Ebs": {
                    "SnapshotId": latest_snapshot
                }
            }
        ]
    )

    image_id = ami["ImageId"]

    print(f"AMI Created: {image_id}")

    waiter = ec2.get_waiter("image_available")
    waiter.wait(ImageIds=[image_id])

    print("AMI Available")

    instance = ec2.run_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.micro"
    )

    instance_id = instance["Instances"][0]["InstanceId"]

    print(f"New Instance: {instance_id}")

    return {
        "statusCode": 200,
        "snapshot": latest_snapshot,
        "ami": image_id,
        "instance": instance_id
    }