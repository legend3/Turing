import asyncio

# test01
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    print("Start......")
    r = yield from asyncio.sleep(3)
    print("Done....")
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello()) # 等价asyncio.run(hello())
loop.close()

print('-' * 50)

# test02
async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '返回值'


async def func():
    print("执行协程函数内部代码")
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response1 = await others()
    print("IO请求结束，结果为：", response1)
    
    response2 = await others()
    print("IO请求结束，结果为：", response2)
    
asyncio.run( func() )