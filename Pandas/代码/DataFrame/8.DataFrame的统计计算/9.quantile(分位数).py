import pandas as pd
# 创建一个DataFrame
data = {
    'col1': [10, 20, 30, 40, 50],
    'col2': [15, 25, 35, 45, 55],
    'col3': [20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
# 按列方向计算0.5分位数（中位数）
col_median = df.quantile(0.5, axis=0)
print("按列方向的0.5分位数（中位数）:\n", col_median)
# 按行方向计算0.5分位数（中位数）
row_median = df.quantile(0.5, axis=1)
print("按行方向的0.5分位数（中位数）:\n", row_median)
