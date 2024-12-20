#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
# 导入多线程处理包
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 把参数打印出来
    print("我是参数 ",in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数in 和 in2打印出来，代表使用
    print("我是参数 " ,in1 , "和参数  ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


if __name__ == "__main__":
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("王老大",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("王大鹏", "王小鹏"))
    t2.start()

    print("All done at:", time.ctime())
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    # while True: # 使用了threading,主线程会等待非守护的子线程完成！因此无需此步骤！！
    #     time.sleep(10)

'''
    优点：
        代码简洁：适合小型任务，直接传递函数和参数即可。
        低复杂度：无额外类定义，适合轻量级并发任务。
    缺点：
        可扩展性差：无法方便地增加线程行为或功能。
        不适合复杂任务：对于需要在类中封装逻辑的任务，不够灵活。
'''