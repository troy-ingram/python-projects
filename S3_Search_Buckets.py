import boto3

resource=boto3.resource("s3")
print("You have " + str(len(list(resource.buckets.all()))) + " S3 Buckets")
for i in resource.buckets.all():
    print(i.name)