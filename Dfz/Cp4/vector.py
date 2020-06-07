# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

if __name__ == '__main__':
    # Figureオブジェクトをplt.figure()で明示的に作った
    plt.figure()

# 矢印（ベクトル）の始点
X = 0, -0.5
Y = 0, -1.0
# 矢印（ベクトル）の成分
U = 2, -1.25
V = 1, 0.5

# 矢印（ベクトル）
# x-y平面に座標（X,Y）を基点として，成分(grad[0],grad[1])のベクトルを描きます
plt.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)

# グラフ表示　軸の設定
plt.xlim([-2, 2])
plt.ylim([-2, 2])

# ラベル表示
plt.xlabel('x')
plt.ylabel('y')

# グラフの描画
plt.grid()
plt.legend(['Vector'])
plt.draw()
plt.show()