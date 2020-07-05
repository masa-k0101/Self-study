# -*- coding: utf-8 -*-
import os, sys
import numpy as np
from c5_6_two_layer_net import TwoLayerNet
sys.path.append(os.pardir)  # パスに親ディレクトリ追加
from c3_2_data_mnist import load_mnist

# MNISTの訓練データとテストデータ読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# 2層のニューラルワーク生成
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 検証用のデータ準備
x_batch = x_train[:3]
t_batch = t_train[:3]

# 数値微分と誤差逆伝播法で勾配算出
grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

# 各重みの差を確認
for key in grad_numerical.keys():
    # 差の絶対値の算出
    diff = np.abs(grad_backprop[key] - grad_numerical[key])
    # 平均と最大値を表示
    print(f"{key}: [差の平均]{np.average(diff):.10f} [最大の差]{np.max(diff):.10f}")