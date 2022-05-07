import boto3
import random

# Create a Standard SQS Queue
client = boto3.client('sqs')

response = client.create_queue(
    QueueName='LUIT-Python',
    tags={
        'Name': 'LUIT-Python'
    }
)

# Create a Lambda function with a Python 3.6 or higher runtime 



#Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.
# sqs = boto3.resource('sqs')
# queue = sqs.Queue('https://sqs.us-east-1.amazonaws.com/254735530617/MyTest')

# message_text = str(random.randint(0,100))

# response = queue.send_message(
#     MessageBody= message_text,
# )


# Create an API gateway with a HTTP API type




# Set the API gateway as a trigger for the Lambda you created