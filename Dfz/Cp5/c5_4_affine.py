# -*- coding: utf-8 -*-
import numpy as np

class Affine:

    def __init__(self, W, b):
        """Affineレイヤー
        Args:
            W (numpy.ndarray): 重み
            b (numpy.ndarray): バイアス
        """
        self.W = W      # 重み
        self.b = b      # バイアス
        self.x = None   # 入力
        self.dW = None  # 重みの微分値
        self.db = None  # バイアスの微分値

    def forward(self, x):
        """順伝播
        Args:
            x (numpy.ndarray): 入力
        Returns:
            numpy.ndarray: 出力
        """
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out

    def backward(self, dout):
        """逆伝播
        Args:
            dout (numpy.ndarray): 右の層から伝わってくる微分値
        Returns:
            numpy.ndarray: 微分値
        """
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx