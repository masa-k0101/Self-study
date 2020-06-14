# -*- coding: utf-8 -*-
import sys
sys.path.append("/Study/python/Deep-learning from scratch")
from c1_AND_gate2 import ANDgate
from c1_OR_gate2 import ORgate
from c1_NAND_gate2 import NANDgate

class XORgate:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def XOR(x1, x2):
        s1 = NANDgate.NAND(x1, x2)
        s2 = ORgate.OR(x1, x2)
        y = ANDgate.AND(s1, s2)
        return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XORgate.XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))