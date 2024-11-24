import threading
import time


# 创建两把锁
lock_1 = threading.Lock()
lock_2 = threading.Lock()


'''
死锁
注：需要加锁的情况下才会发生“死锁”
'''

def func_1():
   print("func_1 starting.........")
   lock_1.acquire()
   print("func_1 申请了 lock_1....")
   time.sleep(2) # 等待另外的函数也在动，形成死锁
   print("func_1 等待 lock_2.......")
   lock_2.acquire() # lock_2还没被释放，形成死锁
   print("func_1 申请了 lock_2.......")

   lock_2.release()
   print("func_1 释放了 lock_2")

   lock_1.release()
   print("func_1 释放了 lock_1")

   print("func_1 done..........")


def func_2():
   print("func_2 starting.........")
   lock_2.acquire()
   print("func_2 申请了 lock_2....")
   time.sleep(4)
   print("func_2 等待 lock_1.......")
   lock_1.acquire() # lock_1还被释放，形成死锁
   print("func_2 申请了 lock_1.......")

   lock_1.release()
   print("func_2 释放了 lock_1")

   lock_2.release()
   print("func_2 释放了 lock_2")

   print("func_2 done..........")


if __name__ == "__main__":

   print("主程序启动..............")
   t1 = threading.Thread(target=func_1, args=())
   t2 = threading.Thread(target=func_2, args=())

   t1.start()
   t2.start()

   t1.join() # (主线程与子线程阻塞关系)
   t2.join()

   print("主程序结束..............")
