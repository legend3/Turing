# coding:utf-8
from selenium import webdriver#加载webdriver方法
import time#导入time包
driver = webdriver.Firefox()#创建谷歌对象，调用火狐浏览器
driver.get('https://www.baidu.com')#在火狐中输入需访问的url路径
time.sleep(1)#设置停留等待时间3s
driver.maximize_window()#全屏模式
driver.refresh()#刷新页面
time.sleep(1)#
driver.set_window_size(960,540)#s设置页面尺寸
time.sleep(1)
driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\test.png")#(浏览器)截屏，保存为test.png
# driver.get('http://192.168.0.86/audit-core/dist/intelligent-tracing/index.html')
driver.get('https://www.baidu.com')
time.sleep(1)
# driver.close()#关闭当前窗口，可用于某个具体窗口关闭
driver.quit()#关闭所有与当前操作有关的窗口，并退驱动。需释放资源时可使用此方法