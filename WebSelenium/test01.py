from selenium import webdriver
import time
class FirstCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        #driver.implicitly_wait(30)
        self.driver.get('http://www.testclass.net/readers/sign_in')
        self.driver.maximize_window()
        time.sleep(3)



    # ----------------------------登录功能login_case---------------------------------------
    def test_login(self):
        self.driver.find_element_by_xpath("//label[text()='电子邮箱']/../input").send_keys("757639413@qq.com")
        self.driver.find_element_by_id("reader_password").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@name='commit']").click()
        time.sleep(5)


    # ----------------------------移动业务订单MobileBusinessOrder---------------------------------------


    def test_close(self):
        self.driver.quit()

if __name__ == '__main__':
    import os, sys

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    fc = FirstCase()
    fc.test_login()
    fc.test_close()
