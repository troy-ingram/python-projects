import boto3
import os
import glob

cwd=os.getcwd()
files=glob.glob(cwd+"/*.py")
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="pythoncoursebucket5927389",
    Key=file.split("/")[-1]
    )