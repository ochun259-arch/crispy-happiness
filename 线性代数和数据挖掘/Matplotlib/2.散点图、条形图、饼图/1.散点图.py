import numpy as np
import matplotlib.pyplot as plt
# 计算正弦曲线上的点的x和y坐标
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
# 创建一个颜色数组，基于y值映射到颜色
colors = y
# 绘制散点图，添加所有属性
plt.scatter(x, y,
            s=10,               # 添加颜色条
            c=colors,           # 散点的大小
            marker='o',         # 散点的颜色，这里使用y值映射颜色
            cmap='viridis',     # 散点的标记样式
            norm=None,          # 颜色映射
            vmin=-1,            # 颜色映射的最小值
            vmax=1,             # 颜色映射的最大值
            alpha=0.5,          # 透明度
            linewidths=0.5,     # 散点边缘的线宽
            edgecolors='w'      # 散点边缘的颜色
            )
plt.colorbar()
# 显示图形
plt.show()

