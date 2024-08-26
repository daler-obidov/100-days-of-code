import smtplib

email = "eclipsedkwx@gmail.com"
password = "tijp vtmp qqvn prvf"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs='dalerboyobidov@gmail.com',
                        msg='Subject:Hi man\n\nNah you cannot')

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(day)

birthday = dt.datetime(year=2008, month=9, day=1)
print(birthday)