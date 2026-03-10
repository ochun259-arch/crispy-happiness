import numpy as np
# 创建三个一维数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
print(f'数组b的形状为{b.shape}, 数组b为：\n', b)
# 沿着新的轴堆叠数组
d = np.stack((a, b), axis=0)
print(f'数组d的形状为{d.shape}, 数组d为：\n', d)
# 沿着第二个轴堆叠数组
e = np.stack((a, b), axis=1)
print(f'数组e的形状为{e.shape}, 数组e为：\n', e)