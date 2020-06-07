# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pylab as plt

#引数の2乗和を計算する関数を例として考える
def func1(x, y):
    return x**2 + y**2

# 描写データの作成
# 3次元で描写するには2次元メッシュが必要
# 2次元配列をarangeを用いて作る
# x, y をそれぞれ1次元領域で分割する
x0 = np.arange(-3, 3.0, 0.25)
x1 = np.arange(-3, 3.0, 0.25)

# 2次元メッシュはmeshgridでつくる
# Xの行にxの行列を，Yは列にyの配列を入れたものになっている
X, Y = np.meshgrid(x0, x1)
Z = func1(X, Y)

# グラフの作成
# figureで2次元の図を生成する
# その後，Axes3D関数で3次元にする
fig = plt.figure()
ax = Axes3D(fig)

# 軸ラベルの設定
ax.set_xlabel("x0")
ax.set_ylabel("x1")
ax.set_zlabel("f(x)")

# グラフ描写
ax.plot_wireframe(X, Y, Z)
plt.show()