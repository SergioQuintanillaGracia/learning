from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("asdf")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("asdf2")

email = driver.find_element(By.NAME, "email")
email.send_keys("asdf3@gmail.com")

sign_up_button = driver.find_element(By.XPATH, "/html/body/form/button")
sign_up_button.click()

# article_count = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[2]/a[1]")
# article_count = int(article_count.text.replace(",", ""))

# article_count.click()

# print(article_count)

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python", Keys.ENTER)