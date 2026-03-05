import pandas as pd

"""
参数：
objs : 要连接的对象列表。
axis : {0, 1, ‘index’, ‘columns’}，默认为 0。
join : 连接方式。可以是：
'outer' ：取所有索引的并集。
'inner' ：取所有索引的交集。
ignore_index : 是否忽略原来的索引，重新生成一个新的默认整数索引。默认值为 False 。
keys : 用于生成多级索引的键列表。每个键对应一个对象。
levels : 用于多级索引的级别列表。通常与 keys 一起使用。
names : 用于多级索引的名称列表。通常与 keys 一起使用。
verify_integrity : 是否验证最终的 DataFrame 是否有重复的索引。默认值为False 。
sort : 是否对结果按照列名进行升序排序。默认值为 False 。
copy : 是否复制数据。
"""
# 创建两个 DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['F4', 'F5', 'F6', 'F7']},
                   index=[4, 5, 6, 7])
# 沿着竖直方向拼接两个DataFrame
result = pd.concat([df1, df2], axis=1)
print(result)