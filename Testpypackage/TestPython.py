# from lib2to3.fixer_util import String
# from telnetlib import EC
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome(executable_path="D:\Trainings\Selenium\Drivers\chromedriver.exe")
#
# driver.get("http://automationpractice.com/index.php")
#
# driver.maximize_window();
#
# driver.implicitly_wait(20);
#
# print(driver.title)
# emailid = "Test20765@gmail.com";
# passwordd = "Test@2131";
#
# driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click();
# driver.find_element_by_xpath("//input[@id='email_create']").send_keys(emailid);
# driver.find_element_by_xpath("//button[@id='SubmitCreate']").click();
# driver.find_element_by_xpath("//input[@id='id_gender1']").click();
# driver.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("hari");
# driver.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("krishna");
# driver.find_element_by_xpath("//input[@id='passwd']").send_keys(passwordd);
#
# selectdays = Select(driver.find_element_by_xpath("//select[@id='days']"));
#
# selectdays.select_by_value("10");
#
# selectmonths = Select(driver.find_element_by_xpath("//select[@id='months']"));
#
# selectmonths.select_by_index(3);
#
# selectYear = Select(driver.find_element_by_xpath("//select[@id='years']"));
#
# selectYear.select_by_value("1988");
#
# driver.find_element_by_xpath("//input[@id='address1']").send_keys("Hyderabad");
# driver.find_element_by_xpath("//input[@id='city']").send_keys("Hyderabad");
#
# selectstate = Select(driver.find_element_by_xpath("//Select[@id='id_state']"));
#
# selectstate.select_by_index(2);
#
# driver.find_element_by_xpath("//input[@id='postcode']").send_keys("00000");
#
# selectcountry = Select(driver.find_element_by_xpath("//Select[@id='id_country']"));
#
# selectcountry.select_by_index(1);
#
# driver.find_element_by_xpath("//input[@id='phone_mobile']").send_keys("1232123456");
#
# driver.find_element_by_xpath("//button[@id='submitAccount']").click();
# # Log out
# driver.find_element_by_xpath("//a[@title='Log me out']").click();
#
# # login to my store
#
# driver.find_element_by_xpath("//input[@id='email']").send_keys(emailid);
# driver.find_element_by_xpath("//input[@id='passwd']").send_keys(passwordd);
# driver.find_element_by_xpath("//button[@id='SubmitLogin']").click();
#
# # select product and add in cart
#
# driver.find_element_by_xpath("(//div[@id='block_top_menu']//a[@title='T-shirts'])[2]").click();
#
# productname = driver.find_element_by_xpath("(//div[@class='top-pagination-content clearfix']//following::li)[1]")
#
# action = ActionChains(driver);
#
# action.move_to_element(productname).perform();
# driver.find_element_by_xpath(
#     "(//div[@class='top-pagination-content clearfix']//following::li)[1]//span[contains(text(),'Add to cart')]").click();
# val = 20  # in seconds
# driver.implicitly_wait(val);
# # prdaddedsuccessmessage = driver.find_element_by_xpath("//div[@class='layer_cart_product col-xs-12 col-md-6']//h2").getText();
# # print(prdaddedsuccessmessage);
# driver.find_element_by_xpath(
#     "//div[@class='layer_cart_product col-xs-12 col-md-6']//following::a[@title='Proceed to checkout']").click();
# driver.find_element_by_xpath("//div[@id='center_column']//following::a[@title='Delete']").click();
# # Log out
# driver.find_element_by_xpath("//a[@title='Log me out']").click();
# driver.close();
