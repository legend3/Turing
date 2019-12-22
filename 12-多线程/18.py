import threading
import time

'''
递归时，最初自己申请了锁,又没归还，又会要申请锁(会死锁)
RLock可以解决这个问题
'''
class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):#acquire(timeout=1)
            num = num+1
            msg = self.name+' set num to '+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0

mutex = threading.RLock()#可重用锁，"大锁"


def testTh():
    for i in range(5):
        t = MyThread()
        t.start()



if __name__ == '__main__':
    testTh()