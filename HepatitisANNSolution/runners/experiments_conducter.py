from model.ann import ANN

silent = False
data_file_name = 'hepatitis.data.txt'

# Relation between hidden layer size and quality

hidden_layer_sizes = [5, 8, 13]

momentum = True
features = 4
stratify = True
epochs = [10]
missing_values_treating_option = 'average'

results = []
for i in range(0, len(hidden_layer_sizes)):
    ann = ANN(hidden_layer_sizes[i], momentum, features, stratify,
              epochs, missing_values_treating_option, data_file_name, silent)
    results.append(ann.k_times_double_cross_validation(5))

# Relation between using momentum and quality
momentum_options = [False, True]

hidden_layer_size = 8###
features = 4
stratify = True
epochs = [10]
missing_values_treating_option = 'average'

results = []
for i in range(0, len(momentum_options)):
    ann = ANN(hidden_layer_size, momentum_options[i], features, stratify,
              epochs, missing_values_treating_option, data_file_name, silent)
    results.append(ann.k_times_double_cross_validation(5))

# Relation between method of dealing with missing values and quality
missing_values_treating_options = ['average', 'median', 'removal']

hidden_layer_size = 8###
momentum = True
features = 4
stratify = True
epochs = [10]

results = []
for i in range(0, len(missing_values_treating_options)):
    ann = ANN(hidden_layer_size, momentum, features, stratify,
              epochs, missing_values_treating_options[i], data_file_name, silent)
    results.append(ann.k_times_double_cross_validation(5))

# Relation between number of features and quality
features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hidden_layer_size = 8###
momentum = True
stratify = True
epochs = [10]
missing_values_treating_option = 'average'

results = []
for i in range(0, len(features)):
    ann = ANN(hidden_layer_size, momentum, features[i], stratify,
              epochs, missing_values_treating_option, data_file_name, silent)
    results.append(ann.k_times_double_cross_validation(5))

# Relation between using stratification and quality
stratification_options = [False, True]

hidden_layer_size = 8###
momentum = True
features = 4
momentum = True
epochs = [10]
missing_values_treating_option = 'average'

results = []
for i in range(0, len(stratification_options)):
    ann = ANN(hidden_layer_size, momentum, features, stratification_options[i],
              epochs, missing_values_treating_option, data_file_name, silent)
    results.append(ann.k_times_double_cross_validation(5))

# Relation between number of iterations and quality
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hidden_layer_size = 8###
momentum = True
features = 4
momentum = True
stratify = True
missing_values_treating_option = 'average'

results = []
for i in range(0, len(epochs)):
    ann = ANN(hidden_layer_sizes, momentum, features, stratify,
              epochs[i], missing_values_treating_option, data_file_name, silent)
    results.append(ann.k_times_double_cross_validation(5))

# Relation between number of iterations and time
