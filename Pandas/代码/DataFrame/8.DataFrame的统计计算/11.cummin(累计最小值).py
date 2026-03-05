import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [3, 2, np.nan, 4, 1],
    'B': [5, np.nan, 3, 2, 6],
    # 'C': ['foo', 'bar', 'baz', 'qux', 'quux']  # 非数值列
})
# 计算每列的累积最小值
cummin_per_column = df.cummin(axis=0)
print("Cumulative min per column:")
print(cummin_per_column)
# 计算每行的累积最小值
cummin_per_row = df.cummin(axis=1)
print("\nCumulative min per row:")
print(cummin_per_row)