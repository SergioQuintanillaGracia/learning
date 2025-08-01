import time
from selenium import webdriver
from selenium.webdriver.common.by import By

ACCOUNT = "minecraft"
EMAIL = "..."
PASSWORD = "..."

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, email, password):
        self.driver.get(f"https://www.instagram.com/accounts/login/")
        time.sleep(2)

        decline_cookies_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        decline_cookies_button.click()

        email_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input")
        password_input.send_keys(password)
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[3]/button/div")
        login_button.click()
        time.sleep(5)

    def find_followers_of_account(self, account):
        self.driver.get(f"https://www.instagram.com/{account}/")
        time.sleep(1.5)

        # see_more_x = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/svg")
        # see_more_x.click()
        # time.sleep(1)

        followers_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span/span")
        followers_button.click()
        time.sleep(1.5)

    def follow_all(self):
        follower_zone = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]")
        follow_buttons = follower_zone.find_elements(By.CSS_SELECTOR, "button")

        for button in follow_buttons:
            button.click()
            time.sleep(1)


follower = InstaFollower()
follower.login(EMAIL, PASSWORD)
follower.find_followers_of_account(ACCOUNT)
follower.follow_all()