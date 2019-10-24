#coding=utf-8
import os
#获取当前文件所在目录的父目录的绝对路径
parentDirPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath=parentDirPath+r"/config/PageElementLocator.ini"
#获取数据文件存放的绝对路径
dataFilePath=parentDirPath+r"/testData/测试数据.xlsx"

#测试数据.xlsx中登陆账号tab每列对应的数字序号
acount_username=2
acount_password=3
acount_isExecute=4
acount_type=5
acount_comment=6
acount_pin=7
execute_testResult=8
execute_time=9

#测试数据.xlsx中搜索书籍tab每列对应的数字序号
book_name=2
book_id=3
book_author=4
book_isExecute=5
book_type=6
acount_comment=7
execute_testResult=8
execute_time=9

#测试书籍.xlsx中购买书籍tab每列对应的数字序号
book_name=2
book_id=3
book_author=4
book_isExecute=5
book_type=6
acount_comment=7
buyer_pin=8
buyer_username=9
buyer_password=10
execute_testResult=11
execute_time=12

#测试书籍.xlsx中价格逻辑验证书籍tab每列对应的数字序号
book_name=2
book_id=3
book_author=4
book_isExecute=5
book_type=6
execute_testResult=8
execute_time=9

#测试书籍.xlsx中VIP逻辑验证书籍tab每列对应的数字序号
book_name=2
book_id=3
book_author=4
book_isExecute=5
book_type=6
acount_username_check_vip=7
acount_password_check_vip=8
execute_testResult=10
execute_time=11

#测试书籍.xlsx中基本信息验证书籍tab每列对应的数字序号
book_name=2
book_id=3
book_author=4
book_publish=5
book_isExecute_book_detail=6
execute_testResult_book_detail=9
execute_time_book_detail=10

if __name__=="__main__":
    print(pageElementLocatorPath)
    print(dataFilePath)