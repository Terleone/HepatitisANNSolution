from _datetime import datetime
from model.ann import ANN

silent = False
data_file_name = 'hepatitis.data.txt'

# Experiments' parameters
hidden_layer_sizes = [5]#, 8, 13]
momentum_options = [False]#, True]
features = [1]#, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stratify_options = [False]#, True]
epochs = [1]#, 2, 3, 4, 5, 6, 7, 8, 9, 10]
missing_values_treating_options = ['average']#, 'median', 'removal']

file = open('results.txt', 'a')
file.write('\nResults from ' + str(datetime.now())
           + '\nhidden layer sizes: ' + str(hidden_layer_sizes) + '\n')
for i in range(0, len(hidden_layer_sizes)):
    for j in range(0, len(momentum_options)):
        for k in range(0, len(features)):
            for l in range(len(stratify_options)):
                for m in range(len(epochs)):
                    for n in range(len(missing_values_treating_options)):
                        ann = ANN(hidden_layer_sizes[i], momentum_options[j], features[k], stratify_options[l],
                                  epochs[m], missing_values_treating_options[n], data_file_name, silent)
                        acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
                        file.write('\n***ENTRY START***\nHidden layer size: ' + str(hidden_layer_sizes[i])
                                   + '\nWith momentum: ' + str(momentum_options[j])
                                   + '\nNumber of features: ' + str(features[k])
                                   + '\nWith stratification: ' + str(stratify_options[l])
                                   + '\nNumber of iterations: ' + str(epochs[m])
                                   + '\nMissing values treating: ' + str(missing_values_treating_options[n])
                                   + '\nAccuracy result = ' + str(acc)
                                   + '\n***ENTRY END***\n')

file.close()
