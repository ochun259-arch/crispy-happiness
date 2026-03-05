import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.5, 5.5, 6.5],
    'C': ['7', '8', '9']
})

print(df)
print("将'A'转换为浮点数类型")
print(df['A'].astype(float))
print("使用字典转换不同的数据类型")
c = df.astype({
    'B': int,
    'C': int
})
print(c)
c = df.astype('float64')
print(c)