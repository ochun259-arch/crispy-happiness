import pandas as pd
data_list = ["小明","小红","小刚"]
columns = ["姓名"]
df = pd.DataFrame(data_list,columns=columns)
print(df)

# 嵌套式
data_list1 = [
    ['小明', 20, 85],
    ['小红', 18, 90],
    ['小刚', 22, 88]
]
columns1 = ['姓名', '年龄', '成绩']
cd = pd.DataFrame(data_list1,columns=columns1)
print(cd)