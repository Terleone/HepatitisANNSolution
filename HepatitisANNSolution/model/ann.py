import tensorflow as tf
from tensorflow import keras
from iohandling.readers import SampleReader
from model.data_preparer import DataPreparer


class ANN:
    def __init__(self, hidden_layer_size, momentum, features, data_file_name):
        self.hidden_layer_size = hidden_layer_size
        self.momentum = momentum
        self.features = features
        self.data_file_name = data_file_name
        return

    def train_test_cycle(self):
        (train_attributes, train_labels), (test_attributes, test_labels) =\
            DataPreparer().prepare_data(SampleReader().read(self.data_file_name), self.features)
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(10,)),
            keras.layers.Dense(self.hidden_layer_size, activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax)
        ])
        model.compile(optimizer=keras.optimizers.SGD(lr=0.01, momentum=(1.0 if self.momentum else 0.0),
                                                     decay=0.0, nesterov=False),
                      loss='mean_absolute_error',
                      metrics=['accuracy'])
        model.fit(train_attributes, train_labels, 1)
        return
