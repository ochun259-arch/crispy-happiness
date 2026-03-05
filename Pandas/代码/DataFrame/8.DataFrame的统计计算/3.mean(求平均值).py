import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
'C': ['foo', 'bar', 'baz', 'qux'] # 非数值列
})
# 计算每列的平均值
# mean_per_column = df.mean()
# print("Mean per column:")
# print(mean_per_column)
# 计算每行的平均值
# mean_per_row = df.mean(axis='columns')
# print("\nMean per row:")

# print(mean_per_row)
# 只计算数值列的平均值
mean_numeric_only = df.mean(numeric_only=True)
print("\nMean numeric only:")
print(mean_numeric_only)