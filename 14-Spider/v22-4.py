import requests

url = "https://www.baidu.com"
data = {
'q': 'python', 'cat': '1001'
}
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# parse.urlencode(data).encode("utf-8")
print(r.status_code)
print(r.encoding)  # requests自动检测编码，可以使用encoding属性查看：
print(r.content)  # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())  # requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)
# upload_files = {'file': open('C:\\Users\\Administrator\\Desktop\\c.txt', 'rb')}  # 上传文件需要更复杂的编码格式，但是requests把它简化成files参数,在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
# r = requests.post(url, files=upload_files)
r.cookies['ts']  # 获取cookie
cs = {'token': '12345', 'status': 'working'}  # 要在请求中传入Cookie，只需准备一个dict传入cookies参数
r = requests.get(url, cookies=cs)
r = requests.get(url, timeout=2.5)  # 2.5秒后超时
