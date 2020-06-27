# 使用BeautifulSoup解析网页
# week1 第一份作业

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

#加入cookie反爬
cookie='50228D29667; _csrf=36be708eeec93b4f1dd0d923b370a7bf0a74a868bea6106baa5682b921123424; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172ee9b7735c8-05f7c26158c1e1-4353760-144000-172ee9b7736c8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593141066; mojo-uuid=c7ded4df176e5682a1927a88b9c2f612; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172eea144ea26c-0031ac5a4e8cc6-73236134-254000-172eea144eb188%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172eea144ea26c-0031ac5a4e8cc6-73236134-254000-172eea144eb188%22%7D; _lxsdk=AC1294E0B75A11EAB787AF911C0DA1B7358CB001BE4B4CB0BFCE250228D29667; mojo-session-id={"id":"c5530083b77476db6f7a5c88a0cde746","time":1593163981733}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593164011; mojo-trace-id=2; _lxsdk_s=172eff8d64c-9d4-d3-234%7C%7C4; __mta=46027419.1593141067408.1593160411479.1593164011274.12'

header = {'user-agent':user_agent,
          'cookie':cookie}


myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

#用于计数-爬取10个电影数据
i=0

#电影列表
movie_list=[]

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    #爬取10个电影数据
    if i==10:
        break

    for atag in tags.find_all('a'):
        movie_url='https://maoyan.com'+atag.get('href')
        response = requests.get(movie_url, headers=header)
        bs_info = bs(response.text, 'html.parser')

        #电影类型字符串初始化
        movie_type = ''

        for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
            film_name = tags.find('h1').text

            #因为类型有多个，所以字符串进行相加
            for atag in tags.find_all('a'):
                movie_type+=atag.text

            #上映时间是第三个li标签，用于计数
            j=0
            for atag in tags.find_all('li'):
                j+=1
                if j==3:
                    time=atag.text[:10]

        #单个电影的列表
        one_list = [film_name, movie_type.strip(), time]

    movie_list.append(one_list)
    i+=1

print(movie_list)

movie1 = pd.DataFrame(data = movie_list)
# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False,  header=['电影名称', '电影类型', '上映时间'])
