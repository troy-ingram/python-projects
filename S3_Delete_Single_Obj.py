import boto3

s3_resource=boto3.client("s3")
s3_resource.delete_object(
    Bucket="pythoncoursebucket5927389",
    Key="Create_S3_Public.py"
    )