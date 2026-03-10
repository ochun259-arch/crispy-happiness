import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, 7, 8],
'C': [12, 33, 1, 6] # 非数值列
})
# 计算每列的中位数
median_per_column = df.median()
print("Median per column:")
print(median_per_column)
# 计算每行的中位数
median_per_row = df.median(axis='columns')
print("\nMedian per row:")
print(median_per_row)
# 只计算数值列的中位数
median_numeric_only = df.median(numeric_only=True)
print("\nMedian numeric only:")
print(median_numeric_only)