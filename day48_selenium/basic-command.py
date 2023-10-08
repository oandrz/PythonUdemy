import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_TO_TRACK = "https://www.amazon.com/Spigen-Designed-Carrying-Accessories-Original/dp/B0C7YYS8S4/ref=sr_1_14?crid=30K0RVRQBDH7A&keywords=rog+alloy+case&qid=1694250956&sprefix=rog+all%2Caps%2C406&sr=8-14"

# To make the page stay
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PRODUCT_TO_TRACK)

price_dollars = driver.find_element(by=By.CLASS_NAME, value="a-price-whole") # Return html tag
price_cents = driver.find_element(by=By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollars.text}.{price_cents.text}")

driver.get("https://python.org")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name) # to get input tag, output: input
print(search_bar.get_attribute("placeholder")) # Search get one of the attribute in the html, in this example get placeholder attribute

button = driver.find_element(By.ID, value="submit")
print(button.size) # Print button size attribute

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text) # get the link based on the CSS selector, docs.python.org

#By XPath -> just like a file structure but html: header/body/div/...
submit_button_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_button_link.text) # print submit website bug

# Select XPath but return the list of all founded
# driver.find_elements(By.CSS_SELECTOR, value=)


# Close website manually
# Close single tab that openned
# driver.close()

# Close browser
driver.quit()