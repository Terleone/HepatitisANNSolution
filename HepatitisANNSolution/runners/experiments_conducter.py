from model.ann import ANN
from iohandling.printers import Drawer
from timeit import default_timer as timer


silent = False
data_file_name = 'hepatitis.data.txt'
drawer = Drawer()

# Relation between hidden layer size and quality

hidden_layer_sizes = [5]#, 8, 13]

momentum = True
features = 4
stratify = True
epochs = 10
missing_values_treating_option = 'average'

acc_results = []
for i in range(0, len(hidden_layer_sizes)):
    ann = ANN(hidden_layer_sizes[i], momentum, features, stratify,
              epochs, missing_values_treating_option, data_file_name, silent)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    acc_results.append(acc)
    drawer.print_confusion_matrix(y_true, y_pred, 'Hidden layer size research: ' + str(hidden_layer_sizes[i]))

drawer.print_chart(hidden_layer_sizes, acc_results, 'Hidden layer size', 'Accuracy',
                   'Relation between hidden layer size and accuracy')

# Relation between using momentum and quality
momentum_options = [False, True]

hidden_layer_size = 13
features = 4
stratify = True
epochs = 10
missing_values_treating_option = 'average'

acc_results = []
for i in range(0, len(momentum_options)):
    ann = ANN(hidden_layer_size, momentum_options[i], features, stratify,
              epochs, missing_values_treating_option, data_file_name, silent)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    acc_results.append(acc)
    drawer.print_confusion_matrix(y_true, y_pred, 'Momentum research: ' + str(momentum_options[i]))

drawer.print_chart([str(option) for option in momentum_options], acc_results, 'Momentum options', 'Accuracy',
                   'Relation between using momentum and accuracy')

# Relation between method of dealing with missing values and quality
missing_values_treating_options = ['average', 'median', 'removal']

hidden_layer_size = 13
momentum = True
features = 4
stratify = True
epochs = 10

acc_results = []
for i in range(0, len(missing_values_treating_options)):
    ann = ANN(hidden_layer_size, momentum, features, stratify,
              epochs, missing_values_treating_options[i], data_file_name, silent)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    acc_results.append(acc)
    drawer.print_confusion_matrix(y_true, y_pred, 'Dealing with missing values research: '
                                  + str(missing_values_treating_options[i]))

drawer.print_chart(missing_values_treating_options, acc_results, 'Missing values treating options', 'Accuracy',
                   'Relation between using\ndifferent methods of treating\nmissing values and accuracy')

# Relation between number of features and quality
features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hidden_layer_size = 13
momentum = True
stratify = True
epochs = 10
missing_values_treating_option = 'average'

acc_results = []
for i in range(0, len(features)):
    ann = ANN(hidden_layer_size, momentum, features[i], stratify,
              epochs, missing_values_treating_option, data_file_name, silent)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    acc_results.append(acc)
    drawer.print_confusion_matrix(y_true, y_pred, 'Number of features research: ' + str(features[i]))

drawer.print_chart(features, acc_results, 'Number of features', 'Accuracy',
                   'Relation between number\nof features and accuracy')

# Relation between using stratification and quality
stratification_options = [False, True]

hidden_layer_size = 13
momentum = True
features = 4
epochs = 10
missing_values_treating_option = 'average'

acc_results = []
for i in range(0, len(stratification_options)):
    ann = ANN(hidden_layer_size, momentum, features, stratification_options[i],
              epochs, missing_values_treating_option, data_file_name, silent)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    acc_results.append(acc)
    drawer.print_confusion_matrix(y_true, y_pred, 'Stratification research: ' + str(stratification_options[i]))

drawer.print_chart([str(option) for option in stratification_options], acc_results, 'Stratification options', 'Accuracy',
                   'Relation between using\nstratification and accuracy')

# Relation between number of iterations and quality
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hidden_layer_size = 13
momentum = True
features = 4
stratify = True
missing_values_treating_option = 'average'

acc_results = []
time_acc_results = []
for i in range(0, len(epochs)):
    start_time = timer()
    ann = ANN(hidden_layer_size, momentum, features, stratify,
              epochs[i], missing_values_treating_option, data_file_name, silent)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    acc_results.append(acc)
    time_acc_results.append(timer() - start_time)
    drawer.print_confusion_matrix(y_true, y_pred, 'Number of iterations research: ' + str(epochs[i]))

drawer.print_chart(epochs, acc_results, 'Number of iterations', 'Accuracy',
                   'Relation between number\nof iterations and accuracy')

# Relation between number of iterations and time

drawer.print_chart(epochs, time_acc_results, 'Number of iterations', 'Time [s]',
                   'Relation between number\nof iterations and time')
