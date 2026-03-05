import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 6],
    # 'C': ['foo', 'bar', 'baz', 'qux', 'quux']  # 非数值列
})
# 计算每列的累积乘积
cumprod_per_column = df.cumprod(axis=0)
print("Cumulative product per column:")
print(cumprod_per_column)
# 计算每行的累积乘积
cumprod_per_row = df.cumprod(axis=1)
print("\nCumulative product per row:")
print(cumprod_per_row)