import pandas as pd
s1 = pd.Series(['小明', '小红', '小刚'], name='姓名')
s2 = pd.Series([20, 18, 22], name='年龄')
s3 = pd.Series([85, 90, 88], name='成绩')
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)
df1 = pd.concat([s1,s2,s3],axis=1)
print(df1)
