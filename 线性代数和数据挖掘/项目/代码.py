from typing import final

import numpy as np  # 导入NumPy库，用于数学计算
import pandas as pd  # 导入Pandas库，用于数据处理
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘制图表

# 从Excel文件中读取数据到DataFrame
df = pd.read_excel("./source.xlsx")

# 使用fillna方法将DataFrame中的缺失值替换为0
df1 = df.fillna(0)

# 从DataFrame中提取考试分数列的值
df2 = df1['attendance'].values

# 从DataFrame中提取出勤分数列的值
df3 = df1['exam'].values

# 使用NumPy的round函数计算最终成绩，考试分数占70%，出勤分数占30%
df4 = np.round(df2 * 0.3 + df3 * 0.7)

# 将计算得到的最终成绩添加到DataFrame的新列'finally'中
df['finally'] = df4

# 使用where函数根据最终成绩判断是否通过（60分及以上），并创建新列'pass'
df['pass'] = np.where(df['finally'] >= 60,'yes','no')

df.to_excel('./source1.xlsx')

# 设置直方图的区间边界，从0到110，步长为10
values = np.arange(0,110,10)

# 使用np.histogram函数计算每个区间的学生人数
hist,base = np.histogram(df['finally'], bins=values)

# 创建一个图表实例
fig = plt.figure()

# 计算条形图的宽度
bar_width = (base[1] - base[0])

# 绘制条形图，x轴是分数区间，y轴是学生人数
plt.bar(base[:-1], hist, width=bar_width, align='edge')

# 在每个条形图上添加文本，显示该区间内的学生人数
for i in range(len(hist)):
    if hist[i]:# 如果该区间有学生，则添加文本
        plt.text(base[i] + bar_width / 2, hist[i] + 0.1, str(hist[i]), ha='center')

# 设置图表的标题和坐标轴标签
plt.title('finally')
plt.xlabel('score')
plt.ylabel('number')

# 设置x轴的刻度，显示分数区间的边界
plt.xticks(base[:])

# 显示条形图
plt.show()

# 创建一个新的图表实例
fig = plt.figure()

# 使用value_counts方法统计通过和未通过的学生数量
pass_counts = df['pass'].value_counts()

# 绘制饼图，显示通过和未通过的比例
plt.pie(pass_counts,labels=pass_counts.index,autopct='%1.1f%%')

# 设置饼图的标题
plt.title('Distribution of Passing Status')

# 显示饼图
plt.show()
