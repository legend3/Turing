from lxml import etree

# 只能读取xml格式内容，html内容报错
html = etree.parse("./v30.html")    #XML-->String

rst = etree.tostring(html, pretty_print=True)
print(rst)
