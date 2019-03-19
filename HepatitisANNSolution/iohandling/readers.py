from model.sample import Sample


class SampleReader:
    """Class responsible for reading data of samples from a file."""
    def read(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        samples = []
        """We use the [0] trick at feature[19] to take only the value of histology and not the new line symbol."""
        for line in lines:
            features = line.split(',')
            samples.append(Sample(features[0], features[1], features[2], features[3], features[4],
                                  features[5], features[6], features[7], features[8], features[9],
                                  features[10], features[11], features[12], features[13], features[14],
                                  features[15], features[16], features[17], features[18], features[19][0]))
        return samples
