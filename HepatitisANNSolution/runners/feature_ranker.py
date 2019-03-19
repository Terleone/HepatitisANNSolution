from iohandling.readers import SampleReader
from iohandling.printers import SamplePresenter
from model.sample import Sample
from scipy import stats

data_file_name = 'hepatitis.data.txt'

reader = SampleReader()
samples = reader.read(data_file_name)
presenter = SamplePresenter()
presenter.print(samples)

"""Creating an empty Sample object to iterate over names of it's attributes."""
for feature_name, none in Sample('', '', '', '', '', '', '', '', '', '',
                                 '', '', '', '', '', '', '', '', '', '', ).__dict__.items():
    if feature_name == 'classification':
        continue
    die = []
    live = []
    for sample in samples:
        if sample.classification == '1':
            die.append(getattr(sample, feature_name))
        elif sample.classification == '2':
            live.append(getattr(sample, feature_name))
    result = stats.ks_2samp(die, live)
    print('Wynik dla cechy ' + feature_name + ':\n\t'
          + 'statistics = ' + str(result[0]) + '\n\t'
          + 'pvalue = ' + str(result[1]) + '\n')
