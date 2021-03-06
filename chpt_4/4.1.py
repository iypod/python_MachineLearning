# 4.1.1
import pandas as pd
from io import StringIO

# サンプルデータを作成
csv_data = '''A, B, C, D
              1.0, 2.0, 3.0, 4.0
              5.0, 6.0,, 8.0
              10.0, 11.0, 12.0,'''

# サンプルデータを読み込む
df = pd.read_csv(StringIO(csv_data))
df

# 各列のnullの数
df.isnull().sum()

# NumPy配列へのアクセスの仕方
df.values

# 4.1.2
# 欠損値を含む行を削除
df.dropna()

# 欠損値を含む列を削除
df.dropna(axis=1)

# 全ての列がNaNである行だけ削除
df.dropna(how='all')

# 非NaN値が4つ未満の行を削除
df.dropna(thresh=4)

# 特定の列にNaNが含まれている行だけを削除
df.dropna(subset=['C'])

# 4.1.3
from sklearn.impute import SimpleImputer
import numpy as np

# 欠損値補完のインスタンスを生成(平均値補完)
imr = SimpleImputer(missing_values=np.nan, strategy='mean')

# データを適合
imr = imr.fit(df.values)

# 補完を実行
imputed_data = imr.transform(df.values)
imputed_data

df.fillna(df.mean())

# 4.1.4
# nothing to code