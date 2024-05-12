import asyncio
from aiohttp import web
import aiohttp

# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')

# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))

# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()



''' 1.编写简单的 HTTP 服务器：
        下面是一个简单的 aiohttp HTTP 服务器示例： '''
# async def handle(request):
#     return web.Response(text="Hello, World!")

# app = web.Application()
# app.router.add_get('/', handle)

# if __name__ == '__main__':
#     web.run_app(app)


''' 2.发送 HTTP 请求：
    使用 aiohttp 发送 HTTP 请求也很简单： '''
# async def fetch():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://example.com') as response:
#             return await response.text()

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     response = loop.run_until_complete(fetch())
#     print(response)



''' 3.处理异步请求：
    aiohttp 允许你在请求处理中使用异步代码。例如，你可以使用异步函数处理请求：'''
async def handle(request):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.com') as response:
            return web.Response(text=await response.text())

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    web.run_app(app)
