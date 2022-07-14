from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


#创建一个D6
die = Die()

#投掷几次骰子并将结果存储在一个列表里
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#对结果进行可视化
x_values = list(range(1, die.num_sides + 1))
#Bar用于绘制条形图的数据集，需要传入x和y
data = [Bar(x=x_values, y=frequencies)]

#Layout用于图表布局和配置对象，这里设置了图表名称
x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果', 
        xaxis=x_axis_config, yaxis=y_axis_config)

#offline.plot这个函数需要一个包含数据和布局对象的字典，还接受一个文件名
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')