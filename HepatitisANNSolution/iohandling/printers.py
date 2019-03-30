from model.sample import Sample


class SamplePresenter:
    """Class responsible for printing data of samples."""
    def print_sample(self, sample):
        for i in range(len(sample.attributes)):
            print(Sample.labels[i] + ': ' + sample.attributes[i])
        return

    def print(self, samples):
        i = 1
        for sample in samples:
            print('Próbka numer ' + str(i))
            self.print_sample(sample)
            print('\n')
            i = i + 1
        return
