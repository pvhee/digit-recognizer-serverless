import json
import random

def classify(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "class": random.randrange(0,100),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
