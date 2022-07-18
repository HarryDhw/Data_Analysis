import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  #csv.reader(f)读取文件并赋值给变量reader
    header_row = next(reader)   #next(reader)读取文件第一行
    # first_row = next(reader)    #再次调用就是读取文件第二行  #为了不影响读取所以注释掉这行

    #对列表调用enumerate()来获取每个元素的索引及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header)#由此可知日期DATE和最高温度TMAX的索引分别是2，5

    #提取并读取数据
    #从文件中获取最高温度和日期
    highs, dates = [], []
    for row in reader:  #读取文件的每一行
        current_date = datetime.strptime(row[2], '%Y-%m-%d')#日期转化
        dates.append(current_date)
        high = int(row[5])  #上边已知最高温度是索引5,并用int转换为整数
        highs.append(high)

#根据最高温度绘制图形
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#设置图形格式
ax.set_title('2018年7月每日最高温度', fontsize=24)
ax.set_xlabel('日期', fontsize=16)
fig.autofmt_xdate() #把日期绘制倾斜以免彼此重复
ax.set_ylabel('温度(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()