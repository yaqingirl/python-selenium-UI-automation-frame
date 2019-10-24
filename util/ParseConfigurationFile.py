from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath
from config.server_info import *

class ParseConfigFile:
    def __init__(self):
        self.cf=ConfigParser()
        self.cf.read(pageElementLocatorPath)

    #items方法获取的结果里把字符都转成小写了
    def getItemsSection(self,sectionName):
        optionsDict=self.cf.items(sectionName)
        return dict(optionsDict)

    def getOptionValue(self,sectionName,optionName):
        value=self.cf.get(sectionName,optionName)
        return dict(value)

    def getUrl(self,key):
        return eval(key)

if __name__=="__main__":
    pc=ParseConfigFile()
    print(pc.getItemsSection('login'))
    # print(pc.getOptionValue('login','loginPage.username'))
    print(pc.getUrl('search'))
