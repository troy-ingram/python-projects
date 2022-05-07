import boto3

#upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Create_S3_Public.py",
    Bucket="pythoncoursebucket5927389",
    Key="upload.txt"
    )