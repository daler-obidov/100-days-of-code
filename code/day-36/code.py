#DO NOT RUN CODE, TWILIO ACCOUNT CANNOT BE CREATED.


import requests
from twilio.rest import Client

STOCK = 'AAPL'
COMPANY_NAME = 'Apple Inc'
API_KEY = 'K8Z3UWLT8GVFL13W'
NEWS_COMPANY = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "04e2cedb74a14526aa6d86f87f0c2f1f"
TWILIO_ID = ""
TWILIO_AUTHTOKEN = ""

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY 
}

response = requests.get(url="https://www.alphavantage.co/query", params=params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percent = (difference / float(yesterday_closing_price)) * 100 
print(diff_percent)

if abs(diff_percent) < 1:
    news_params = {
        "apiKey": NEWS_APIKEY,
        "qInTitle": COMPANY_NAME,

    }
    n_response = requests.get(url=NEWS_COMPANY, params=news_params)
    news = n_response.json()["articles"]
    three_articles = news[:3]
    print(three_articles)

formatted_article = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

client = Client(TWILIO_ID, TWILIO_AUTHTOKEN)

for article in formatted_article:
    message = client.message.create(
        body=article,
        from_="",
        to=''
    )
    