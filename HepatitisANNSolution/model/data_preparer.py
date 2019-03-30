from sklearn.model_selection import train_test_split
import numpy


class DataPreparer:
    """Class responsible for preparing data sets for training and testing."""
    def prepare_data(self, samples):
        return train_test_split(samples, test_size=0.5)
