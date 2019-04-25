from _datetime import datetime
from model.ann import ANN

silent = True
data_file_name = 'hepatitis.data.txt'
nr_of_double_cross_validations = 5
features = 6

hidden_layer_sizes = [5, 8, 13]
momentum_options = [False, True]

file = open('results.txt', 'a')
file.write('\nResults from ' + str(datetime.now())
           + '\nhidden layer sizes: ' + str(hidden_layer_sizes) + '\n')
for i in range(0, len(hidden_layer_sizes)):
    for j in range(0, len(momentum_options)):
        ann = ANN(hidden_layer_sizes[i], momentum_options[j], features, data_file_name, silent)
        file.write('Hidden layer size:' + str(hidden_layer_sizes[i]) + '\n'
                   + 'With momentum: ' + str(momentum_options[j]) + '\n'
                   + str(ann.k_times_double_cross_validation(5)) + '\n')

file.close()
