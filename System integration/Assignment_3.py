from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

username_field = driver.find_element("name","username")
password_field = driver.find_element("name","password")

username_field.send_keys("Admin")
password_field.send_keys("admin123")

login_button = driver.find_element("xpath","/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login_button.click()
time.sleep(3)
assert "OrangeHRM" in driver.title

claim_button = driver.find_element("xpath","/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span")
claim_button.click()
time.sleep(2)
# assert "Employee Claims" in driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h5")

section_heading = driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h5")
assert section_heading.text == "Employee Claims"

assign_claim_btn = driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div[2]/div[1]/button")
assign_claim_btn.click()
time.sleep(3)

emp_name = driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div")
emp_name.send_keys("Li")


time.sleep(3)
option_1 = driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div[2]/div[2]")
option_1.click()

drop_dwn1 = driver.find_element("xpath", "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[2]")
drop_dwn1.click()
driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[4]").click()

currency_list = driver.find_element("xpath", "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]")
currency_list.send_keys("c")

Remarks = driver.find_element("xpath", "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/textarea")
Remarks.send_keys("This is a claim against Form. 360")

driver.find_element("xpath","/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]").click()
time.sleep(2)

driver.close()

