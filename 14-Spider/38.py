# encoding: utf8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,os
from LOG.Logger import Logger
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class InterfaceConfigure():
    driver = webdriver.Firefox()
    count = 0
    list = ("http://192.168.0.185:5000/fbdownload/txt-7k.txt",  # 敏感接口
            "http://192.168.0.185:5000/fbdownload/doc-excel.rar",
            "http://192.168.0.185:5000/fbdownload/doc-1M.doc",
            "http://192.168.0.185:5000/fbdownload/xlsxFile.xlsx",
            "http://192.168.0.185:5000/fbdownload/docx-22K.docx",
            "http://192.168.0.185:5000/fbdownload/excel-2003.xls",
            "http://192.168.0.185:5000/fbdownload/txt-docx.zip",
            "http://192.168.0.185:5000/fbdownload/csv-4k.csv",
            "http://192.168.0.185:5000/webapi/entry.cgi"
            )

    def __init__(self,logName):
        self.logName = logName
        self.logger = Logger(self.logName, os.path.split(__file__)[1]).getlog()

    def login(self,url,username,password,verification_code):
        # 打开首页
        self.driver.get(url)
        time.sleep(2)
        self.driver.maximize_window()
        # 填写登录信息
        self.driver.find_element_by_name(u"username").send_keys(username)
        self.driver.find_element_by_name(u"password").send_keys(password)
        self.driver.find_element_by_name(u"vcode").send_keys(verification_code)
        # 点击登录
        self.driver.find_element_by_class_name(u"login-btn").click()
        self.logger.debug('登录失败！')
        self.logger.warn('登录成功！')

    def ApplicationDetails_down(self,item):
        # (适用1.9.1以下,无文件接口自动合并)

        # 适用1.9.1以上
        Restful = "http://192.168.0.185:5000/fbdownload/${id1}"

        # 点击系统配置
        self.driver.find_element_by_xpath("//a[@href='/audit-core/dist/sys-configuration/index.html']").click()
        time.sleep(2)
        # 点击应用配置
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/a[1]").click()
        time.sleep(2)
        # 选择应用
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/section/div[1]/section/div/input").send_keys("185")
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/section/div[1]/section/div/div/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='single-app-item']").click()
        time.sleep(3)

        self.count += 1
        self.driver.switch_to_window(self.driver.window_handles[self.count])
        self.logger.debug(u'选择应用失败！')
        self.logger.warn(u'选择应用成功！')
        # 搜索
        self.driver.find_element_by_xpath(u"//input[@placeholder='检索url']").send_keys(self.list[item])
        self.driver.find_element_by_xpath(u"//input[@placeholder='检索url']").send_keys(Keys.ESCAPE)
        time.sleep(1)

        # 点击查看样例(适用1.9.1以下，无文件接口自动合并)
        self.driver.find_element_by_xpath(u"//button[@data-btn='"+self.list[item]+"']").click()
        # 点击设置敏感接口
        time.sleep(3)
        self.driver.find_element_by_xpath(u"//span[.='设为敏感接口']/..").click()
        time.sleep(2)

        # 点击配置(配置合并接口)  （1.9.1以上，适合文件接口自动合并）
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div[3]/div[2]/section/div/div[1]/div[2]/table/tbody/tr[2]/td[9]/div/div[2]/button").click()
        # time.sleep(2)

        self.count += 1
        self.driver.switch_to_window(self.driver.window_handles[self.count])
        time.sleep(5)
        self.logger.debug(u'进入设置敏感接口失败！')
        self.logger.warn(u'进入设置敏感接口成功！')

    def SetSensitiveInterface(self, labelCounts):
        for i in range(0, int(labelCounts)):
            self.driver.find_element_by_xpath("//span[@tabindex='0']").click()
            time.sleep(1)

            datalabels = self.driver.find_elements_by_xpath("//li[@tabindex='-1']")  # 判断ul中是否存在li子元素
            # boxes = self.driver.find_elements_by_xpath("//div[@aria-label='checkbox-group']/label[@aria-checked='false']")
            if len(datalabels) != 0:
                self.driver.find_element_by_xpath(u"//li[@tabindex='-1']").click()
                time.sleep(1)
            else:
                break

        # 点击保存监控
        self.driver.find_element_by_xpath(u"//span[.='保存并监控']/..").click()
        time.sleep(3)
        # 点击关闭 #/html/body/div[2]/div/div/div[3]/button
        self.driver.find_element_by_xpath(u"//button[.='关闭']").click()
        time.sleep(2)
        self.logger.debug(u'配置数据标签应用失败！')
        self.logger.warn(u'配置数据标签应用成功！')

    #  关闭
    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("argv error,Configure_sensitive_file_interface.py [url] [username] [password] [verification_code] [labelCounts]")
        sys.exit(1)
    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    verification_code = sys.argv[4]
    labelCounts = sys.argv[5]
    logName = os.path.abspath("logs/").split("Turing")[0] + "Turing/LOG/logs/" + \
              os.path.split(__file__)[1].split(".")[0] + ".log"
    logger = Logger(logName, os.path.split(__file__)[1]).getlog()
    try:
        ic = InterfaceConfigure(logName)
        ic.login(url,username,password,verification_code)
        time.sleep(2)

        for item in range(0, len(ic.list)-1):  # 此for循环仅适用1.9.1以下版本
            ic.ApplicationDetails_down(item)
            time.sleep(2)
            ic.SetSensitiveInterface(labelCounts)
    except Exception as e:
        print(e)
        ic.close()

ic.close()