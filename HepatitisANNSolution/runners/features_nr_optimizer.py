from model.ann import ANN

data_file_name = 'hepatitis.data.txt'
nr_of_double_cross_validations = 5

hidden_layer_size = 13
momentum = True
stratify = True
epochs = 10
missing_values_treating_option = 'average'


results = []
for i in range(1, 11):
    ann = ANN(hidden_layer_size, momentum, i, stratify, epochs, missing_values_treating_option, data_file_name)
    acc, y_true, y_pred = ann.k_times_double_cross_validation(5)
    results.append((i, acc))
print(results)
