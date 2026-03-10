import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    # 'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
})
# 计算每列的方差
var_per_column = df.var()
print("Variance per column:")
print(var_per_column)
# 计算每行的方差
var_per_row = df.var(axis='columns')
print("\nVariance per row:")
print(var_per_row)
# 只计算数值列的方差，并且使用无偏估计（ddof=1）
var_numeric_only = df.var(numeric_only=True, ddof=1)
print("\nVariance numeric only with ddof=1:")
print(var_numeric_only)