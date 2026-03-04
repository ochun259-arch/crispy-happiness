import matplotlib.pyplot as plt
 # 数据
labels = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]
 # 创建条形图，并添加关键字参数
plt.bar(labels, values,
        width=0.3,       # 条形的宽度
        bottom=0,
        align='edge',  # 条形与x位置的对齐方式
        data=None,
        color='r',  # 条形的填充颜色, 和facecolor等价
        edgecolor='r',   # 条形边缘的颜色
        # facecolor = 'g', # 填充颜色
        linewidth=2,     # 条形边缘的线宽
        linestyle='-',   # 条形边缘的线型
        alpha=0.7,       # 条形的透明度
        hatch='x',       # 条形的填充图案
        log = False,     # 条形的高度不以对数尺度表示。
        label='test'     # 为条形创建图例时使用的标签
       )
help(plt.bar)
# 显示图例
plt.legend()

# 显示图表
plt.show()


'''
    data参数的使用
'''
import matplotlib.pyplot as plt

# 数据字典
data = {'categories': ['A', 'B', 'C', 'D'],
        'values': [10, 20, 15, 25]}

# 使用 data 参数，直接通过键引用数据
plt.bar(x='categories', height='values', data=data)
plt.show()

'''
   picker参数使用
'''

import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# 创建条形图并启用 picker
bars = plt.bar(categories, values, picker=True)

# 设置点击事件的回调函数
def on_pick(event):
    # 获取被点击的条形
    if isinstance(event.artist, plt.Rectangle):  # 只对条形进行操作
        event.artist.set_facecolor('red')  # 改变被点击条形的填充颜色
        plt.draw()  # 更新图形

# 连接事件
plt.gcf().canvas.mpl_connect('pick_event', on_pick)

plt.show()