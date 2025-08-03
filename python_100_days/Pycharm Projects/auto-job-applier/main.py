import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

EMAIL = "..."
PASSWORD = "..."

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4271013415&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

time.sleep(0.4)

# Sign in
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/section/div/div/div/div[2]/button")
sign_in_button.click()

email_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_input.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/section/div/div/form/div[2]/button")
sign_in_button.click()

time.sleep(1)


def refresh_jobs():
    global job_ids

    job_area = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul")
    jobs = job_area.find_elements(By.CSS_SELECTOR, "li")

    job_ids = [i.get_attribute("id") for i in jobs]
    job_ids = [id for id in job_ids if id]  # Remove empty ids

job_ids = []
refresh_jobs()

job_index = 0

while job_index < len(job_ids):
    job = driver.find_element(By.CSS_SELECTOR, f"#{job_ids[job_index]}")

    job.click()

    time.sleep(1)

    # Save jobs
    save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button:nth-child(3)")
    save_button.click()

    # Follow company
    company_button = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name > a:nth-child(1)")
    company_button.click()

    time.sleep(1.5)

    follow_button = driver.find_element(By.CSS_SELECTOR, ".follow")
    follow_button.click()

    # time.sleep(0.8)
    #
    # not_now_button = driver.find_element(By.CSS_SELECTOR, "#ember420")
    # not_now_button.click()

    driver.back()

    time.sleep(1.5)

    refresh_jobs()
    job_index += 1