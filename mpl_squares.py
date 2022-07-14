import matplotlib.pyplot as plt

#设置字体
# import numpy as np
# #import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# print(matplotlib.matplotlib_fname()) #显示设置字体的路径


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#自动计算数据
x_values = range(1, 101)
y_values = [i**2 for i in x_values]

#使用内置样式
plt.style.use('Solarize_Light2')
#查看内置样式的方法
# import matplotlib.pyplot as plt
# print(plt.style.available)

fig, ax = plt.subplots()
#linewidth决定了plot绘制的线条粗细
#前两个参数代表x轴和y轴的数据
# ax.plot(x_values, y_values, linewidth=3)

#使用scatter用来绘制点，s参数设置大小
# ax.scatter(2, 4, s=200)
#分别传递两个x和y的列表可以绘制一系列点
ax.scatter(x_values, y_values, s=10)
#自定义颜色，c参数代表颜色
# ax.scatter(1, 1, c='red', s=20)
#也可以使用RGB
# ax.scatter(100, 10000, c=(1, 0, 0), s=20)

#使用颜色映射(颜色渐变)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20)
ax.scatter(input_values, squares, c=(1, 0, 0), s=50)

#设置图表标题并给坐标轴加上标签
ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

#设置每个坐标轴的取值范围
ax.axis([0, 110, 0, 11000])

#设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()

# #自动保存,第一个参数是文件名，第二个参数是去掉周围空白
# plt.savefig('picture1.png', bbox_inches='tight')