#coding=utf-8
from util.ObjectMap import *
from appModules.LoginAction import LoginAction
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *


class ShoppingCartPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.shoppingCartOptions = self.parseCF.getItemsSection('shoppingcart')


    def shoppingCartTitle(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartTitle'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartBookListObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartBookListObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def shoppingCartBookOptionListObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartBookOptionListObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def shoppingCartDeleteButton(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartDeleteButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartDeleteConfirmButton(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartDeleteConfirmButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartSettlementButton(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartSettlementButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartBuyConfirmButton(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartBuyConfirmButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartPayableAmountObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartPayableAmountObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartBookImageListObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartBookImageListObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def shoppingCartBookNameListObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartBookNameListObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def shoppingCartBookPriceListObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartBookPriceListObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def shoppingCartSettlementAmountObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartSettlementAmountObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartSettlementAvailAmountObj(self):
        try:
            locateType,locateExpression = self.shoppingCartOptions['shoppingCartPage.shoppingCartSettlementAvailAmountObj'.lower()].split('>')
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
    LoginAction.login('你的用户名','你的密码',browser,'https://jdread.jd.com/h5/m/p_cart_shop')
    # minePage=MinePage(browser)
    # minePage.ExitButtonObj().click()

    cartPage=ShoppingCartPage(browser)

    time.sleep(2)
    print(cartPage.shoppingCartTitle().is_displayed())
    # time.sleep(2)
    # bookCityPage.toolButtonObj().click()

    time.sleep(2)
    browser.quit()


