# -*- coding: utf-8 -*-
import sys
sys.path.append("C:/Study/Python/Deep-learning from scratch")
import numpy as np
import pickle
from data_mnist import load_mnist
from Sigmoid_function import sigmoid
from softmax import softmax

def get_data():
    (x_train, t_train), (x_test, t_test)= load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("C:/Study/Python/Deep-learning from scratch/workspace/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
        print(network['W1'])
        print(network['b1'])
        return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

x, t = get_data()
print("All count:"+str(len(x)))
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))