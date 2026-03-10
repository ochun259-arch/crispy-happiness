import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    # 'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
    'C': [32, 10, 0, 1]  # 非数值列
})
# 计算每列的最小值
min_per_column = df.min()
print("Min per column:")
print(min_per_column)
# 计算每行的最小值
min_per_row = df.min(axis='columns')
print("\nMin per row:")
print(min_per_row)
# 只计算数值列的最小值
min_numeric_only = df.min(numeric_only=True)
print("\nMin numeric only:")
print(min_numeric_only)