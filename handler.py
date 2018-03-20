import numpy as np
import json
import base64
import logging


def classify(event, context):
    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)

    data = json.loads(event['body'])

    if 'image' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't classify image")
        return

    img = base64.decodestring(data['image'])

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "shape": a.shape[0]
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

if __name__ == "__main__":
    classify('', '')
