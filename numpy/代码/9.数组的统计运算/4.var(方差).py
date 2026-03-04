"""
numpy.var(a, axis=None, dtype=None, out=None, keepdims=<no value>)
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
# 计算整个数组的方差
total_var = np.var(arr)
# 计算每一列的方差
var_col = np.var(arr, axis=0)
# 计算每一行的方差
var_row = np.var(arr, axis=1)
print(total_var)
print(var_col)
print(var_row)