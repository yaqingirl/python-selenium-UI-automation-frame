from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.parseCF=ParseConfigFile()
        self.loginOptions=self.parseCF.getItemsSection('login')


    def userNameObj(self):
        try:
            locateType,locateExpression = self.loginOptions['loginPage.username'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element


    def passwordObj(self):
        try:
            locateType,locateExpression = self.loginOptions['loginPage.password'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def loginButton(self):
        try:
            locateType,locateExpression = self.loginOptions['loginPage.loginButton'.lower()].split('>')
            element = getElement(self.driver,locateType,locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element



if __name__=="__main__":
    from selenium import webdriver
    import time
    from util.SimulateLogin_galaxyS5 import simulator_login

    # 设置浏览器为iphone模式打开
    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)

    browser.get("https://plogin.m.jd.com/user/login.action")

    login=LoginPage(browser)
    time.sleep(2)
    login.userNameObj().send_keys("你的用户名")
    login.passwordObj().send_keys("你的密码")
    login.loginButton().click()
    time.sleep(3)
    simulator_login(browser)
    # get the session cookie  
    cookie = [item["name"]+"="+item["value"] for item in browser.get_cookies()]

    # print cookie  
    cookiestr = ';'.join(cookie)
    print(cookiestr)
    browser.quit()