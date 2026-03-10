import matplotlib.pyplot as plt
# 数据
sizes = [25, 35, 20, 21]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
 # 绘制饼图，使用 **kwargs 定制扇形
plt.pie(sizes,                   # 饼图中每个扇形的尺寸
        explode=[0.5, 0, 0, 0],    # 用于指定每个扇形是否突出显示
        labels=labels,           # 用于指定每个扇形的标签
        colors=colors,           # 用于指定每个扇形的颜色
        autopct='%.1f%%',       # 用于在饼图上显示每个扇形的百分比
        startangle=0,          # 饼图开始的角度，默认为 0（即从 x 轴正方向开始）
        shadow=True,            # 用于指定是否为饼图添加阴影
        radius=1,                # 饼图的半径
        wedgeprops=dict(edgecolor='black', linewidth=2, linestyle='-'),  # 指定饼图中每个扇形的属性
        textprops=dict(color='red', weight='bold'),  # 用于指定饼图中标签的文本属性，这里指定文本的颜色和字体的粗细为粗体
        center=(0, 0),            # 用于指定饼图的中心位置
        frame=False,              # 用于指定是否为饼图添加一个坐标轴
        normalize = True ,         # 为True则x中的值将被归一化以使它们的总和等于1
        hatch = 'x'                # 图案填充
)
 # 显示图表
plt.show()
