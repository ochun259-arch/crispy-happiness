import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    # 'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
})
# 计算每列的标准差
std_per_column = df.std()
print("Standard deviation per column:")
print(std_per_column)
# 计算每行的标准差
std_per_row = df.std(axis='columns')
print("\nStandard deviation per row:")
print(std_per_row)
# 只计算数值列的标准差，并且使用无偏估计（ddof=1）
std_numeric_only = df.std(numeric_only=True, ddof=1)
print("\nStandard deviation numeric only with ddof=1:")
print(std_numeric_only)