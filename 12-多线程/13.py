#encoding=utf-8
import threading
import time

# Python2
# from Queue import Queue

# Python3
import queue

'''
(只是介绍queue，其实list也行；此模型不涉及线程安全!)
Queue 使用与多线程编程的先进先出FIFO数据结构，可以用来在生产者和消费者线程之间安全的传递消息和其他数据。
安全是因为它会为调用者处理时锁定。Queue的大小（包含的元素的个数）会受限，以限制内存使用或处理。

注:无需加锁!且不会死锁
'''
class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count +1
                    msg = '生成产品'+str(count)
                    # put是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg = self.name + '消费了 '+queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(1):#循环多次向queue中添加内容
        queue.put('初始产品'+str(i))
    for i in range(2):#循环多次创建Producer线程
        p = Producer()
        p.start()
    for i in range(5):#循环多次创建Consumer线程
        c = Consumer()
        c.start()