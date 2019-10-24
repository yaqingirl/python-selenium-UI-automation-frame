#coding=utf-8
import re
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from util.decorator.PhoneModelDecorator import set_phone_model,options
from appModules.LoginAction import LoginAction
from config.VarConfig import *
from pageObjects.BookCityPage import BookCityPage
from pageObjects.ClassificationPage import ClassificationPage
from pageObjects.CollectionPage import CollectionPage
from pageObjects.DiscountPage import DiscountPage
from pageObjects.FreebookPage import FreebookPage
from pageObjects.LeaderboardPage import LeaderboardPage
from pageObjects.MinePage import MinePage
from pageObjects.MyBooksPage import  MyBooksPage
from pageObjects.ShoppingCart import ShoppingCartPage
from pageObjects.WeeklyDiscountPage import WeeklyDiscountPage
from util.Log import *
from util.ParseConfigurationFile import ParseConfigFile
from config.accounts import *
from util.ObjectMap import *
from util.ParseExcel import ParseExcel
from util.getApiData import GetCollectionBooks


class TestBookCity(unittest.TestCase):
    excelObj = ParseExcel(dataFilePath)

    @classmethod
    @set_phone_model(phone_model)
    def setUpClass(cls) -> None:
        TestBookCity.browser = webdriver.Chrome(chrome_options=options)
        logger.info("开始登陆...")
        TestBookCity.browser.get("https://plogin.m.jd.com/user/login.action")
        TestBookCity.login_cookie = LoginAction.login(not_vip_username, not_vip_password, TestBookCity.browser)

    @classmethod
    def tearDownClass(cls) -> None:
        TestBookCity.browser.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass
    def test_More_Tools_Button(self):
        logger.info("开始执行唤起更多工具按钮脚本...")
        pc = ParseConfigFile()

        try:

            TestBookCity.browser.get(pc.getUrl('bookcity'))

            logger.info('启动浏览器，访问"书城"页面...')
            bookcityPage = BookCityPage(TestBookCity.browser)

            logger.info('点击右上角更多按钮...')
            bookcityPage.toolButtonObj().click()

            try:

                self.assertIs(bookcityPage.firstPageButtonObj().is_displayed(), True)
                logger.info('调起菜单成功！用例通过')

            except AssertionError as e:
                logger.debug('更多按钮操作失败！用例不通过')
                raise e


        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e

    def test_Switch_Channel_Button(self):
        logger.info("开始执行频道切换按钮脚本...")
        pc = ParseConfigFile()

        try:

            TestBookCity.browser.get(pc.getUrl('bookcity'))

            logger.info('启动浏览器，访问"书城"页面...')
            bookcityPage = BookCityPage(TestBookCity.browser)

            logger.info('点击频道折叠按钮...')
            bookcityPage.channelFoldDownButton().click()
            bookcityPage.channelVIPButton().click()
            TestBookCity.browser.refresh()
            titleText=bookcityPage.VIPText().text

            try:

                self.assertIs( '开通京东读书VIP，海量书籍免费借阅' in titleText, True)
                logger.info('切换频道成功！用例通过')

            except AssertionError as e:
                logger.debug('切换频道失败！用例不通过')
                raise e


        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e

    def test_Check_Domain(self):
            logger.info("开始执行频道切换按钮脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)

                domainname=bookcityPage.domainName().text
                domainurl=bookcityPage.domainUrl().text

                try:

                    self.assertIs( ('e.m.jd.com' in domainurl) and ('京东读书' in domainname) , True)
                    logger.info('检查域名成功！用例通过')

                except AssertionError as e:
                    logger.debug('检查域名失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_More_Tools_Index_Button(self):
        logger.info("开始执行更多按钮首页按钮脚本...")
        pc = ParseConfigFile()

        try:

            TestBookCity.browser.get(pc.getUrl('bookcity'))

            bookcityPage = BookCityPage(TestBookCity.browser)
            bookcityPage.toolButtonObj().click()
            index_image=bookcityPage.indexButtonImageInMoreTools()
            index_button=bookcityPage.firstPageButtonObj()
            if index_image.is_displayed() and index_button.is_displayed():
                index_button.click()

            # my_books_image=bookcityPage.myBooksButtonImageInMoreTools()
            # shop_cart_image=bookcityPage.shoppingCartButtonImageInMoreTools()
            # mine_image=bookcityPage.mineButtonImageInMoreTools()

            try:

                self.assertIs(bookcityPage.domainName().is_displayed(), True)

                logger.info('书城首页按钮点击成功！用例通过')

            except AssertionError as e:
                logger.debug('书城首页按钮点击失败！用例不通过')
                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")
            raise e


        except NoSuchElementException as e:

            logger.error("数据问题..重试")
            raise e


        except Exception as e:

            logger.error(e)

            raise e

    def test_More_Tools_My_Books_Button(self):
        logger.info("开始执行更多按钮-【我的书籍】按钮脚本...")
        pc = ParseConfigFile()

        try:

            TestBookCity.browser.get(pc.getUrl('bookcity'))

            bookcityPage = BookCityPage(TestBookCity.browser)
            bookcityPage.toolButtonObj().click()
            my_books_image=bookcityPage.myBooksButtonImageInMoreTools()
            my_books_button = bookcityPage.myBookPageButtonObj()
            if my_books_image.is_displayed() and my_books_button.is_displayed():
                my_books_button.click()
            mybooksPage=MyBooksPage(TestBookCity.browser)
            # mybooks_title=mybooksPage.mybooksTitle()
            time.sleep(5)
            print(TestBookCity.browser.page_source)

            try:

                self.assertIs(mybooksPage.mybooksTitle().is_displayed(), True)

                logger.info('书城更多按钮-【我的书籍】点击成功！用例通过')

            except AssertionError as e:
                logger.debug('书城更多按钮-【我的书籍】点击失败！用例不通过')
                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")
            raise e


        except NoSuchElementException as e:

            logger.error("数据问题..重试")
            raise e


        except Exception as e:

            logger.error(e)

            raise e

    def test_More_Tools_Shopping_Cart_Button(self):
        logger.info("开始执行更多按钮-【购物车】按钮脚本...")
        pc = ParseConfigFile()

        try:

            TestBookCity.browser.get(pc.getUrl('bookcity'))

            bookcityPage = BookCityPage(TestBookCity.browser)
            bookcityPage.toolButtonObj().click()

            shopping_cart_image = bookcityPage.shoppingCartButtonImageInMoreTools()
            shopping_cart_button = bookcityPage.shoppingCartPageButtonObj()
            if shopping_cart_image.is_displayed() and shopping_cart_button.is_displayed():
                shopping_cart_button.click()
            # shop_cart_image=bookcityPage.shoppingCartButtonImageInMoreTools()
            # mine_image=bookcityPage.mineButtonImageInMoreTools()
            shoppingCartPage = ShoppingCartPage(TestBookCity.browser)
            time.sleep(5)


            try:

                self.assertIs(shoppingCartPage.shoppingCartTitle().is_displayed(), True)

                logger.info('书城更多按钮-【购物车】点击成功！用例通过')

            except AssertionError as e:
                logger.debug('书城更多按钮-【购物车】点击失败！用例不通过')
                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")
            raise e


        except NoSuchElementException as e:

            logger.error("数据问题..重试")
            raise e


        except Exception as e:

            logger.error(e)

            raise e

    def test_More_Tools_Mine_Button(self):
        logger.info("开始执行更多按钮-【我的】按钮脚本...")
        pc = ParseConfigFile()

        try:

            TestBookCity.browser.get(pc.getUrl('bookcity'))

            bookcityPage = BookCityPage(TestBookCity.browser)
            bookcityPage.toolButtonObj().click()

            mine_image = bookcityPage.mineButtonImageInMoreTools()
            mine_button = bookcityPage.minePageButtonObj()
            if mine_image.is_displayed() and mine_button.is_displayed():
                mine_button.click()
            minePage = MinePage(TestBookCity.browser)
            time.sleep(5)

            try:

                self.assertIs(minePage.title().is_displayed(), True)

                logger.info('书城更多按钮-【我的】点击成功！用例通过')

            except AssertionError as e:
                logger.debug('书城更多按钮-【我的】点击失败！用例不通过')
                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")
            raise e


        except NoSuchElementException as e:

            logger.error("数据问题..重试")
            raise e


        except Exception as e:

            logger.error(e)

            raise e

    def test_Banner_Click(self):
            logger.info("开始执行书城banner点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)

                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.channelNewEraButton().click()
                time.sleep(2)
                bookcityPage.newEraBanner().click()
                time.sleep(5)
                collectionPage=CollectionPage(TestBookCity.browser)
                titleElement=collectionPage.title()

                try:

                    self.assertIs(titleElement.is_displayed(), True)
                    logger.info('书城banner点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城banner点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_Leaderboard_Button_Click(self):
            logger.info("开始执行五个圈-排行按钮点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.channelFeaturedButton().click()
                time.sleep(2)
                bookcityPage.leaderBoardButton().click()

                time.sleep(2)
                leaderboardPage=LeaderboardPage(TestBookCity.browser)
                titleElement=leaderboardPage.title()
                title_text=titleElement.text

                try:

                    self.assertIs('排行榜'==title_text, True)
                    logger.info('书城五个圈-排行按钮点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城五个圈-排行按钮点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_Classification_Button_Click(self):
            logger.info("开始执行五个圈-分类按钮点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.channelFeaturedButton().click()
                time.sleep(2)
                bookcityPage.classificationButton().click()

                time.sleep(2)
                classificationPage=ClassificationPage(TestBookCity.browser)
                titleElement=classificationPage.title()
                title_text=titleElement.text

                try:

                    self.assertIs('分类'==title_text, True)
                    logger.info('书城五个圈-分类按钮点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城五个圈-分类按钮点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_Discount_Button_Click(self):
            logger.info("开始执行五个圈-特价按钮点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)

                bookcityPage.channelFeaturedButton().click()
                time.sleep(2)
                bookcityPage.discountButton().click()

                time.sleep(2)
                discountPage=DiscountPage(TestBookCity.browser)
                titleElement=discountPage.title()
                title_text=titleElement.text

                try:

                    # self.assertIs('特价专区'==title_text , True)
                    result1='特价专区'==title_text
                    result2 = re.search(r'\d+件[\s\S]+元', title_text)
                    result3 = "双周特价"==title_text
                    if result1:
                        self.assertIs('特价专区' == title_text, True)
                    elif None!=result2:
                        self.assertIs(None!=result2,True)

                    logger.info('书城五个圈-特价按钮点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城五个圈-特价按钮点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_Freebook_Button_Click(self):
            logger.info("开始执行五个圈-免费按钮点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.channelFeaturedButton().click()
                time.sleep(2)
                bookcityPage.freebookButton().click()

                time.sleep(2)
                freePage=FreebookPage(TestBookCity.browser)
                time.sleep(2)
                titleElement=freePage.title()
                title_text=titleElement.text

                try:

                    self.assertIs('免费专区'==title_text, True)
                    logger.info('书城五个圈-免费按钮点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城五个圈-免费按钮点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_VIP_Button_Click(self):
            logger.info("开始执行五个圈-VIP按钮点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.vipButton().click()
                time.sleep(2)
                titleElement=bookcityPage.VIPText()

                try:

                    self.assertIs(titleElement.is_displayed(), True)
                    logger.info('书城五个圈-VIP按钮点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城五个圈-VIP按钮点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    @set_phone_model(phone_model)
    def test_Discount_Collection_Title(self):
            logger.info("开始执行本周特价title点击脚本...")
            pc = ParseConfigFile()

            try:

                browser = webdriver.Chrome(chrome_options=options)

                browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(browser)

                collectionName=bookcityPage.firstCollectionTitle().text
                counterHour=bookcityPage.firstCollectionCounterHour().text
                counterMinute=bookcityPage.firstCollectionCounterMinute().text

                checkHour= str(24-int(time.localtime().tm_hour)-1).zfill(2)
                checkMinute=str(60-int(time.localtime().tm_min)-1).zfill(2)

                bookcityPage.firstCollectionTitle().click()
                time.sleep(5)

                weeklyDiscountTitleText=WeeklyDiscountPage(browser).title().text

                try:

                    self.assertIs(checkHour==counterHour, True)
                    self.assertIs(checkMinute==counterMinute, True)
                    # self.assertIs("本周特价"==collectionName,True)
                    # self.assertIs("本周特价"==weeklyDiscountTitleText,True)


                    logger.info('书城本周特价title点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城本周特价title点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")
                raise e


            except NoSuchElementException as e:

                logger.error("数据问题..重试")
                raise e


            except Exception as e:

                logger.error(e)

                raise e

    @set_phone_model(phone_model)
    def test_Discount_Collection_List(self):
            logger.info("开始执行本周特价列表检查脚本...")
            pc = ParseConfigFile()

            try:

                browser = webdriver.Chrome(chrome_options=options)

                browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(browser)


                page_book_set=set([bookcityPage.firstCollectionFirstBookName().text.replace(" ",""),
                                   bookcityPage.firstCollectionSecondBookName().text.replace(" ",""),
                                   bookcityPage.firstCollectionThirdBookName().text.replace(" ","")])
                collectionName=bookcityPage.firstCollectionTitle().text
                api_book_set=set(GetCollectionBooks.getBookNameDataList(collectionName))
                # print(page_book_set)
                # print(api_book_set)
                booklist_check=page_book_set.issubset(api_book_set)

                # api_firstbook_jd_price= str(int(float(GetCollectionBooks.getDataList(collectionName)[0]['jd_price']) * 100)) + "阅豆"
                # api_firstbook_price= str(int(float(GetCollectionBooks.getDataList(collectionName)[0]['price']) * 100)) + "阅豆"
                api_firstbook_jd_price = str(round(GetCollectionBooks.getDataList(collectionName)[0]['jd_price'],2))
                api_firstbook_price = str(round(GetCollectionBooks.getDataList(collectionName)[0]['price'],2))
                page_firstbook_jd_price=str(round(float(bookcityPage.firstCollectionFirstBookNewPrice().text.strip('￥')),2))
                page_firstbook_price=str(round(float(bookcityPage.firstCollectionFirstBookOldPrice().text.strip('￥')),2))


                try:

                    self.assertIs(booklist_check, True)
                    self.assertIs((api_firstbook_jd_price==page_firstbook_jd_price)and(api_firstbook_price ==page_firstbook_price),True)

                    logger.info('书城本周特价列表检查成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城本周特价列表检查失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_First_Collection_Book_Click_Redirect(self):
            logger.info("开始执行本周特价书籍点击脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.channelFeaturedButton().click()
                time.sleep(2)
                page_first_book_name=bookcityPage.firstCollectionFirstBookName().text
                bookcityPage.firstCollectionFirstBookName().click()
                time.sleep(3)
                book_detail_page_title=TestBookCity.browser.title

                try:

                    self.assertIs(page_first_book_name==book_detail_page_title, True)

                    logger.info('书城本周特价书籍点击成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城本周特价书籍点击失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    def test_First_Collection_Detail_List(self):
            logger.info("开始执行本周特价合集页列表检查脚本...")
            pc = ParseConfigFile()

            try:

                TestBookCity.browser.get(pc.getUrl('bookcity'))

                logger.info('启动浏览器，访问"书城"页面...')
                bookcityPage = BookCityPage(TestBookCity.browser)
                bookcityPage.channelFoldDownButton().click()
                time.sleep(2)
                bookcityPage.channelFeaturedButton().click()
                time.sleep(2)
                collectionName=bookcityPage.firstCollectionTitle().text

                bookcityPage.firstCollectionTitle().click()

                collectionPage=CollectionPage(TestBookCity.browser)
                book_element_list=collectionPage.bookNameList()
                book_name_set=set([e.text.replace(" ","") for e in book_element_list if e.text!=''])
                api_book_name_set = set(GetCollectionBooks.getBookNameDataList(collectionName))
                book_name_set_check = book_name_set.issubset(api_book_name_set)

                api_thirdbook_name=GetCollectionBooks.getDataList(collectionName)[2]['name']
                api_thirdbook_old_price= str(GetCollectionBooks.getDataList(collectionName)[2]['price'])
                api_thirdbook_cur_price= str(GetCollectionBooks.getDataList(collectionName)[2]['jd_price'])
                api_thirdbook_catagory=GetCollectionBooks.getDataList(collectionName)[2]['category_third'][0]

                page_thirdbook_name =collectionPage.bookNameList()[2].text
                # page_thirdbook_old_price =collectionPage.bookOldPriceList()[2].text.strip('￥')
                # page_thirdbook_cur_price =collectionPage.bookCurPriceList()[2].text.strip('￥')


                try:

                    self.assertIs(book_name_set_check,True)
                    self.assertIs(api_thirdbook_name==page_thirdbook_name,True)
                    # self.assertIs(api_thirdbook_catagory==page_thirdbook_catagory,True)
                    # self.assertIs(api_thirdbook_cur_price==page_thirdbook_cur_price,True)
                    # self.assertIs(api_thirdbook_old_price==page_thirdbook_old_price,True)

                    logger.info('书城本周特价合集页列表检查脚本成功！用例通过')

                except AssertionError as e:
                    logger.debug('书城本周特价合集页列表检查脚本失败！用例不通过')
                    raise e


            except ElementNotVisibleException as e:

                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:

                logger.error("数据问题..重试")

            except Exception as e:

                logger.error(e)

                raise e

    # def test_Three_books_Collections_List(self):
    #         logger.info("开始执行其余所有合集页列表检查脚本...")
    #         pc = ParseConfigFile()
    #
    #         try:
    #
    #             TestBookCity.browser.get(pc.getUrl('bookcity'))
    #
    #             logger.info('启动浏览器，访问"书城"页面...')
    #             bookcityPage = BookCityPage(TestBookCity.browser)
    #             bookcityPage.channelFoldDownButton().click()
    #             time.sleep(2)
    #             bookcityPage.channelFeaturedButton().click()
    #             time.sleep(2)
    #             title_elements = bookcityPage.allBooksCollectionTitles()
    #             # list_elements = bookcityPage.allBooksCollectionLists()
    #             first_book_names=bookcityPage.allCollectionFirstBookNames()
    #             second_book_names=bookcityPage.allCollectionSecondBookNames()
    #             third_book_names=bookcityPage.allCollectionThirdBookNames()
    #
    #             for i in range(1,len(title_elements)):
    #                 # bookcityPage = BookCityPage(browser)
    #                 # title_elements = bookcityPage.threeBooksCollectionTitles()
    #                 title=title_elements[i]
    #                 # time.sleep(2)
    #                 TestBookCity.browser.execute_script("arguments[0].scrollIntoView();" ,title)
    #                 collectionName=title.text
    #
    #                 page_book_set = set([first_book_names[i].text.replace(" ",""),
    #                                      second_book_names[i].text.replace(" ",""),
    #                                      third_book_names[i].text.replace(" ","")])
    #                 api_book_set = set(GetCollectionBooks.getBookNameDataList(collectionName))
    #                 booklist_check = page_book_set.issubset(api_book_set)
    #
    #                 try:
    #
    #                     self.assertIs(booklist_check,True)
    #                     logger.info('书城%s合集页列表检查脚本成功！用例通过'%collectionName)
    #
    #                 except AssertionError as e:
    #                     logger.debug('书城%s合集页列表检查脚本失败！用例不通过'%collectionName)
    #                     raise e
    #
    #         except ElementNotVisibleException as e:
    #
    #             logger.error("数据问题，元素没有找到..")
    #
    #         except NoSuchElementException as e:
    #
    #             logger.error("数据问题..重试")
    #
    #         except Exception as e:
    #
    #             logger.error(e)
    #
    #             raise e
    #
    # #书城大多数的合集都属于此类
    # def test_Three_books_Collections_Detail_List(self):
    #         logger.info("开始执行其余所有合集页列表检查脚本...")
    #         pc = ParseConfigFile()
    #
    #         try:
    #
    #             TestBookCity.browser.get(pc.getUrl('bookcity'))
    #
    #             logger.info('启动浏览器，访问"书城"页面...')
    #             bookcityPage = BookCityPage(TestBookCity.browser)
    #             bookcityPage.channelFoldDownButton().click()
    #             time.sleep(2)
    #             bookcityPage.channelFeaturedButton().click()
    #             time.sleep(2)
    #             title_elements = bookcityPage.threeBooksCollectionTitles()
    #
    #             for i in range(1,len(title_elements)):
    #                 bookcityPage = BookCityPage(TestBookCity.browser)
    #                 title_elements = bookcityPage.threeBooksCollectionTitles()
    #                 title=title_elements[i]
    #                 time.sleep(2)
    #                 TestBookCity.browser.execute_script("arguments[0].scrollIntoView();" ,title)
    #                 collectionName=title.text
    #                 title.click()
    #                 collectionPage=CollectionPage(TestBookCity.browser)
    #                 book_element_list=collectionPage.bookNameList()
    #                 book_name_set=set([e.text.replace(" ","") for e in book_element_list if e.text!=''])
    #
    #                 api_book_name_set = set(GetCollectionBooks.getBookNameDataList(collectionName))
    #                 book_name_set_check = book_name_set.issubset(api_book_name_set)
    #                 api_thirdbook_name=GetCollectionBooks.getDataList(collectionName)[2]['name']
    #                 page_thirdbook_name =collectionPage.bookNameList()[2].text
    #
    #                 if api_book_name_set==None:
    #                     continue
    #
    #
    #                 try:
    #
    #                     self.assertIs(book_name_set_check,True)
    #                     self.assertIs(api_thirdbook_name==page_thirdbook_name,True)
    #                     logger.info('书城%s合集页列表检查脚本成功！用例通过'%collectionName)
    #
    #                 except AssertionError as e:
    #                     logger.debug('书城%s合集页列表检查脚本失败！用例不通过'%collectionName)
    #                     raise e
    #                 finally:
    #                     collectionPage.backButton().click()
    #
    #
    #         except ElementNotVisibleException as e:
    #
    #             logger.error("数据问题，元素没有找到..")
    #
    #         except NoSuchElementException as e:
    #
    #             logger.error("数据问题..重试")
    #
    #         except Exception as e:
    #
    #             logger.error(e)
    #
    #             raise e


if __name__=="__main__":
    # unittest.main()

    #通过多个测试集合组成一个测试套
    testsuit =  unittest.TestSuite()
    testsuit.addTest(TestBookCity("test_More_Tools_Button"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



