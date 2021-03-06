import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "Your stock API key"
NEWS_API_KEY = "Your news API key"

account_sid = "Your account SID "  # This account sid is basically for identification of twilio account
auth_token = "Your account's authentication token"
client = Client(account_sid, auth_token)
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]
print(f"Yesterday's closing price : {yesterdays_closing_price}")

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day before yesterday's closing price : {day_before_yesterday_closing_price}")
difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆"
else:
    up_down = "⬇"
print(f"The difference in closing price is {difference}")
diff_percent = round((difference / float(yesterdays_closing_price)) * 100)
print(f"Difference in percentage : {diff_percent}%")

if abs(diff_percent) > 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    print(articles)
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]
    for article in formatted_articles:
        try:
            message = client.messages.create(
                body=article,
                from_="Your twilio trial number",
                to="Receiver's phone number"
            )
        except TwilioRestException as e:
            print(e)

