import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame(
    {'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': ['foo', 'bar', 'baz', np.nan]
})
# 计算每列非 NaN 值的数量
count_per_column = df.count()
print("Count per column:")
print(count_per_column)
# 计算每行非 NaN 值的数量
count_per_row = df.count(axis=1)
print("\nCount per row:")
print(count_per_row)
# 只计算数值列的非 NaN 值的数量
count_numeric_only = df.count(numeric_only=True)
print("\nCount numeric only:")
print(count_numeric_only)