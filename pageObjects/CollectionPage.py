#coding=utf-8
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *


class CollectionPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.mineOptions = self.parseCF.getItemsSection('collection')


    def title(self):
        try:
            locateType,locateExpression = self.mineOptions['collectionPage.title'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def bookNameList(self):
        try:
            locateType,locateExpression = self.mineOptions['collectionPage.bookNameList'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements

    def bookCurPriceList(self):
        try:
            locateType, locateExpression = self.mineOptions['collectionPage.bookCurPriceList'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def bookOldPriceList(self):
        try:
            locateType, locateExpression = self.mineOptions['collectionPage.bookOldPriceList'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def bookCatagoryList(self):
        try:
            locateType, locateExpression = self.mineOptions['collectionPage.bookCatagoryList'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def backButton(self):
        try:
            locateType, locateExpression = self.mineOptions['collectionPage.backButton'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

if __name__=="__main__":
    from selenium import webdriver
    import time

    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)

    browser.get('https://test-jdread.jd.com/h5/m/p_compilation?collectId=648')
    collectionPage=CollectionPage(browser)
    title1=collectionPage.title()

    time.sleep(2)
    browser.quit()


