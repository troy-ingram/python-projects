import boto3

client=boto3.client("ec2")

response = client.describe_vpcs()
# print(response)

vpcs = client.describe_vpcs()["Vpcs"]
for vpc in vpcs:
    print(vpc["VpcId"])