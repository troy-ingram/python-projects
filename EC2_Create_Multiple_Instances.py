import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(
    ImageId='ami-03ededff12e34e59e',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2
    )