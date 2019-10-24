#coding=utf-8
import json
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from appModules.LoginAction import LoginAction
from config.accounts import not_vip_username, not_vip_password
from pageObjects.BookDetailPage import BookDetailPage
from pageObjects.ReadBookPage import ReadBookPage
from pageObjects.ShoppingCart import ShoppingCartPage
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
from util.AIWaitOperate import AIclick
from util.getApiData import MyBooks
from util.SendMail import text_mail
from util.decorator.PhoneModelDecorator import set_phone_model,options


class TesShoppingCart(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    @classmethod
    @set_phone_model(phone_model)
    def setUpClass(cls) -> None:
        TesShoppingCart.browser = webdriver.Chrome(chrome_options=options)

        logger.info("开始登陆...")
        TesShoppingCart.browser.get("https://plogin.m.jd.com/user/login.action")
        TesShoppingCart.login_cookie = LoginAction.login(not_vip_username, not_vip_password, TesShoppingCart.browser)

    @classmethod
    def tearDownClass(cls) -> None:
        TesShoppingCart.browser.quit()

    def test_Add_Book_and_Delete_Book(self):
        #获取是否执行列
        isExecuteUser=TesShoppingCart.excelObj.get_col_values(book_isExecute,sheet_name='购买书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                bookid=TesShoppingCart.excelObj.get_cell_value(idx+2,book_id)
                bookname=TesShoppingCart.excelObj.get_cell_value(idx+2,book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                # 通过接口api拿到我的书籍列表中的书
                my_books_data = MyBooks.getData(TesShoppingCart.excelObj.get_cell_value(idx + 2, buyer_pin))
                # 判断buyer是否已经拥有该书：
                have_flag = bookid in my_books_data
                if have_flag:
                    TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                else:
                    try:

                        TesShoppingCart.browser.get(pc.getUrl('bookdetail')%(bookid))

                        logger.info('启动浏览器，访问"书详页"页面...')
                        book_detail_page=BookDetailPage(TesShoppingCart.browser)

                        add_shopping_cart_button = book_detail_page.shopCartButton()
                        TesShoppingCart.browser.execute_script("arguments[0].scrollIntoView();", add_shopping_cart_button)

                        add_shopping_cart_button.click()
                        time.sleep(2)
                        add_shopping_cart_button.click()
                        shopping_cart_page = ShoppingCartPage(TesShoppingCart.browser)

                        try:
                            first_book_in_shopping_cart = shopping_cart_page.shoppingCartBookListObj()[0].text
                            self.assertIs(bookname in first_book_in_shopping_cart, True)

                            shopping_cart_page.shoppingCartBookOptionListObj()[0].click()
                            shopping_cart_page.shoppingCartDeleteButton().click()
                            time.sleep(2)
                            shopping_cart_page.shoppingCartDeleteConfirmButton().click()

                            TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                            TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')
                            logger.info('购物车删除书籍，用例通过！')
                            break

                        except AssertionError as e:
                            logger.debug('购物车删除书籍，用例不通过！')
                            TesShoppingCart.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                            TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
                            TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
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

    def test_Add_Book_and_Buy_Book(self):
        # 获取是否执行列
        isExecuteUser = TesShoppingCart.excelObj.get_col_values(book_isExecute, sheet_name='购买书籍')
        pc = ParseConfigFile()

        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            if i == 'Y':
                bookid = TesShoppingCart.excelObj.get_cell_value(idx + 2, book_id)
                bookname = TesShoppingCart.excelObj.get_cell_value(idx + 2, book_name)
                logger.info("执行测试数据：%s,%s" % (bookid, bookname))
                # 通过接口api拿到我的书籍列表中的书
                my_books_data = MyBooks.getData(TesShoppingCart.excelObj.get_cell_value(idx + 2, buyer_pin))
                # 判断buyer是否已经拥有该书：
                have_flag = bookid in my_books_data
                if have_flag:
                    TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                else:
                    try:

                        TesShoppingCart.browser.get(pc.getUrl('bookdetail') % (bookid))

                        logger.info('启动浏览器，访问"书详页"页面...')
                        book_detail_page = BookDetailPage(TesShoppingCart.browser)

                        add_shopping_cart_button = book_detail_page.shopCartButton()
                        # TesShoppingCart.browser.execute_script("arguments[0].scrollIntoView();", add_shopping_cart_button)

                        add_shopping_cart_button.click()
                        time.sleep(2)
                        add_shopping_cart_button.click()
                        shopping_cart_page = ShoppingCartPage(TesShoppingCart.browser)
                        price=shopping_cart_page.shoppingCartBookPriceListObj()[0].text
                        book_image=shopping_cart_page.shoppingCartBookImageListObj()[0]
                        book_name_in_cart=shopping_cart_page.shoppingCartBookNameListObj()[0]

                        try:
                            self.assertIs(book_image.is_displayed(), True)
                            self.assertIs(book_name_in_cart.is_displayed(), True)
                            first_book_in_shopping_cart = shopping_cart_page.shoppingCartBookListObj()[0].text
                            self.assertIs(bookname in first_book_in_shopping_cart, True)

                            shopping_cart_page.shoppingCartBookOptionListObj()[0].click()
                            shopping_cart_page.shoppingCartSettlementButton().click()

                            time.sleep(2)
                            avail_amount = shopping_cart_page.shoppingCartSettlementAvailAmountObj().text.strip('-')
                            settlement_amount = shopping_cart_page.shoppingCartSettlementAmountObj().text
                            check_price=False
                            if price==avail_amount and price==settlement_amount:
                                check_price=True
                            self.assertIs(check_price,True)
                            shopping_cart_payable_amount=shopping_cart_page.shoppingCartPayableAmountObj().text
                            if '￥0' in shopping_cart_payable_amount:
                                shopping_cart_buy_confirm_btn=shopping_cart_page.shoppingCartBuyConfirmButton()
                                shopping_cart_buy_confirm_btn.click()
                                time.sleep(2)
                                self.assertIs("支付完成"==TesShoppingCart.browser.title,True)
                                TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                                TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                                TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_time, str(
                                    round((time.time() - start_time) / 1000, 2)) + 's')
                                logger.info('购物车购买书籍，用例通过！')
                                break
                            else:
                                logger.warning('余额不足...')
                                text_mail('来自m站自动化测试脚本', '在购物车购买书籍测试用例中%s账户余额不足，请及时充值' % (not_vip_username))
                                self.assertTrue(1 == 2)

                        except AssertionError as e:
                            logger.debug('购物车删除书籍，用例不通过！')
                            TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                            TesShoppingCart.excelObj.write_cell_value(idx + 2, execute_time,
                                                                      str(time.time() - start_time) + 'ms', 'red')
                            TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                            raise e

                    except ElementNotVisibleException as e:
                        TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                        logger.error("数据问题，元素没有找到..")

                    except NoSuchElementException as e:

                        TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                        logger.error("数据问题..重试")

                    except Exception as e:
                        TesShoppingCart.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                        logger.error(e)

                        raise e
            else:
                continue

if __name__=="__main__":
    # unittest.main()

    #通过多个测试集合组成一个测试套
    testsuit =  unittest.TestSuite()
    # testsuit.addTest(TestRead("test_Buy_In_Read_Page"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



