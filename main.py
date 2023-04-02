import datetime as dt
import random
import smtplib
import pandas

NAME = "[NAME]"
REGARDS = "Usman"
message = ""
MY_EMAIL = "your-email@example.com"
MY_PASSWORD = "your-password"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


def generate_content(path, name):
    with open(path) as file:
        global message
        message = file.read()
        message = message.replace(NAME, name)
        message = message.replace("Angela", REGARDS)


data = pandas.read_csv("birthdays.csv")
new_dict = {(new_value["month"], new_value["day"]): new_value for (index, new_value) in data.iterrows()}
if today_tuple in new_dict:
    num = random.randint(0, 2)
    if num == 0:
        path = "letter_templates/letter_1.txt"
        generate_content(path, new_dict[today_tuple]["name"])
    elif num == 1:
        path = "letter_templates/letter_2.txt"
        generate_content(path, new_dict[today_tuple]["name"])
    else:
        path = "letter_templates/letter_3.txt"
        generate_content(path, new_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=new_dict[today_tuple]["email"],
            msg=f"Subject:HAPPY BIRTHDAY\n\n{message}"
        )
