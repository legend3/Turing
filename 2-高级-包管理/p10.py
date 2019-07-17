#（此时）因为__init__.py中增添了__all__=['p01']，所以按照`__all__` 指定的子包或者模块进行加载，则不会载入`__init__`中的内容
from pkg02 import *

# inInit()

stu = p01.Student()
stu.say()

p01.sayHello()

stu2 = p02.Student2()
stu2.say()