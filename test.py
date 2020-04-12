import calendar
import time,os,sys
import datetime as dt
from datetime import datetime as dtdt
from collections import namedtuple
import pytest
import warnings

# # try:
# #     num = int(input("请输入数字："))
# #     print(100//num)
# # except  ZeroDivisionError as e:
# #     print("我去！小学没毕业呀！")
# #     print(e)
# #     num += 20
# #     print(100//num)
# # else:
# #     print("有效计算！")
# # finally:
# #     print("计算完成！")
# #
# # print("I am %s years old,and %s"%(input("请输入年龄："),"男"))
#
# #calendar
# print(time.daylight)
# print(time.time())
# '''
#     w日期列间隔
#     l周期行间隔
#     c月期列间隔
# '''
# #yearAll = calendar.calendar(2019,w=6,l=1,c=10)
# yearAll = calendar.calendar(2019)
# print(type(yearAll))
# # print(yearAll)
#
# #return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# leapYear = calendar.isleap(2019)
# # print(leapYear)
#
# leapYears = calendar.leapdays(2008,2019)
# print(leapYears)
#
# w,func = calendar.monthrange(2019,4)
# print("四月始于周:",w,"\r\n","总有",func,"天")
#
# m = calendar.monthcalendar(2019,5)
# print(type(m))
# print(m)
#
# prcal = calendar.prcal(2019)
# print(type(prcal),'\r\n')    #<class 'NoneType'>
#
# prmonth = calendar.prmonth(2019,4)
#
# weekday = calendar.weekday(2019,4,4)
# print('\r\n','周:',weekday)
#
#
# #time
# func = time.localtime()
# print(func)    #time.struct_time(tm_year=2019, tm_mon=4, tm_mday=4, tm_hour=18, tm_min=11, tm_sec=17, tm_wday=3, tm_yday=94, tm_isdst=0)
# print(func.tm_hour)
# print(func.tm_min)
# print(func.tm_sec)
#
# asct = time.asctime(func)#h获取时间元组，返回字符床之后的时间格式
# print(type(asct))
# print(asct)
#
# ct = time.ctime()
# print(type(ct))
# print(ct)
#
# lt = time.localtime()
# ts = time.mktime(func)
# print(type(ts))
# print(ts)
#
# for i in range(5):
#     print("Bullshit")
#     time.sleep(2)

# t0 = time.clock()  #Unix下real时间(wall time)，
# print(t0)
# t1 = time.perf_counter() #User时间(代码执行时间)
#
# t2 = time.clock()
# print(t2)
# print(t2 - t0)
#
# d1 = dt.date(1986,1,1)
# d2 = dt.time(5,36,00)
#
# print(dtdt.combine(d1,d2))
#
# strftime = d1.strftime("%Y-%m-%d")
# print(strftime + "格式化时间")


# l = [1,2,3,4,5,6,7,8,9,10]
# def A(n):
#     return n + 10
# l2 = map(A,l)
# l3 = [i for i in l2]
# print(l3)

# T = namedtuple('AA',['A','B'])
# func = T(A={'a':1},B={'B':2})
# print(func.A['a'])

# print(tmpdir.mkdir('C:\\Users\\Administrator\\Desktop\\home'))

# def multiply(a, b):
#     """
#     >>> multiply(4, 3)
#     12
#     >>> multiply('a', 3)
#     'aaa'
#     """
#     return a * b


# def warnings_to_stdout():
#     """ Redirect all warnings to stdout.
#     """
#     showwarning_orig = warnings.showwarning

#     def showwarning(msg, cat, fname, lno, file=None, line=0):
#         showwarning_orig(msg, cat, os.path.basename(fname), line, sys.stdout)
#     warnings.showwarning = showwarning
#     warnings.simplefilter('always')


# def test_lame_function_2(x,y):
#     return x+y


# if __name__ == '__main__':
#     # import doctest
#     # doctest.testmod(verbose=True)
#     with warnings.catch_warnings(record=True) as caught_warnings:
#         warnings.simplefilter("error")
#         rv = test_lame_function_2(1,2)
#         print(rv)
#     print(caught_warnings)
#     for warning in caught_warnings:
#         print(warning)
    # assert  == 1
    # print('success!')


a = [[1,2],[4,5]]

for k,v in a:
    print(k,"--",v)