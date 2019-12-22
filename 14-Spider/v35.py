from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.128 Safari/537.36"
}
req = request.Request(url=url,headers=headers)
rsp = request.urlopen(req)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

print("==" * 20)
print(soup.name)
print(soup.attrs)

print("==" * 20)
print(soup.div)

print("==" * 20)
print(soup.div.attrs)

print("==" * 20)
# print(soup.find_all('div'))

#查找div标签,只会查找出一个a标签
print("&&" * 20)
for k in soup.find_all('a'):
    print(k)
    print(k['href'])
    # print(type(k["href"]))
    # print(k[r'[a-z]+'])

print("==" * 20)
titles = soup.select("title")
print(titles[0])
print(titles[1])

print("==" * 12)
metas = soup.select("meta[content='always']")
# print(metas[0])


print("==" * 12)