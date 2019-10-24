#coding=utf-8
from selenium import webdriver
options=webdriver.ChromeOptions()
def set_phone_model(phone_model):
    def __deco(func):
        def _deco(self,*arg, **kw):
            mobile_emulation = {'deviceName': phone_model}
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            func(self,*arg, **kw)
            return options
        return _deco
    return __deco




