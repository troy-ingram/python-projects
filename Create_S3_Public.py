import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("testbucket097359275834720743029592")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

print(response)