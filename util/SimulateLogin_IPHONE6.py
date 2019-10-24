#coding=utf-8
from selenium import webdriver
import time
from PIL import Image
import cv2
import aircv as ac
from selenium.webdriver.common.action_chains import ActionChains
from util.Log import *

# 该方法作用是：在图img中，pos的位置画一个半径为circle_radius的圆，颜色为color，笔粗为line_width
def draw_circle(img, pos, circle_radius, color, line_width):
    result_img = cv2.circle(img, pos, circle_radius, color, line_width)
    # 这三行代码可以让result_img图片展示在屏幕上，按任意键结束展示
    # cv2.imshow('objDetect', result_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return result_img

def get_position(browser):
    # 截取带验证码的登录页面，保存为im.png（本文的目标网站的登录验证码方式是在大图中点击目标小图）

    browser.save_screenshot(r'../img/im.png')

    # 用PIL库操作图片
    im = Image.open(r'../img/im.png')
    # 灰度化，保存为im_grey.png
    im_grey = im.convert('L')
    im_grey.save(r'../img/im_grey.png')
    # 在im.png图中截取目标小图（验证码图片）：im_crop.png
    # 不同大小的显示器可能不同，需要自己手动算一下，计算方法就是在画图工具中看下验证码图片左上角坐标和右下角坐标。可能需要多次试验才能准确截取
    im_crop = im.crop((526, 880, 578, 927))
    im_crop.save(r'../img/im_crop.png')
    im_crop_grey = im_crop.convert('L')  # 灰度化
    im_crop_grey.save(r'../img/im_crop_grey.png')

    # 以上是准备要用到图片，下面是找出验证码在网页中的坐标，并模拟点击，以通过验证码校验

    # 以下步骤是：在im_grey.png图中的场景图片中找出im_crop_grey.png图一样的图案（这里注意，是在im_grey.png中上半部分场景中去找），并画一个圈
    # 1.因为im_grey.png图的场景图片中目标图案比较大，所以要缩小im_grey.png图，保存为result.png，缩小的倍数需要手工计算一下（多试几组值，观察
    #   缩小后的result.png中的目标图是否与im_crop.png长和宽相差不大即可）
    # 2.找出目标图im_crop_grey.png在result.png的位置，并画一个圈,保存为result_img1.png
    # 3.按比例计算目标图im_crop.png在im_grey原始图中的位置，并画一个圈

    # 下面是步骤1、2
    # 我的im_grey.png原始大小是750*1334，计算后需要缩小1.22倍
    res = cv2.resize(cv2.imread(r'../img/im_grey.png'), (615, 1094), interpolation=cv2.INTER_CUBIC)  # 该方法可缩放图片

    cv2.imwrite(r'../img/result.png', res)  # 保存缩小后的图片

    imsrc = ac.imread(r'../img/result.png')
    imobj = ac.imread(r'../img/im_crop_grey.png')

    # find the match position
    try:
        pos = ac.find_template(imsrc, imobj)  # 该方法很厉害，能够找到jmobj在imsrc中的坐标位置。如果找不到返回None
        circle_center_pos = (int(pos['result'][0]), int(pos['result'][1]))
    except TypeError as e:
        print('没有定位到，请重试！')

    # 定义一些花圈的参数
    circle_radius = 25
    color = (0, 255, 0)
    line_width = 3

    # 为方便调试打印下坐标
    #print(circle_center_pos)
    # 画圈，并保存画圈后的图片
    result_img1 = draw_circle(imsrc, circle_center_pos, circle_radius, color, line_width)
    cv2.imwrite(r'../img/result_img1.png', result_img1)

    # 下面是步骤3：
    # 以上计算的坐标是在缩小1。43倍以后的图片上，想要计算计算在原始图中的坐标需要把坐标*1.22
    real_pos = (int(pos['result'][0] * 1.22), int(pos['result'][1] * 1.22))
    #print(real_pos)
    result_img2 = draw_circle(ac.imread(r'../img/im_grey.png'), real_pos, circle_radius, color, line_width)
    cv2.imwrite(r'../img/result_img2.png', result_img2)
    return real_pos

def verify_code(browser):

    flag=True
    while flag:
        #获得点击的坐标
        #// *[ @ id = "captcha"] / div[1] / div / img

        real_pos=get_position(browser)
        #im.png大小是750*1334，浏览器最大化的大小是375*667，刚好截图大小是网页中html大小的两倍，所以坐标需要除以2
        ##但是由于浏览器最大化，im.png的分辨率太大，导致定位稍微不准确就不能定位，需要优化，失败后可多次重试定位
        x=int(real_pos[0]/2)
        y=int(real_pos[1]/2)
        #如果点击范围不在弹出的验证码弹框范围内，则进行刷新，重新定位
        if not (x>44 and x<333 and y>236 and y<417) :
            time.sleep(1)
            browser.find_element_by_xpath('// *[ @ id = "captcha"] / div[1] / div').click()
            logger.info('x=%s和y=%s不在范围内容'%(str(x),str(y)))

            continue
        else:
            flag=False
            menu = browser.find_element_by_xpath("/html")
            actions = ActionChains(browser)
            logger.info('在浏览器中点击位置：' + str(x) + ',' + str(y))
            actions.move_to_element_with_offset(menu, x, y)  # 把坐标挪到定位好的坐标上

            # 点击定位好的坐标
            actions.click()
            try:
                actions.perform()
            except Exception as e:
                logger.error(e)


# 如果成功（//*[@id="captcha_dom"]这个元素的style="display: none;"），则结束
# 否则失败，就重试
def simulator_login(browser):

    #本模块测试需要打开这个while
    while (1):
        verify_code(browser)
        try:
    #这个条件不同情况下调用需要修改
            element = browser.find_element_by_xpath('//*[@id="captcha"]/div[1]')
        except Exception as e:
            logger.info("登录成功！")
            return
    # while(1):
    #     verify_code(browser)
    #     try:
    #         #这个条件不同情况下调用需要修改
    #         element = browser.find_element_by_xpath('//*[text()="退出登录"]')
    #         #print(type(element))
    #     except Exception as e:
    #         print("验证失败！")
    #     else:
    #         print("验证成功！")
    #         return
if __name__=="__main__":
    # 访问要自动登录的网站的登录页面
    # 设置浏览器为iphone模式打开
    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=options)

    browser.get("https://plogin.m.jd.com/user/login.action")
    browser.find_element_by_xpath('//input[@id="username"]').send_keys("你的用户名")
    browser.find_element_by_xpath('//input[@id="password"]').send_keys("liujinhong1995")
    browser.find_element_by_xpath('//a[@id="loginBtn"]').click()
    time.sleep(3)
    simulator_login(browser)
    browser.quit()
#browser.close()

