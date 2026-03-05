import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 1],
})
# 计算每列的累积最大值
cummax_per_column = df.cummax(axis=0)
print("Cumulative max per column:")
print(cummax_per_column)
# 计算每行的累积最大值
cummax_per_row = df.cummax(axis=1)
print("\nCumulative max per row:")
print(cummax_per_row)