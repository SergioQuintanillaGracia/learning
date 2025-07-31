from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
# price = f"{price_dollar}.{price_cents}"
# print(price)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.text)
#
# docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs_link.text)
#
# bug_link = driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget > div:nth-child(1) > ul:nth-child(3) li a")
events = [event.text for event in events]
print(events)

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget > div:nth-child(1) > ul:nth-child(3) li time")
dates = [date.text for date in dates]
print(dates)

res = {i: {"time": dates[i], "name": events[i]} for i in range(len(events))}
print(res)

# driver.close()  # Closes active tab
driver.quit()  # Quits the entire browser