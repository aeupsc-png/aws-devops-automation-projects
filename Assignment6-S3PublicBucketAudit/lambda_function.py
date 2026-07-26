import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:627917841032:S3PublicBucketAlert"


def lambda_handler(event, context):

    public_buckets = []

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        bucket_name = bucket["Name"]

        print(f"Checking bucket: {bucket_name}")

        public = False

        # Check Block Public Access
        try:
            response = s3.get_public_access_block(Bucket=bucket_name)
            config = response["PublicAccessBlockConfiguration"]

            if not all(config.values()):
                public = True
                print(f"{bucket_name}: Block Public Access disabled")

        except s3.exceptions.NoSuchPublicAccessBlockConfiguration:
            public = True
            print(f"{bucket_name}: No Public Access Block configuration")

        except Exception as e:
            print(e)

        # Check Bucket Policy
        try:
            policy = s3.get_bucket_policy_status(Bucket=bucket_name)

            if policy["PolicyStatus"]["IsPublic"]:
                public = True
                print(f"{bucket_name}: Public bucket policy detected")

        except Exception:
            pass

        # Check ACL
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)

            for grant in acl["Grants"]:
                grantee = grant.get("Grantee", {})

                if (
                    grantee.get("Type") == "Group"
                    and "AllUsers" in grantee.get("URI", "")
                ):
                    public = True
                    print(f"{bucket_name}: Public ACL detected")

        except Exception:
            pass

        if public:
            public_buckets.append(bucket_name)

    if public_buckets:

        message = (
            "Public S3 Bucket(s) Detected:\n\n"
            + "\n".join(public_buckets)
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="S3 Public Bucket Alert",
            Message=message
        )

        print("SNS alert sent.")

    else:
        print("No public buckets found.")

    return {
        "statusCode": 200,
        "publicBuckets": public_buckets
    }