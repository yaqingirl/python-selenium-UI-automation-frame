#coding=utf-8
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pageObjects.SearchBookPage import SearchBookPage
from util.decorator.PhoneModelDecorator import set_phone_model,options
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *

class TestSearch(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @set_phone_model('Galaxy S5')
    def test_Search_By_Name(self):
        logger.info("开始执行搜索脚本...")
        #获取是否执行列
        isExecuteUser=TestSearch.excelObj.get_col_values(book_isExecute,sheet_name='搜索书籍')
        pc = ParseConfigFile()
        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                bookname=TestSearch.excelObj.get_cell_value(idx+2,book_name)
                logger.info("执行测试数据：%s"%(bookname))
                try:
                    browser = webdriver.Chrome(chrome_options=options)
                    browser.get(pc.getUrl('search'))
                    logger.info('启动浏览器，访问"搜索"页面...')

                    searchbookPage = SearchBookPage(browser)
                    logger.info('触发搜索...')
                    searchbookPage.SearchInputBoxObj().send_keys(bookname)
                    searchbookPage.SearchInputBoxObj().send_keys(Keys.ENTER)  # 通过回车键来代替鼠标的左键

                    try:
                        name=searchbookPage.SearchResultFirstBookName().text
                        # 搜索结果中第一本书的名字和输入的书名相等
                        self.assertIs(name==bookname,True)
                        logger.info('通过书名搜索用例通过')
                        TestSearch.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        TestSearch.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except Exception as e:
                        logger.debug('通过书名搜索用例不通过')
                        TestSearch.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        TestSearch.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
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

    @set_phone_model('Galaxy S5')
    def test_Search_By_Author(self):
        logger.info("开始执行搜索脚本...")
        #获取是否执行列
        isExecuteUser=TestSearch.excelObj.get_col_values(book_isExecute,sheet_name='搜索书籍')
        pc = ParseConfigFile()
        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                bookauthor=TestSearch.excelObj.get_cell_value(idx+2,book_author)
                logger.info("执行测试数据：%s"%(bookauthor))
                try:

                    browser = webdriver.Chrome(chrome_options=options)
                    browser.get(pc.getUrl('search'))
                    logger.info('启动浏览器，访问"搜索"页面...')
                    searchbookPage = SearchBookPage(browser)
                    logger.info('触发搜索...')
                    searchbookPage.SearchInputBoxObj().send_keys(bookauthor)
                    searchbookPage.SearchInputBoxObj().send_keys(Keys.ENTER)  # 通过回车键来代替鼠标的左键

                    try:
                        author=searchbookPage.SearchResultFirstBookAuthor().text
                        # 搜索结果中第一本书的作者和输入的人名相等
                        self.assertTrue(author==bookauthor)
                        logger.info('通过作者搜索用例通过')
                        TestSearch.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        TestSearch.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')

                    except AssertionError as e:
                        logger.debug('通过作者搜索用例不通过')
                        TestSearch.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        TestSearch.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
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
    unittest.main()
    #通过多个测试集合组成一个测试套
    testsuit =  unittest.TestSuite()
    testsuit.addTest(TestSearch("test_Search_By_Author","test_Search_By_Name"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)





