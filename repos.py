from textwrap import indent
import requests

#使用Plotly可视化仓库
from plotly.graph_objs import Bar
from plotly import offline

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}') #查看响应是否是200
#将API响应赋给一个变量
response_dict = r.json()  #因为返回的是json格式信息，所以使用json()方法转换为python字典
print(f'Total repositories: {response_dict["total_count"]}')

#探索有关仓库的信息
repo_dicts = response_dict['items']

#为可视化准备x和y列表
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)
    repo_url = repo_dict['html_url']
    repo_link = f'<a href="{repo_url}" target="_blank">{repo_name}</a>'
    repo_links.append(repo_link)

#可视化 marker参数用于更改颜色和样式
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '用户',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '星数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

#研究每个仓库
# print('\nSelected information about each repository:')
# for repo_dict in repo_dicts:
#     print(f'Name: {repo_dict["name"]}')
#     print(f'Owner: {repo_dict["owner"]["login"]}')
#     print(f'Stars: {repo_dict["stargazers_count"]}')
#     print(f'Repository: {repo_dict["html_url"]}')
#     print(f'Created: {repo_dict["created_at"]}')
#     print(f'Updated: {repo_dict["updated_at"]}')
#     print(f'Description: {repo_dict["description"]}')

#监视API的速率限制
#https://api.github.com/rate_limit