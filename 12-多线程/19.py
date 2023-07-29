import multiprocessing
from time import sleep, ctime


def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)



if __name__ == '__main__':
    p = multiprocessing.Process(target = clock, args = (5,)) # 创建多进程对下个——直接方式
    p.start()

    while True: # 保持主进程活跃
        print('sleeping.......')
        sleep(1)

