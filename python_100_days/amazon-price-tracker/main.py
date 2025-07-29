from dotenv import dotenv_values
import requests
import smtplib
from bs4 import BeautifulSoup

env = dotenv_values(".env")

email = env["EMAIL_ADDRESS"]
password = env["EMAIL_PASSWORD"]

amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "ACCEPT-LANGUAGE": "en-US,en;q=0.5",
    "USER-AGENT": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"
}

response = requests.get(amazon_url, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price_str = soup.select_one(selector=".a-offscreen").text.replace("$", "")
price = float(price_str)
product_name_words = soup.select_one(selector="#productTitle").text.split()
product_name = " ".join(product_name_words).encode("utf-8")
print(product_name)

target_price = 100

if price < target_price:
    with smtplib.SMTP(env["SMTP_ADDRESS"]) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Low price alert\n\n"
                f"{product_name} is now {price}\n"
                f"{amazon_url}"
        )