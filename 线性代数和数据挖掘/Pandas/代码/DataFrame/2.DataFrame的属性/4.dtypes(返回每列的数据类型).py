import pandas as pd
data = {
   '姓名': ['小明', '小红', '小刚'],
   '年龄': [20, 18, 22],
   '成绩': [85, 90, 88]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)
print(df.dtypes)