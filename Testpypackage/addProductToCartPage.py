# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# from Locators.locators import Locators
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class addProductToCartPage():
#     # constructor
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.cartmenu = "(//div[@id='block_top_menu']//a[@title='T-shirts'])[2]"
#         self.AddCart = "(//div[@class='top-pagination-content clearfix']//following::li)[1]//span[contains(text(),'Add to cart')]"
#         self.Checkout = "//div[@class='layer_cart_product col-xs-12 col-md-6']//following::a[@title='Proceed to checkout']"
#
#     def Click_Menu(self):
#         # element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.cartmenu)))
#         self.driver.find_element_by_xpath(self.cartmenu).click()
#
#     def Click_AddProduct(self):
#         productname = self.driver.find_element_by_xpath(
#             "(//div[@class='top-pagination-content clearfix']//following::li)[1]")
#         action = ActionChains(self.driver)
#         action.move_to_element(productname).perform()
#         self.driver.find_element_by_xpath(self.AddCart).click()
#
#     def Click_Checkout(self):
#         self.driver.find_element_by_xpath(self.Checkout).click()
#
