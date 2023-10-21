from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "/Users/angela/Development/chromedriver"
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login/"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("test-type")
        chrome_options.add_argument("disable-popup-blocking")
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-button")
        go_button.click()
        time.sleep(80)

        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text

        print(f"Download speed is {self.down} and Upload speed is {self.up}")

        self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)

        email_input = self.driver.find_element(By.CSS_SELECTOR, value='[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        email_input.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.CSS_SELECTOR, value='[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')
        next_button.click()

        username_input = self.driver.find_element(By.CSS_SELECTOR, value='[class="css-901oao r-1awozwy r-1nao33i r-6koalj r-37j5jr r-1inkyih r-16dba41 r-135wba7 r-bcqeeo r-13qz1uu r-qvutc0"]')
        username_input.send_keys("")

        next_button_username = self.driver.find_element(By.CSS_SELECTOR, value='[class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
        next_button_username.click()

        input("Press Enter when Done Login")

    def password_field(self):
        password_input = self.driver.find_element(By.CSS_SELECTOR, value='[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(By.CSS_SELECTOR, value='[class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
        login_button.click()