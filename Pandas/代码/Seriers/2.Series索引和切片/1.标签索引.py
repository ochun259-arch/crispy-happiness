import pandas as pd
# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c','d', 0])
# 通过标签索引获取元素
print(series['a'])
print(series['c'])
print(series[0])   # 之所以能通过下标访问，是因为之前的标签就是从0开始，一次递增