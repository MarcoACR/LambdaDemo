import json
import boto3


def handler(event, context):
    print(event)
    return {'statusCode': 200, 'body': 'Success!'}
