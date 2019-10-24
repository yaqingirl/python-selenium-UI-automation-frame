from appModules.LoginAction import LoginAction
from pageObjects.BookDetailPage import BookDetailPage
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class AllCommentPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF=ParseConfigFile()
        self.locatorOptions=self.parseCF.getItemsSection('allbookcomment')

    def commentsObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.commentsObj'.lower()].split('>')
            print(locateType,locateExpression)
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return elements
    def writeCommentButton(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.writeCommentButton'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsTitle(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsTitle'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsCountObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsCountObj'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsSortByObj(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsSortByObj'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsSortTypeChangeButton(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsSortTypeChangeButton'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsSortUnSelected(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsSortUnSelected'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsSortSelected(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsSortSelected'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsUserHead(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsUserHead'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsUserName(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsUserName'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsUserLevel(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsUserLevel'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsUserrater(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsUserrater'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsContent(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsContent'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def allCommentsTime(self):
        try:
            locateType,locateExpression = self.locatorOptions['allBookCommentPage.allCommentsTime'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
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
    LoginAction.login('你的用户名', '你的密码', browser, 'https://jdread.jd.com/h5/m/p_book_evaluate_more?ebookId=30225691')
    # minePage=MinePage(browser)
    # minePage.ExitButtonObj().click()
    all_comment_page=AllCommentPage(browser)
    print(all_comment_page.commentsObj()[0].text)


    time.sleep(2)
    browser.quit()