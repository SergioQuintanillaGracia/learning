import random
import smtplib
import datetime as dt

email = "..."
password = "..."
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Secure our connection (so the message will be encrypted)
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="...",
#         msg="Subject:Python email tests\n\n"
#             "This is the content"
#     )
#     # connection.close()  # Not needed, as we are using `with`

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# print(year)
#
# date_of_birth = dt.datetime(year=1990, month=2, day=20, hour=4)
# print(date_of_birth)

def get_random_quote():
    with open("quotes.txt") as f:
        quotes = [line.strip() for line in f.readlines()]

    return random.choice(quotes)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:  # If it is tuesday
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:Today's Quote\n\n"
                f"{get_random_quote()}"
        )