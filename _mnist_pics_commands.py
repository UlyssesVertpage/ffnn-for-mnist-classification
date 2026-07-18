
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf
# # import matplotlib.pyplot as plt
# import os
import random


# # Загрузка данных MNIST
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# # Создание папки для сохранения данных
# os.makedirs('./armed_n_dangerous/mnist_data', exist_ok=True)

# # Сохранение данных в файлы .npy
# np.save('./armed_n_dangerous/mnist_data/x_train.npy', x_train)
# np.save('./armed_n_dangerous/mnist_data/y_train.npy', y_train)
# np.save('./armed_n_dangerous/mnist_data/x_test.npy', x_test)
# np.save('./armed_n_dangerous/mnist_data/y_test.npy', y_test)








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






# # Просмотр одной случайной цифры
# index = random.randint(0, len(x_train) - 1)
# print(f"\nПросмотр цифры с индексом {index}:")
# print(f"Метка: {y_train[index]}")

# plt.figure(figsize=(6, 6))
# plt.imshow(x_train[index], cmap='gray')
# plt.title(f'Цифра: {y_train[index]}')
# plt.axis('off')
# plt.show()



# # Просмотр первых 25 цифр из тренировочного набора
# plt.figure(figsize=(10, 10))
# for i in range(25):
#     plt.subplot(5, 5, i + 1)
#     plt.imshow(x_train[i], cmap='gray')
#     plt.title(f'Метка: {y_train[i]}')
#     plt.axis('off')
# plt.tight_layout()
# plt.show()



# # Просмотрим по 3 примера каждой цифры (от 0 до 9)
# fig, axes = plt.subplots(3, 10, figsize=(15, 5))

# for digit in range(10):
#     # Найдем индексы для текущей цифры
#     indices = np.where(y_train == digit)[0][:3]
    
#     for i, idx in enumerate(indices):
#         axes[i, digit].imshow(x_train[idx], cmap='gray')
#         axes[i, digit].set_title(f'Цифра: {digit}')
#         axes[i, digit].axis('off')

# plt.tight_layout()
# plt.show()



# # Детальная информация о данных
# print("Детальная информация о MNIST данных:")
# print(f"Количество тренировочных примеров: {len(x_train)}")
# print(f"Количество тестовых примеров: {len(x_test)}")
# print(f"Размер изображения: {x_train[0].shape}")
# print(f"Тип данных: {x_train.dtype}")
# print(f"Диапазон значений пикселей: [{x_train.min()}, {x_train.max()}]")

# # Распределение цифр в тренировочном наборе
# unique, counts = np.unique(y_train, return_counts=True)
# print("\nРаспределение цифр в тренировочном наборе:")
# for digit, count in zip(unique, counts):
#     print(f"Цифра {digit}: {count} примеров ({count/len(y_train)*100:.1f}%)")

# # Распределение цифр в тестовом наборе
# unique_test, counts_test = np.unique(y_test, return_counts=True)
# print("\nРаспределение цифр в тестовом наборе:")
# for digit, count in zip(unique_test, counts_test):
#     print(f"Цифра {digit}: {count} примеров ({count/len(y_test)*100:.1f}%)")



# # Функция для интерактивного просмотра
# def interactive_view(dataset_x, dataset_y, start_index=0):
#     fig, ax = plt.subplots(figsize=(8, 8))
    
#     def update_display(index):
#         ax.clear()
#         ax.imshow(dataset_x[index], cmap='gray')
#         ax.set_title(f'Индекс: {index}, Цифра: {dataset_y[index]}')
#         ax.axis('off')
#         plt.draw()
    
#     update_display(start_index)
    
#     def on_key(event):
#         nonlocal start_index
#         if event.key == 'right':
#             start_index = (start_index + 1) % len(dataset_x)
#         elif event.key == 'left':
#             start_index = (start_index - 1) % len(dataset_x)
#         update_display(start_index)
    
#     fig.canvas.mpl_connect('key_press_event', on_key)
#     plt.show()

# # Использование интерактивного просмотра
# print("Используйте стрелки ← → для навигации")
# interactive_view(x_train, y_train)



# print(x_train[0], y_train[0])
# print(x_train[1], y_train[1])
# print(x_train[2], y_train[2])



# # Сохранение нескольких изображений как отдельные файлы:
# from PIL import Image
# import os

# # Создаем папку для примеров
# os.makedirs('./armed_n_dangerous/mnist_examples', exist_ok=True)

# # Сохраняем несколько примеров как PNG файлы
# for i in range(10):
#     # Конвертируем в PIL Image
#     img = Image.fromarray(x_train[i])
#     # Сохраняем
#     img.save(f'./armed_n_dangerous/mnist_examples/digit_{y_train[i]}_{i}.png')

# print("10 изображений сохранены в папку './mnist_examples/'")




# # Посмотрим на числовые значения пикселей для одной цифры
# index = 0  # можно изменить на любой другой индекс
# print(f"Метка: {y_train[index]}")
# print("Матрица пикселей (28x28):")
# print(x_train[index])

# # Визуализация с числовыми значениями (первые 10x10 пикселей)
# plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(x_train[index], cmap='gray')
# plt.title(f'Полное изображение: {y_train[index]}')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# # Покажем только первые 10x10 пикселей для читаемости
# plt.imshow(x_train[index][:10, :10], cmap='gray')
# plt.title('Первые 10x10 пикселей')
# for i in range(10):
#     for j in range(10):
#         plt.text(j, i, f'{x_train[index][i, j]:3d}', 
#                 ha='center', va='center', fontsize=8)
# plt.axis('off')

# plt.tight_layout()
# plt.show()