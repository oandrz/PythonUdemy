import requests
from bs4 import BeautifulSoup
import os
import smtplib


PRODUCT_TO_TRACK = "https://www.amazon.com/Spigen-Designed-Carrying-Accessories-Original/dp/B0C7YYS8S4/ref=sr_1_14?crid=30K0RVRQBDH7A&keywords=rog+alloy+case&qid=1694250956&sprefix=rog+all%2Caps%2C406&sr=8-14"
header = {
    "Request Line":"GET / HTTP/1.1",
    "Host": "myhttpheader.com",
    "Cache-Control": "max-age=0",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "x-forwarded-proto": "https",
    "x-https": "on",
}

EMAIL = os.getenv("EMAIL")
DEST_EMAIL = os.getenv("DESt_EMAIL")
PASS = os.getenv("PASS")

response = requests.get(PRODUCT_TO_TRACK, headers=header)
soup_page = BeautifulSoup(response.text, "html.parser")
print(soup_page)
print(soup_page.find(class_="a-offscreen"))
price = float(soup_page.find(class_="a-offscreen").text.split("$")[1])

if price < 39.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=DEST_EMAIL,
            to_addrs="",
            msg="Hey man, look up!"
        )
        print("email send successfully")