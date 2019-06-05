from model.sample import Sample
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
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


class Drawer:
    def print_chart(self, x, y, x_label, y_label, title):
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x, y, 'bo')
        plt.savefig('chart_' + x_label + '&' + y_label + '.png')
        plt.clf()
        plt.close()

    def print_confusion_matrix(self, y_true, y_pred, title):
        classes = ['die', 'live']
        cm = confusion_matrix(y_true, y_pred)
        fig, ax = plt.subplots()
        im = ax.imshow(cm, interpolation='nearest')
        ax.figure.colorbar(im, ax=ax)
        ax.set(xticks=np.arange(cm.shape[1]),
               yticks=np.arange(cm.shape[0]),
               xticklabels=classes, yticklabels=classes,
               title=title,
               ylabel='True label',
               xlabel='Predicted label')

        fmt = 'd'
        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], fmt),
                        ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black")
        fig.tight_layout()
        plt.savefig('matrix_' + title + '.png')
        plt.clf()
        plt.close()
