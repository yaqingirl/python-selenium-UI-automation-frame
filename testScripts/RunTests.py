#coding=utf-8
import unittest
from util import HTMLTestRunner
from util.SendMail import html_mail

if __name__=="__main__":
    # 加载当前目录下所有有效的测试模块(以test开头的py文件),“.”表示当前目录
    testSuite = unittest.TestLoader().discover('.')
    filename = "../test.html"  # 定义个报告存放路径，支持相对路径。
    # 以二进制方式打开文件，准备写
    fp = open(filename, 'wb')
    # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述，均可以配
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告', description='京东阅读M站自动化测试报告')
    # 运行测试集合
    runner.run(testSuite)
    fp.close()
    html_mail("M站自动化测试",r'../test.html')