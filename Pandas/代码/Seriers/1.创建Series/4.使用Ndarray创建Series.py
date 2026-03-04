import pandas as pd
import numpy as np
data = np.array([1,2,3,4,5])
series = pd.Series(data,dtype=float,name="oo")
print(series)

"""
    name参数的使用
"""

s1 = pd.Series([1,2,3],name="yy")
s2 = pd.Series([4,5,6],name="yc")
# 合并s1，s2生成一个新的DataFrame
df = pd.concat([s1,s2],axis=1)
print(df)
