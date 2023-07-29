import datetime as dt
import random
import smtplib

my_email = ""
password = ""

now = dt.datetime.now()
wd = now.isoweekday()

with open("./quotes") as files:
    list_quotes = files.readlines()

    if wd == 6:
        quotes = random.choice(list_quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="oentoro.andreas@gmail.com",
                msg=quotes.encode('utf-8')
            )
            print("Message successfully sent")
    else:
        print(f"Wrong week day currently it's {dt.datetime.weekday()}")
