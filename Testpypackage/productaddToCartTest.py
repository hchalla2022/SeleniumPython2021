# import unittest
#
# from selenium import webdriver
#
#
# class productaddToCartTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(executable_path="D:/Trainings/Selenium/Drivers/chromedriver.exe")
#         cls.driver.maximize_window()
#         cls.driver.implicitly_wait(20)
#
#     def test_login_valid(self):
#         driver = self.driver
#         self.driver.get("http://automationpractice.com/index.php")
#         emailid = "Test20765@gmail.com"
#         passwordd = "Test@2131"
#         login = Loginpage(driver)
#         login.click_SignInLink()
#         login.enter_Username(emailid)
#         login.enter_password(passwordd)
#         login.click_loginbutton()
#
#         # Add product to cart
#         addproduct = AddProductToCartPage(driver)
#         addproduct.Click_Menu()
#         addproduct.Click_AddProduct()
#         addproduct.Click_Checkout()
#         addproduct.Click_DeleteProduct()
#
#     @classmethod
#     def tearDown(cls):
#         cls.driver.close()
#         print("Test completed")
#
# # if __name__ == "__main__":
# #     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
# #         output="C:/Users/hchalla2020/PycharmProjects/pythonProject2021/reports"))
# #     print("Report Generation  has been completed")
