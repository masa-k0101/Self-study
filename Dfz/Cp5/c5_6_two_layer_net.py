# -*- coding: utf-8 -*-
import numpy as np
from c5_4_affine import Affine
from c4_2_gradient_2d2 import Gradient
from c5_1_relu_function import ReLU
from c5_5_softmax_with_loss import SoftmaxWithLoss

class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        """２層のニューラルネットワーク
        Args:
            input_size (int): 入力層のニューロンの数
            hidden_size (int): 隠れ層のニューロンの数
            output_size (int): 出力層のニューロンの数
            weight_init_std (float, optional): 重みの初期値の調整パラメーター。デフォルトは0.01。
        """

        # 重みの初期化
        self.params = {}
        self.params['W1'] = weight_init_std * \
            np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * \
            np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        # レイヤー生成
        self.layers = {}    # Python 3.7からは辞書の格納順が保持されるので、OrderedDictは不要
        self.layers['Affine1'] = \
            Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = ReLU()
        self.layers['Affine2'] = \
            Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()

    def predict(self, x):
        """ニューラルネットワークによる推論
        Args:
            x (numpy.ndarray): ニューラルネットワークへの入力
        Returns:
            numpy.ndarray: ニューラルネットワークの出力
        """
        # レイヤーを順伝播
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        """損失関数の値算出
        Args:
            x (numpy.ndarray): ニューラルネットワークへの入力
            t (numpy.ndarray): 正解のラベル
        Returns:
            float: 損失関数の値
        """
        # 推論
        y = self.predict(x)

        # Softmax-with-Lossレイヤーの順伝播で算出
        loss = self.lastLayer.forward(y, t)
        return loss

    def accuracy(self, x, t):
        """認識精度算出
        Args:
            x (numpy.ndarray): ニューラルネットワークへの入力
            t (numpy.ndarray): 正解のラベル
        Returns:
            float: 認識精度
        """
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / x.shape[0]
        return accuracy

    def numerical_gradient(self, x, t):
        """重みパラメーターに対する勾配を数値微分で算出
        Args:
            x (numpy.ndarray): ニューラルネットワークへの入力
            t (numpy.ndarray): 正解のラベル
        Returns:
            dictionary: 勾配を格納した辞書
        """
        grads = {}
        grads['W1'] = \
            Gradient.numerical_gradient(lambda: self.loss(x, t), self.params['W1'])
        grads['b1'] = \
            Gradient.numerical_gradient(lambda: self.loss(x, t), self.params['b1'])
        grads['W2'] = \
            Gradient.numerical_gradient(lambda: self.loss(x, t), self.params['W2'])
        grads['b2'] = \
            Gradient.numerical_gradient(lambda: self.loss(x, t), self.params['b2'])

        return grads

    def gradient(self, x, t):
        """重みパラメーターに対する勾配を誤差逆伝播法で算出
         Args:
            x (numpy.ndarray): ニューラルネットワークへの入力
            t (numpy.ndarray): 正解のラベル
        Returns:
            dictionary: 勾配を格納した辞書
        """
        # 順伝播
        self.loss(x, t)     # 損失値算出のために順伝播する

        # 逆伝播
        dout = self.lastLayer.backward()
        for layer in reversed(list(self.layers.values())):
            dout = layer.backward(dout)

        # 各レイヤーの微分値を取り出し
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db

        return grads