from model.ann import ANN


data_file_name = 'hepatitis.data.txt'
features = 10
momentum = False
hidden_layer_size = 13

ann = ANN(hidden_layer_size, momentum, features, data_file_name)
ann.train_test_cycle()
