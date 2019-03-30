from model.sample import Sample


class SampleReader:
    """Class responsible for reading data of samples from a file."""
    def read(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        samples = []
        for line in lines:
            features = line.split(',')
            """We use the [0] trick at feature[19] to take only the value of histology and not the new line symbol."""
            features[19] = features[19][0]
            samples.append(Sample(features[0], features[1:]))
        return samples
