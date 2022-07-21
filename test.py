# import matplotlib.pyplot as plt
# print(plt.style.available)

# from datetime import datetime

# first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(first_date)

# '''
# 模块datetime 中设置日期和时间格式的实参
# %A 星期几  如Monday
# %B 月份名   如January
# %m 用数表示的月份   如(01~12)
# %d 用数表示的月份中的一天   如(01~31)
# %Y 四位的年份   如2019
# %y 两位的年份   如19
# %H 24小时制的小时数 (00~23)
# %I 12小时制的小时数 (01~12)
# %p am或pm
# %M 分钟数(00~59)
# %S 秒数(00~59)
# '''

# for index, item in enumerate(['harry', 'yoyo', 'jimi']):
#     print(index, item)

import plotly.express as px

for key in px.colors.named_colorscales():
    print(key)