import boto3
import os
import glob

s3_resource=boto3.client("s3")
#list all bucket objects
objects=s3_resource.list_objects(Bucket="pythoncoursebucket5927389")["Contents"]

#loop through and list all objects
for object in objects:
    print(object["Key"]+"...")
    s3_resource.delete_object(
        Bucket="pythoncoursebucket5927389",
        Key=object["Key"]
        )
    print("Deleted")