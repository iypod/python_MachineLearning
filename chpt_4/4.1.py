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

# 欠損値を含む行を削除
df.dropna()

# 欠損値を含む列を削除
df.dropna(axis=1)

# 全ての列がNaNである行だけ削除
df.dropna(how='all')

# 非NaN値が4つ未満の行を削除
df.dropna(thresh=4)

