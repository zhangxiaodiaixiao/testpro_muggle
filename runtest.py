from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import threading



def send_mail(file_new):
	f=open(file_new,'rb')   
	mail_body=f.read()
	f.close()

	msg=MIMEText(mail_body,'html','utf-8')
	msg['Subject']=Header('自动化测试报告','utf-8')
	smtp=smtplib.SMTP()
	smtp.connect('smtp.qq.com')
	smtp.login('1172533210@qq.com','xbpyjhmfbmysgjgh')
	smtp.sendmail('1172533210@qq.com','1172533210@qq.com',msg.as_string())
	smtp.quit()
	print('email has send out!')


def new_report(testreport):
	lists=os.listdir(testreport)
	lists.sort(key=lambda fn:os.path.getmtime(testreport+'\\'+fn))
	file_new=os.path.join(testreport,lists[-1])
	print(file_new)
	return file_new

if __name__ == '__main__':
	test_dir='C:\\Users\\ZMD\\Desktop\\mztestpro\\bbs\\test_case'
	test_report='C:\\Users\\ZMD\\Desktop\\mztestpro\\bbs\\report'

	discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
	now_time=time.strftime("%Y-%m-%d %H-%M-%S")
	file_name=test_report+'/report/'+now_time+'result.html'
	fp=open(file_name,'wb')
	runnner=HTMLTestRunner(stream=fp,title='后台管理测试报告',description='用例执行情况：')
	runnner.run(discover)
	fp.close()
	new_report=new_report(test_report)
	send_mail(new_report)