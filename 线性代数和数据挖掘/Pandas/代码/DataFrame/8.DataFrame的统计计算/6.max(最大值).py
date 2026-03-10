import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
})
# 计算每列的最大值
# max_per_column = df.max()
# print("Max per column:")
# print(max_per_column)
# # 计算每行的最大值
# max_per_row = df.max(axis='columns')
# print("\nMax per row:")
# print(max_per_row)
# 只计算数值列的最大值
max_numeric_only = df.max(numeric_only=True)
print("\nMax numeric only:")
print(max_numeric_only)