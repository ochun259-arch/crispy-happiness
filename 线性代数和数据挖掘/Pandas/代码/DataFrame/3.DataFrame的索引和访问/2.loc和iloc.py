import pandas as pd
data = {
    '姓名': ['小明', '小红', '小刚'],
    '年龄': [20, 18, 22],
    '成绩': [85, 90, 88]
}
df = pd.DataFrame(data)
print(df.loc[0,'年龄'])
print(df.loc[0:2,"姓名":"成绩"])
print(df.iloc[0,2])
print(df.iloc[0:2,1:3])
