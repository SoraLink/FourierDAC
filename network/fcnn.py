import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

class FulleyConnectNN:
    def __init__(self, input_shape, output_shape):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.net = self.create_network

    def create_network(self):
        model = Sequential([
            Dense(32, activation='relu', input_shape=self.input_shape),
            Dense(32,activation='softmax',),
        ])
        