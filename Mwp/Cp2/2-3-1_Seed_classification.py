#import scipy as sp
import pandas as pd
#import numpy as np
from sklearn.model_selection import cross_val_score,LeaveOneOut,KFold,StratifiedKFold
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
#from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

file_id = 'seeds_datasets.txt'
file_path = '/Study/python/workspace/'
rfile = file_path + file_id
data = pd.read_csv(rfile,delim_whitespace=True,header=None)

datas = data.loc[:, :7]
features = data.loc[:, :6]
targets = data.loc[:, 7]
#datas = data.loc[:, :7].getvalues()
#features = data.loc[:, :6].get_values()
#targets = data.loc[:, 7].get_values()

#正規化
datas -= datas.mean(axis=0)
datas /= datas.std(axis=0)

# 特徴量を描画する
for t,marker,c,in zip(range(3),"<ox","rgb"):
    plt.scatter(datas[targets == t+1,0],
                datas[targets == t+1,2],
                marker=marker,
                c=c)

# LOO で交差検証する
# 予測した結果の入れ物
predicted_labels1 = []
loo = LeaveOneOut()
for train, test in loo.split(features):
    train_data = features[train]
    target_data = targets[train]

    # k-NN 法を使う
    model = KNeighborsClassifier(n_neighbors=1)
    # 訓練データを学習させる
    model.fit(train_data, target_data)
    # テストデータを予測させる
    predicted_label = model.predict(features[test])
    # 予測した結果を追加する
    predicted_labels1.append(predicted_label)

# 正解率を出力する
score1 = accuracy_score(targets, predicted_labels1)
print(score1)

# LOO で交差検証する
# 予測した結果の入れ物
predicted_labels2 = []
loo = LeaveOneOut()
for train, test in loo.split(datas):
    train_data = datas[train]
    target_data = targets[train]

    # k-NN 法を使う
    model = KNeighborsClassifier(n_neighbors=1)
    # 訓練データを学習させる
    model.fit(train_data, target_data)
    # テストデータを予測させる
    predicted_label = model.predict(datas[test])
    # 予測した結果を追加する
    predicted_labels2.append(predicted_label)

# 正解率を出力する
score2 = accuracy_score(targets, predicted_labels2)
print(score2)

# k分割法で検証する
clf = LogisticRegression()

kfolds = []
#kfolds.append(KFold(n_splits=3)) #ダメな例
kfolds.append(KFold(n_splits=10, shuffle=True, random_state=0))
#kfolds.append(StratifiedKFold(n_splits=10))

# 正解率を出力する
for kfold in kfolds:
    print("{}".format(cross_val_score(clf, features, targets, cv=kfold)))