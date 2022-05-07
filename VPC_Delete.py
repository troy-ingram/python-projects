import boto3

client = boto3.client("ec2")

client.delete_vpc(
    VpcId="vpc-057c43483242773df"
    )
