import pandas as pd
import numpy as np

"""
参数：
axis : {0 or ‘index’, 1 or ‘columns’}，默认为 0。表示沿着哪个轴进行排序。0按照行标签排序，1按照列标签排序。
level : 如果索引是多级索引，指定要排序的级别。可以是整数或整数列表。
ascending : 默认为 True 。表示排序是升序还是降序。
inplace : 是否在原地修改 DataFrame。
kind : {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}，默认为 ‘quicksort’。排序算法。
na_position : {‘first’, ‘last’}，默认为 ‘last’。缺失值的放置位置。
sort_remaining : 是否对剩余的级别进行排序。仅在多级索引时有效。默认值为True 。
ignore_index : 是否忽略原来的索引，重新生成一个新的默认整数索引。默认值为 False 。
key : 函数，默认为 None 。应用于索引的函数，排序将基于函数的返回值。
"""
# 创建一个多级索引的DataFrame
arrays = [np.array(['qux', 'qux', 'foo', 'foo']),
          np.array(['two', 'one', 'two', 'one'])]
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]},index=arrays)
print(df)
print("按第一层索引升序排序")
res1 = df.sort_index(level=0)
print(res1)
print("按第二层索引降序进行排序")
res2 = df.sort_index(level=1,ascending=False)
print(res2)
print("按整个索引升序排序")
res3 = df.sort_index(ascending=True)
print(res3)