# 4.2.1
# nothing to code

# 4.2.2
from inspect import classify_class_attrs
from turtle import color
from typing import ItemsView
import pandas as pd
import sklearn
from sklearn import preprocessing

# サンプルデータを生成(Tシャツの色・サイズ・価格・クラスラベル)
df = pd.DataFrame([
    ['green', 'M', 10.1, 'class2'],
    ['red', 'L', 13.5, 'class1'],
    ['blue', 'XL', 15.3, 'class2']
])

# 列名を設定
df.columns = ['color', 'size', 'price', 'classlabel']
df

# 4.2.3
# Tシャツのサイズと整数を対応させるディクショナリを生成
size_mapping = {'XL':3, 'L':2, 'M':1}

# Tシャツのサイズを整数に変換
df['size'] = df['size'].map(size_mapping)
df

# Tシャツサイズの逆変換
inv_size_mapping = {v: k for k, v in size_mapping.items()}
df['size'].map(inv_size_mapping)

# 4.2.4
import numpy as np

# クラスラベルと整数を対応させるディクショナリを生成
enumerate(np.unique(df['classlabel']))
class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}
class_mapping

# クラスラベルを整数に変換
df['classlabel'] = df['classlabel'].map(class_mapping)
df

# 逆をやる
inv_class_mapping = {v: k for k, v in class_mapping.items()}
df['classlabel'] = df['classlabel'].map(inv_class_mapping)
df

from sklearn.preprocessing import LabelEncoder
# ラベルエンコーダのインスタンスを生成
class_le = LabelEncoder()

# クラスラベルから整数に変換
y = class_le.fit_transform(df['classlabel'].values)
y

# クラスラベルを文字列に戻す
class_le.inverse_transform(y)

# 4.2.4

# Tシャツの色、サイズ、価格を抽出
df[['color', 'size', 'price']]
df[['color', 'size', 'price']].values
X = df[['color', 'size', 'price']].values
color_le = LabelEncoder()
X[:, 0]
X[:, 0] = color_le.fit_transform(X[:, 0])
X

# one-hot encoding
from sklearn.preprocessing import OneHotEncoder
X = df[['color', 'size', 'price']].values
X

# one-hot encoderの生成
color_ohe = OneHotEncoder()
# one-hot encodingを実行
X[:,0]
X[:,0].reshape(-1,1)
color_ohe.fit_transform(X[:,0].reshape(-1,1))
color_ohe.fit_transform(X[:,0].reshape(-1,1)).toarray()

from sklearn.compose import ColumnTransformer
X
c_transf = ColumnTransformer([('onehot', OneHotEncoder(), [0]),
                              ('nothing', 'passthrough', [1,2])])
c_transf.fit_transform(X)
c_transf.fit_transform(X).astype(float)

# pandasによるone-hot encoding
df[['price', 'color', 'size']]
pd.get_dummies(df[['price', 'color', 'size']])
# 冗長な列を削除する
pd.get_dummies(df[['price', 'color', 'size']], drop_first=True)

# one-hot encoderで、冗長な列を削除する
color_ohe = OneHotEncoder(categories='auto', drop='first')
c_transf = ColumnTransformer([('onehot', color_ohe, [0]),
                              ('nothing', 'passthrough', [1,2])])
c_transf.fit_transform(X).astype(float)
