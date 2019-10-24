#coding=utf-8
from pageObjects.DiscountPage import DiscountPage
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *


class WeeklyDiscountPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.mineOptions = self.parseCF.getItemsSection('weeklydiscount')


    def title(self):
        try:
            locateType,locateExpression = self.mineOptions['weeklydiscountPage.title'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstBook(self):
        try:
            locateType,locateExpression = self.mineOptions['weeklydiscountPage.firstBook'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
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

    browser.get('https://jdread.jd.com/h5/m/p_free_module')
    discountPage=DiscountPage(browser)
    title1=discountPage.title()
    print(title1.text)

    time.sleep(2)
    browser.quit()


