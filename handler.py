import numpy as np
import json

def classify(event, context):
    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)


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
