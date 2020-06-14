# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

class Sigmoid:

    def __init__(self, x):
        self.x = x
        
    def sigmoid(x):
        # xをオーバーフローしない範囲に補正
        sigmoid_range = 34.538776394910684
        x2 = np.maximum(np.minimum(x, sigmoid_range), -sigmoid_range)
        # シグモイド関数
        return 1 / (1 + np.exp(-x2))
    
    def sigmoid_grad(x):
        return (1.0 - Sigmoid.sigmoid(x)) * Sigmoid.sigmoid(x)

if __name__ == '__main__':
    X = np.arange(-5.0, 5.0, 0.1)
    Y = Sigmoid.sigmoid(X)
    plt.plot(X, Y)
    plt.ylim(-0.1, 1.1)
    plt.show()
