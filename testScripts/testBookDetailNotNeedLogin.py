#coding=utf-8
import json
import re
import string
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from pageObjects.AllCommentPage import AllCommentPage
from pageObjects.BookCityPage import BookCityPage
from pageObjects.BookDetailPage import BookDetailPage
from pageObjects.DiscountPage import DiscountPage
from pageObjects.WeeklyDiscountPage import WeeklyDiscountPage
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
from util.getApiData import BookDetai, GetTwentycomments, CollectionDetail
from util.getApiData.GetCollectionBooks import getDataList
from util.decorator.PhoneModelDecorator import set_phone_model,options

class testBookDetailNotNeedLogin(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    @classmethod
    @set_phone_model(phone_model)
    def setUpClass(cls) -> None:
        testBookDetailNotNeedLogin.browser = webdriver.Chrome(chrome_options=options)

    @classmethod
    def tearDownClass(cls) -> None:
        testBookDetailNotNeedLogin.browser.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_price_free_book(self):
        logger.info("开始执行书详页免费书价格脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNotNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='价格逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            bookType=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y'==i and "免费"==bookType:
                bookid=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:

                    testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
                    price=bookDetailPage.priceObj()

                    try:

                        self.assertIs(price.is_displayed() and "免费"==price.text,True)
                        logger.info('书详页免费书价格脚本执行成功！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time) / 1000, 2)) + 's')

                    except AssertionError as e:
                        logger.debug('书详页免费书价格脚本执行失败！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(time.time() - start_time) + 'ms', 'red')
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

    def test_price_no_discount_book(self):
        logger.info("开始执行书详页非折扣书价格脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNotNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='价格逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            bookType=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y'==i and "没折扣"==bookType:
                bookid=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:
                    testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
                    realprice_obj=bookDetailPage.realPriceObj()
                    # realprice=realprice_obj.text.strip('阅豆')
                    realprice=str(int(round(float(realprice_obj.text.strip('￥'))*100)))
                    api_realprice=str(BookDetai.getData(bookid)['jd_price'])

                    try:

                        self.assertIs(realprice_obj.is_displayed() and api_realprice==realprice,True)
                        logger.info('书详页非折扣书籍脚本执行成功！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time) / 1000, 2)) + 's')

                    except AssertionError as e:
                        logger.debug('书详页非折扣书籍价格脚本执行失败！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(time.time() - start_time) + 'ms', 'red')
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

    def test_price_sell_out_book(self):
        logger.info("开始执行书详页下柜书价格脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNotNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='价格逻辑验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            bookType=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y'==i and "下柜"==bookType:
                bookid=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:

                    testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
                    price=bookDetailPage.priceObj()

                    try:

                        self.assertIs(price.is_displayed() and "此书已下柜"==price.text,True)
                        logger.info('书详页下柜书价格脚本执行成功！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time) / 1000, 2)) + 's')

                    except AssertionError as e:
                        logger.debug('书详页下柜书书价格脚本执行失败！用例不通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'fail', 'red')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time, str(time.time() - start_time) + 'ms', 'red')
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

    def test_price_sell_off_book(self):
        logger.info("开始执行书详页打折书价格脚本...")

        pc = ParseConfigFile()

        try:

            # books_data=getDataList('本周特价')
            testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookcity'))

            bookcityPage = BookCityPage(testBookDetailNotNeedLogin.browser)
            bookcityPage.channelFoldDownButton().click()
            time.sleep(2)

            bookcityPage.channelFeaturedButton().click()
            time.sleep(2)
            bookcityPage.discountButton().click()
            # time.sleep(2)
            # discountPage = DiscountPage(testBookDetailNotNeedLogin.browser)
            # discountPage.first_book().click()

            time.sleep(2)
            current_url=testBookDetailNotNeedLogin.browser.current_url
            collection_id=re.search(r'\d{4}',current_url).group(0)

            collection_data=CollectionDetail.getDataJson(collection_id)


            bookid=str(collection_data['data']['items'][0]['ebook_id'])

            testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

            logger.info('启动浏览器，访问"书籍详情"页面...')
            bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
            real_price_obj = bookDetailPage.realPriceObj()
            original_price_obj=bookDetailPage.originalPriceObj()
            discount_obj=bookDetailPage.discountObj()
            # color=discount.get_attribute('color')


            api_realprice = str(BookDetai.getData(bookid)['jd_price'])
            api_price = str(BookDetai.getData(bookid)['price'])
            api_discount= str(BookDetai.getData(bookid)['discount'])

            real_price=str(int(round(float(real_price_obj.text.strip('￥')) * 100)))
            original_price=str(int(round(float(original_price_obj.text.strip('￥'))* 100)))
            discount= discount_obj.text

            try:

                self.assertIs(real_price_obj.is_displayed() and api_realprice == real_price, True)
                self.assertIs(original_price_obj.is_displayed() and api_price == original_price, True)
                self.assertIs(discount_obj.is_displayed() and api_discount == discount, True)

                logger.info('书详页折扣书价格脚本执行成功！用例通过')

            except AssertionError as e:
                logger.debug('书详页折扣书价格脚本执行失败！用例通过')

                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e

    def test_book_cover_author_publish_recmmand_name(self):
        logger.info("开始执行书详页-书籍封面、书名、作者和出版社脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNotNeedLogin.excelObj.get_col_values(book_isExecute_book_detail, sheet_name='基本信息验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            data_Type=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y'==i :
                bookid=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_name)
                bookAuthor=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_author)
                bookPublish=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_publish)

                logger.info("执行测试数据：%s,%s,%s,%s"%(bookid,bookname,bookAuthor,bookPublish))
                try:

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

                    bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
                    book_cover_obj=bookDetailPage.bookCoverObj()
                    book_publish_obj=bookDetailPage.publishObj()
                    book_author_obj=bookDetailPage.authorObj()
                    book_name_obj=bookDetailPage.bookNameObj()
                    book_recommand_obj=bookDetailPage.foldRecommandObj()

                    try:

                        self.assertIs(book_cover_obj.is_displayed(),True)
                        self.assertIs(book_publish_obj.text.strip(string.whitespace)==bookPublish.strip(string.whitespace),True)
                        self.assertIs(book_author_obj.text.strip(string.whitespace)==bookAuthor.strip(string.whitespace),True)
                        self.assertIs(book_name_obj.text.strip(string.whitespace)==bookname.strip(string.whitespace),True)
                        self.assertIs(book_recommand_obj.is_displayed(),True)

                        logger.info('执行书详页-书籍封面、书名、作者和出版社脚本成功！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult_book_detail, 'success', 'green')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time_book_detail, str(round((time.time() - start_time) / 1000, 2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页--书籍封面、书名、作者和出版社脚本失败！用例不通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult_book_detail, 'fail', 'red')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time_book_detail, str(time.time() - start_time) + 'ms', 'red')
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

    def test_book_comment(self):
        logger.info("开始执行书详页-书籍评论脚本...")

        #获取是否执行列
        isExecuteUser=testBookDetailNotNeedLogin.excelObj.get_col_values(book_isExecute_book_detail, sheet_name='基本信息验证书籍')
        pc = ParseConfigFile()

        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            data_Type=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_type)
            if 'Y'==i :
                bookid=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_id)
                bookname=testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, book_name)

                logger.info("执行测试数据：%s,%s"%(bookid,bookname))
                try:

                    logger.info('启动浏览器，访问"书籍详情"页面...')
                    testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))
                    bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
                    api_book_comment_stars_count = int(BookDetai.getData(bookid)['star'])
                    api_book_comment_count = int(BookDetai.getData(bookid)['comment_count'])

                    try:
                        if api_book_comment_count > 0:

                            book_comment_stars_obj = bookDetailPage.activeCommentStarObj()
                            book_comment_count_obj = bookDetailPage.commentCountObj()
                            book_comments_count = int(
                                re.search(r'\d+', book_comment_count_obj.text.strip(string.whitespace)).group())

                            self.assertIs(api_book_comment_stars_count==len(book_comment_stars_obj),True)
                            self.assertIs(api_book_comment_count==book_comments_count,True)
                        else:
                            book_comment_text=bookDetailPage.commentCountObj().text
                            self.assertIs("暂无评分"==book_comment_text,True)

                        logger.info('执行书详页-书籍评论脚本成功！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult_book_detail, 'success', 'green')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time_book_detail, str(round((time.time() - start_time) / 1000, 2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-书籍评论脚本失败！用例不通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_testResult_book_detail, 'fail', 'red')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, execute_time_book_detail, str(time.time() - start_time) + 'ms', 'red')
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

    def test_activity(self):
        logger.info("开始执行书详页促销活动脚本...")

        pc = ParseConfigFile()

        try:

            # books_data=getDataList('双周特价')
            # books_data=getDataList('本周特价')
            #
            # bookid=str(books_data[0]['ebook_id'])
            testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookcity'))

            book_city_page=BookCityPage(testBookDetailNotNeedLogin.browser)
            book_city_page.discountButton().click()
            time.sleep(1)

            discount_page=WeeklyDiscountPage(testBookDetailNotNeedLogin.browser)
            discount_page.firstBook().click()
            time.sleep(1)
            bookid=re.search(r'[0-9]{8}', testBookDetailNotNeedLogin.browser.current_url).group()


            testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

            logger.info('启动浏览器，访问"书籍详情"页面...')
            bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
            activity_obj = bookDetailPage.acivityObj()
            activity_text = activity_obj.text.strip(string.whitespace)
            api_activity=BookDetai.getData(bookid)['promotion_msg']

            try:

                self.assertIs(activity_text==api_activity, True)


                logger.info('书详页促销活动脚本执行成功！用例通过')

            except AssertionError as e:
                logger.debug('书详页促销活动脚本执行失败！用例通过')

                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e

    def test_book_detail_comment(self):
        logger.info("开始执行书详页-书评列表验证脚本...")

        # 获取是否执行列
        isExecuteUser = testBookDetailNotNeedLogin.excelObj.get_col_values(book_isExecute, sheet_name='书详页书评验证书籍')
        pc = ParseConfigFile()

        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            if 'Y' == i:
                bookid = testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, catagory_book_id)
                bookname = testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, catagory_book_name)
                username = testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, catagory_acount_username)
                password = testBookDetailNotNeedLogin.excelObj.get_cell_value(idx + 2, catagory_acount_password)

                logger.info("执行测试数据：%s,%s,%s,%s" % (bookid, bookname, username, password))
                try:

                    testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (bookid))

                    logger.info('启动浏览器，访问"书详页"页面...')
                    book_detail_page=BookDetailPage(testBookDetailNotNeedLogin.browser)
                    comment_title=book_detail_page.commentTitleObj()
                    testBookDetailNotNeedLogin.browser.execute_script("arguments[0].scrollIntoView();", comment_title)

                    api_comments=GetTwentycomments.getCommentsByPopular(bookid)
                    api_comments_num=len(api_comments)

                    try:

                        if api_comments_num == 0:
                            no_comment_text = book_detail_page.noCommentTextObj()
                            self.assertIs(no_comment_text.is_displayed(), True)

                        else:

                            if api_comments_num > 3:
                                all_comments_text=book_detail_page.allCommentsTextObj()
                                self.assertIs(all_comments_text.is_displayed(), True)

                            first_comment_user_head=book_detail_page.commentUserHeadImg()
                            first_comment_user_name=book_detail_page.commentUserNameObj()
                            first_comment_user_level=book_detail_page.commentUserLevelObj()
                            first_comment_content=book_detail_page.commentContentObj()
                            first_comment_time=book_detail_page.commentTimeObj()
                            check_result=first_comment_user_head.is_displayed() and \
                                         first_comment_user_name.is_displayed()and \
                                        first_comment_user_level.is_displayed() and \
                                        first_comment_content.is_displayed() and \
                                        first_comment_time.is_displayed()
                            self.assertIs(check_result, True)

                        logger.info('执行书详页-书评列表验证脚本成功！用例通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_testResult, 'success',
                                                                 'green')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_time,
                                                                             str(round((time.time() - start_time) / 1000, 2)) + 's')

                    except AssertionError as e:
                        logger.debug('执行书详页-书评列表验证脚本失败！用例不通过')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_testResult, 'fail', 'red')
                        testBookDetailNotNeedLogin.excelObj.write_cell_value(idx + 2, catagory_execute_time,
                                                                             str(time.time() - start_time) + 'ms', 'red')
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

    def test_recomment_books(self):
        logger.info("开始执行书详页相关书籍推荐脚本...")

        pc = ParseConfigFile()

        try:

            testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % ('30331055'))

            logger.info('启动浏览器，访问"书籍详情"页面...')
            bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)
            page_recommand_books=[ item for item in bookDetailPage.allRecommandBooksObj()]

            try:

                for i in page_recommand_books:
                    self.assertIs(i.is_displayed(), True)

                logger.info('书详页相关图书推荐脚本执行成功！用例通过')

            except AssertionError as e:
                logger.debug('书详页相关图书推荐脚本执行失败！用例通过')

                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e

    def test_all_comments(self):
        logger.info("开始执行书详页全部评论脚本...")

        pc = ParseConfigFile()

        try:

            ebookid=30331055

            testBookDetailNotNeedLogin.browser.get(pc.getUrl('allcomments') % (ebookid))

            logger.info('启动浏览器，访问"书籍详情"页面...')
            all_comments_Page = AllCommentPage(testBookDetailNotNeedLogin.browser)
            all_comments_Page_title = all_comments_Page.allCommentsTitle()
            all_comments_Page_write_button = all_comments_Page.writeCommentButton()
            all_comments_page_comments_count = re.search(r'\d+', all_comments_Page.allCommentsCountObj().text).group()
            api_all_comments_count = GetTwentycomments.getData(ebookid)['total']
            check_count = str(all_comments_page_comments_count) == str(api_all_comments_count)
            all_comments_page_sort_by=all_comments_Page.allCommentsSortByObj()
            all_comments_sort_type_change_button=all_comments_Page.allCommentsSortTypeChangeButton()
            all_comments_sort_unselected=all_comments_Page.allCommentsSortUnSelected()
            all_comments_sort_selected=all_comments_Page.allCommentsSortSelected()


            try:

                self.assertIs(all_comments_Page_title.is_displayed(), True)
                self.assertIs(all_comments_Page_write_button.is_displayed(), True)
                self.assertIs(check_count, True)
                check_sort_by_default=all_comments_page_sort_by.text=="按热度"
                self.assertIs(check_sort_by_default, True)
                all_comments_sort_type_change_button.click()
                time.sleep(2)
                all_comments_sort_unselected.click()
                time.sleep(2)
                check_sort_by=all_comments_page_sort_by.text=="按时间"
                self.assertIs(check_sort_by, True)
                api_first_comment=GetTwentycomments.getCommentsByCreattime(ebookid)[0]['comment']
                page_first_comment=all_comments_Page.allCommentsContent()
                if api_first_comment==page_first_comment.text:
                    check_content=True
                else:
                    check_content=False
                self.assertIs(check_content, True)

                first_comment_user_head = all_comments_Page.allCommentsUserHead()
                first_comment_user_name = all_comments_Page.allCommentsUserName()
                first_comment_user_level = all_comments_Page.allCommentsUserLevel()
                first_comment_content = all_comments_Page.allCommentsContent()
                first_comment_time = all_comments_Page.allCommentsTime()
                check_result = first_comment_user_head.is_displayed() and \
                               first_comment_user_name.is_displayed() and \
                               first_comment_user_level.is_displayed() and \
                               first_comment_content.is_displayed() and \
                               first_comment_time.is_displayed()
                self.assertIs(check_result, True)

                logger.info('书详页全部评论脚本执行成功！用例通过')

            except AssertionError as e:
                logger.debug('书详页全部评论脚本执行失败！用例通过')

                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e

    def test_book_messages(self):
        logger.info("开始执行书详页图书信息脚本...")

        pc = ParseConfigFile()

        try:

            ebookid='30331055'

            testBookDetailNotNeedLogin.browser.get(pc.getUrl('bookdetail') % (ebookid))

            logger.info('启动浏览器，访问"书籍详情"页面...')
            bookDetailPage = BookDetailPage(testBookDetailNotNeedLogin.browser)

            api_book_message={}.fromkeys(['file_size','isbn','publish_time','word_count','format','edition'])
            api_book_message['file_size']=str(BookDetai.getData(ebookid)['file_size'])+'M'
            api_book_message['isbn']=BookDetai.getData(ebookid)['isbn']
            api_book_message['publish_time']=BookDetai.getData(ebookid)['publish_time']
            api_book_message['word_count']=str(round(BookDetai.getData(ebookid)['word_count']/10000,1))+'万'
            api_book_message['format']=BookDetai.getData(ebookid)['format']
            api_book_message['edition']=str(BookDetai.getData(ebookid)['edition'])

            book_Message_Title=bookDetailPage.bookMessageTitle()
            testBookDetailNotNeedLogin.browser.execute_script("arguments[0].scrollIntoView();", book_Message_Title)
            book_File_Size_Label=bookDetailPage.bookFileSizeLabel()
            book_File_Size_Obj=bookDetailPage.bookFileSizeObj()
            book_File_Type_Label=bookDetailPage.bookFileTypeLabel()
            book_File_Type_Obj=bookDetailPage.bookFileTypeObj()
            book_ISBN_Code_Label=bookDetailPage.bookISBNCodeLabel()
            book_ISBN_Code_Obj=bookDetailPage.bookISBNCodeObj()
            book_Chars_Num_Label=bookDetailPage.bookCharsNumLabel()
            book_Chars_Num_Obj=bookDetailPage.bookCharsNumObj()
            book_Public_Time_Label=bookDetailPage.bookPublicTimeLabel()
            book_Public_Time_Obj=bookDetailPage.bookPublicTimeObj()
            book_Public_Times_Label=bookDetailPage.bookPublicTimesLabel()
            book_Public_Times_Obj=bookDetailPage.bookPublicTimesObj()


            try:

                self.assertIs(book_Message_Title.is_displayed(), True)
                self.assertIs(book_File_Size_Label.is_displayed(), True)
                self.assertIs(book_File_Type_Label.is_displayed(), True)
                self.assertIs(book_ISBN_Code_Label.is_displayed(), True)
                self.assertIs(book_Chars_Num_Label.is_displayed(), True)
                self.assertIs(book_Public_Time_Label.is_displayed(), True)
                self.assertIs(book_Public_Times_Label.is_displayed(), True)
                self.assertIs(api_book_message['file_size'] in book_File_Size_Obj.text, True)
                self.assertIs(api_book_message['isbn'] in book_ISBN_Code_Obj.text, True)
                self.assertIs(api_book_message['publish_time'] in book_Public_Time_Obj.text, True)
                self.assertIs(api_book_message['word_count'] in book_Chars_Num_Obj.text, True)
                self.assertIs(api_book_message['format'] in book_File_Type_Obj.text, True)
                self.assertIs(api_book_message['edition'] in book_Public_Times_Obj.text+'未知', True)

                logger.info('书详页相关图书推荐脚本执行成功！用例通过')

            except AssertionError as e:
                logger.debug('书详页相关图书推荐脚本执行失败！用例通过')

                raise e

        except ElementNotVisibleException as e:

            logger.error("数据问题，元素没有找到..")

        except NoSuchElementException as e:

            logger.error("数据问题..重试")

        except Exception as e:

            logger.error(e)

            raise e


if __name__=="__main__":
    # unittest.main()

    #通过多个测试集合组成一个测试套
    testsuit =  unittest.TestSuite()
    testsuit.addTest(testBookDetailNotNeedLogin("test_price_free_book"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



