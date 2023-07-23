#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2019-12-22 11:35:22
lastTime: 2023-07-24 01:24:03
LastAuthor: Do not edit
FilePath: /Turing/13-协程/v11.py
Description: 
version: 
'''


import threading
import asyncio

# #@asyncio.coroutine
# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     print('Start..... (%s)' % threading.currentThread())
#     await asyncio.sleep(2)
#     print('Done..... (%s)' % threading.currentThread())
#     print('Hello again! (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# print('-----'*15)

# async def sub_coroutine():
#     print("sub coroutine started")
#     await asyncio.sleep(1)
#     return "sub coroutine finished"

# async def main_coroutine():
#     print("main coroutine started")
#     result = await sub_coroutine()
#     print("main coroutine received result:", result)

# asyncio.run(main_coroutine())








# print('-3.2.3 Task对象-')

# """
# 1.Tasks用于并发调度协程,通过`asyncio.create_task(协程对象)`的方式创建Task对象,这样可以让协程加入事件循环中等待被调度执行。
# 除了使用 `asyncio.create_task()` 函数以外,还可以用低层级的 `loop.create_task()` 或 `ensure_future()` 函数。不建议手动实例化 Task 对象。

# 2.本质上是将协程对象封装成task对象,并将协程立即加入事件循环,同时追踪协程的状态。

# 3.注意：`asyncio.create_task()` 函数在 Python 3.7 中被加入。在 Python 3.7 之前,可以改用低层级的 `asyncio.ensure_future()` 函数。
# """


# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return "返回值"


# async def main():
#     print("main开始")

#     # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
#     task1 = asyncio.create_task(func())

#     # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
#     task2 = asyncio.create_task(func())

#     print("main结束")

#     # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
#     # 此处的await是等待相对应的协程全都执行完毕并获取结果
#     ret1 = await task1
#     ret2 = await task2
#     print(ret1, ret2)

# asyncio.run(main())


# print('-' * 50)


# test03
async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")

    # 创建协程，将协程封装到Task对象中并添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    # 在调用
    task_list = [
        asyncio.create_task(func(), name="n1"),
        asyncio.create_task(func(), name="n2")
    ]

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
    # 此处的await是等待所有协程执行完毕，并将所有协程的返回值保存到done
    # 如果设置了timeout值，则意味着此处最多等待的秒，完成的协程返回值写入到done中，未完成则写到pending中。
    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done, pending)


asyncio.run(main())


print('-' * 50)


async def func():
    print("执行协程函数内部代码")

    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response = await asyncio.sleep(2)

    print("IO请求结束，结果为：", response)


coroutine_list = [func(), func()]

# 错误：coroutine_list = [ asyncio.create_task(func()), asyncio.create_task(func()) ]  
# 此处不能直接 asyncio.create_task，因为将Task立即加入到事件循环的任务列表，
# 但此时事件循环还未创建，所以会报错。


# 使用asyncio.wait将列表封装为一个协程，并调用asyncio.run实现执行两个协程
# asyncio.wait内部会对列表中的每个协程执行ensure_future，封装为Task对象。
done,pending = asyncio.run( asyncio.wait(coroutine_list) )
print(done)
