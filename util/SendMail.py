#!/usr/bin/python3
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

my_sender = 'xxxxx@qq.com'  # 发件人邮箱账号
my_pass = 'xxxxxxxxxxxx'  # qq邮箱的授权码（登陆qq邮箱，在设置-账户里进行设置）


def text_mail(subject,content):
    my_user = 'xxxxxxxxxx@jd.com'  # 收件人邮箱账号，我这边发送给自己

    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["ZYQ", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["ZYQ", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print(e)
    return ret


def file_mail(subject,content,file_path):
    receivers = ['xxxxxxxxxx@jd.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    # message['From'] = Header('zyq',charset='utf-8')
    # message['To'] = Header('zyq',charset='utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(content, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.html"'
    message.attach(att1)


    try:

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def html_mail(subject,html):

    receivers = ['xxxxxxxxxx@jd.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25

    # 读取html文件内容
    f = open(html, 'rb')
    mail_body = f.read()
    f.close()

    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail('xxxxxxxxxx@qq.com', receivers, message.as_string())
        print("发送邮件成功！！！")
        server.quit()
    except smtplib.SMTPException:

        print("发送邮件失败！！！")
    except Exception as e:
        print("error")

if __name__=="__main__":
    # ret = text_mail("m站测试","来自m站自动化的文本邮件")
    # if ret:
    #     print("邮件发送成功")
    # else:
    #     print("邮件发送失败")
    html_mail("m站自动化测试发来的",r'../test.html')