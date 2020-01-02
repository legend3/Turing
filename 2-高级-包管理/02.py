# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib
tuling = importlib.import_module("01")  # 相当于导入了一个叫01的模块并把导入模块赋值给了tuling


stu = tuling.Student()
stu.say()
