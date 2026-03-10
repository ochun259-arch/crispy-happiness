import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})
# 打印原始DataFrame
print(df)
print(df.dropna())
print(df.dropna(axis=1))           # 0表示按行删除，1表示按列删除 (默认0）
print(df.dropna(how='any'))        # 有一个为nan则删除该行或该列  （默认any）
print(df.dropna(how='all'))        # 该行或该列都是nan则删除该行或该列
print(df.dropna(thresh=2))         # 指定该行或该列有多少个nan则删除该行或该列
print(df.dropna(subset='A'))       # 指  定在哪一列中搜索nan （默认搜索所有列）