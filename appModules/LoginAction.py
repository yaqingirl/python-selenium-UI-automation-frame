#coding=utf-8
from pageObjects.LoginPage import LoginPage
from util.SimulateLogin_galaxyS5 import *
from util.Log import *

class LoginAction:
    def __init__(self):
        logger.info("login..")

    @staticmethod
    def login(username,password,browser,source_url=None):
        '''
        登陆，并返回cookie且跳转到source_url
        :param username:
        :param password:
        :param browser:
        :param source_url:
        :return:登陆cookie
        '''
        try:

            # browser.get("https://plogin.m.jd.com/user/login.action")
            page = LoginPage(browser)
            page.userNameObj().send_keys(username)
            page.passwordObj().send_keys(password)
            page.loginButton().click()
            time.sleep(3)

            while (1):
                verify_code(browser)
                try:
                    # 这个条件不同情况下调用需要修改
                    time.sleep(3)
                    element = browser.find_element_by_xpath('// *[ @ class = "jcap_refresh"]')
                except Exception as e:
                    logger.info("登录成功！")
                    # get the session cookie  
                    # cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
                    # print cookie  
                    # cookiestr = ';'.join(cookie)
                    time.sleep(2)
                    cookie=browser.get_cookie('pt_key')
                    cookie.pop('expiry')
                    if source_url:
                        browser.get(source_url)
                    return cookie


        except Exception as e:
            logger.error(e)
            raise e
if __name__=="__main__":
    from selenium import webdriver
    import time

    # 设置浏览器为iphone模式打开
    mobile_emulation = {'deviceName': 'Galaxy S5'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://plogin.m.jd.com/user/login.action")
    #browser.get("http://test-jdread.jd.com/h5/m/p_my_details")
    cookie=LoginAction.login('你的用户名','你的密码',browser,"http://jdread.jd.com/h5/m/p_my_details")
    # print(cookie)
    for key,value in cookie.items():
        print(key,value)
    browser.quit()