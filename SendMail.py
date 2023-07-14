import smtplib
import datetime as dt
import random

MyEmail = "vpathem4@gmail.com"
MyPassword = "MY_PASSWORD"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("MyProjects-python\MailQuotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MyEmail, MyPassword)
        connection.sendmail(
            from_addr=MyEmail,
            to_addrs="vijaypathem4@gmail.com",
            msg=f"Subject:motivation \n\n {quote}"
        )


    