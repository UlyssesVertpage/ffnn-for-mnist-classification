



import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow as tf
# # import matplotlib.pyplot as plt
# import os
# import random




# Загрузка данных из .npy файлов
X = np.load('./armed_n_dangerous/mnist_data/x_train.npy')
Y = np.load('./armed_n_dangerous/mnist_data/y_train.npy')

# Проверка размеров данных
print("Размеры данных:")
print(f"x_test: {X.shape}")    # (10000, 28, 28)
print(f"y_test: {Y.shape}")    # (10000,)

# print(type(Y))      # <class 'numpy.ndarray'>
# print(type(Y[0]))   # <class 'numpy.uint8'>

X_train = X[:10000]
Y_train = Y[:10000]
X_test = X[10000:13000]
Y_test = Y[10000:13000]

print("Размеры данных:")
print(f"X_train: {X_train.shape}")    # (10000, 28, 28)
print(f"Y_train: {Y_train.shape}")    # (10000,)
print(f"X_test: {X_test.shape}")    # (10000, 28, 28)
print(f"Y_test: {Y_test.shape}")    # (10000,)


# # Сохранение данных в файлы .npy
np.save('./armed_n_dangerous/mnist_data_10000/x_train.npy', X_train)
np.save('./armed_n_dangerous/mnist_data_10000/y_train.npy', Y_train)
np.save('./armed_n_dangerous/mnist_data_10000/x_test.npy', X_test )
np.save('./armed_n_dangerous/mnist_data_10000/y_test.npy', Y_test )














