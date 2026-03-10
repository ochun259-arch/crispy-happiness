"""
numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<novalue>)
"""
import numpy as np

#1、 计算整个数据的平均值
# 创建一个一维数组
arr = np.array([1, 2, 3, 4, 5])
# 计算整个数组的平均值
mean_arr = np.mean(arr)
# 输出结果
print(mean_arr)
# 创建一个二维数组
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
# 计算整个二维数组的平均值
mean_arr_2d = np.mean(arr_2d)
# 输出结果
print(mean_arr_2d)

# 2、 沿相应方向获得平均值
# 计算二维数组沿着列的平均值
mean_arr_2d_col = np.mean(arr_2d, axis=0)
# 输出结果
print(mean_arr_2d_col)
# 计算二维数组沿着行的平均值
mean_arr_2d_row = np.mean(arr_2d, axis=1)
# 输出结果
print(mean_arr_2d_row)
# 使用 keepdims=True 保留维度
mean_arr_2d_row_keepdims = np.mean(arr_2d, axis=1, keepdims=True)
# 输出结果
print(mean_arr_2d_row_keepdims)

# 3、 数组为空以及数据有nan的情况
# 情形 1：整个数组为空
a_empty = np.array([])
mean_empty = np.mean(a_empty)
print("空数组的均值:", mean_empty)
# 注意：运行时会显示警告 "Mean of empty slice."，并返回 nan

# 情形 2：指定轴上的所有元素都是 NaN
# 构造一个二维数组，其中第一列全为 NaN，第二列包含有效数字
a = np.array([[np.nan, 2],
              [np.nan, 4]])
mean_axis0 = np.mean(a, axis=0)
print("沿轴0计算均值:", mean_axis0)
# 解释：
# 第一列：所有值都是 NaN，所以均值为 nan
# 第二列：均值为 (2 + 4) / 2 = 3