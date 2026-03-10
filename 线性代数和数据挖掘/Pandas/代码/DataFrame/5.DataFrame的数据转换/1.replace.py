import pandas as pd
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'a', 'b', 'a']
})
print("原始DataFrame")
print(df)
print("单一值替换")
print(df.replace(to_replace='a',value='x'))
print("列表替换所有匹配值")
print(df.replace(to_replace=[2,4,'b'],value='ok'))
print("字典替换所有匹配值")
data = {
    3:100,
    'a':'什么'
}
print(df.replace(to_replace=data))
print("使用正则表达式替换")
df = pd.DataFrame({
    'col1': ['apple', 'banana', 'cherry', 'agerape', 'apricote'],
    'col2': ['apple pie', 'banana split', 'cherry tart', 'grape juice', 'apricote jam']
})
"""
    ^：匹配字符串的开始。
    a：匹配字符 "a"。
    .*：匹配任意数量的字符（包括零个字符）。
    e：匹配字符 "e"。
    $：匹配字符串的结束。
"""
df_replaced = df.replace(to_replace=r'^a.*e$', value='fruit', regex=True)
print(df_replaced)