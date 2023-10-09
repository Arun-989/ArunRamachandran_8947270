from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
# Open Rediffmail
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(3)
# Login
username_field = driver.find_element("id", "login1")
password_field = driver.find_element("id", "password")
username_field.send_keys("aram789@rediffmail.com")
password_field.send_keys("Test@789!")
login_button = driver.find_element(By.NAME, 'proceed')
login_button.click()
time.sleep(3)
# Verify Title
assert "Rediffmail" in driver.title
# Compose Mail
write_mail = driver.find_element(By.CLASS_NAME, 'rd_write')
write_mail.click()
time.sleep(3)
# Add To Email address
email_address = driver.find_element(By.XPATH,
                                    '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/ul[2]/li[2]/div/div/ul/li[1]/ul/li/input[1]')
email_address.send_keys("aramachandran7270@conestogac.on.ca")
# Add Subject
email_subject = driver.find_element(By.CSS_SELECTOR, 'input[class="rd_inp_sub rd_subject_datacmp2"]')
email_subject.send_keys("Sample Mail send from Rediff Mail")
# Add Body Content
email_body = driver.find_element(By.XPATH, '/html/body')
email_body.send_keys('This is a sample content for the mail from aram789@rediffmail.com', Keys.ENTER,
                     'Thanks and Regards,', Keys.ENTER, 'Arun Ramachandran')
time.sleep(3)
# Send Mail
email_send_button = driver.find_element(By.CSS_SELECTOR, 'a[class="send_ng_compo rd_btn_cmp_send"]')
email_send_button.click()
time.sleep(2)
# Verify success message
email_success = driver.find_element(By.ID, 'rdNotify')

if email_success.text == 'Your mail has been sent':
    print("The mail is sent successfully!")
else:
    print("The mail is not sent!!!")
time.sleep(3)
# Logout
logout_link = driver.find_element(By.LINK_TEXT, 'Logout')
logout_link.click()
time.sleep(2)
driver.quit()
print("The execution completed successfully")
