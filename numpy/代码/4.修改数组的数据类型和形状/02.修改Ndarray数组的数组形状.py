# 修改Ndarray数组的形状
print("----------reshape----------")
# reshape：
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print('shape--a', a.shape)

b = a.reshape((3, 2))
print(a)
print(b)
print('shape--b',b.shape)

print("----------resize----------")
# resize:
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print('before:', a.shape)

a.resize((3, 2))

print('after:', a.shape)
print(a)

a.resize((2, 2))
print(a)

a.resize((5, 5))
print(a)


print("----------flatten----------")
# flatten:
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)
b = a.flatten()
print(b)
b[0] = 10
print(a)
print(b)


print("----------ravel----------")
# ravel:
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.ravel()
print(b)


import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.flatten()
c = a.ravel()
d = a.ravel(order='F')

a[0][0] = 100
a[1][0] = 50
print('a', a)
print('b', b)
print('c', c)
print('d', d)


print("----------转置----------")
# T:转置：
import numpy as np

# 创建一个二维数组
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

# 获取转置
transposed_arr = arr_2d.T

print("Original array:")
print(arr_2d)
print("Transposed array:")
print(transposed_arr)