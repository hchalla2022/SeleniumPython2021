import unittest

from selenium import webdriver

from Pages.loginPage import loginPage


class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Trainings/Selenium/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_valid_login(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php")

        emailid = "Test20765@gmail.com"
        passwordd = "Test@2131"

        login = loginPage(driver)
        login.click_SignInLink()
        login.enter_Username(emailid)
        login.enter_password(passwordd)
        login.click_loginbutton()

        print("Login is successfully")

        # Add product to cart

        login.Click_Menu()
        login.Click_AddProduct()
        login.Click_Checkout()

        print("Product added in cart")

        # Delete product from cart

        login.Click_DeleteProduct()

        print("Product has been deleted")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        print("Test completed")
