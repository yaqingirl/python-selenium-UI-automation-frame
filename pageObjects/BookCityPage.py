#coding=utf-8
from appModules.LoginAction import LoginAction
from config.VarConfig import phone_model
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class BookCityPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF=ParseConfigFile()
        self.bookcityOptions=self.parseCF.getItemsSection('bookcity')


    def toolButtonObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.toolButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def firstPageButtonObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.firstPageButton'.lower()].split('>')

            element = getVisibilityElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def minePageButtonObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.minePageButton'.lower()].split('>')

            element = getVisibilityElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def shoppingCartPageButtonObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.shoppingCartPageButton'.lower()].split('>')
            element = getVisibilityElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def myBookPageButtonObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.myBookPageButton'.lower()].split('>')
            element = getVisibilityElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def channelFoldDownButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.channelFoldDownButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def channelVIPButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.channelVIPButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def channelNewEraButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.channelNewEraButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


    def VIPText(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.vipText'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def domainName(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.domainName'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def domainUrl(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.domainUrl'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def loginButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.loginButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def newEraBanner(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.newEraBanner'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def leaderBoardButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.leaderBoardButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def classificationButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.classificationButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def discountButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.discountButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def freebookButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.freebookButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def vipButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookCityPage.vipButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


    def firstCollectionTitle(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionTitle'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionCounterDay(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionCounterDay'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionCounterHour(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionCounterHour'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionCounterMinute(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionCounterMinute'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


    def firstCollectionFirstBookName(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionFirstBookName'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionSecondBookName(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionSecondBookName'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionThirdBookName(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionThirdBookName'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionForthBookName(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionForthBookName'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionFifthBookName(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionFifthBookName'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionSixthBookName(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionSixthBookName'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionFirstBookNewPrice(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionFirstBookNewPrice'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def firstCollectionFirstBookOldPrice(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.firstCollectionFirstBookOldPrice'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def threeBooksCollectionTitles(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.threeBooksCollectionTitles'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def allBooksCollectionLists(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.allBooksCollectionLists'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def allBooksCollectionTitles(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.allBooksCollectionTitles'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def allCollectionFirstBookNames(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.allCollectionFirstBookNames'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def allCollectionSecondBookNames(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.allCollectionSecondBookNames'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def allCollectionThirdBookNames(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.allCollectionThirdBookNames'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def indexButtonImageInMoreTools(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.indexButtonImageInMoreTools'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def myBooksButtonImageInMoreTools(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.myBooksButtonImageInMoreTools'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCartButtonImageInMoreTools(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.shoppingCartButtonImageInMoreTools'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def mineButtonImageInMoreTools(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.mineButtonImageInMoreTools'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def threeBookContainers(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.threeBookContainers'.lower()].split('>')
            elements = getElements(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def channelFeaturedButton(self):
        try:
            locateType, locateExpression = self.bookcityOptions['bookCityPage.channelFeaturedButton'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


if __name__=="__main__":
    from selenium import webdriver
    import time

    mobile_emulation = {'deviceName': phone_model}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://plogin.m.jd.com/user/login.action")
    LoginAction.login('你的用户名','你的密码',browser,'http://jdread.jd.com/h5/m')

    bookCityPage=BookCityPage(browser)
    login_btn=bookCityPage.loginButton()
    login_btn.click()
    # bookCityPage.toolButtonObj().click()
    # bookCityPage.minePageButtonObj().click()

    # time.sleep(2)
    # bookCityPage.toolButtonObj().click()

    time.sleep(2)
    browser.quit()


