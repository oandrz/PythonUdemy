##################### Extra Hard Starting Project ######################
import random, pandas, smtplib, datetime as dt

my_email = ""
password = ""
template = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv
birthday_list = pandas.read_csv("./birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
list_of_person_having_bd_today = birthday_list[
    (birthday_list["day"] == today.day) &
    (birthday_list["month"] == today.month)
]
if list_of_person_having_bd_today.size != 0:
    name_list = list_of_person_having_bd_today["name"].tolist()
    email_list = list_of_person_having_bd_today["email"].tolist()

    with open(f"./letter_templates/{random.choice(template)}") as file:
        template = file.read()
        cards = [template.replace("[NAME]", name) for name in name_list]
        with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user=my_email, password=password)
            for index in range(0, len(cards)):
                connections.sendmail(
                    from_addr=my_email,
                    to_addrs=email_list[index],
                    msg=cards[index]
                )
                print(f"Successfully send message for {email_list[index]}")
else:
    print("We don't have person that has a birthday today")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




