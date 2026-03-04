import matplotlib.pyplot as plt

 # 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
 # 数据
labels = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]
 # 创建条形图，并添加关键字参数
plt.bar(labels, values,
        width=0.3,       # 条形的宽度
        color='b',       # 条形的填充颜色,
        edgecolor='r',   # 条形边缘的颜色
        linewidth=2,     # 条形边缘的线宽
        linestyle='-',   # 条形边缘的线型
        alpha=0.7,       # 条形的透明度
        hatch='x',       # 条形的填充图案
        align='center',  # 条形与x位置的对齐方式
        label='条形图'     # 为条形创建图例时使用的标签
       )
help(plt.bar)
# 显示图例
plt.legend()

# 显示图表
plt.show()