import pandas as pd
# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c','d', 'e'])
# 通过位置切片
print(series[:])
# 通过标签切片
print(series['b':'d'])