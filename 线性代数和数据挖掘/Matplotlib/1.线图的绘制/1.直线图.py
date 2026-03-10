import numpy as np
import matplotlib.pyplot as plt
 # 只有两个点的x和y坐标
x = np.array([0, 5])  # 两个点的x坐标
y = np.array([0, 10])
# 对应的y坐标
# 使用Matplotlib绘制两个点的直线，并添加kwargs属性
plt.plot(x, y, '-',
            label='Line between two points',  # 图例标签
            linewidth=2,  # 线宽
            color='red',  # 线的颜色
            marker='o',  # 标记样式
            markersize=10,  # 标记的大小
            markeredgecolor='black',  # 标记边缘的颜色
            markeredgewidth=2,  # 标记边缘的宽度
            markerfacecolor='none',  # 标记内部的颜色
            alpha=1.0  # 透明度
         )

# 显示图例
plt.legend()
 # 显示图形
plt.show()