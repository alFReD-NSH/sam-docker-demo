import json
import selenium
import pandas
import boto3
import os

print('1')

S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print(boto3.client('s3').list_bucket(S3_BUCKET_NAME))

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
