import pandas as pd
# 定义一个变量data，并赋值为0
data = 9
# 使用pandas库的Series函数创建一个Series对象
# 第一个参数是要作为Series数据的值，这里是0
# 第二个参数是一个列表，用于指定Series的索引，这里指定了索引为['a','b','c']
series = pd.Series(data,index=['a','b','c'])
series1 = pd.Series(data)
print(series)
print(series1)
