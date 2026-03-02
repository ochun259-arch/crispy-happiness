# 查看Ndarray数组的形状
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1)
print(arr1.shape)


# 查看Ndarray数组的数据类型
import numpy as np

# 可以在创建的时候去指定数据类型
arr1 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

print(arr1)
print(arr1.dtype)


# size:统计数组中有多少个元素
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1)
print(arr1.shape)
print(arr1.size)


# ndim：查看数组的维度
import numpy as np

arr1 = np.array([[[[1, 2, 3], [4, 5, 6]]]])

print(arr1)
print(arr1.shape)
print(arr1.ndim)