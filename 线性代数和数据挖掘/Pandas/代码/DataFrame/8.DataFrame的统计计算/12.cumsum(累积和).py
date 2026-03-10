import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 6],
    # 'C': ['foo', 'bar', 'baz', 'qux', 'quux']  # 非数值列
})
# 计算每列的累积和
cumsum_per_column = df.cumsum(axis=0)
print("Cumulative sum per column:")
print(cumsum_per_column)
# 计算每行的累积和
cumsum_per_row = df.cumsum(axis=1)
print("\nCumulative sum per row:")
print(cumsum_per_row)