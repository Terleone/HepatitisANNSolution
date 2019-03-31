from sklearn.model_selection import train_test_split
import numpy as np


class DataPreparer:
    """Class responsible for preparing data sets for training and testing."""
    def prepare_data(self, samples, features):
        for sample in samples:
            sample.convert_to_ranked()
            sample.question_mark_to_min_int()
        (train_samples, test_samples) = train_test_split(samples, test_size=0.5)

        train_attributes = np.empty(shape=(len(train_samples), 10))
        train_labels = np.empty(shape=len(train_samples))
        for i in range(len(train_samples)):
            sample = train_samples[i]
            train_attributes[i] = sample.attributes[0:features]
            train_labels[i] = sample.classification
        test_attributes = np.empty(shape=(len(test_samples), 10))
        test_labels = np.empty(shape=len(test_samples))
        for i in range(len(test_samples)):
            sample = test_samples[i]
            test_attributes[i] = sample.attributes[0:features]
            test_labels[i] = sample.classification
        return (train_attributes, train_labels), (test_attributes, test_labels)
