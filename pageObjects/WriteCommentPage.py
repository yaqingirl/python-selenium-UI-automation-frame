from appModules.LoginAction import LoginAction
from pageObjects.BookDetailPage import BookDetailPage
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class WriteCommentPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF=ParseConfigFile()
        self.locatorOptions=self.parseCF.getItemsSection('writebookcomment')

    def titleObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.titleObj'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element


    def commentDetailObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.commentDetailObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def commentStarObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.commentStarObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def commentStarTextObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.commentStarTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def publishButton(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.publishButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookNameObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.bookNameObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookAuthorObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.bookAuthorObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def publishButtonText(self):
        try:
            locateType,locateExpression = self.locatorOptions['writeBookCommentPage.publishButtonText'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

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
    LoginAction.login('你的用户名', '你的密码', browser, 'https://jdread.jd.com/h5/m/p_book_evaluate_write?ebookId=30507500')
    # minePage=MinePage(browser)
    # minePage.ExitButtonObj().click()
    write_comment_page=WriteCommentPage(browser)
    print(write_comment_page.titleObj().is_displayed(),
    write_comment_page.bookNameObj().is_displayed(),
    write_comment_page.bookAuthorObj().is_displayed(),
    len(write_comment_page.commentStarObj())==5,
          write_comment_page.commentStarTextObj().text == "非读不可"
          )

    write_comment_page.commentDetailObj().send_keys("这本书真的很棒！")
    time.sleep(2)
    write_comment_page.publishButton().click()


    time.sleep(2)
    browser.quit()