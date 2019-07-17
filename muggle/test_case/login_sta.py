from time import sleep
import unittest,random,sys
sys.path.append('./models')
sys.path.append('./page_obj')

from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.Mytest):
	'''用户登录模块'''
	
	def user_login_verify(self,username='',password=''):
		login(self.driver).user_login(username,password)
	def test_login1(self):
		'''用户名&密码为空'''
		self.user_login_verify()
		po=login(self.driver)
		self.assertEqual(po.user_error_hint(),'username is required')
		function.insert_img(self.driver,'username_null.png')
	def test_login2(self):
		'''密码为空'''
		self.user_login_verify(username="test",password="")
		po=login(self.driver)
		self.assertEqual(po.pwd_error_hint(),'密码不能小于5位')
		function.insert_img(self.driver,'password_null.png')
	def test_login3(self):
		'''用户名错误'''
		self.user_login_verify(username="test1",password="qq123456")
		po=login(self.driver)
		function.insert_img(self.driver,'username_error.png')
	def test_login4(self):
		'''密码少于5位'''
		self.user_login_verify(username="test",password="qq12")
		po=login(self.driver)
		self.assertEqual(po.pwd_error_hint(),'密码不能小于5位')
		function.insert_img(self.driver,'password_less_five.png')
	def test_login5(self):
		'''密码错误&大于5位'''
		self.user_login_verify(username="test",password="qq1234")
		po=login(self.driver)
	#	self.assertEqual(po.pwd_error_hint(),'密码不能小于5位')
		function.insert_img(self.driver,'password_error.png')
	def test_login6(self):
		'''普通管理员登录'''
		self.user_login_verify(username="test",password="qq123456")
		po=login(self.driver)
		now_url=self.driver.current_url
		self.assertEqual(now_url,"http://admin.muggle-inc.com/desktop")
	#	self.assertEqual(po.pwd_error_hint(),'密码不能小于5位')
		function.insert_img(self.driver,'user_success.png')
	def test_login7(self):
		'''超级管理员登录'''
		self.user_login_verify(username="Sanit",password="Fansclub321")
		po=login(self.driver)
		now_url=self.driver.current_url
		self.assertEqual(now_url,"http://admin.muggle-inc.com/desktop")
		function.insert_img(self.driver,'super_user_success.png')


if __name__ == '__main__':
	unittest.main()
