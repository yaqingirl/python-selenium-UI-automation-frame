from appModules.LoginAction import LoginAction
from pageObjects.BookDetailPage import BookDetailPage
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class CatagoryPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF=ParseConfigFile()
        self.loginOptions=self.parseCF.getItemsSection('bookcatagory')


    def titleObj(self):
        try:
            locateType,locateExpression = self.loginOptions['bookCatagoryPage.titleObj'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element


    def sortButton(self):
        try:
            locateType,locateExpression = self.loginOptions['bookCatagoryPage.sortButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def firstChapter(self):
        try:
            locateType,locateExpression = self.loginOptions['bookCatagoryPage.firstChapter'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def canAccessChapters(self):
        try:
            locateType,locateExpression = self.loginOptions['bookCatagoryPage.canAccessChapters'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def cannotAccessChapters(self):
        try:
            locateType,locateExpression = self.loginOptions['bookCatagoryPage.cannotAccessChapters'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements

if __name__=="__main__":
    from selenium import webdriver
    import time
    from util.SimulateLogin_galaxyS5 import simulator_login

    mobile_emulation = {'deviceName': 'Galaxy S5'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://plogin.m.jd.com/user/login.action")
    # 测试退出按钮
    LoginAction.login('你的用户名', '你的密码', browser, 'https://jdread.jd.com/h5/m/p_book_detail/30132192')
    # minePage=MinePage(browser)
    # minePage.ExitButtonObj().click()
    book_detail_page=BookDetailPage(browser)
    book_detail_page.catalogButton().click()
    time.sleep(2)
    catagoryPage = CatagoryPage(browser)
    time.sleep(2)
    print(catagoryPage.titleObj().is_displayed())
    print(catagoryPage.sortButton().is_displayed())
    # print(catagoryPage.canAccessChapters()[0].is_displayed())
    # print(catagoryPage.cannotAccessChapters()[0].is_displayed())
    print(catagoryPage.firstChapter().is_displayed())
    # time.sleep(2)
    # bookCityPage.toolButtonObj().click()

    time.sleep(2)
    browser.quit()