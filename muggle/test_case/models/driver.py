from selenium.webdriver import Remote
from selenium import webdriver

def browser():
	driver=webdriver.Firefox()
	'''
	host='127.0.0.1:4444'
	dc={'browserName':'firefox'}
	driver=Remote(command_executor='http/'+host+'/wb/hub',desired_capabilities=dc)
	'''
	return driver
if __name__ == '__main__':
	dr=browser()
	dr.get("http://www.baidu.com")
	dr.quit()