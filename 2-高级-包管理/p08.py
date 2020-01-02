'''
    导入包及包中模块
'''
import pkg01.p01  # （包和模块都会可以被执行）最先执行p01中的输出    "我是模块p01呀，你特么的叫我干毛"

pkg01.inInit()

stu = pkg01.p01.Student()
stu.say()

pkg01.p01.sayHello()
