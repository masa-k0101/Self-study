# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 値を元に戻す
    return grad

def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
            
        return grad

def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

if __name__ == '__main__':
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)

    X = X.flatten()
    Y = Y.flatten()

    grad = numerical_gradient(function_2, np.array([X, Y]))

    # Figureオブジェクトをplt.figure()で明示的に作った
    plt.figure()

    # 矢印（ベクトル)
    # x-y平面に座標（X,Y）を基点として，成分(grad[0],grad[1])のベクトルを描きます
    plt.quiver(X, Y, -grad[0], -grad[1], angles="xy",color="#666666")

    # グラフ表示　軸の設定
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])

    # ラベル表示
    plt.xlabel('x0')
    plt.ylabel('x1')

    # グラフの描画
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
