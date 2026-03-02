# 使用array函数创建Ndarray数组
# 创建一维数组
import numpy as np
# 可以直接使用array函数进行创建
arr1 = np.array([1, 2, 3, 4, 5])
print(type(arr1))
print(arr1)
# 也可以将列表、元组等数据转化为Ndarray数组
ls1 = [1, 2, 3, 4, 5]
arr2 = np.array(ls1)
print(type(ls1))
print(type(arr2))
print(ls1)
print(arr2)


# 创建二维数组
import numpy as np
# 可以直接使用array函数进行创建
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(type(arr1))
print(arr1)


# 创建三维数组
import numpy as np
# 可以直接使用array函数进行创建
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(type(arr1))
print(arr1)