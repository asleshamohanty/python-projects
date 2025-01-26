import smtplib
'''
my_email = "aslesham.social@gmail.com"
password = "qhes jomr fegi aeka"

with smtplib.SMTP("smtp.gmail.com") as connection:# creating a new stmp object called connection & in brackets is smtp server location of email provider
    connection.starttls() # tls is Transport Layer Security is a way of securing our connection to email server - encrypts message
    connection.login(user = my_email, password = password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="asleshasocial@yahoo.com",
                        msg="Subject: Hello \n\n This is the body of the message")
'''

import datetime as dt

now = dt.datetime.now()
year = now.year

print(year)

date_of_birth = dt.datetime(year = 2005, month= 9, day = 29)