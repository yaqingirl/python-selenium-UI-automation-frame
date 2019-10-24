#coding=utf-8
import time

def AIclick(element):
    for i in range(15):  # 循环60次，从0至59
        if i >= 14:  # 当i大于等于59时，打印提示时间超时
            print("timeout")
            break
        try:  # try代码块中出现找不到特定元素的异常会执行except中的代码
            element.click()
        except:  # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
            print("wait for find element")
        else:
            break
        time.sleep(1)