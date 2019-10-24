#coding=utf-8
import json
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from appModules.LoginAction import LoginAction
from pageObjects.BookCityPage import BookCityPage
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
    browser = ''

    @set_phone_model(phone_model)
    def setUp(self) -> None:
        TestRead.browser = webdriver.Chrome(chrome_options=options)

        logger.info("开始登陆...")
        TestRead.browser.get("https://plogin.m.jd.com/user/login.action")
        TestRead.login_cookie=LoginAction.login('你的用户名', "你的密码", TestRead.browser)

    def tearDown(self) -> None:
        pass

    def test_P(self):
        logger.info("开始执行唤起菜单脚本...")
        #获取是否执行列

        TestRead.browser.get('https://jdread.jd.com/h5/m')

        bcp=BookCityPage(TestRead.browser)
        bcp.toolButtonObj().click()

        time.sleep(2)





if __name__=="__main__":
    # unittest.main()

    #通过多个测试集合组成一个测试套
    testsuit =  unittest.TestSuite()
    testsuit.addTest(TestRead("test_Buy_In_Read_Page"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)



