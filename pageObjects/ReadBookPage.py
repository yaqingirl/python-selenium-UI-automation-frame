#coding=utf-8
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *


class ReadBookPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.readBookOptions = self.parseCF.getItemsSection('readbook')

    #登陆状态
    # minePage.exitButton = xpath > // *[text() = "退出登录"]
    # minePage.loginEntryButton = xpath > // label[contains(text(), "点击登录")]
    def LeftSectionObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.leftSectionObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def RightSectionObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.rightSectionObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def CenterSectionObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.centerSectionObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def ChapterTitleObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.chapterTitleObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def ChapterFirstContentObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.chapterFirstContentObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def SettingButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.settingButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def DirButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.dirButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def LastChapterFreeDir(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.lastChapterFreeDir'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def YesOrNotBuyBookDialog(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.yesOrNotBuyBookDialog'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    #弹框中是否购买询问时的确认按钮
    def BuyBookConfirmButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.buyBookConfirmButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    #结算框里的提交按钮
    def BuyBookCommitButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.buyBookCommitButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def MoreToolsObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.moreToolsObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def IndexButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.indexButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def MyBookButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.myBookButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def CartButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.cartButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def MyButton(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.myButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def HeaderMenuObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.headerMenuObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def JDFooterBar(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.jDFooterBar'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def JDHeaderBar(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.jDHeaderBar'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def chapterNeedPayrDirs(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.chapterNeedPayrDirs'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def LastChapterNeedPayrDir(self):
        try:
            locateType,locateExpression = self.readBookOptions['readBookPage.lastChapterFreeDir'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
if __name__=="__main__":
    from selenium import webdriver
    import time

    #设置浏览器为iphone模式打开
    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)

    browser.get('https://test-jdread.jd.com/static/read/dist/index.html?ebookId=30416575&name=之江新语')

    time.sleep(2)

    readbookPage=ReadBookPage(browser)
    readbookPage.CenterSectionObj().click()
    time.sleep(2)
    readbookPage.SettingButton().click()


    #测试翻页
    # logger.info('点击"阅读"页面的右侧翻页6次...')
    # for i in range(6):
    #     readbookPage.RightSectionObj().click()
    #     time.sleep(1)
    #
    # logger.info(readbookPage.ChapterTitleObj().text)
    # logger.info(readbookPage.ChapterFirstContentObj().text)

    time.sleep(2)
    browser.quit()


