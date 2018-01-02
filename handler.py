import json
import random
import keras
from keras.models import Sequential
from keras import layers
from keras.datasets import mnist
from keras import backend as K

def classify(event, context):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "class": random.randrange(0,100),
        "x_train": x_train.shape[0],
        "x_test": x_test.shape[0],
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
