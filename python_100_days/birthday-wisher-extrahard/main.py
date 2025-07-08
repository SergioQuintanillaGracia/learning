import random
import smtplib
import datetime as dt
import os
import pandas as pd

##################### Extra Hard Starting Project ######################

email = "..."
password = "..."

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
dataframe = pd.read_csv("birthdays.csv")
data = dataframe.to_dict(orient="records")

now = dt.datetime.now()
# Get entries that correspond to today
send_list = [entry for entry in data if entry["month"] == now.month and entry["day"] == now.day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for entry in send_list:
    templates_folder = "letter_templates"
    random_template_file = f"{templates_folder}/{random.choice(os.listdir(templates_folder))}"

    with open(random_template_file) as f:
        template = f.read().strip()

    letter = template.replace("[NAME]", entry["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=entry["email"],
            msg="Subject:Happy Birthday!\n\n"
                f"{letter}"
        )