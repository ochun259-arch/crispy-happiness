import pandas as pd
# 定义一个列表data1，其中包含了整数1-5
data1 = [1,2,3,4,5]
# 定义一个元组data2，其中包含了整数5-1
data2 = (5,4,3,2,1)
# 使用pandas库的Series函数创建第一个Series对象series
# 第一个参数data1是要作为Series数据的值，即列表[1,2,3,4,5]
# 第二个参数是一个列表['a','b','c','d','e']，用于指定Series1的索引
series1 = pd.Series(data1,index=['a','b','c','d','e'])
# 使用pandas库的Series函数创建第二个Series对象series2
# 第一个参数data2是要作为Series2数据的值，即元组(5,4,3,2,1)
# 第二个参数是一个列表['a','b','c','d','e']，用于指定Series2的索引
series2 = pd.Series(data2,index=['a','b','c','d','e'])
print(series1)
print(series2)

