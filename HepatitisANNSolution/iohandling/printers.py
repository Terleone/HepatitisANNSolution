from model.sample import Sample
import matplotlib.pyplot as plt
import numpy as np

class SamplePresenter:
    """Class responsible for printing data of samples."""
    def print_sample(self, sample, ranked):
        for i in range(len(sample.attributes)):
            print(Sample.ranked_labels[i] if ranked else Sample.labels[i] + ': ' + sample.attributes[i])
        return

    def print(self, samples, ranked=False):
        i = 1
        for sample in samples:
            print('Próbka numer ' + str(i))
            self.print_sample(sample, ranked)
            print('\n')
            i = i + 1
        return


class ChartDrawer:
    def print_chart(self, x, y, x_label, y_label, title):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x, y, 'bo')
        plt.savefig(y_label + '_and_' + x_label + '.png')
