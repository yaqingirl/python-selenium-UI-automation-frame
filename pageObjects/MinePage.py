#coding=utf-8
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *


class MinePage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.mineOptions = self.parseCF.getItemsSection('mine')

    #登陆状态
    # minePage.exitButton = xpath > // *[text() = "退出登录"]
    # minePage.loginEntryButton = xpath > // label[contains(text(), "点击登录")]
    def ExitButtonObj(self):
        try:
            locateType,locateExpression = self.mineOptions['minePage.exitButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    #未登陆状态
    def LoginEntryButton(self):
        try:
            locateType,locateExpression = self.mineOptions['minePage.loginEntryButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def title(self):
        try:
            locateType,locateExpression = self.mineOptions['minePage.title'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
if __name__=="__main__":
    from selenium import webdriver
    import time

    browser = webdriver.Chrome()
    #测试退出按钮
    # LoginAction.login('你的用户名','liujinhong1995',browser,'http://test1-jdread.jd.com/h5/m/p_my_details')
    # minePage=MinePage(browser)
    # minePage.ExitButtonObj().click()

    #测试登陆入口按钮
    browser.get('http://test-jdread.jd.com/h5/m/p_my_details')
    minePage=MinePage(browser)
    minePage.LoginEntryButton().click()
    # time.sleep(2)
    # bookCityPage.toolButtonObj().click()

    time.sleep(2)
    browser.quit()


