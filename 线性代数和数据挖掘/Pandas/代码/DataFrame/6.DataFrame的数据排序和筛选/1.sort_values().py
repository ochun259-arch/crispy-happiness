import numpy as np
import pandas as pd
# 创建一个示例 DataFrame
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
# 打印原始DataFrame
print(df)
print("根据'col1'列对DataFrame进行排序")
res1 = df.sort_values(by=['col1'])
print(res1)
print("根据'col1'和 'col2'列对DataFrame进行排序")
res2 = df.sort_values(by=['col1','col2'])
print(res2)