from iohandling.readers import SampleReader
from iohandling.printers import SamplePresenter

data_file_name = 'hepatitis.data.txt'

reader = SampleReader()
samples = reader.read(data_file_name)
presenter = SamplePresenter()
presenter.print(samples)
