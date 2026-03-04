"""
numpy.std(a, axis=None, dtype=None, out=None, keepdims=<no value>)
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 计算整个数组的标准差
total_std = np.std(arr)
# 计算每一列的标准差
std_col = np.std(arr, axis=0)
# 计算每一行的标准差
std_row = np.std(arr, axis=1)
print(total_std)
print(std_col)
print(std_row)