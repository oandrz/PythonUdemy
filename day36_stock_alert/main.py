import requests
import os
import datetime
from twilio.rest import Client

STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]
YOUR_PHONE_NUMBER = os.environ["YOUR_PHONE_NUMBER"]
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENT_CHANGE_THRESHOLD = 5.0

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_sms(news):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message_content = f"TSLA: {percent_change}%\n\n"
    for article in news:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        message_content += f"Headline: {title}\nBrief: {description}\nLink: {url}\n\n"

    message = client.messages.create(
        body=message_content,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )
    print(message.status)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def send_news():
    today_date = datetime.datetime.now()
    print(today_date.date().replace(today_date.year, today_date.month, today_date.day - 7))
    news_param = {
        "q": COMPANY_NAME,
        "from": today_date.date().replace(today_date.year, today_date.month, today_date.day - 7),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_param)
    news_response.raise_for_status()
    news = news_response.json()["articles"][:3]
    print(type(news))
    send_sms(news)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_request_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get("https://www.alphavantage.co/query", params=stock_request_params)
response.raise_for_status()

# Parse the JSON response
data = response.json()

# Get the closing prices for the last two days
time_series = data["Time Series (Daily)"]
dates = list(time_series.keys())[:2]
prices = [float(time_series[date]["4. close"]) for date in dates]

# Calculate the percentage change
percent_change = ((prices[1] - prices[0]) / prices[0]) * 100

# Check if the percentage change exceeds the threshold
if abs(percent_change) <= PERCENT_CHANGE_THRESHOLD:
    send_news()
else:
    print("Safe")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

