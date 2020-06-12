# -*- coding: utf-8 -*-
import sys
sys.path.append("C:/Study/Python/Deep-learning from scratch")
import numpy as np
from c3_1_cross_entropy_function import cross_entropy_error

#交差エントロピー誤差サンプル
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print (cross_entropy_error(np.array(y), np.array(t)))

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print (cross_entropy_error(np.array(y), np.array(t)))
