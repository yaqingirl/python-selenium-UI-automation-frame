#coding=utf-8
import json
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from appModules.LoginAction import LoginAction
from config.accounts import not_vip_username, not_vip_password
from pageObjects.ReadBookPage import ReadBookPage
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
from util.AIWaitOperate import AIclick
from util.getApiData import MyBooks
from util.SendMail import text_mail
from util.decorator.PhoneModelDecorator import set_phone_model,options


class TestRead(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    @classmethod
    @set_phone_model(phone_model)
    def setUpClass(cls) -> None:
        TestRead.browser = webdriver.Chrome(chrome_options=options)

        logger.info("开始登陆...")
        TestRead.browser.get("https://plogin.m.jd.com/user/login.action")
        TestRead.login_cookie = LoginAction.login(not_vip_username, not_vip_password, TestRead.browser)

    @classmethod
    def tearDownClass(cls) -> None:
        TestRead.browser.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_Popup_Menu(self):
        logger.info("开始执行唤起菜单脚本...")
        #获取是否执行列
        isExecuteUser=TestRead.excelObj.get_col_values(book_isExecute,sheet_name='阅读书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                bookid=TestRead.excelObj.get_cell_value(idx+2,book_id)
                bookname=TestRead.excelObj.get_cell_value(idx+2,book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:

                    TestRead.browser.get(pc.getUrl('read')%(bookid,bookname))
                    logger.info('启动浏览器，访问"阅读"页面...')
                    readbookPage = ReadBookPage(TestRead.browser)

                    logger.info('点击"阅读"页面的中间1次...')
                    center_section=readbookPage.CenterSectionObj()
                    ActionChains(TestRead.browser).move_to_element(center_section).click().perform()

                    try:
                        settingButton = readbookPage.SettingButton()
                        #智能点击
                        AIclick(settingButton)
                        self.assertIs(readbookPage.JDHeaderBar().is_displayed(),True)
                        logger.info('调起菜单成功！用例通过')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('调起菜单失败！用例通过')
                        TestRead.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
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

    def test_More_Tools_Button(self):
        logger.info("开始执行唤起更多工具按钮脚本...")
        #获取是否执行列
        isExecuteUser=TestRead.excelObj.get_col_values(book_isExecute,sheet_name='阅读书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                bookid=TestRead.excelObj.get_cell_value(idx+2,book_id)
                bookname=TestRead.excelObj.get_cell_value(idx+2,book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:

                    TestRead.browser.get(pc.getUrl('read')%(bookid,bookname))

                    logger.info('启动浏览器，访问"阅读"页面...')
                    readbookPage = ReadBookPage(TestRead.browser)

                    logger.info('点击右侧区域翻一页...')
                    AIclick(readbookPage.RightSectionObj())

                    logger.info('点击"阅读"页面的中间1次...')
                    # AIclick(readbookPage.CenterSectionObj())
                    center_section=readbookPage.CenterSectionObj()
                    # center_section.click()
                    ActionChains(TestRead.browser).move_to_element(center_section).click().perform()
                    time.sleep(2)

                    logger.info('点击右上角更多按钮...')
                    # readbookPage.HeaderMenuObj().click()
                    TestRead.browser.execute_script("arguments[0].click()",readbookPage.HeaderMenuObj())
                    time.sleep(2)

                    try:
                        searchIndexButtonJS = "document.getElementsByClassName('jdr-dropdown-item')[0].click()"
                        TestRead.browser.execute_script(searchIndexButtonJS)
                        time.sleep(2)

                        self.assertIs("<title>精选</title>" in TestRead.browser.page_source,True)
                        logger.info('调起菜单成功！用例通过')

                    except Exception as e:
                        logger.debug('更多按钮操作失败！用例不通过')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_time,
                                                           str(time.time() - start_time) + 'ms', 'red')
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
            else:
                continue

    def test_Turn_Page(self):
        logger.info("开始执行翻页脚本...")
        #获取是否执行列
        isExecuteUser=TestRead.excelObj.get_col_values(book_isExecute,sheet_name='阅读书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                bookid=TestRead.excelObj.get_cell_value(idx+2,book_id)
                bookname=TestRead.excelObj.get_cell_value(idx+2,book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:

                    TestRead.browser.get(pc.getUrl('read')%(bookid,bookname))

                    logger.info('启动浏览器，访问"阅读"页面...')
                    readbookPage = ReadBookPage(TestRead.browser)
                    logger.info('点击"阅读"页面的右侧翻页7次...')

                    for i in range(7):
                        readbookPage.RightSectionObj().click()
                        time.sleep(1)

                    logger.info('点击"阅读"页面的左侧翻页1次...')
                    readbookPage.LeftSectionObj().click()

                    try:
                        title=readbookPage.ChapterTitleObj().text
                        content=readbookPage.ChapterFirstContentObj().text
                        # 章节标题包含：不能在“温室”里培养干部；且内容包含：现在在一些地方，则通过用例
                        self.assertIs((('不能在“温室”里培养干部' in title) and ('现在在一些地方' in content)),True)
                        logger.info('翻页后判断文中内容用例通过')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except Exception as e:
                        logger.debug('翻页后判断文中内容用例不通过')
                        TestRead.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        TestRead.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')


                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

    def test_Buy_In_Read_Page(self):
        logger.info("开始执行书内购买脚本...")
        #获取是否执行列
        isExecute=TestRead.excelObj.get_col_values(book_isExecute,sheet_name='购买书籍')
        pc = ParseConfigFile()
        buy_success=False

        for idx,i in enumerate(isExecute[1:]):
            start_time=time.time()
            if (not buy_success) and i=='Y':
                bookid = TestRead.excelObj.get_cell_value(idx + 2, book_id)
                buyerUsername=TestRead.excelObj.get_cell_value(idx + 2, buyer_username)
                buyerPassword=TestRead.excelObj.get_cell_value(idx + 2, buyer_password)
                bookname=TestRead.excelObj.get_cell_value(idx + 2, book_name)
                logger.info("执行测试数据：%s,%s,%s" % (bookid,buyerUsername,buyerPassword))

                #通过接口api拿到我的书籍列表中的书
                my_books_data=MyBooks.getData(TestRead.excelObj.get_cell_value(idx + 2, buyer_pin))
                #判断buyer是否已经拥有该书：
                have_flag= bookid in my_books_data
                if have_flag:
                    TestRead.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                else:
                    try:

                        TestRead.browser.get(pc.getUrl('read') % (bookid, bookname))
                        logger.info('访问"阅读"页面成功...')
                        time.sleep(2)
                        readbookPage = ReadBookPage(TestRead.browser)
                        readbookPage.CenterSectionObj().click()
                        logger.info('点击中间区域成功...')
                        time.sleep(2)
                        readbookPage.DirButton().click()
                        logger.info('点击目录成功...')
                        chapter_dirs=readbookPage.chapterNeedPayrDirs()

                        if chapter_dirs and len(chapter_dirs)!=0:
                            first_need_pay_chapter=chapter_dirs[1]
                        else:
                            raise NoSuchElementException()

                        ###滚动屏幕，漏出最后一个可读的章节目录，以便点击
                        TestRead.browser.execute_script("arguments[0].scrollIntoView(false);", first_need_pay_chapter)

                        # browser.execute_script(scrollJS1)
                        TestRead.browser.implicitly_wait(5)
                        # scrollJS2 = "window.scrollBy(0,50)"
                        # browser.execute_script(scrollJS2)

                        time.sleep(2)
                        readbookPage.LastChapterFreeDir().click()
                        logger.info('点击最后一章试读章节目录成功...')

                        time.sleep(2)
                        turnPageFlag=True
                        while turnPageFlag:
                            readbookPage.RightSectionObj().click()
                            time.sleep(1)
                            if readbookPage.YesOrNotBuyBookDialog().is_displayed():
                                turnPageFlag=False
                                time.sleep(1)
                                logger.info('打开询问是否购买弹窗成功...')

                        time.sleep(2)
                        readbookPage.BuyBookConfirmButton().click()
                        logger.info('点击确认购买按钮成功...')

                        time.sleep(2)
                        bCanBuy=readbookPage.BuyBookCommitButton().text
                        try:
                            if '确认购买'==bCanBuy:
                                readbookPage.BuyBookCommitButton().click()
                                time.sleep(2)
                                # 通过接口api拿到我的书籍列表中的书
                                my_books_data = MyBooks.getData(TestRead.excelObj.get_cell_value(idx + 2, buyer_pin))
                                # 判断buyer是否已经拥有该书：
                                have_flag = bookid in my_books_data

                                self.assertIs(have_flag,True)
                                logger.info('文内购买书籍用例通过')
                                buy_success=True
                                TestRead.excelObj.write_cell_value(idx+2,book_isExecute,'N')
                                TestRead.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                                TestRead.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')
                            elif '充值并购买' == bCanBuy:
                                logger.warning('余额不足...')
                                buy_success=True
                                text_mail('来自m站自动化测试脚本', '在文内购买书籍测试用例中%s账户余额不足，请及时充值' % (buyerUsername))
                                self.assertTrue(1==2)

                        except AssertionError as e:
                            logger.debug('文内购买书籍用例不通过')
                            TestRead.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                            TestRead.excelObj.write_cell_value(idx + 2, execute_time,str(time.time() - start_time) + 'ms', 'red')
                            TestRead.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
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

    def test_Buy_In_Read_Page_Not_Enought_Money(self):
        logger.info("开始执行书内购买脚本...")
        #获取是否执行列
        isExecute=TestRead.excelObj.get_col_values(book_isExecute,sheet_name='购买书籍余额不足')
        pc = ParseConfigFile()
        complete_flag=False

        for idx,i in enumerate(isExecute[1:]):
            start_time=time.time()
            if (not complete_flag) and i=='Y':
                bookid = TestRead.excelObj.get_cell_value(idx + 2, book_id)
                buyerUsername=TestRead.excelObj.get_cell_value(idx + 2, buyer_username)
                buyerPassword=TestRead.excelObj.get_cell_value(idx + 2, buyer_password)
                bookname=TestRead.excelObj.get_cell_value(idx + 2, book_name)
                logger.info("执行测试数据：%s,%s,%s" % (bookid,buyerUsername,buyerPassword))

                #通过接口api拿到我的书籍列表中的书
                my_books_data=MyBooks.getData(TestRead.excelObj.get_cell_value(idx + 2, buyer_pin))
                #判断buyer是否已经拥有该书：
                have_flag= bookid in my_books_data
                if have_flag:
                    TestRead.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                else:
                    try:

                        TestRead.browser.get(pc.getUrl('read')%(bookid,bookname))

                        logger.info('访问"阅读"页面成功...')

                        time.sleep(2)
                        readbookPage = ReadBookPage(TestRead.browser)
                        readbookPage.CenterSectionObj().click()
                        logger.info('点击中间区域成功...')

                        time.sleep(2)
                        readbookPage.DirButton().click()
                        logger.info('点击目录成功...')

                        time.sleep(2)
                        last_free_chapter=readbookPage.LastChapterNeedPayrDir()
                        TestRead.browser.execute_script("arguments[0].scrollIntoView();", last_free_chapter)
                        last_free_chapter.click()
                        logger.info('点击最后一章试读章节目录成功...')

                        time.sleep(2)
                        turnPageFlag=True
                        while turnPageFlag:
                            readbookPage.RightSectionObj().click()
                            time.sleep(1)
                            if readbookPage.YesOrNotBuyBookDialog().is_displayed():
                                turnPageFlag=False
                                time.sleep(1)
                                logger.info('打开询问是否购买弹窗成功...')

                        time.sleep(2)
                        readbookPage.BuyBookConfirmButton().click()
                        logger.info('点击确认购买按钮成功...')

                        time.sleep(2)
                        canOrNotCanBuy=readbookPage.BuyBookCommitButton().text
                        try:

                            self.assertIs('充值并购买'==canOrNotCanBuy,True)
                            logger.info('文内购买书籍余额不足判断,测试用例通过')
                            TestRead.excelObj.write_cell_value(idx+2,execute_testResult,'success','green')
                            TestRead.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms')
                            complete_flag=True

                        except AssertionError as e:
                            logger.debug('文内购买书籍余额不足判断测试用例不通过')
                            complete_flag=True
                            TestRead.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                            TestRead.excelObj.write_cell_value(idx + 2, execute_time,str(time.time() - start_time) + 'ms', 'red')
                            TestRead.excelObj.write_cell_value(idx + 2, book_isExecute, 'N')
                            raise e

                    except ElementNotVisibleException as e:

                        logger.error("数据问题，元素没有找到..重试")

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
    testsuit.addTest(TestRead("test_Buy_In_Read_Page"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



