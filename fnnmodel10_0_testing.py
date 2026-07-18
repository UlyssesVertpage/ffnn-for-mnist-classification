










import numpy as np
import math

class UV:

    # actFuncsList = ['sigmoid', 'relu', 'softmax', 'tanh', 'linear']
    
    def __init__(self, learningRate=1.0, momentum=0.8): #, inputLayer_shape=(28, 28)):
        # self.inputLayer = np.zeros(shape=inputLayer_shape)
        self.weights = []           # np.array([])
        self.biases = []
        self.actFuncs = []
        self.lossList = []
        self.learningRate = learningRate
        self.momentum = momentum
        print("init.")
    def __repr__(self): return "repr."
    def addLayer(self, nrPrev, nrNext, actFunc):
        # === ВЕСА ===
        ### СТАРОЕ. Такая иниц-я, к сожалению, пока ещё не работала.
        # self.weights.append(np.reshape(np.random.random(nrPrev*nrNext), shape=(nrPrev, nrNext)))        # TODO: Добавить возможность инициализровать по-разному: нулями, в [0, 1), в (-1, 1) и т.д.
        ### Хорошая иниц-я для 'relu'!
        self.weights.append(np.reshape(np.random.randn(nrPrev, nrNext) * np.sqrt(2.0 / nrPrev), shape=(nrPrev, nrNext)))
        ### Хорошая иниц-я для 'sigmoid'!
        # self.weights.append(np.reshape(np.random.randn(nrPrev, nrNext) * np.sqrt(1.0 / nrPrev), shape=(nrPrev, nrNext)))
        
        # === СМЕЩЕНИЯ ===
        # self.biases.append(np.random.uniform(-1, 1, (nrNext)))       # TODO: Сделать возможность выбора начальных значений смещений. Как именно заполняем? нулями? в [-0.1; 0.1]? рандомы в (-1; 1)?
        self.biases.append(np.zeros(nrNext))
        # self.biases.append(np.ones(nrNext) * 0.01)   # Предотвращает "мёртвые нейроны" в ReLU, гарантируя начальную активацию.

        self.actFuncs.append(actFunc)
    
    # ===== Фукнции активации ================================================================
    def sigmoid(self, x): return 1 / (1 + np.exp(-x))
    def relu(self, x): return np.maximum(0, x)
    def softmax(self, x): exp_x = np.exp(x - np.max(x)); return exp_x / np.sum(exp_x)
    def tanh(self, x): return np.tanh(x)
    def linear(self, x): return x

    def d_sigmoid(self, x): s = self.sigmoid(x); return s * (1 - s)
    def d_relu(self, x): return np.where(x > 0, 1.0, 0.0)
    # def d_relu(x): return (x > 0).astype(float)
    # def d_softmax(self, x):
    #     J = - x[..., None] * x[:, None, :] # off-diagonal Jacobian
    #     iy, ix = np.diag_indices_from(J[0]) 
    #     J[:, iy, ix] = x * (1.0 - x) # diagonal
    #     return J.sum(axis=1)
    def d_softmax(self, x): s = self.softmax(x); return s * (1 - s)  # упрощенная версия
    # Для обратного распространения с MSE или cross-entropy
    # эта производная обычно не используется напрямую
    # ===== и их производные =================================================================


    def train(self, trainData='', validData='', epochs=1, batchSize=100):

        for epoch_index in range(epochs):
            x_train, y_train = trainData
            # x_valid, y_valid = validData             # TODO Настроить валидацию
            for batch_index in range(math.ceil(x_train.shape[0] / batchSize)):
                x_batch = x_train[batch_index*batchSize : (batch_index+1)*batchSize]
                # if (epoch_index == 9):
                #     print([list(i) for i in x_batch])
                #     exit()
                y_batch = y_train[batch_index*batchSize : (batch_index+1)*batchSize]
                zList = [[] for i in range(len(self.weights))]
                aList = [[] for i in range(len(self.weights))]
                batch_data = x_batch.copy()
                for i in range(len(self.weights)):
                    for x in batch_data:
                        x = x.reshape(1, -1)
                        b = self.biases[i]
                        w = self.weights[i]
                        z = np.dot(x, w) + b
                        a = getattr(self, self.actFuncs[i])(z)
                        zList[i].append(z); aList[i].append(a)
                    batch_data = aList[i]
                aList.insert(0, x_batch)

                # print(zList)
                # print()
                # print(aList)
                # print()
                # exit()

                aLast = [np.reshape(i, shape=10) for i in aList[-1]]
                diff = (aLast - y_batch).mean(axis=0)
                # print(aLast, y_batch)
                # exit()
                loss = diff**2
                self.lossList.append(loss)
                for i in range(len(aList)):
                    aList[i] = np.array(aList[i]).mean(axis=0)
                for i in range(len(zList)):
                    zList[i] = np.array(zList[i]).mean(axis=0)

                dLoss_dW = [0 for i in range(len(self.weights))]
                dLoss_dB = [0 for i in range(len(self.biases))]
                dLoss_dZ = np.array([])
                for i in range(len(self.weights)-1, -1, -1):
                    if (i == len(self.weights)-1):
                        dLoss_dA = np.array(2 * diff)           # НАДО ЛИ ЕЩЁ ПРАВИТЬ? TODO
                    else:
                        dLoss_dA = np.dot(dLoss_dZ, self.weights[i+1].T)
                    dA_dZ = getattr(self, 'd_' + self.actFuncs[i])(zList[i])
                    dLoss_dZ = dLoss_dA * dA_dZ
                    dLoss_dW[i] = np.dot(aList[i].reshape(-1, 1), dLoss_dZ)
                    dLoss_dB[i] = dLoss_dZ

                # print(dLoss_dW)
                # TODO Вот здесь применить learningRate и momentum
                for i in range(len(self.weights)):
                    self.weights[i] = self.weights[i] - self.learningRate * dLoss_dW[i]
                    self.biases[i] = self.biases[i] - self.learningRate * dLoss_dB[i]
            
            print(f'Epoch {epoch_index+1} was passed.')
        print('\n'*2, '='*10, 'TRAIN IS OVER', '='*10, '\n'*2)







    def test(self, testData=''):
        x_test, y_test = testData
        answers = []; percents = []

        for j in range(len(x_test)):
            x = x_test[j]
            zList = [0 for i in range(len(self.weights))]
            aList = [0 for i in range(len(self.weights))]
            for i in range(len(self.weights)):
                # ЛЮТЫЙ TODO: Определиться и в функции Train, как быть с этим reshape, потому как надо бы выяснить, может ли aList[i] то быть решейпнутым в (1, -1) или нет...
                x = x.reshape(1, -1)
                b = self.biases[i]
                w = self.weights[i]
                z = np.dot(x, w) + b
                a = getattr(self, self.actFuncs[i])(z)
                zList[i] = z; aList[i] = a
                x = aList[i]
            isCurrRight = a.argmax() == y_test[j].argmax()
            # print(isCurrRight)
            answers.append(f'[{j+1}]  {"TRUE" if isCurrRight else "FALSE"} \t Correct: {y_test[j].argmax()}, Predicted: {a.argmax()}')
            percents.append(isCurrRight)

        # for i in range(len(answers)):
        #     print(answers[i])
        for i in range(len(answers)//100):
            print(answers[99::100][i])
        print(f'\n{percents.count(True) / len(percents) * 100}%  ===  ({percents.count(True)} / {len(percents)})')












# uv = UV(inputLayer_shape=(4, 4))
# uv.addLayer(4, 3, 'relu')
# uv.addLayer(3, 2, 'softmax')
# # print(uv.getWeights())
# # print(uv.getBiases())
# # print(uv.getActFuncs())

# # trainData = np.reshape(np.random.random(28*28), shape=(28, 28))
# trainData = np.random.random(4)

# # У rightAnswers должна быть такая же размерность, как у self.weights[-1],
# # то есть равная кол-ву нейронов в выходном слое.
# # rightAnswers = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]]
# rightAnswers = [[0.0, 1.0]]

# # print(trainData)
# # print(uv.getWeights())
# uv.train(trainData=trainData, rightAnswers=rightAnswers)
