






# class fnnmodel:


# a1 = 131983
# print(len(f'{id(a1):x}'))
# print(f'{id(a1):x}')








# L1 = [0,1,2,3,4,5,6]

# L1.append(4)
# print(L1)
# print(L1.pop())
# print(L1)

# print(L1.index(4))
# L1.insert(2, 7)
# print(L1)
# print(L1.__add__([8]))




# class Mine:
#     def __init__(self):
#         print("init.")
#     def __repr__(self):
#         # print("repr.")
#         return "repr."
#     def __call__(self, *args, **kwds):
#         print("call.")

# mine = Mine()         # __init__
# print(mine)           # __repr__
# mine()                # __call__






import numpy as np

# a = np.array([[2, 0], [0, 2]])
# b = np.array([[1, 1], [1, 1]])
# print(a*b)                    # [[2 0][0 2]]
# print(np.matmul(a,b))         # [[2 2][2 2]]

# a = np.array([[1, 3], [5, 7]])
# b = np.array([[2, 4], [6, 8]])
# print(a*b)                    # [[ 2 12][30 56]]
# print(np.matmul(a, b))        # [[20 28][52 76]]
# ^^^^^^^^^^^^^^^^^^^^^^ this is same as 'print(a@b)'

# print(np.linspace(0, 10, 3))   # [ 0.  5. 10.]
# print(np.linspace(0, 10, 11))  # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

# a = np.array([[1,2,3], [4,5,6]])
# print(np.average(a))    # 3.5

# a = np.array([0, 1, 2, 3, 4])
# a[::2] = 2
# print(a)        # [2 1 2 3 2]

# print(np.empty(3))  # [4.22885582e-307 1.07047267e-312 1.02614709e-307]

# print(np.dtypes.)     # print(np.dtypes.__all__)

# a = np.array([[4,2,1], [6,3,5]])
# print(np.sort(a))
# print(a)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# print(np.concatenate((a, b), axis=0))   # [[1 2] [3 4] [5 6]]

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(np.concatenate((a, b), axis=1))   # [[1 2 5 6] [3 4 7 8]]

# a = np.array([1, 2, 3, 4, 5, 6])    # a.shape --> (6,)
# b = np.expand_dims(a, axis=1)       # b.shape --> (6, 1)
# print(b)                            # [[1] [2] [3] [4] [5] [6]]
# c = np.expand_dims(a, axis=0)       # c.shape --> (1, 6)
# print(c)                            # [[1 2 3 4 5 6]]

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b = np.nonzero(a < 5)   # два array'я, где в первом индексы подходящих строк (axis=0), а во втором - подходящих столбцов (axis=1)
# print(b)                # (array([0, 0, 0, 0]), array([0, 1, 2, 3]))
# c = a[a > 6]
# print(c)                # [ 7  8  9 10 11 12]
# c[0] = 999
# print(a)                # не изменился

# a = np.arange(0, 6)     # [0 1 2 3 4 5]
# b = a[np.newaxis, :]
# print(b)                # [[0 1 2 3 4 5]]
# b = a[:, np.newaxis]
# print(b)                # [[1] [2] [3] [4] [5] [6]]

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b1 = a[0, :]
# print(b1)               # [1 2 3 4]
# b2 = a[1, :]    
# print(b2)               # [5 6 7 8]
# b3 = a[1, 2:]   
# print(b3)               # [7 8]
# b3[0] = 999 
# print(a)                # изменился!
# a[1][2] = 7             # меняем ориг. обратно
# b4 = a[1, 2:].copy()    # берём уже копию
# print(b4)               # [7 8]
# b4[0] = 777 
# print(b4)               # [777   8]
# print(a)                # не изменился


# Стандартное отклонение (корень из дисперсии)
# a = np.array([1, 2])
# print(a.std())      # (((1 - 1.5)**2 + (2 - 1.5)**2) / 2)**0.5
# a = np.array([1, 2, 3])
# print(a.std())      # (((1 - 2)**2 + (2 - 2)**2 + (3 - 2)**2) / 3)**0.5


# data = np.array([[1, 2], [5, 3], [4, 6]])
# print(data.max(axis=0))     # array([5, 6]) ===== [5 6]
# print(data.max(axis=1))     # array([2, 5, 6]) ===== [2 5 6]

# rng = np.random.default_rng()
# print(rng.random(3))            # [0.9405053  0.70094177 0.19071308]
# print(np.random.random(3))      # [0.72027625 0.41542541 0.92627909]
# print(np.random.random())       # 0.9893254655625123

# a = np.array([1,2,3])
# print(id(a))
# a = np.append(a,4)
# print(a)
# print(id(a))











# # Пробую в layers добавить слоёв:
# layers = np.array([[]], 'int16')
# print(layers, layers.shape)
# # print(np.concatenate((layers, np.zeros(3, 'int16')), axis=0))
# layers = np.concatenate((layers, np.zeros((1,3), 'int16')), axis=1)
# print(layers, layers.shape)
# layers = np.concatenate((layers, np.zeros((1,5), 'int16')), axis=0)
# print(layers, layers.shape)
# layers = np.concatenate((layers, np.zeros((1,7), 'int16')), axis=0)
# print(layers, layers.shape)
# # print(np.zeros((1,3), 'int16'))
# # Вывод: все слои должны будут иметь одну и ту же размерность.





# Тогда layers запрогаем как List:
# layers = []
# layers.append(np.zeros((3), 'int16'))
# layers.append(np.floor(10 * np.random.random(3)))
# layers.append((10 * np.random.random(3)).astype(np.int16))
# print(layers)
# print(layers[0])
# print(layers[0].dtype)
# В целом работает..






# a1 = np.arange(11, dtype='int8')
# print(a1)       # [ 0  1  2  3  4  5  6  7  8  9 10]
# for i in range(len(a1)):
#     print(a1[i], type(a1[i]))
# for i in a1:
#     print(i, type(i))



# nrNumPrev = 4
# nrNumNext = 3
# layer = np.reshape(np.random.random(nrNumPrev*nrNumNext), shape=(nrNumPrev, nrNumNext))
# print(layer.dtype)    # 'float64'

# nrNumNext = 3
# a = np.random.uniform(-1, 1, (nrNumNext))
# print(a.dtype)        # 'float64'



# inputLayer = np.zeros(shape=(2, 4))
# print(inputLayer)








# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))

# X = np.array([0.2, 0.3])

# # W1 = np.array([[4, 5], [6, 7]])
# # b1 = np.array([1, 1])

# # W2 = np.array([[3], [2]])
# # b2 = np.array([4])


# W1 = np.array([[0.4, 0.5], [0.6, 0.7]])
# b1 = np.array([0.1, 0.1])

# W2 = np.array([[0.3], [0.2]])
# b2 = np.array([0.4])


# z1 = np.dot(X, W1) + b1
# a1 = sigmoid(z1)
# print(z1, a1)

# z2 = np.dot(a1, W2) + b2
# a2 = sigmoid(z2)
# print(z2, a2)





# zList = [[1.09190307, 2.73428661, -3.2342, 0, -0.0001, 4.242424]]

# def relu(x): return np.maximum(0, x)

# d_a2_d_z2 = [0.0 if (relu(zList[0][i]) == 0) else 1.0 for i in range(len(zList[0]))]

# print(d_a2_d_z2)

# # d_a2_d_z2 = 0 if (relu(zList[0]) == 0) else 1

# # d_a2_d_z2 = []
# # for i in range(len(zList[0])):
# #     t = 0
# #     if (relu(zList[0][i]) != 0): t = 1
# #     else: t = 0

    
    
    



# # d_loss_d_z = np.array([0.162141, 0.837859]) * np.array([1.5, 1.5])
# # print(d_loss_d_z)

# d_loss_d_z2 = np.array([0.162141, 0.837859])
# a1 = np.array([0.58904043, 0.60108788, 0.8174727])
# d_loss_d_W2 = np.dot(a1.reshape(-1, 1), d_loss_d_z2.reshape(1, -1))

# print(a1.reshape(-1, 1))
# # print(d_loss_d_z2)
# # print(d_loss_d_z2.reshape(1, 1))              # ValueError: cannot reshape array of size 2 into shape (1,1)
# print(d_loss_d_z2.reshape(1, -1))
# # print(d_loss_d_z2.reshape(-1, 1))
# # print(d_loss_d_z2.reshape(-1, -1))            # ValueError: can only specify one unknown dimension
# print(d_loss_d_W2)











# def softmax(x):
#     exp_x = np.exp(x - np.max(x))
#     return exp_x / np.sum(exp_x)
# # def d_softmax(x):
# #     s = softmax(x).reshape(-1, 1)
# #     return np.diagflat(s) - np.dot(s, s.T)

# # a1 = np.array([0.2, 0.7, 0.3])
# a1 = np.array([[0.2, 0.7, 0.3], [0.9, 0.1, 0.5]])

# print(softmax(a1))
# # print(d_softmax(a1))        # возвращает матрицу 3x3 (видимо Якоби)
# #                             # нужно ещё почитать этот момент






# def softmax_grad(s):
#     J = - s[..., None] * s[:, None, :] # off-diagonal Jacobian
#     iy, ix = np.diag_indices_from(J[0]) 
#     J[:, iy, ix] = s * (1. - s) # diagonal
#     return J.sum(axis=1)

                            

# # def softmax2(x):
# #     """Compute the softmax of vector x."""
# #     exps = np.exp(x)
# #     return exps / np.sum(exps)


# a1 = np.array([[0.2, 0.7, 0.3]])
# # a1 = np.array([[0.2, 0.7, 0.3], [0.9, 0.1, 0.5]])
# # print(softmax2(a1))
# print(softmax_grad(a1))





















# a1 = np.array([[2], [4]])
# # a2 = np.array([[6,1], [2,5]])
# a2 = np.array([[6,0,1], [2,7,5]])

# print(np.dot(a1, a2))











# a1 = np.array([[0.84395852], [0.85694072], [0.78860344], [0.84633243]])
# a2 = np.array([[0.29616352,  0.28507933,  0.19124472,  0.29628926,  0.06054214,  0.13492558, 0.1839138,  -0.09077863,  0.21679504,  0.26812694]])

# print(a1.shape, a2.shape)





# from math import ceil

# print(ceil(100/10))







# a = np.array([1, 2, 3, 4, 5, 6])
# print(np.append(a, 7))
# print(a)

# L = [1, 2, 3, 4, 5]
# print(np.mean(L))






# a = np.random.random(12).reshape((3, 4)).round(2)
# print(a)
# [[0.45 0.42 0.27 0.28]
#  [0.72 0.96 0.69 0.03]
#  [0.25 0.18 0.35 0.93]]

# a1 = np.array([[0.45, 0.42, 0.27, 0.28],
#                [0.72, 0.96, 0.69, 0.03],
#                [0.25, 0.18, 0.35, 0.93]])

# a2 = np.array([[0.95, 0.16, 0.64, 0.89],
#                [0.03, 0.07, 0.18, 0.36],
#                [0.85, 0.84, 0.41, 0.54]])

# a3 = np.concat((a1, a2), axis=np.newaxis)
# print(a3.shape)
# print(a3)

# a3 = np.concat((a1, a2), axis=0)
# print(a3.shape)
# print(a3)

# a3 = np.concat((a1, a2), axis=1)
# print(a3.shape)
# print(a3)

# a3 = np.concat((a1, a2))    # def: axis=0
# print(a3.shape)
# print(a3)

# # a3 = np.concat((a1, a2)).reshape(2, 3, 4)         # SAME
# a3 = np.concat((a1, a2)).reshape(2, *a1.shape)      # SAME
# print(a3.shape)
# print(a3)



# a = np.random.random(4).reshape((1, 4)).round(2)
# print(a)










# aList = [   
#             # [0]
#             np.array([[0.45, 0.42, 0.27, 0.28],
#                       [0.72, 0.96, 0.69, 0.03],
#                       [0.25, 0.18, 0.35, 0.93],
#                       [0.41, 0.68, 0.49, 0.05]
#             ]),
            
#             # [1]
#             [
#                 np.array([0.57198587, 0.51019553, 0.70334767, 0.57539096]),
#                 np.array([0.67090456, 0.64963921, 0.8112416 , 0.62509812]),
#                 np.array([0.5834835 , 0.53623427, 0.73951918, 0.68734718]),
#                 np.array([0.59750687, 0.57093938, 0.71077121, 0.56262743])
#             ],

#             # [2]
#             [
#                 np.array([0.91827699, 0.93507843, 0.59990247, 0.79904116, 0.72113731, 0.45995268, 0.89936513, 0.82224525, 0.56540104, 0.47255356]),
#                 np.array([0.94027165, 0.9519119 , 0.62427814, 0.82161741, 0.75236544, 0.49028663, 0.91721794, 0.85142036, 0.60062016, 0.49384536]),
#                 np.array([0.92801975, 0.94452852, 0.61442471, 0.80450125, 0.73206374, 0.48607818, 0.9089257 , 0.83780755, 0.58311476, 0.48402094]),
#                 np.array([0.92356188, 0.93848406, 0.60309067, 0.80545414, 0.73051592, 0.46534063, 0.90188066, 0.82744845, 0.5713933 , 0.47803259])
#             ]
#         ]












# aList = [   
#             # [0]
#             np.array([[0.45, 0.42, 0.27, 0.28],
#                       [0.72, 0.96, 0.69, 0.03],
#                       [0.25, 0.18, 0.35, 0.93],
#                       [0.41, 0.68, 0.49, 0.05]
#             ]),
            
#             # [1]
#             [
#                 np.array([0.57, 0.51, 0.70, 0.57]),
#                 np.array([0.67, 0.64, 0.81, 0.62]),
#                 np.array([0.58, 0.53, 0.73, 0.68]),
#                 np.array([0.59, 0.57, 0.71, 0.56])
#             ],

#             # [2]
#             [
#                 np.array([0.91, 0.93, 0.59, 0.79, 0.72, 0.45, 0.89, 0.82, 0.56, 0.47]),
#                 np.array([0.94, 0.95, 0.62, 0.82, 0.75, 0.49, 0.91, 0.85, 0.60, 0.49]),
#                 np.array([0.92, 0.94, 0.61, 0.80, 0.73, 0.48, 0.90, 0.83, 0.58, 0.48]),
#                 np.array([0.92, 0.93, 0.60, 0.80, 0.73, 0.46, 0.90, 0.82, 0.57, 0.47])
#             ]
#         ]


# aList = [
#     np.array([[[0.45, 0.42, 0.27, 0.28],
#             [0.72, 0.96, 0.69, 0.03],
#             [0.25, 0.18, 0.35, 0.93],
#             [0.41, 0.68, 0.49, 0.05]],

#            [[0.45, 0.42, 0.27, 0.28],
#             [0.72, 0.96, 0.69, 0.03],
#             [0.25, 0.18, 0.35, 0.93],
#             [0.41, 0.68, 0.49, 0.05]]]),
            
#     [
#         np.array([[0.99007337, 0.97990015, 0.9561233 , 0.97552732]]), 
#         np.array([[0.99007337, 0.97990015, 0.9561233 , 0.97552732]])
#     ],
    
#     [
#         np.array([[0.73311012, 0.90756042, 0.87692057, 0.92316887, 0.87756351, 0.86409886, 0.96714049, 0.96173917, 0.80978664, 0.9276617 ]]),
#         np.array([[0.73311012, 0.90756042, 0.87692057, 0.92316887, 0.87756351, 0.86409886, 0.96714049, 0.96173917, 0.80978664, 0.9276617 ]])
#     ]
# ]

# aList = [
#     np.array([[[1,2,3,4],
#                [5,6,7,8],
#                [9,10,11,12],
#                [27,14,15,16]],

#               [[1,2,3,4],
#                [5,6,7,8],
#                [9,10,11,12],
#                [27,14,15,16]]]),
            
#     [
#         np.array([[1,2,3,4]]), 
#         np.array([[5,6,7,8]])
#     ],
    
#     [
#         np.array([[1,2,3,4,5,6,7,8,9,10]]),
#         np.array([[11,12,13,14,15,16,17,18,19,20]])
#     ]
# ]


# # print(np.mean(a=aList))         #  The detected shape was (3, 2) + inhomogeneous part.
# # print(np.mean(a=aList, axis=0))         #  The detected shape was (3, 2) + inhomogeneous part.
# # print(np.mean(a=aList, axis=1))         #  The detected shape was (3, 2) + inhomogeneous part.

# for i in range(len(aList)):
#     aList[i] = np.array(aList[i]).mean(axis=0)
#     print(aList[i])




# a1 = np.array([[0.45, 0.42, 0.27, 0.28],
#                [0.72, 0.96, 0.69, 0.03],
#                [0.25, 0.18, 0.35, 0.93],
#                [0.41, 0.68, 0.49, 0.05]])

# a2 = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [27,14,15,16]])

# print(a2 - a1)


















# a = [np.array([[0.93779876, 0.89093683, 0.86886835, 0.77660224, 0.80843853,
#         0.88553768, 0.82385315, 0.94760776, 0.94259844, 0.88478985]]), np.array([[0.93779876, 0.89093683, 0.86886835, 0.77660224, 0.80843853,
#         0.88553768, 0.82385315, 0.94760776, 0.94259844, 0.88478985]])]

# # print(a)
# # print(a[0].shape)

# a = [np.reshape(i, 10) for i in a]
# print(a)

# Y_train = np.array([[0.45, 0.42, 0.27, 0.28, 0.72, 0.96, 0.69, 0.03, 0.25, 0.18],
#                     [0.35, 0.93, 0.41, 0.68, 0.49, 0.05, 0.45, 0.42, 0.27, 0.28]])
# print(Y_train)

# print(a - Y_train)















# [array([[[0.45, 0.42, 0.27, 0.28],
#         [0.72, 0.96, 0.69, 0.03],
#         [0.25, 0.18, 0.35, 0.93],
#         [0.41, 0.68, 0.49, 0.05]],

#        [[0.45, 0.42, 0.27, 0.28],
#         [0.72, 0.96, 0.69, 0.03],
#         [0.25, 0.18, 0.35, 0.93],
#         [0.41, 0.68, 0.49, 0.05]]]), 
# 
# [array([[0.98303625, 0.91322561, 0.92335707, 0.99500246]]), array([[0.98303625, 0.91322561, 0.92335707, 0.99500246]])], 
# 
# [array([[0.87310362, 0.83398884, 0.69748042, 0.72784315, 0.8287259 , 0.69728537, 0.81684526, 0.91093632, 0.8439499 , 0.6569129 ]]), 
#         array([[0.87310362, 0.83398884, 0.69748042, 0.72784315, 0.8287259 , 0.69728537, 0.81684526, 0.91093632, 0.8439499 , 0.6569129 ]])]]









# a = np.array([[0.45, 0.42, 0.27, 0.28],
#               [0.72, 0.96, 0.69, 0.03],
#               [0.25, 0.18, 0.35, 0.93],
#               [0.41, 0.68, 0.49, 0.05]])


# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12],
#               [13,14,15,16]])
# print(a.mean())             # 8.5
# print(a.mean(axis=0))       # [ 7.  8.  9. 10.]
# print(a.mean(axis=1))       # [ 2.5  6.5 10.5 14.5]




# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12],
#               [27,14,15,16]])
# print(a.mean(axis=0))       # [ 8.5  8.   9.  10. ]
# # print((1+5+9+19)/4)         # 8.5
# # print((1+5+9+27)/4)         # 10.5




















# # from fnnmodel9_batching import UV

# # print(x.shape, w.shape, b.shape, np.dot(x, w). shape, z.shape)

# X_train = np.load('./armed_n_dangerous/mnist_data_10/x_train.npy')
# Y_train = np.load('./armed_n_dangerous/mnist_data_10/y_train.npy')
# # X_train = np.load('./armed_n_dangerous/mnist_data_1000/x_train.npy')
# # Y_train = np.load('./armed_n_dangerous/mnist_data_1000/y_train.npy')

# # X_test  = np.load('./armed_n_dangerous/mnist_data_1000/x_test.npy')
# # Y_test  = np.load('./armed_n_dangerous/mnist_data_1000/y_test.npy')

# # uv = UV()
# # uv.addLayer(16, 4, 'sigmoid')
# # uv.addLayer(4, 10, 'sigmoid')
# # uv.train(epochs=1, batchSize=2, trainData=[X_train, Y_train]) #, testData=[X_test, Y_test])

# # X_train = [[i/255 for i in x] for x in X_train]
# # x0 = X_train[0]
# # print(type(x0[0]))
# # for i in x0: print(i)
# # print(1/255)

# Y_train_new = []
# for i in range(len(Y_train)):
#     t = np.zeros(10)
#     t[Y_train[i]] = 1.0
#     # print(t)
#     Y_train_new.append(t)
# # print((np.array(Y_train_new)).shape)
# # y0 = Y_train_new[0]
# # print(y0, type(y0))     # 7 <class 'numpy.uint8'>

# # print(Y_train_new)
# y0 = Y_train_new[0]
# print(7==(np.argwhere(y0==1.)))
# # print(np.argpartition)
# print(7==y0.argmax())









# print(28*28)      # 784












# a = np.array([[1,2,3,9,5,6,7,8,9]])
# # print(a.shape)
# # print(a)

# # a = a.reshape(1, -1)
# # print(a.shape)
# # print(a)

# print(np.where(a[0] == a[0].max()))





# a = np.array([[1,2,3,9,5,6,7,8,9]])
# b = a
# # b = a.copy()
# a[0][0] = 5
# print(a, b)





# W1 = np.random.randn(8, 4) * np.sqrt(2.0 / 8)
W1 = np.random.randn(4, 10) * np.sqrt(2.0 / 10)

print(W1)

