import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client('ec2')

VOLUME_ID = "vol-02d9587a9f05a6330"

# Change back to 30 for final submission
RETENTION_DAYS = 30

def lambda_handler(event, context):

    response = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Created by Lambda Automation"
    )

    snapshot_id = response["SnapshotId"]

    ec2.create_tags(
        Resources=[snapshot_id],
        Tags=[
            {
                "Key": "CreatedBy",
                "Value": "Lambda-Backup"
            }
        ]
    )

    print(f"Created Snapshot: {snapshot_id}")

    snapshots = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:CreatedBy",
                "Values": ["Lambda-Backup"]
            }
        ]
    )["Snapshots"]

    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

    deleted = []

    for snapshot in snapshots:
        if snapshot["StartTime"] < cutoff:
            ec2.delete_snapshot(
                SnapshotId=snapshot["SnapshotId"]
            )
            print(f"Deleted Snapshot: {snapshot['SnapshotId']}")
            deleted.append(snapshot["SnapshotId"])

    return {
        "statusCode": 200,
        "created_snapshot": snapshot_id,
        "deleted_snapshots": deleted
    }