import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
'C': [12, np.nan,np.nan, np.nan]
})
# 计算每列的总和
sum_per_column = df.sum()
print("Sum per column:")
print(sum_per_column)
# 计算每行的总和
sum_per_row = df.sum(axis='columns')
print("\nSum per row:")
print(sum_per_row)
# 只计算数值列的总和
sum_numeric_only = df.sum(numeric_only=True)
print("\nSum numeric only:")
print(sum_numeric_only)
# 使用 min_count 参数
sum_with_min_count = df.sum(min_count=2)
print("\nSum with min_count=2:")
print(sum_with_min_count)