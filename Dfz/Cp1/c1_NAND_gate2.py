# -*- coding: utf-8 -*-
import numpy as np

class NANDgate():
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        
    def NAND(x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7
        tmp = np.sum(w*x) + b
        if tmp <= 0:
            return 0
        else:
            return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NANDgate.NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))