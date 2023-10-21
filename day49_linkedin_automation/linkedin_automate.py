import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def apply_job():
    time.sleep(5)
    job_apply_button = driver.find_element(By.CLASS_NAME, value="jobs-apply-button")
    job_apply_button.click()

    time.sleep(5)
    next_button = driver.find_element(By.CSS_SELECTOR, value='[aria-label="Continue to next step"]')
    next_button.click()

    time.sleep(5)
    review_button = driver.find_element(By.CSS_SELECTOR, value='[aria-label="Review your application"]')
    review_button.click()

    time.sleep(5)
    submit_button = driver.find_element(By.CSS_SELECTOR, value='[aria-label="Submit application"]')
    submit_button.click()


URL = "https://www.linkedin.com/jobs/search/?currentJobId=3701161517&f_AL=true&geoId=103035651&keywords=Software%20Engineer&location=Berlin%2C%20Germany&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sign_in_button = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
sign_in_button.click()

email_input = driver.find_element(By.ID, value="username")
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, value="password")
password_input.send_keys(PASSWORD)

form_sign_in_button = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
form_sign_in_button.click()

input("Press Enter when you have solved the Captcha")

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
print(len(all_listings))

for job in all_listings:
    job.click()
    time.sleep(2)

    try:
        apply_job()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
