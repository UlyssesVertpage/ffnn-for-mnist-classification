
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# # import matplotlib.pyplot as plt
# import os
import random


# # Загрузка данных MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# # Создание папки для сохранения данных
# os.makedirs('./armed_n_dangerous/mnist_data', exist_ok=True)

# Сохранение данных в файлы .npy
np.save('./armed_n_dangerous/mnist_data/x_train.npy', x_train)
np.save('./armed_n_dangerous/mnist_data/y_train.npy', y_train)
np.save('./armed_n_dangerous/mnist_data/x_test.npy', x_test)
np.save('./armed_n_dangerous/mnist_data/y_test.npy', y_test)





