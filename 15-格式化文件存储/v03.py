import xml.etree.ElementTree as et


tree = et.parse(r'to_edit.xml')#'r'是防止字符转义

'''
getroot()--->Return root element of this tree
获取到当前树的root（最高）元素
'''
root = tree.getroot()#root--->School
for e in root.iter('Name'):
    print(e.text)


for stu in root.iter('Student'):
    name = stu.find('Name')

    if name != None:
        name.set( 'test', name.text * 2)#设置Name元素的test属性的属性值

stu = root.find('Student')#第一个Student，因此stu为一个对象地址
e = et.Element('ADDer')#创建一个元素
e.attrib = {'a':'b'}#设置属性键值对
e.text = 'i do it!'#设置属性内容

stu.append(e)
# 一定要把修改后的内容写回文件，否则修改无效
tree.write('to_edit.xml')
