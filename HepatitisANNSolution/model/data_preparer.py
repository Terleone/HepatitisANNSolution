from sklearn.model_selection import train_test_split
import numpy as np


class DataPreparer:
    """Class responsible for preparing data sets for training and testing."""
    def prepare_data(self, samples, features, stratify, missing_values_option):
        for sample in samples:
            sample.convert_to_ranked()
            #sample.question_mark_to_min_int()
        samples = self.handle_missing_values(samples, features, missing_values_option)
        (train_samples, test_samples) = train_test_split(samples, test_size=0.5,
                                                         stratify=[sample.classification for sample in samples]
                                                         if stratify else None)

        train_attributes = np.empty(shape=(len(train_samples), features))
        train_labels = np.empty(shape=len(train_samples))
        for i in range(len(train_samples)):
            sample = train_samples[i]
            train_attributes[i] = sample.attributes[0:features]
            train_labels[i] = sample.classification
        test_attributes = np.empty(shape=(len(test_samples), features))
        test_labels = np.empty(shape=len(test_samples))
        for i in range(len(test_samples)):
            sample = test_samples[i]
            test_attributes[i] = sample.attributes[0:features]
            test_labels[i] = sample.classification
        return (train_attributes, train_labels), (test_attributes, test_labels)

    def handle_missing_values(self, samples, features, missing_values_option):

        if missing_values_option == 'average':
            averages = []
            for i in range(0, features):
                partial_sum = 0.0
                for sample in samples:
                    feature = sample.attributes[i]
                    if feature != '?':
                        partial_sum = partial_sum + float(feature)
                averages.append(partial_sum / len(samples))
            for sample in samples:
                for i in range(0, features):
                    if sample.attributes[i] == '?':
                        sample.attributes[i] = averages[i]
        elif missing_values_option == 'median':
            medians = []
            for i in range(0, features):
                values = [sample.attributes[i] for sample in samples]
                values.sort()
                length = len(values)
                medians.append(values[int(length / 2)] if length % 2 == 0
                               else float(values[int(length / 2)]) + float(values[int((length / 2)) - 1]))
            for sample in samples:
                for i in range(0, features):
                    if sample.attributes[i] == '?':
                        sample.attributes[i] = medians[i]
        elif missing_values_option == 'removal':
            new_samples = filter(lambda s: '?' not in s.attributes, samples)
            samples = new_samples
        else:
            raise Exception('missing_values_option has improper value.')
        return samples
