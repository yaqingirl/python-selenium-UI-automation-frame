#coding=utf-8
import json
import re
import string
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from appModules.LoginAction import LoginAction
from config.accounts import not_vip_username, not_vip_password
from config.server_info import bookcity, url
from pageObjects.AllCommentPage import AllCommentPage
from pageObjects.BookCityPage import BookCityPage
from pageObjects.BookDetailPage import BookDetailPage
from pageObjects.DiscountPage import DiscountPage
from pageObjects.ShoppingCart import ShoppingCartPage
from pageObjects.WeeklyDiscountPage import WeeklyDiscountPage
from pageObjects.WriteCommentPage import WriteCommentPage
from testScripts.testBookCity import TestBookCity
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
from util.getApiData import BookDetai, RecommandBooks, GetTwentycomments
from util.getApiData.GetCollectionBooks import getDataList
from util.decorator.PhoneModelDecorator import set_phone_model,options


class testBookDetailNeedLogin(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @set_phone_model(phone_model)
    def test_VIP_user_read_VIP_book(self):
        logger.info("开始执行书详页-VIP用户查看VIP书详页脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute,sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            data_Type=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_type)
            if 'Y'==i and "VIP_user_VIP_book"==data_Type:
                bookid=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_id)
                bookname=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_name)
                username=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)


                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,username,password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    #登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser,pc.getUrl('bookdetail')%(bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(browser)
                    vip_price=bookDetailPage.vipOriginalPriceObj()
                    vip_read_button=bookDetailPage.vipReadButtonObj()
                    vip_read_button_text=bookDetailPage.vipReadButtonTextObj()
                    vip_read_for_free_text=bookDetailPage.vipReadForFreeTextObj()
                    vip_flag=bookDetailPage.vipFlagObj()

                    try:

                        self.assertIs(vip_read_for_free_text.is_displayed() ,True)
                        self.assertIs(vip_read_button.is_displayed() ,True)
                        self.assertIs("VIP免费读"==vip_read_button_text.text ,True)
                        self.assertIs(vip_price.is_displayed() ,True)
                        self.assertIs(vip_flag.is_displayed(),True)

                        logger.info('执行书详页-VIP用户查看VIP书详页脚本成功！用例通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-VIP用户查看VIP书详页脚本失败！用例不通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_VIP_user_read_NVIP_book(self):
        logger.info("开始执行书详页-VIP用户查看NVIP书详页脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute,sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            data_Type=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_type)
            if 'Y'==i and "VIP_user_NVIP_book"==data_Type:
                bookid=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_id)
                bookname=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_name)
                username=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)


                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,username,password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    #登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser,pc.getUrl('bookdetail')%(bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(browser)

                    read_button_text=bookDetailPage.readButtonTextObj()
                    price=bookDetailPage.realPriceObj()

                    try:

                        self.assertIs("立即阅读"==read_button_text.text ,True)
                        self.assertIs(price.is_displayed() ,True)

                        logger.info('执行书详页-VIP用户查看NVIP书详页脚本成功！用例通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-VIP用户查看NVIP书详页脚本失败！用例不通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_NVIP_user_read_VIP_book(self):
        logger.info("开始执行书详页-NVIP用户查看VIP书详页脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute,sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            data_Type=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_type)
            if 'Y'==i and "NVIP_user_VIP_book"==data_Type:
                bookid=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_id)
                bookname=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_name)
                username=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)


                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,username,password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    browser.get(pc.getUrl('bookdetail')%(bookid))
                    bookDetailPage = BookDetailPage(browser)

                    read_button_text=bookDetailPage.readButtonTextObj()
                    price=bookDetailPage.realPriceObj()
                    no_vip_read_text=bookDetailPage.noVipReadTextObj()
                    vip_flag=bookDetailPage.vipFlagObj()


                    try:

                        self.assertIs("立即阅读"==read_button_text.text ,True)
                        self.assertIs(price.is_displayed() ,True)
                        self.assertIs("开通VIP，免费阅读此书>"==no_vip_read_text.text,True)
                        self.assertIs(vip_flag.is_displayed(),True)

                        logger.info('执行书详页-NVIP用户查看VIP书详页脚本成功！用例通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-NVIP用户查看VIP书详页脚本失败！用例不通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_NVIP_user_read_NVIP_book(self):
        logger.info("开始执行书详页-NVIP用户查看NVIP书详页脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute,sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            data_Type=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_type)
            if 'Y'==i and "NVIP_user_NVIP_book"==data_Type:
                bookid=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_id)
                bookname=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,book_name)
                username=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)


                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,username,password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    browser.get(pc.getUrl('bookdetail')%(bookid))

                    bookDetailPage = BookDetailPage(browser)

                    read_button_text=bookDetailPage.readButtonTextObj()
                    price=bookDetailPage.realPriceObj()


                    try:

                        self.assertIs("立即阅读"==read_button_text.text ,True)
                        self.assertIs(price.is_displayed() ,True)
                        self.assertIs("VIP免费阅读" not in browser.page_source,True)
                        self.assertIs("开通VIP，免费阅读此书>" not in browser.page_source,True)


                        logger.info('执行书详页-NVIP用户查看NVIP书详页脚本成功！用例通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-NVIP用户查看NVIP书详页脚本失败！用例不通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx+2,execute_testResult_book_detail,'fail','red')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, execute_time_book_detail,str(time.time()-start_time)+'ms', 'red')
                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_shopping_cart_button(self):
        logger.info("开始执行书详页-购物车按钮脚本...")

        # 获取是否执行列
        isExecuteUser = testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            data_Type = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y' == i and "VIP_user_NVIP_book" == data_Type:
                bookid = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                username = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)

                logger.info("执行测试数据：%s,%s,%s,%s" % (bookid, bookname, username, password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    # 登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser, pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(browser)

                    bookDetailPage.shoppingCarButton().click()
                    time.sleep(2)

                    try:

                        self.assertIs("购物车"==browser.title,True)

                        logger.info('执行书详页购物车脚本成功！用例通过')


                    except AssertionError as e:
                        logger.debug('执行书详页-购物车脚本失败！用例不通过')

                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_book_write_comment_page(self):
        logger.info("开始执行书详页-写书评页面元素验证脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute,sheet_name='写书评验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if 'Y'==i :
                bookid=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,catagory_book_id)
                bookname=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,catagory_book_name)
                username=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, catagory_acount_username)
                password=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, catagory_acount_password)
                bookauthor=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, catagory_book_author)


                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,username,password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    # 登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser, pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')

                    bookDetailPage = BookDetailPage(browser)
                    bookDetailPage.writeBookCommentButton().click()
                    time.sleep(2)
                    writeCommentPage=WriteCommentPage(browser)


                    try:

                        self.assertIs( writeCommentPage.titleObj().is_displayed(),True)
                        self.assertIs(writeCommentPage.bookNameObj().text==bookname,True)
                        a=writeCommentPage.bookAuthorObj().text+"[著]"
                        self.assertIs(a==bookauthor,True)
                        style=writeCommentPage.publishButtonText().get_attribute("style")
                        #黑色color:rgb(222,219,214)
                        #红色：color:rgb(239,60,60)
                        #返回内容'color: rgb(222, 219, 214);'

                        logger.info('执行书详页-目录验证脚本成功！用例通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_testResult, 'success', 'green')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-目录验证脚本失败！用例不通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx+2,catagory_execute_testResult,'fail','red')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_time,str(time.time()-start_time)+'ms', 'red')
                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_write_book_comment(self):
        logger.info("开始执行书详页-写书评页面验证脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute,sheet_name='写书评验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if 'Y'==i :
                bookid=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,catagory_book_id)
                bookname=testBookDetailNeedLogin.excelObj.get_cell_value(idx+2,catagory_book_name)
                username=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, catagory_acount_username)
                password=testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, catagory_acount_password)


                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,username,password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    # 登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")

                    LoginAction.login(username, password, browser, pc.getUrl('allcomments') % (bookid))
                    all_comments_page = AllCommentPage(browser)
                    all_comments_page.writeCommentButton().click()

                    # LoginAction.login(username, password, browser, pc.getUrl('writecomment') % (bookid))
                    logger.info('启动浏览器，访问"写书评"页面...')
                    write_comment_page = WriteCommentPage(browser)

                    try:

                        self.assertIs( write_comment_page.titleObj().is_displayed(),True)
                        # self.assertIs( write_comment_page.bookAuthorObj().is_displayed(),True)
                        self.assertIs( len(write_comment_page.commentStarObj())== 5,True)
                        # self.assertIs(write_comment_page.bookNameObj().is_displayed(),True)
                        self.assertIs(write_comment_page.commentStarTextObj().text == "非读不可",True)

                        write_comment_page.commentDetailObj().send_keys("这本书真的很棒！")
                        time.sleep(2)
                        write_comment_page.publishButton().click()

                        time.sleep(2)

                        response_text=all_comments_page.commentsObj()[0].text
                        comment_content_check='这本书真的很棒！' in response_text
                        time_check='刚刚' in response_text
                        check_result=  comment_content_check and time_check
                        self.assertIs(check_result,True)


                        logger.info('执行书详页-写书评验证脚本成功！用例通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_testResult, 'success', 'green')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-写书评验证脚本失败！用例不通过')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx+2,catagory_execute_testResult,'fail','red')
                        testBookDetailNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_time,str(time.time()-start_time)+'ms', 'red')
                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    @set_phone_model(phone_model)
    def test_add_shop_cart_button(self):
        logger.info("开始执行书详页-加入购物车按钮脚本...")

        # 获取是否执行列
        isExecuteUser = testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            data_Type = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y' == i and "VIP_user_NVIP_book" == data_Type:
                bookid = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                username = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)

                logger.info("执行测试数据：%s,%s,%s,%s" % (bookid, bookname, username, password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    # 登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser, pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(browser)

                    add_shopping_cart_button=bookDetailPage.shopCartButton()
                    browser.execute_script("arguments[0].scrollIntoView();", add_shopping_cart_button)

                    add_shopping_cart_button.click()
                    time.sleep(2)
                    add_shopping_cart_button.click()

                    try:

                        shopping_cart_page = ShoppingCartPage(browser)
                        first_book_in_shopping_cart=shopping_cart_page.shoppingCartBookListObj()[0].text
                        self.assertIs( bookname in first_book_in_shopping_cart,True)
                        shopping_cart_page.shoppingCartBookOptionListObj()[0].click()
                        shopping_cart_page.shoppingCartDeleteButton().click()
                        time.sleep(2)
                        shopping_cart_page.shoppingCartDeleteConfirmButton().click()

                        logger.info('执行书详页加入购物车脚本成功！用例通过')


                    except AssertionError as e:
                        logger.debug('执行书详页-加入购物车脚本失败！用例不通过')

                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue
    @set_phone_model(phone_model)
    def test_read_book_button(self):
        logger.info("开始执行书详页-阅读按钮脚本...")

        # 获取是否执行列
        isExecuteUser = testBookDetailNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='VIP逻辑验证书籍')
        pc = ParseConfigFile()

        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            data_Type = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y' == i and "VIP_user_VIP_book" == data_Type:
                bookid = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                username = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)

                logger.info("执行测试数据：%s,%s,%s,%s" % (bookid, bookname, username, password))

                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    # 登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser, pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(browser)

                    read_button=bookDetailPage.readButton()
                    browser.execute_script("arguments[0].scrollIntoView();", read_button)

                    try:

                        self.assertIs( read_button.text=='VIP免费读',True)
                        read_button.click()
                        time.sleep(2)
                        check_url='%sstatic/read/dist/index.html?ebookId=%s&name='%(url,bookid) in  browser.current_url
                        self.assertIs(check_url,True)
                        logger.info('执行书详页阅读按钮脚本成功！用例通过')

                    except AssertionError as e:
                        logger.debug('执行书详页-阅读按钮脚本失败！用例不通过')

                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            elif 'Y' == i and "VIP_user_VIP_book" != data_Type :
                bookid = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                username = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_username_check_vip)
                password = testBookDetailNeedLogin.excelObj.get_cell_value(idx + 2, acount_password_check_vip)

                logger.info("执行测试数据：%s,%s,%s,%s" % (bookid, bookname, username, password))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    # 登陆
                    logger.info('登录操作执行...')
                    browser.get("https://plogin.m.jd.com/user/login.action")
                    LoginAction.login(username, password, browser, pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(browser)

                    read_button = bookDetailPage.readButton()
                    browser.execute_script("arguments[0].scrollIntoView();", read_button)

                    try:

                        self.assertIs(read_button.text == '立即阅读', True)
                        read_button.click()
                        time.sleep(2)
                        check_url = '%sstatic/read/dist/index.html?ebookId=%s&name=' % (url,bookid) in browser.current_url
                        self.assertIs(check_url, True)
                        logger.info('执行书详页阅读按钮脚本成功！用例通过')

                    except AssertionError as e:
                        logger.debug('执行书详页-阅读按钮脚本失败！用例不通过')

                        raise e

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e

            else:
                continue
if __name__=="__main__":
    # unittest.main()

    #通过多个测试集合组成一个测试套
    testsuit =  unittest.TestSuite()
    testsuit.addTest(testBookDetailNeedLogin("test_price_free_book"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



