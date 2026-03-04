"""
numpy.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>,
initial=<no value>, where=<no value>)
"""
import numpy as np
# 1、计算整个数据的总和
arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(arr)
# 计算整个数组的和
total_sum = np.sum(arr)
print(total_sum)
# 2、沿着相应方向计算总和
# 计算每一列的和
sum_col = np.sum(arr, axis=0)
print(sum_col)
# 计算每一行的和
sum_row = np.sum(arr, axis=1)
print(sum_row)
# 保留原始维度
sum_row_keep = np.sum(arr, axis=1, keepdims=True)
print(sum_row_keep)