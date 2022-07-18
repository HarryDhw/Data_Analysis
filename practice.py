# import matplotlib.pyplot as plt

# x_values = range(1, 5001)
# y_values = [y**3 for y in x_values]
# plt.style.use('ggplot')

# fig, ax = plt.subplots()

# ax.set_title('立方值', fontsize=24)
# ax.set_xlabel('值', fontsize=18)
# ax.set_ylabel('值的立方', fontsize=18)
# ax.tick_params(axis='both', labelsize=18)

# # ax.plot(x_values, y_values, linewidth=5)
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=30)


# plt.show()

# import matplotlib.pyplot as plt
# from random_walk import RandomWalk

# rw = RandomWalk()
# rw.fill_walk()

# plt.style.use('ggplot')

# fig, ax = plt.subplots(figsize=(16, 10))

# ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)

# plt.show()

from fileinput import filename
from plotly.graph_objects import Bar, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
print(max(rw.x_values))
print(min(rw.x_values))
print(list(range(-5, 5)))

x_values = [i for i in range(min(rw.x_values), max(rw.x_values) + 1)]
data = [Bar(x=x_values, y=rw.y_values)]

x_config = {'title': 'X点'}
y_config = {'title': 'Y点'}
my_layout = Layout(title='随机漫步点位',
        xaxis=x_config, yaxis=y_config)

offline.plot({'data': data, 'layout': my_layout}, filename='SJMB.html')















# from die import Die
# import matplotlib.pyplot as plt

# die8_1 = Die(8)
# die8_2 = Die(8)

# results = [die8_1.roll() + die8_2.roll() for i in range(1000)]
# # for num in range(1000):
# #     result = die8_1.roll() + die8_2.roll()
# #     results.append(result)

# # counts = []
# max_num = die8_1.num_sides + die8_2.num_sides
# # for value in range(2, max_num + 1):
# #     nums = results.count(value)
# #     counts.append(nums)
# counts = [results.count(value) for value in range(2, max_num + 1)]

# die_numbers = list(range(2, max_num + 1))

# # data = [Bar(x=die_numbers, y=counts)]

# # x_axis = {'title': '结果', 'dtick': 1}
# # y_axis = {'title': '出现的频率'}
# # my_layout = Layout(title='投掷两个D8 1000次的结果',
# #         xaxis=x_axis, yaxis=y_axis)

# # offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

# plt.style.use('Solarize_Light2')

# fig, ax = plt.subplots(figsize=(16, 10))
# ax.scatter(x=die_numbers, y=counts, c='blue', s=200)

# ax.set_title('两个D8骰子投掷1000次的结果', fontsize=24)
# ax.set_xlabel('结果', fontsize=16)
# ax.set_ylabel('频率', fontsize=16)

# ax.tick_params(axis='both', labelsize=16)

# plt.show()