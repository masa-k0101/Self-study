import numpy as np

from matplotlib import pyplot as plt
#irisデータをインポート
from sklearn.datasets import load_iris

#0割りと浮動小数点エラーを無視
np.seterr(divide='ignore', invalid='ignore')

data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

for t,marker,c,in zip(range(3),">ox","rgb"):
    plt.scatter(features[target == t,0],
                features[target == t,1],
                marker=marker,
                c=c)

plength = features[:,2]
is_setosa = (labels == 'setosa')

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa:{0}.'.format(max_setosa))
print('Minimum of others:{0}.'.format(min_non_setosa))

features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')

#初期値を設定
best_acc = -1.0
best_fi = -1.0
best_t = -1.0

for fi in range(features.shape[1]):
    threth = features[:,fi].copy()
    threth.sort()
    
    for t in threth:
        pred = (features[:,fi]>t)
        acc = (labels[pred] == 'virginica').mean()
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t        