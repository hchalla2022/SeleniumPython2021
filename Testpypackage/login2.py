# from selenium import webdriver
#
# import unittest
#
#
# class LoginTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(executable_path="D:/Trainings/Selenium/Drivers/chromedriver.exe")
#         cls.driver.maximize_window()
#         cls.driver.implicitly_wait(20)
#         cls.driver.get("http://automationpractice.com/index.php")
#
#     def test_login_valid(self):
#         # login to my store
#         self.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click();
#         self.driver.find_element_by_xpath("//input[@id='email']").send_keys("Test20765@gmail.com")
#         self.driver.find_element_by_xpath("//input[@id='passwd']").send_keys("Test@2131")
#         self.driver.find_element_by_xpath("//button[@id='SubmitLogin']").click()
#
#
# @classmethod
# def tearDown(cls):
#     cls.driver.close()
#     print("Test completed")
