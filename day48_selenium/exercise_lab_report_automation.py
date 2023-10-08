from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name_input = driver.find_element(By.CLASS_NAME, value="top")
first_name_input.send_keys("Andreas")
last_name_input = driver.find_element(By.CLASS_NAME, value="middle")
last_name_input.send_keys("Andreas")
email_input = driver.find_element(By.CLASS_NAME, value="bottom")
email_input.send_keys("blaze796@gmail.com")
button_sign_up = driver.find_element(By.CLASS_NAME, value="btn-block")
button_sign_up.click()

# driver.quit()
