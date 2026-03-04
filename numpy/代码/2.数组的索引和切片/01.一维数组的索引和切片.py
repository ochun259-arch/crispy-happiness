
# 一维数组的索引方式
import numpy as np

# 创建了一个一维数组
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[4])
print(arr[-1])
print(arr[-3])
arr[0] = 10
print(arr)


# 一维数组的切片方式
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr1 = arr[4:7]
print('arr1数组元素为', arr1)

arr2 = arr[1:6:2]
print('arr2数组元素为', arr2)

# 将一个标量值赋值给一个切片时，该值会自动传播到整个选区。
arr[4:7] = 6
print('arr数组元素为：', arr)

# 也可以使用:代表全部元素
arr[:] = 10
print('arr数组元素为：', arr)

arr[:4] = 1
print(arr)