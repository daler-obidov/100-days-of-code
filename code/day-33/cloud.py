import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 39.647099
MY_LONG = 66.960289
email = "eclipsedkwx@gmail.com"
password = "tijpvtmpqqvnprvf"

def is_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LAT-5 <= iss_longitude <= MY_LAT+5:
        return True
        
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss and is_night:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs='dilshodboy19@gmail.com',
                msg='Subject:Look up\n\nThe ISS is above you in the sky!'
            )
