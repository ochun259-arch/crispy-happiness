import pandas as pd
# 创建一个包含重复行的 DataFrame
df = pd.DataFrame({
    'A': [1, 1, 2, 2, 3, 3],
    'B': [1, 1, 2, 2, 3, 3],
    'C': [1, 1, 2, 2, 3, 3]
})
print(df)
print("默认删除")
print(df.drop_duplicates())
print("指定列删除重复行")
print(df.drop_duplicates(subset='A'))
print("保留最后一次出现的重复项")
print(df.drop_duplicates(keep="last"))     # 默认为"first"
print("删除所有重复项")
print(df.drop_duplicates(keep=False))
