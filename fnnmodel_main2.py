
from fnnmodel10_0_testing import UV
# from fnnmodel12_ds_did import UV
import numpy as np



# X_train = np.load('./armed_n_dangerous/mnist_data_10000/x_train.npy')
# Y_train = np.load('./armed_n_dangerous/mnist_data_10000/y_train.npy')
# X_test  = np.load('./armed_n_dangerous/mnist_data_10000/x_test.npy') # 3000
# Y_test  = np.load('./armed_n_dangerous/mnist_data_10000/y_test.npy') # 3000


X_train = np.load('./armed_n_dangerous/mnist_data/x_train.npy')
Y_train = np.load('./armed_n_dangerous/mnist_data/y_train.npy')
X_test  = np.load('./armed_n_dangerous/mnist_data/x_test.npy')
Y_test  = np.load('./armed_n_dangerous/mnist_data/y_test.npy')


# # print(x.shape, w.shape, b.shape, np.dot(x, w). shape, z.shape)
# X_train = np.load('./armed_n_dangerous/mnist_data_1000/x_train.npy')
# Y_train = np.load('./armed_n_dangerous/mnist_data_1000/y_train.npy')
# X_test  = np.load('./armed_n_dangerous/mnist_data_1000/x_test.npy') # 300
# Y_test  = np.load('./armed_n_dangerous/mnist_data_1000/y_test.npy') # 300

print(f'X_train: {X_train.shape}')
print(f'Y_train: {Y_train.shape}')
print(f'X_test: {X_test.shape}')
print(f'Y_test: {Y_test.shape}')


X_train_norm = np.array([np.array([i/255 for i in x]) for x in X_train])
Y_train_norm = []
for i in range(len(Y_train)):
    t = np.zeros(10)
    t[Y_train[i]] = 1.0
    Y_train_norm.append(t)
Y_train_norm = np.array(Y_train_norm)

X_test_norm = np.array([np.array([i/255 for i in x]) for x in X_test])
Y_test_norm = []
for i in range(len(Y_test)):
    t = np.zeros(10)
    t[Y_test[i]] = 1.0
    Y_test_norm.append(t)
Y_test_norm = np.array(Y_test_norm)


uv = UV(learningRate=0.05)
uv.addLayer(784, 512, 'relu')
uv.addLayer(512, 512, 'relu')
uv.addLayer(512, 10, 'softmax')
# print(uv.weights)
uv.train(epochs=10, batchSize=10, trainData=[X_train_norm, Y_train_norm]) #, testData=[X_test, Y_test])
uv.test(testData=[X_test_norm, Y_test_norm])
# print(uv.weights)


# print(Y_test_norm[0].max())

# def train(b=''):
#     print(type(b))
#     x, y = b
#     print(type(x), type(y))
#     print(type(x[0]), type(y[0]))
#     print(x.shape[0])

# train(b=[X_train_norm, Y_train_norm])









# print(uv.sigmoid(np.array([[1,2,3,4,5]])).argmax())
# print(type(uv.sigmoid(np.array([[1,2,3,4,5]]))))







