import sys,traceback


class DanaValueError(ValueError):
    # def __init__(self):
    #     super().__init__(self)

    def __str__(self):  # 修改获取DanaValueError地址信息为自定义的返回值
        return str(traceback.print_exc())


try:
    '''
        触发DanaValueError异常两种方式
    '''
    raise DanaValueError  # 1.异常类的实例同时被创建，那么类的__str__() 方法就会被调用
    # num = int(input("Plz input your number:"))  # 2.正常代码逻辑触发
    # rst = 100 / num
    print("计算结果是： {0}".format(rst))
except DanaValueError as d:
    print(d)
else:
    print("No Exception")
finally:
    print("反正我会被执行")
