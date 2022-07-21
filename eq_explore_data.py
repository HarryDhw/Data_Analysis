import json
import plotly.express as px
import pandas as pd

#探索数据的结构
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #读取json格式文件

#打印出地震数据是否和文件上的地震数据相对应
all_eq_datas = all_eq_data['features']
print(len(all_eq_datas))

#提取震级数据
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_datas:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

#用pandas绘制更易懂
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()

#绘制地震级散点图
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    # labels={'x': '经度', 'y': '纬度'}, #使用pandas后可删除掉这行
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=1200,
    height=800,
    title='全球地震散点图',
    size='震级', #用点的大小表示震级强度
    size_max=10, #设置点的最大值
    color='震级', #用颜色深浅表示震级强度
    color_continuous_scale='darkmint', #自带的渐变配色进行更改
    hover_name='位置',
)

#查询自带的渐变配色方案
# for key in px.colors.named_colorscales():
#     print(key)

fig.write_html('global_earthquakes.html')
fig.show()

# readable_file = 'readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4) #把上边读取出来的json文件写入到新文件里
