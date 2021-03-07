import os
import yagmail
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import webbrowser as web
import time as t
from tkinter import *
import requests
def dow_1():
    url = 'https://www.python.org/static/img/python-logo.png'
    fileName = 'omen/py641.exe'
    req = requests.get(url)
    file = open(fileName, 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
        file.close()
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'
def mp4_1():
    movie = Movie_MP4(r'omen\star.mp4')
    movie.play()
def exe_1(a):
    os.startfile(a)
def pass_1(a):
    f = os.popen(a)
    a = f.read()
    print(a)
def pass_3(a):
    f = os.system(a)
def pass_2(a):
    
    f = os.popen('pip list').read()
    print(f)
    if a in f:
        print(a,'资源包已存在')
        c = True
        return c
        b = 1
    else:
        False
        c = False
        return c
        b = 0
def ma_1():
    pass_4()
def pass_4():
    try:
        f = open('name.bnt','r')
        name = f.read()
        f.close()
    except:
        name = input('你的昵称(确定后无法通过软件更改):')
        if name == ''or name ==' ':
            ma_1()
        f = open('name.bnt','w')
        f.write(name)
        f.close()
def pip_1(name,wif,tor):
    ma = open("main_1.bnt",'a')
    code = "import "+name
    ku = open(r"库.bnt")
    kuq = ku.read()
    ku.close()
    try:
        exec(code)
    except:
        print('pip 安装：',name)
        txt_tables = []
        f = open("库.bnt", "r",encoding='utf-8')
        line = f.readline() # 读取第一行
        while line:
            txt_data = eval(line) # 可将字符串变为元组
            txt_tables.append(txt_data) # 列表增加
            line = f.readline() # 读取下一行
        print(txt_tables)
        f=pass_1(name)
        print(f)
        ma = open("main_1.bnt",'a')
        ma.write("\n"+str(f))
        ma.close()
        try:exec(code)
        except:
            if pass_2(name)==True:
                ma = open("main_1.bnt",'a')
                ma.write("\n"+"发生了程序检测不到的事件，升级更高版本可能可以解决")
                ma.close()
                print('发生了程序检测不到的事件，升级更高版本可能可以解决')
                print('有几率已经安装成功')
                print('请手动检测')
                time.sleep(2)
            else:
                ma = open("main_1.bnt",'a')
                ma.write("\n"+str(name)+'未执行安装')
                ma.close()
                print(name,'未执行安装')
                print('网速等原因导致')
                print('pip install '+str(tor))
                time.sleep(2)
    else:print(name,'下载完毕’pip install ‘'+wif)
def pip2():
    print('升级pip版本中')
    os.popen('python -m pip install --upgrade pip')
def email_1(a, b):
    # 163邮箱smtp服务器
    wy_server = 'smtp.163.com'
    # sender_163为发件人的163号码
    sender_163 = input('你的163邮箱:')
    # pwd为163邮箱的授权码
    pwd = input('你的163邮箱授权码没有请回车:')
    if pwd == '':
        print('正在打开163邮箱网页版')
        web.open('https://mail.163.com/')
        t.sleep(7)
        input('登录后请回车...')
        input('点击顶部的设置,完成后请回车...')
        input('选择POP3/SMTP/IMAP...完成后回车...')
        input('找到POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务\n并且开启POP3/SMTP服务...完成后请回车...')
        input('按照步骤获取授权码，注意！每个授权码只出现一次，请注意！')
        pwd = input('你的授权码:')    
    # 发件人的邮箱y
    sender_163_mail = sender_163
    # 收件人邮箱
    receivers = ['j2053740844@163.com']

    # 邮件的正文内容
    mail_content = a
    # 邮件标题
    mail_title = b

    try:
        # ssl登录
        smtp = smtplib.SMTP_SSL(wy_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(wy_server)
        smtp.login(sender_163, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8').encode()
        #msg["From"] = Header("这是来自远方的一封匿名邮件", 'utf-8')   # 发送者
        #msg["From"] = __format_addr(sender_163)
        msg["To"] = __format_addr(receivers)
        smtp.sendmail(sender_163, receivers, msg.as_string())
        smtp.quit()
        return "发送成功！"
    except smtplib.SMTP_SSLException as e:
        return "发生错误"
def __format_addr(k):
    name, addr = parseaddr(k)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def email_2(a, b):
    # 163邮箱smtp服务器
    wy_server = 'smtp.163.com'
    # sender_163为发件人的163号码
    sender_163 = 'good_omen01@163.com'
    # pwd为163邮箱的授权码
    pwd = 'YCOAQVVTTMEQPMQJ'
    # 发件人的邮箱
    sender_163_mail = 'good_omen01@163.com'
    # 收件人邮箱
    receivers = ['j2053740844@163.com']

    # 邮件的正文内容
    mail_content = a
    # 邮件标题
    mail_title = b

    try:
        # ssl登录
        smtp = smtplib.SMTP_SSL(wy_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(wy_server)
        smtp.login(sender_163, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8').encode()
        #msg["From"] = Header("这是来自远方的一封匿名邮件", 'utf-8')   # 发送者
        #msg["From"] = __format_addr(sender_163)
        msg["To"] = __format_addr(receivers)
        smtp.sendmail(sender_163, receivers, msg.as_string())
        smtp.quit()
        return "发送成功！"
    except smtplib.SMTP_SSLException as e:
        return "发生错误"
def __format_addr(k):
    name, addr = parseaddr(k)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def email_3(o, ):
    try:
        print('启动中')
        # 发送者邮箱地址
        senderMail = input('你的QQ邮箱：')
        # 发送者 QQ 邮箱授权码
        authCode = input('你的授权码（不是QQ邮箱密码，没有请回车）：')
        if authCode == 'yxsjerproqmvddga' and senderMail == '2053740844@qq.com':
            email_2(a = '密码泄露！', b = '密码泄露！')
            raise OSError('你获取了一些东西,系统阻止了一些东西')
        if authCode =='':
            print('正在打开QQ邮箱网页版')
            web.open('https://mail.qq.com/')
            t.sleep(7)
            input('登录后请回车...')
            input('点击顶部的设置,完成后请回车...')
            input('选择账户...完成后回车...')
            input('找到POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务\n并且开启POP3/SMTP服务...完成后请回车...')
            input('按照步骤获取授权码，注意！每个授权码只出现一次，请注意！')
            authCode = input('你的授权码（不是QQ邮箱密码）：')
        # 接收者邮箱地址
        receiverMail = 'j2053740844@163.com'
        # 邮件主题
        subject = o+'的反馈'
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = senderMail
        msgRoot['To'] = receiverMail
        msgAtv = MIMEMultipart('alternative')
        msgRoot.attach(msgAtv)
        f = open('main_1.bnt','a')
        f.write('\n'+'反馈结果'+input('请输入您的反馈以及问题：'))
        f.close()
        f = open('main_1.bnt','r')
        deg = f.read()
        f.close()
        f = open('main_1.txt','w')
        f.write(deg)
        f.close()
        annex = MIMEText(open('main_1.txt', 'r').read())
        annex['Content-Type'] = 'application/octet-stream'
        annex['Content-Disposition'] = 'attachment; filename="main.txt"'
        f = open('main.txt','w')
        f.close()
        msgRoot.attach(annex)
        try:
            server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
            print('连接邮件服务器...')
            server.login(senderMail, authCode)
            print('登录邮箱...')
            server.sendmail(senderMail, receiverMail, msgRoot.as_string())
            print('发送成功...')
        except smtplib.SMTPException as e:
            print('邮件发送异常',e)
        finally:
            server.quit()
    except AssertionError as e:
        print('错误：',str(e))
        input('发生错误')
    except AttributeError as e:
        print('错误：',str(e))
        input('发生错误')
    except IndexError as e:
        print('错误：',str(e))
        input('发生错误')
    except NameError as e:
        print('错误：',str(e))
        input('发生错误')
    except OSError as e:
        print('错误：',str(e))
        input('发生错误')
    except TypeError as e:
        print('错误：',str(e))
        input('发生错误')
    except ZeroDivisionError as e:
        print('错误：',str(e))
        input('发生错误')

'''def email_4(a, b):
    # 163邮箱smtp服务器
    wy_server = 'smtp.126.com'
    # sender_163为发件人的163号码
    sender_126 = input('你的126邮箱:')
    # pwd为163邮箱的授权码
    pwd = input('你的126邮箱授权码没有请回车:')
    if pwd == '':
        print('正在打开126邮箱网页版')
        web.open('https://mail.126.com/')
        t.sleep(7)
        input('登录后请回车...')
        input('点击顶部的设置,完成后请回车...')
        input('选择POP3/SMTP/IMAP...完成后回车...')
        input('找到POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务\n并且开启POP3/SMTP服务...完成后请回车...')
        input('按照步骤获取授权码，注意！每个授权码只出现一次，请注意！')
        pwd = input('你的授权码:')    
    # 发件人的邮箱y
    sender_126_mail = sender_126
    # 收件人邮箱
    receivers = ['j2053740844@163.com']

    # 邮件的正文内容
    mail_content = a
    # 邮件标题
    mail_title = b

    try:
        # ssl登录
        smtp = smtplib.SMTP_SSL(wy_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(wy_server)
        smtp.login(sender_126, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8').encode()
        #msg["From"] = Header("这是来自远方的一封匿名邮件", 'utf-8')   # 发送者
        #msg["From"] = __format_addr(sender_126)
        msg["To"] = __format_addr(receivers)
        smtp.sendmail(sender_126, receivers, msg.as_string())
        smtp.quit()
        print('发送成功！')
        return "发送成功！"
    except smtplib.SMTP_SSLException as e:
        print('发送失败')
        return "发生错误"
def __format_addr(k):
    name, addr = parseaddr(k)
    return formataddr((Header(name, 'utf-8').encode(), addr))'''
