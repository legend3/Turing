from urllib import request
from bs4 import BeautifulSoup

'''
String
'''
url = 'http://www.baidu.com'
rsp = request.urlopen(url)
content = rsp.read()#byte
soup = BeautifulSoup(content,'lxml')
# bs自动转码
content = soup.prettify()
print(content)

'''
File
'''
soupFile = BeautifulSoup(open('./v30.html'),'lxml')#'lxml'，转化成lxml类型
# bs自动转码
print(soupFile)
contentFile = soupFile.prettify()
print(contentFile)