# -*- coding: utf-8 -*-
import	numpy	as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([215,121,130,87,121,145,205])
y = softmax(a)
print(y)
print(np.sum(y))