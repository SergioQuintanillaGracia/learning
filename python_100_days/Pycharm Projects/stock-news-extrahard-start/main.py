import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK = "..."
API_KEY_NEWS = "..."
API_KEY_TWILIO = "..."

twilio_account_sid = "..."
twilio_auth_token = "..."

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
print(response.json())
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_keys = list(data)

date_last_day = data_keys[0]
date_before_last_day = data_keys[1]

price_close_last = float(data[date_last_day]["4. close"])
price_close_before_last = float(data[date_before_last_day]["4. close"])

print(price_close_last, price_close_before_last)

percentage_change = abs(price_close_last - price_close_before_last) / price_close_before_last * 100

if percentage_change > 5:
    print("Price increased / decreased by at least 5% between the last 2 datapoints")

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # NOTE: I'm only getting the first news piece so I only send an SMS to my phone (instead of 3)

    parameters = {
        "apiKey": API_KEY_NEWS,
        "q": COMPANY_NAME,
        "searchIn": "title",
        "language": "en"
    }

    response = requests.get("https://newsapi.org/v2/everything", parameters)
    response.raise_for_status()
    data = response.json()
    news = data["articles"]

    title = news[0]["title"]
    description = news[0]["description"]

    percentage_change_str = f"{percentage_change:.2f}%"
    if price_close_last >= price_close_before_last:
        percentage_change_str = f"🔺{percentage_change_str}"
    else:
        percentage_change_str = f"🔻{percentage_change_str}"

    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
        body = f"{STOCK}: {percentage_change_str}\nHeadline: {title}\nBrief: {description}",
        from_ = "...",
        to = "..."
    )
    print(f"Sending message:\n{STOCK}: {percentage_change_str}\nHeadline: {title}\nBrief: {description}")
    print(message.status)

else:
    print("Price didn't vary significantly")


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

