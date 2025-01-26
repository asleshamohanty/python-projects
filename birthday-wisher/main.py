import smtplib
import pandas
import random
import datetime as dt

my_email = "aslesham.social@gmail.com"
password = "qhes jomr fegi aeka"

data = pandas.read_csv("birthdays.csv")
month = data['month'].tolist()
day = data['day'].tolist()
name = data['name'].tolist()

now = dt.datetime.now()
current_day = now.day
current_month = now.month


letters = [".\letter_templates\letter_1.txt", ".\letter_templates\letter_2.txt", ".\letter_templates\letter_2.txt"]
chosen_letter = random.choice(letters)


for i in range(len(data)):
    if month[i] == current_month and day[i] == current_day:
        with open (chosen_letter, "r") as file:
            file_data = file.read()
            file_data = file_data.replace("[NAME]", name[i])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="asleshasocial@yahoo.com",
                                msg=f"Subject: Happy Birthday! \n\n {file_data}")





