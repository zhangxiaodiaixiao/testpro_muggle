#from selenium.webdriver.common.action_chains import ActionChasins
from selenium.webdriver.common.by import By
from base import Page
from time import sleep

class login(Page):
	url='/'


	Login_username_loc=(By.NAME,'username')
	Login_password_loc=(By.NAME,'password')
	Login_button_loc=(By.TAG_NAME,'button')


	def login_username(self,username):
		self.find_element(*self.Login_username_loc).send_keys(username)
	def login_password(self,password):
		self.find_element(*self.Login_password_loc).send_keys(password)
	def login_button(self):
		self.find_element(*self.Login_button_loc).click()
	def user_login(self,username='username',password='1111'):
		self.open()
#		self.bbs_login()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		sleep(1)

	user_error_hint_loc=(By.XPATH,'//div[2]')
	pwd_error_hint_loc=(By.XPATH,'//div[2]/div/div[2]')
	def user_error_hint(self):
		return self.find_element(*self.user_error_hint_loc).text
	def pwd_error_hint(self):
		return self.find_element(*self.pwd_error_hint_loc).text
