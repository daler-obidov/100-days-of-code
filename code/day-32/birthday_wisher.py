import datetime as dt
import pandas
import random
import smtplib

email = "eclipsedkwx@gmail.com"
password = "tijpvtmpqqvnprvf"

today = dt.datetime.now()
today_t = (today.month, today.day)

data = pandas.read_csv('code/day-32/birthdays.csv')

birthdays_dict = {(data['month'], data['day']): data for (i, data) in data.iterrows()}

if today_t in birthdays_dict:
    birthday_person = birthdays_dict[today_t]
    file = f"code/day-32/letter_{random.randint(1,3)}.txt"
    with open(file) as l_file:
        contents = l_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=birthday_person['email'],
            msg=f'Subject:Happy Birthday!\n\n{contents}'
        )

