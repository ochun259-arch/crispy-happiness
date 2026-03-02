# 使用numpy对数组进行全数字+1操作
import numpy as np
arr = np.array([1,2,3,4,5])
my_list = [1,2,3,4,5]
print(my_list)
print(arr)
print(type(arr))
# Numpy数组可以直接进行+1操作，它会令所有数组中的数字都去进行+1
arr = arr + 1
print(arr)

# 使用list完成两个列表元素的加法
a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c)
# 使用numpy完成两个列表元素的加法
x = np.array(a)
y = np.array(b)
z = x + y
print(z)
