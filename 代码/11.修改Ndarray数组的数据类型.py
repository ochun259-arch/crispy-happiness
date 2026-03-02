# 修改Ndarray数组的数据类型
import numpy as np

# 创建一个浮点数数组
arr = np.array([1.1, 2.2, 3.3])

# 使用 astype 方法将数组转换为整数类型
new_arr = arr.astype(np.int32)

print("Old array:", arr)
print("old type:", arr.dtype)
print("New array:", new_arr)
print("new type:", new_arr.dtype)

"""
    casting参数说明：
    'no'： 表示根本不应该进行转换数据类型。 不允许转换
    'equiv'： 允许数值上等价的类型转换，即转换前后数据的位表示相同。这意味着转
              换不会导致数据丢失。  不导致数据丢失情况下，位表示相同就可以转换。
    'safe'：允许安全的类型转换，即转换过程中不会丢失信息。
    'same_kind'：允许相同数据类型类别内的转换。例如，允许整型和整型之间、浮点
    型和浮点型之间的转换，但是不允许整型和浮点型之间的转换。
    'unsafe'：允许任何类型的转换，不考虑是否会导致数据丢失或改变。这是最不安全
    的选项，因为它可能会静默地丢弃数据。
比如：
从 int64 到 int32 的转换：
    'no'：不允许。
    'equiv'：不允许。
    'safe'：不允许。
    'same_kind'：允许。
    'unsafe'：允许。
从 float64 到 int32 的转换：
    'no'：不允许，因为会丢失小数部分。
    'equiv'、'safe'、'same_kind'：不允许，因为这不是数值上等价或安全的转换。
    'unsafe'：允许，但会丢失小数部分。
"""


arr1 = np.ones((3,2),dtype=np.int32)
print(arr1,"\n","arr1的数据类型为：",arr1.dtype)
arr1_astype = arr1.astype(np.float32,casting='unsafe')
print(arr1_astype,"\n","arr1_astype的数据类型为：",arr1_astype.dtype)