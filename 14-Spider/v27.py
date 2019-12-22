'''
中文unicode案例
'''


import re

hello = u'你好，世界'

#[\u4e00-\u9fa5]+')大部分中文unicode编码范围
pattern = re.compile(r'[\u4e00-\u9fa5]+')

m = pattern.findall(hello)
print(m)

m = pattern.finditer(hello)

for item in m:
    print(item.group())