# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

class Relu:
    def __init__(self, x):
        self.x = x
        
    def relu(x):
        return np.maximum(0, x)

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = Relu.relu(x)
    plt.plot(x, y)
    plt.ylim(-1.0, 5.5)
    plt.show()