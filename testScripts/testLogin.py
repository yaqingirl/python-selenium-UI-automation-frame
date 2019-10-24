#coding=utf-8
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

from appModules.LoginAction import LoginAction
from pageObjects.BookCityPage import BookCityPage
from pageObjects.MinePage import MinePage
from util.ObjectMap import getElement
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
from config.server_info import *
from util.decorator.PhoneModelDecorator import set_phone_model,options


class TestLogin(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @set_phone_model(phone_model)
    def test_Login(self):
        logger.info("开始执行登录脚本...")
        #获取是否执行列
        isExecuteUser=TestLogin.excelObj.get_col_values(acount_isExecute)
        for idx,i in enumerate(isExecuteUser[1:]):
            start_time=time.time()
            if i=='Y':
                username=TestLogin.excelObj.get_cell_value(idx + 2, acount_username)
                password=TestLogin.excelObj.get_cell_value(idx + 2, acount_password)
                usertype=TestLogin.excelObj.get_cell_value(idx+2,acount_type)
                logger.info("执行测试数据：%s,%s,%s"%(username,password,usertype))
                try:

                    browser = webdriver.Chrome(chrome_options=options)

                    browser.get(minepage)
                    logger.info('启动浏览器，访问"我的"页面...')
                    minePage = MinePage(browser)
                    minePage.LoginEntryButton().click()
                    logger.info('点击"我的"页面的登录按钮...')
                    LoginAction.login(username, password, browser)
                    logger.info('登录操作执行...')

                    try:
                        #minePage.ExitButtonObj()  # 如果在"我的"页面找到退出按钮，则通过测试用例，如果没找到该按钮则测试用例未通过
                        browser.implicitly_wait(5)
                        self.assertIs(minePage.ExitButtonObj().is_displayed(),True)
                        logger.info('在"我的"页面找【退出】按钮')
                    except Exception as e:
                        # self.assertTrue(1 == 2)

                        logger.debug('在"我的"页面找到【退出】按钮，失败，用例不通过')
                        TestLogin.excelObj.write_cell_value(idx+2,execute_testResult,'fail','red')
                        TestLogin.excelObj.write_cell_value(idx + 2, execute_time,str(time.time()-start_time)+'ms', 'red')
                        raise e

                    else:
                        logger.info('在"我的"页面找到【退出】按钮，成功,用例通过')
                        TestLogin.excelObj.write_cell_value(idx + 2, execute_testResult, 'success', 'green')
                        TestLogin.excelObj.write_cell_value(idx + 2, execute_time, str(round((time.time() - start_time)/1000,2)) + 's')


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
    def test_Login_Button(self):
        logger.info("开始执行登陆按钮脚本...")
        pc = ParseConfigFile()

        try:

            browser = webdriver.Chrome(chrome_options=options)

            browser.get(pc.getUrl('bookcity'))

            logger.info('启动浏览器，访问"书城"页面...')
            bookcityPage = BookCityPage(browser)
            time.sleep(3)

            # bookcityPage.loginButton().click()
            login_button=bookcityPage.loginButton()
            browser.execute_script("arguments[0].click();",login_button)

            jd_login_button = getElement(browser, 'xpath', '// a[. = "登 录"]')
            try:

                self.assertIs(jd_login_button.is_displayed(), True)
                logger.info('书城登陆按钮点击成功！用例通过')

            except AssertionError as e:
                logger.debug('书城登陆按钮点击失败！用例不通过')
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
    testsuit.addTest(TestLogin("test_Login"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



