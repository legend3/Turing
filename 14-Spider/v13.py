
from urllib import request, parse,error
from http import cookiejar
'''
使用cookiejar自动获取cookie
'''
#  创建cookiejar的实例
cookie = cookiejar.CookieJar()

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

url = "http://192.168.0.64:80"
def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''

    # 此url需要从登录form的action属性中提取
    # url = "http://www.renren.com/PLogin.do"
                                                                                        # url_login = url + "/audit-core/fullTextRetrieval/analyze.do"
    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        # "email": "13119144223",
        # "password": "123456"
        "username": "webadmin",
        "password": "webadmin123456",
        "vcode": "wannengyanzhengma"
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    try:
        # 使用opener发起请求
        rsp = opener.open(req)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

def getHomePage():
    # url = "http://www.renren.com/965187997/profile"
    # url_analyze = url + "/audit-core/fullTextRetrieval/analyze.do"

    try:
        # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
        rsp = opener.open(url)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    html = rsp.read().decode()
    with open("rsp.html", "w",encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()
