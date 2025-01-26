import datetime as dt
import smtplib
import random

with open ("quotes.txt", "r") as file:
    data = file.readlines()
    quote = random.choice(data)




my_email = "aslesham.social@gmail.com"
password = "qhes jomr fegi aeka"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:# creating a new stmp object called connection & in brackets is smtp server location of email provider
        connection.starttls() # tls is Transport Layer Security is a way of securing our connection to email server - encrypts message
        connection.login(user = my_email, password = password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="asleshasocial@yahoo.com",
                            msg= f"Subject: Monday Motivation \n\n {quote}")
else:
    print(quote)
