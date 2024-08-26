import smtplib
import datetime as dt
import random

email = "eclipsedkwx@gmail.com"
password = "tijp vtmp qqvn prvf"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('code/day-32/quotes.txt') as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email, password)
        message = f'Subject: MOTIVATION for you\n\n{quote}'.encode('utf-8')
        connection.sendmail(from_addr=email,
                            to_addrs='dalerboyobidov@gmail.com',
                            msg=message)
