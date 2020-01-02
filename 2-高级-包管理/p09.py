# from pkg01 import *  # 只会执行__init__.py文件中所有的函数和类
# inInit()
# pkg01.p01.sayHello()  # 不能执行

from pkg01 import p01   #（只能执行模块部分）不会执行__init__.py的内容(会执行__init__.py的print输出)
# pkg01.inInit()  # 不会被执行
stu = p01.Student()
p01.sayHello()
