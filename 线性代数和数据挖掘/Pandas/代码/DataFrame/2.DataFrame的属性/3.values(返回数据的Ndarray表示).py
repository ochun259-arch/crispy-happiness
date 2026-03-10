import pandas as pd
import numpy as np

data = {
 '姓名': ['小明', '小红', '小刚'],
 '年龄': [20, 18, 22],
 '成绩': [85, 90, 88]
}
s = np.array(data)
print(s)
print("-"*50)

df = pd.DataFrame(data)
print(df)
print(df.values)