import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [np.nan, np.nan, 6],
    'C': [7, np.nan, 9]
})
"""标量填充"""
print("标量填充")
print(df)
print(df.fillna(value=0))         # 指定某个值填充，可以是单个值也可以是字典，或者是一个Series
print(df.ffill())                 # 使用上一个有效观测值填充
print(df.bfill())                 # 使用下一个有效观测值填充
print(df.fillna(0,axis=1))  # 0表示按列填充，1表示按行填充 （默认0）
"""指定列标签填充"""
data = {
    'A':'a',
    'B':'b',
    'C':'c'
}
print("指定列标签填充")
print(df.fillna(value=data))
"""使用limit参数"""
print("使用limit参数")
print(df.fillna(value=0,limit=2))    # limit限制填充的数量
    