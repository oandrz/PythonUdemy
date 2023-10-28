from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time


FORM_URL = "https://forms.gle/M7epH37ZHHj6dx5m7"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.791612994582835%2C%22east%22%3A-122.38449183825684%2C%22south%22%3A37.728981926922344%2C%22west%22%3A-122.50345317248535%7D%2C%22mapZoom%22%3A14%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(ZILLOW_URL, headers=header)
page = response.text

soup_page = BeautifulSoup(page, "html.parser")

property_prices = soup_page.find_all(attrs={"data-test": "property-card-price"})
all_prices = [price.get_text().split("+")[0] for price in property_prices if "$" in price.text]
print(len(all_prices))

property_address = soup_page.findAll(attrs={"data-test": "property-card-addr"})
all_address = [address.get_text() for address in property_address]
print(len(all_address))

all_link = []
property_link = soup_page.findAll(attrs={"data-test": "property-card-link"})
for link in property_link:
    href = link.get("href")
    if "http" not in href:
        all_link.append(f"https://www.zillow.com{href}")
    else:
        all_link.append(href)

print(len(all_link))

property_dic = {}

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options)
driver.get(FORM_URL)
time.sleep(10)

for n in range(len(all_address)):
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(all_address[n])

    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(all_prices[n])

    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_input.send_keys(all_link[n])

    submit_button = driver.find_element(By.CSS_SELECTOR, value='[class="NPEfkd RveJvd snByac"]')
    submit_button.click()

    submit_another = driver.find_element(By.LINK_TEXT, value="Submit another response")
    submit_another.click()

    print(f"index {n} done")


