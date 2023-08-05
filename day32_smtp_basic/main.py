import smtplib

my_email = ""
password = ""

# Provide the host of mail smtp
connection = smtplib.SMTP("smtp.gmail.com")

'''
transport layer securities to secure our email to the server, so that when somebody wants to read the email in the 
middle of sending the email will get encryupted
'''
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="oentoro.andreas@gmail.com",
    msg="Hello World\n This is testing email"
)
connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="oentoro.andreas@gmail.com",
        msg="Hello World\n This is testing email"
    )