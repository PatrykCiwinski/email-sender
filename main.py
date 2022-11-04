import datetime as dt
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now=dt.datetime.now()
day_of_week=now.weekday()

with open(file="quotes.txt") as quotes:
     data=quotes.readlines()
     quote=random.choice(data)

my_email="leszek.chrobol@gmail.com"
password="qaz123w4"
msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = "patryk.ciwinski@gmail.com"
msg['Subject'] = "Quote of the day"
body = quote
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
with smtplib.SMTP("smtp.gmail.com", 587)as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(my_email,"patryk.ciwinski@gmail.com", text)


print(quote)