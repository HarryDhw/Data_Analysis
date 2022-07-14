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

import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(16, 10))

ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)

plt.show()