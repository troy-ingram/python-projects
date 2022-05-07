import boto3

s3_resource=boto3.client("s3")

objects = s3_resource.list_objects(Bucket='pythoncoursebucket5927389')["Contents"]
if len(objects)>0:
    print("objects exist:")
    for object in objects:
        print(object["Key"])
