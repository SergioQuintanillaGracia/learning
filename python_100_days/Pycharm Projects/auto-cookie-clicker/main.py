import time
from selenium import webdriver
from selenium.webdriver.common.by import By

BUY_INTERVAL = 5  # Time between purchases of most expensive item in shop
PLAYTIME = 300  # Time the program will be running. After it, the total number of cookies per second will be printed

driver = webdriver.Firefox()
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(1)

language_english_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_english_button.click()

time.sleep(2)

cookie_button = driver.find_element(By.ID, "bigCookie")


products_area = driver.find_element(By.CSS_SELECTOR, "#products")
cookie_text = driver.find_element(By.CSS_SELECTOR, "#cookies")

prev_buy_timestamp = time.time()
start_time = time.time()
current_time = time.time()

while current_time - PLAYTIME < start_time:
    cookie_button.click()

    current_time = time.time()

    if current_time - BUY_INTERVAL >= prev_buy_timestamp:
        prev_buy_timestamp = current_time

        products = products_area.find_elements(By.XPATH, "*")[1:]
        enabled_products = [product for product in products if ("enabled" in product.get_attribute("class"))]
        enabled_products.reverse()
        enabled_product_ids = [product.get_attribute("id") for product in enabled_products]

        if len(enabled_products) > 0 != -1:
            enabled_products[0].click()

cookies_per_second = float(cookie_text.text.split()[-1])
print(f"Final cookies per second after {PLAYTIME}: {cookies_per_second}")

driver.quit()