import numpy as np
import matplotlib.pyplot as plt
# 创建数据
x = np.arange(0, 3 * np.pi, 0.01)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 在第一个位置创建子图
plt.subplot(2, 1, 1)  # 2行1列，第一个子图
plt.plot(x, y_sin)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y_sin')
# 在第二个位置创建子图
plt.subplot(2, 1, 2)  # 2行1列，第二个子图
plt.plot(x, y_cos)
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('y_cos')
# 调用 tight_layout  用于自动调整子图（subplot）之间的间距，以避免子图内容被遮挡。它主要解决了当你有多个子图时，子图之间可能会重叠的问题。
plt.tight_layout()
 # 显示图形
plt.show()