from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getElement(driver,locateType,locateExpression):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locateExpression))
        return element
    except Exception as e:
        print(e)
        raise e

def getVisibilityElement(driver,locateType,locateExpression):
    '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0,如果满足条件就返回这个元素'''
    try:
        element=WebDriverWait(driver,30).until(EC.visibility_of_element_located((locateType,locateExpression)))

        return element
    except Exception as e:
        print(e)
        raise e

def getElements(driver,locateType,locateExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType,value=locateExpression))
        return elements
    except Exception as e:
        print(e)
        raise e



if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    #driver.find_element("id","kw").send_keys("selenium")
    searchBox=getElement(driver,"id","kw")
    print(searchBox.tag_name)
    print(searchBox.is_displayed())
    # elements = getElements(driver,"tag name","a")
    # print(len(elements))
    driver.quit()
