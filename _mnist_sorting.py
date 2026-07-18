



import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf
# # import matplotlib.pyplot as plt
# import os
import random




# Загрузка данных из .npy файлов
x_train = np.load('./armed_n_dangerous/mnist_data/x_train.npy')
y_train = np.load('./armed_n_dangerous/mnist_data/y_train.npy')
x_test = np.load('./armed_n_dangerous/mnist_data/x_test.npy')
y_test = np.load('./armed_n_dangerous/mnist_data/y_test.npy')

# Проверка размеров данных
print("Размеры данных:")
print(f"x_train: {x_train.shape}")  # (60000, 28, 28)
print(f"y_train: {y_train.shape}")  # (60000,)
print(f"x_test: {x_test.shape}")    # (10000, 28, 28)
print(f"y_test: {y_test.shape}")    # (10000,)



# Сохранение всех изображений файлов:
from PIL import Image

# print(type(y_train))
# print(type(y_train[0]))

L = [[i, 0] for i in range(10)]

# for i in range(len(x_train)):
for i in range(len(x_train)):
    # Конвертируем в PIL Image
    img = Image.fromarray(x_train[i])
    # Сохраняем
    d = y_train[i]
    img.save(f'./armed_n_dangerous/_mnist_sorted/digit_{d}_{L[d][1] + 1}.png')
    L[d][1] += 1

