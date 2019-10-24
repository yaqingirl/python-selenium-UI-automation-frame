#coding=utf-8
from appModules.LoginAction import LoginAction
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class BookDetailPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF=ParseConfigFile()
        self.bookcityOptions=self.parseCF.getItemsSection('bookdetail')


    def priceObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.priceObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def discountObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.discountObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def realPriceObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.realPriceObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def originalPriceObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.originalPriceObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def vipReadForFreeTextObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.vipReadForFreeTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def vipOriginalPriceObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.vipOriginalPriceObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def vipReadButtonTextObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.vipReadButtonTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def vipReadButtonObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.vipReadButtonObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def readButtonTextObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.readButtonTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def noVipReadTextObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.noVipReadTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def vipFlagObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.vipFlagObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def bookCoverObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookCoverObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def bookNameObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookNameObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def activeCommentStarObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.activeCommentStarObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def commentCountObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentCountObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def authorObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.authorObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def publishObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.publishObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def acivityObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.acivityObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shoppingCarButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.shoppingCarButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def foldRecommandObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.foldRecommandObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def catalogButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.catalogButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def writeBookCommentButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.writeBookCommentButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def allRecommandBooksObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.allRecommandBooksObj'.lower()].split('>')
            elements = getElements(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return elements
    def allCommentsTextObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.allCommentsTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def noCommentTextObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.noCommentTextObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentUserHeadImg(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentUserHeadImg'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentUserNameObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentUserNameObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentUserLevelObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentUserLevelObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentRaterObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentRaterObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentContentObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentContentObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentTimeObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentTimeObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def commentTitleObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.commentTitleObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookMessageTitle(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookMessageTitle'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookFileSizeLabel(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookFileSizeLabel'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookFileSizeObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookFileSizeObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookISBNCodeLabel(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookISBNCodeLabel'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookISBNCodeObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookISBNCodeObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookCharsNumLabel(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookCharsNumLabel'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookCharsNumObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookCharsNumObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookPublicTimeLabel(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookPublicTimeLabel'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookPublicTimeObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookPublicTimeObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookFileTypeLabel(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookFileTypeLabel'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookFileTypeObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookFileTypeObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookPublicTimesLabel(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookPublicTimesLabel'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookPublicTimesObj(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookPublicTimesObj'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def bookExplainText(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.bookExplainText'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def shopCartButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.shopCartButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element
    def readButton(self):
        try:
            locateType,locateExpression = self.bookcityOptions['bookDetailPage.readButton'.lower()].split('>')
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
    # browser.get("https://jdread.jd.com/h5/m/p_book_detail/30108231")
    #
    # bookDetailPage=BookDetailPage(browser)
    #
    # print(bookDetailPage.priceObj().text)

    # browser.get("https://jdread.jd.com/h5/m/p_book_detail/30489245")
    #
    # bookDetailPage = BookDetailPage(browser)
    #
    # print(bookDetailPage.discountObj().text)
    # print(bookDetailPage.realPriceObj().text)
    # print(bookDetailPage.originalPriceObj().text)
    browser.get("https://jdread.jd.com/h5/m/p_book_detail/30502437")

    bookDetailPage = BookDetailPage(browser)

    print(bookDetailPage.priceObj().text)



    # time.sleep(2)
    # bookCityPage.toolButtonObj().click()

    time.sleep(2)
    browser.quit()


