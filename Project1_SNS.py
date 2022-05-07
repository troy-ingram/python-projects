import boto3

client = boto3.client('sns')

response = client.create_topic(
    Name='Project-Topic'
)

# print(response['TopicArn'])

response = client.subscribe(
    TopicArn= response['TopicArn'],
    Protocol='email',
    Endpoint='troyingram86@gmail.com',
)