#coding=utf-8
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *
from selenium.webdriver.common.keys import Keys


class SearchBookPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.readBookOptions = self.parseCF.getItemsSection('searchbook')


    def SearchInputBoxObj(self):
        try:
            locateType,locateExpression = self.readBookOptions['searchBookPage.searchInputBox'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


    def SearchResultFirstBookName(self):
        try:
            locateType,locateExpression = self.readBookOptions['searchBookPage.searchResultFirstBookName'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def SearchResultFirstBookAuthor(self):
        try:
            locateType,locateExpression = self.readBookOptions['searchBookPage.searchResultFirstBookAuthor'.lower()].split('>')
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

    # browser.get('https://test-jdread.jd.com/h5/m/p_book_type_search')
    # searchbookPage=SearchBookPage(browser)
    # searchbookPage.SearchInputBoxObj().send_keys("之江新语")
    # searchbookPage.SearchInputBoxObj().send_keys(Keys.ENTER)  # 通过回车键来代替鼠标的左键
    # print(searchbookPage.SearchResultFirstBookName().text)
    browser.get('https://test-jdread.jd.com/h5/m/p_book_type_search')
    searchbookPage=SearchBookPage(browser)
    searchbookPage.SearchInputBoxObj().send_keys("习近平")
    searchbookPage.SearchInputBoxObj().send_keys(Keys.ENTER)  # 通过回车键来代替鼠标的左键
    print(searchbookPage.SearchResultFirstBookAuthor().text)
    time.sleep(2)

    browser.quit()


