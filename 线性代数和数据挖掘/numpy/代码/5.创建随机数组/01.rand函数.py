# rand
# 生成一个0~1之间的随机数
import numpy as np

# 设置随机数种子
np.random.seed(5)

# 生成1个单行的随机数组
arr1 = np.random.rand()
print("arr1:",arr1)

# 生成1个一行三列的随机数组
arr2 = np.random.rand(3)
print("arr2:",arr2)

# 生成1个2行2列的随机数组
arr3 = np.random.rand(2,2)
print("arr3:",arr3)

# 生成一个3行2列的随机数组
arr4 = np.random.rand(3,2,2)
print("arr4:",arr4)