import tensorflow as tf
from tensorflow import keras
from iohandling.readers import SampleReader
from model.data_preparer import DataPreparer


class ANN:
    def __init__(self, hidden_layer_size, momentum, features, stratify, epochs, missing_values_treating,
                 data_file_name, silent=False):
        self.hidden_layer_size = hidden_layer_size
        self.momentum = momentum
        self.features = features
        self.stratify = stratify
        self.epochs = epochs
        self.missing_values_treating = missing_values_treating
        self.data_file_name = data_file_name
        self.silent = silent
        return

    def k_times_double_cross_validation(self, k):
        acc_sum = 0.0
        y_true = []
        y_pred = []
        for i in range(0, k):
            partial_acc_sum, partial_y_true, partial_y_pred = self.double_cross_validation()
            acc_sum = acc_sum + partial_acc_sum
            y_true = y_true + partial_y_true
            y_pred = y_pred + partial_y_pred
        return acc_sum / k, y_true, y_pred

    def double_cross_validation(self):
        (train_attributes, train_labels), (test_attributes, test_labels) =\
            DataPreparer().prepare_data(SampleReader().read(self.data_file_name), self.features,
                                        self.stratify, self.missing_values_treating)
        acc1, y_true1, y_pred1 = self.train_test_cycle(train_attributes, train_labels, test_attributes, test_labels)
        acc2, y_true2, y_pred2 = self.train_test_cycle(test_attributes, test_labels, train_attributes, train_labels)
        return (acc1 + acc2) / 2, self.to_array(y_true1, y_true2), self.to_array(y_pred1, y_pred2)

    def train_test_cycle(self, train_attributes, train_labels, test_attributes, test_labels):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(self.features,)),
            keras.layers.Dense(self.hidden_layer_size, activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax)
        ])
        model.compile(optimizer=keras.optimizers.SGD(lr=0.01, momentum=(1.0 if self.momentum else 0.0),
                                                     decay=0.0, nesterov=False),
                      loss='mean_absolute_error',
                      metrics=['accuracy'])
        model.fit(x=train_attributes, y=train_labels, batch_size=1, epochs=self.epochs,
                  verbose=1 if not self.silent else 0)
        y_pred = model.predict_classes(test_attributes, 1)
        scores = model.evaluate(test_attributes, test_labels)
        if not self.silent:
            print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        return scores[1], test_labels, y_pred

    def to_array(self, numpy_array1, numpy_array2):
        array = []
        for i in range(0, len(numpy_array1)):
            array.append(numpy_array1[i])
        for i in range(0, len(numpy_array2)):
            array.append(numpy_array2[i])
        return array
