class SamplePresenter:
    """Class responsible for printing data of samples."""
    def print_sample(self, sample):
        for attr, value in sample.__dict__.items():
            print(attr + ': ' + value)
        return

    def print(self, samples):
        i = 1
        for sample in samples:
            print('Próbka numer ' + str(i))
            self.print_sample(sample)
            print('\n')
            i = i + 1
        return
