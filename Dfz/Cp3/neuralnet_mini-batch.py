# -*- coding: utf-8 -*-
import sys
sys.path.append("C:/Study/Python/Deep-learning from scratch")
import numpy as np
from data_mnist import load_mnist

# データの読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

#要素数を表示
print(x_train.shape)
print(t_train.shape)

#1行目の要素数をsizeに設定
train_size = x_train.shape[0]
print("train_size: " +str(train_size))
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
print("batch_mask: ")
print(batch_mask)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]