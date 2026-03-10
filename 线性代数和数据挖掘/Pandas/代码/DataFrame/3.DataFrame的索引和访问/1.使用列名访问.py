import pandas as pd
import numpy as np

data = {
    '姓名': ['小明', '小红', '小刚'],
    '年龄': [20, 18, 22],
    '成绩': [85, 90, 88]
}
df = pd.DataFrame(data)
print(df["年龄"])
print(df[["成绩","年龄"]])
print(df.dtypes)