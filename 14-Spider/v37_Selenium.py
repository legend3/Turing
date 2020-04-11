# encoding:utf8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
"""
python 3.7
selenium   3.141.0
geckodriver-v0.26.0.exe
chromedriver-80.0.3987.16.exe
"""

# 可能需要手动添加路径
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# print(type(driver))
url = "https://www.baidu.com"
driver.get(url)

# 返回与ID属性值匹配的第一元素
text = driver.find_element_by_id('kw').text
print(text)
print(driver.title)
# # 得到页面的快照
# driver.save_screenshot('index.png')  # 保存到当前目录，命名为index
# driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\1.png')  # 保存到桌面，命令为1


# id="kw" 的是百度的输入框，我们得到输入框的ui元素后直接输入“大熊猫"
# driver.find_element_by_id('kw').send_keys(u"大熊猫")
# id="su"是百度搜索的按钮，click模拟点击
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\daxiongmao.png")


# #获取当前页面的cookie
# print(driver.get_cookies())  # cookie的所有值信息
# print(driver.get_cookie('name'))  # cookie某个值

# 模拟输入两个按键 ctrl+ a
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# time.sleep(2)
# ctr+x 是剪切快捷键
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
# time.sleep(2)
# driver.find_element_by_id('kw').send_keys(u'航空母舰')
# driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\hangmu.png")
# 回车键
# driver.find_element_by_id('su').send_keys(Keys.RETURN)

# time.sleep(5)
# driver.save_screenshot('hangmu2.png')
#
#
# # 清空输入框 , clear
# driver.find_element_by_id('kw').clear()
# driver.save_screenshot('clear.png')

'''
Selenium教程
'''
# web元素定位
# driver = webdriver.Firefox()
# driver.get("http://192.168.0.27")
# time.sleep(2)
# # 通常用的多的id、name、class
# driver.find_element_by_name(u"username").send_keys(u"webadmin")
# driver.find_element_by_name(u"password").send_keys(u"webadmin123456")
# driver.find_element_by_name(u"vcode").send_keys(u"wannengyanzhengma")
# # driver.find_elements_by_class_name("input-icon")[1]#多个同名的类名在整个list中位置的定位
# time.sleep(2)
#
# # 登录
# # driver.find_element_by_link_text("登录").click()#定位不到'登录'
# driver.find_element_by_class_name("login-btn").click()
# time.sleep(2)

'''
Xpath定位，有时候无法查到测试对象较为完善的属性及属性值（时）！Xpath通过元素在被测页面中的位置属性进行查找.
Xpath是某个元素在XML文件中所处的位置，通过Xpath定位元素，精准度较高，但由于Xpath需遍历页面，因此查找性能较弱
'''
# 绝对路径
# driver.find_element_by_xpath("/html/body/div[1]/div/aside/a[3]/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/a[1]/div[2]/div[1]/span/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[2]/div[1]/div[1]/input").send_keys("15067111600")
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[2]/div[2]/div[2]/button").click()
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[8]/div/div[1]/button/i").click()
# time.sleep(3)
#
# # 相对路径(未找到DevTools的“最简xpath”)
# driver.fin
# # checkbox操作
# driver.find_element_by_xpath("/html/body/div[1]/div/div/aside/a[6]/span").click()  # 进入"系统配置"
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/a[2]/div[1]/div[1]").click() # 进入“接口配置”
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[8]/div/div[3]/button/i").click()# 点击某接口“配置敏感接口”选项
# time.sleep(2)
# labelList = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/label[1]/span[1]/span").click()
# time.sleep(2)
# print("labelsCounts is {0}".format(len(labelList)))
# for label in labelList:
#     label.click()
#     time.sleep(2)
# time.sleep(4)

# try:
#     for item in range(2, 10):
#         # 点击系统配置
#         driver.find_element_by_xpath("//a[@href='/audit-core/dist/sys-configuration/index.html']").click()
#         time.sleep(2)
#         # 点击应用配置
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/a[1]").click()
#         time.sleep(2)
#         # 选择应用
#         driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/section/div[1]/section/div/input").send_keys("185")
#         time.sleep(1)
#         driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/section/div[1]/section/div/div/button").click()
#         time.sleep(2)
#         driver.find_element_by_xpath("//div[@class='single-app-item']").click()
#         time.sleep(3)
#
#         count = count+1
#         driver.switch_to_window(driver.window_handles[count])
#         time.sleep(2)
#
#         # 点击查看样例
#         driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr["+str(item)+"]/td[7]/div/div/button").click()
#         # driver.find_element_by_xpath("//button[ends-with(@data-btn,'doc-excel.rar')]").click()
#         # driver.find_element_by_css_selector(".urlGrid > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(7) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)").click()
#         # driver.find_element_by_xpath("//tr[@data-order='1']/td[@data-td-order='6']/div[@class='table-td']/div[@class='btn-group']/button[@data-btn='http://192.168.0.185:5000/fbdownload/doc-excel.rar']").click()
#         # 点击设置敏感接口
#         time.sleep(3)
#         driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button[2]").click()
#         time.sleep(2)
#
#         count = count + 1
#         print(count)
#         driver.switch_to_window(driver.window_handles[count])
#
#         # 配置敏感标签
#         for i in range(0,14):
#             driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[4]/div[2]/div[1]/div[2]/div/span").click()
#             time.sleep(1)
#
#             datalabels = driver.find_elements_by_xpath("/html/body/ul/li[1]")  # 判断ul中是否存在li子元素
#             if len(datalabels) != 0:
#                 driver.find_element_by_xpath("/html/body/ul/li[1]").click()
#                 time.sleep(1)
#             else:
#                 break
#         # 点击保存监控
#         driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[7]/button[2]").click()
#         time.sleep(2)
#         # 点击关闭
#         driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button").click()
#         # 点击接口配置(再次回到敏感接口配置页面)
#         # driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/span[2]/span[1]/a").click()
#         time.sleep(2)
# except Exception as e:
#     print(e)
#     driver.quit()


# 关闭浏览器
driver.quit()
