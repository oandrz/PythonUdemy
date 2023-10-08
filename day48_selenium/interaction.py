from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

link_text_example = driver.find_element(by=By.LINK_TEXT, value="View source")
link_text_example.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python") # send input to the particular element
search.send_keys(Keys.ENTER) # add input like enter, shift, every key in the keyboard

driver.quit()