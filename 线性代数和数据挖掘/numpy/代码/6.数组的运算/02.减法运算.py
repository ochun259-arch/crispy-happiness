import numpy as np

print("----------标量和数组----------")
# 生成一个2行3列的Ndarray数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
# 使用减法计算
# 数组加上标量，会使数组的每一个元素都加上该标量得到一个新数组
arr -= 1
print(arr)

print("----------数组和数组----------")
# 生成两个2行3列的数组
arr1 = np.array([[11, 12, 13], [14, 15, 16]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# 数组减去数组，会使对应位置的元素相减
arr3 = arr1 - arr2
print(arr1)
print(arr2)
print('运算的结果为：\n', arr3)