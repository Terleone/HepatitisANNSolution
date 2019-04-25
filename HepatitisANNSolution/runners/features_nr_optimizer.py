from model.ann import ANN

data_file_name = 'hepatitis.data.txt'
nr_of_double_cross_validations = 5
momentum = False
hidden_layer_size = 13


results = []
for i in range(1, 11):
    ann = ANN(hidden_layer_size, momentum, i, data_file_name)
    results.append((i, ann.k_times_double_cross_validation(5)))
print(results)
