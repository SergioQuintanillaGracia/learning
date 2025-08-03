import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_LINK = "..."

response = requests.get(ZILLOW_LINK)
zillow_web = response.text

soup = BeautifulSoup(zillow_web, "html.parser")

anchor_elements = soup.select(".StyledPropertyCardDataWrapper a")
links = [a["href"] for a in anchor_elements]
print(links)

prices = soup.select(".PropertyCardWrapper__StyledPriceLine")
prices = [price.text.split("+")[0].split("/")[0] for price in prices]
print(prices)

addresses = soup.select(".StyledPropertyCardDataWrapper address")
addresses = [address.text.strip().replace("|", "") for address in addresses]
print(addresses)

driver = webdriver.Firefox()

for link, price, address in zip(links, prices, addresses):
    driver.get(GOOGLE_FORM_LINK)

    time.sleep(1)

    addr_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")

    addr_input.send_keys(address)
    price_input.send_keys(price)
    link_input.send_keys(link)
    submit_button.click()

    time.sleep(1)