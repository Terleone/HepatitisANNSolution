from iohandling.readers import SampleReader
from iohandling.printers import SamplePresenter
from model.sample import Sample
from scipy import stats

data_file_name = 'hepatitis.data.txt'

reader = SampleReader()
samples = reader.read(data_file_name)
presenter = SamplePresenter()
presenter.print(samples)

ranking = []
"""Creating an empty Sample object to iterate over names of it's attributes."""


for i in range(len(Sample.labels)):
    die = []
    live = []
    for sample in samples:
        if sample.classification == '1':
            die.append(sample.attributes[i])
        elif sample.classification == '2':
            live.append(sample.attributes[i])
    result = stats.ks_2samp(die, live)
    if result[1] <= 0.1:
        ranking.append((Sample.labels[i], result[0]))

    print('Wynik dla cechy ' + Sample.labels[i] + ':\n\t'
        + 'statistics = ' + str(result[0]) + '\n\t'
        + 'pvalue = ' + str(result[1]) + '\n')

ranking.sort(key=lambda tup: tup[1], reverse=True)
print("Cechy wedlug przydatnosci:")
for feature in ranking:
    print("\t" + feature[0])
