# -*- coding: utf-8 -*-
import numpy as np

#data mnistをインポート
from 3-2_data_mnist import load_mnist
#リサイズやトリミング、回転、反転など基本的な処理はPillow
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

#「(訓練画像、訓練ラベル)、（テスト画像、テストラベル）」という形式、引数は「一次配列にして、正規化はせず
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label) # 5
print(img.shape) # (784,)
img = img.reshape(28, 28)
print(img.shape) # (28, 28)

img_show(img)

print(x_train.shape) #(60000,784)
print(t_train.shape) #(60000,)
print(x_test.shape) #(10000, 784)
print(t_test.shape) #(10000,)
