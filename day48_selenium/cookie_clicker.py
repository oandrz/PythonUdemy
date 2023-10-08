from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in prices:
            element_text = price.text
            if element_text != "":
                price = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(price)

        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        most_expensive_upgrade = max(affordable_upgrades)
        item_to_purchase = affordable_upgrades[most_expensive_upgrade]
        print(f"Most expensive upgrade: {item_to_purchase}")

        driver.find_element(by=By.ID, value=item_to_purchase).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
