# -*- coding: utf-8 -*-
import numpy as np

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    print("x.size=" + str(x.size))
    for idx in range(x.size):
        print("\n"+"idx:"+str(idx))
        print("x[idx]:"+str(x[idx]))
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        print("fxh1:")
        print(fxh1)

    x[idx] = tmp_val - h
    fxh2 = f(x) # f(x-h)
    print("fxh2:")
    print(fxh2)
    grad[idx] = (fxh1 - fxh2) / (2*h)
    print("grad[idx]:")
    print(grad[idx])
    x[idx] = tmp_val # 値を元に戻す
    return grad

def function_2(x):
    print("1-x[0]:"+str(x[0]))
    print("x[1]:"+str(x[1]))
    print("sum:"+str(np.sum(x**2)))
    return np.sum(x**2)

if __name__ == '__main__':
    grad = numerical_gradient(function_2, np.array([3.0, 4.0]))
    print(grad)
