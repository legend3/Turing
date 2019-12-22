'''
爬去豆瓣电影数据(一个页面下拉，永远有下拉不完的东西，则可证实使用了ajax<下拉一段，ajax一次....下拉一段，ajax一次....>)
了解ajax的基本爬取方式

'''
from urllib import request
import json


url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"#根据start、limit定位到具体页面


rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)