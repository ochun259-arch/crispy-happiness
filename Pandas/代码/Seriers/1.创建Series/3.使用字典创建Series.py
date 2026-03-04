import pandas as pd
data = {'a':1,'b':2,'c':3}
series = pd.Series(data)
print(series)

'''
    注意 ： 如果使用字典创建Series，并且指定了与字典的键不同的index参数，那么生成的Series数组
中的数据就是以index参数的值为索引，但索引所对应的值是NaN。
     在Pandas中， NaN （Not a Number）是一个特殊的浮点数，用于表示缺失数据或无
    效数据。
'''

data1 = {'a':1,'b':2,'c':3}
s = pd.Series(data,index=['a','b','c','d'])
print(s)

data2 = {'a':1,'b':2,'c':3}
s1 = pd.Series(data,index=['f','g','h','j'])
print(s1)