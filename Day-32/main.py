import smtplib
import random
import datetime as dt 

myemail="xyz@gmail.com"
password="abcd efg"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=myemail,password=password)




now =dt.datetime.now()

with open("E:/CODE/100 days of Code-Python/Day-32/quotes.txt") as file:
  quotes_list=file.readlines()

quote_to_send=random.choice(quotes_list)

if(now.weekday()==3):
  connection.sendmail(from_addr=myemail,to_addrs="jitchowdhuryndp@gmail.com",msg=f"Subject:Good Morning\n\n{quote_to_send}")
connection.close()