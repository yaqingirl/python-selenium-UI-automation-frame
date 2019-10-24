#coding=utf-8
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *


class MyBooksPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.mybooksOptions = self.parseCF.getItemsSection('mybooks')


    def mybooksTitle(self):
        try:
            locateType,locateExpression = self.mybooksOptions['mybooksPage.mybooksTitle'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


if __name__=="__main__":
    from selenium import webdriver
    import time

    mobile_emulation = {'deviceName': 'Galaxy S5'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://plogin.m.jd.com/user/login.action")
    #测试退出按钮
    LoginAction.login('你的用户名','你的密码',browser,'https://jdread.jd.com/h5/m/p_book_my_list/1')
    # minePage=MinePage(browser)
    # minePage.ExitButtonObj().click()

    minePage=MyBooksPage(browser)

    time.sleep(2)
    print(minePage.mybooksTitle().is_displayed())
    # time.sleep(2)
    # bookCityPage.toolButtonObj().click()

    time.sleep(2)
    browser.quit()


