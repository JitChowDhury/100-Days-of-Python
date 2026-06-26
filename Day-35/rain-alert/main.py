import requests
import json
import smtplib
import os

api_key=os.environ.get("WEATHER_API_KEY")

MY_EMAIL="jitchowdhury8717@gmail.com"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(
  user=MY_EMAIL,
  password="mewp ivga pcof eecw"
)

parameters={
  "lat":22.5726,
  "lon":88.3639,
  "cnt":4,
  "appid":api_key,
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()
# with open("data.json","w") as file:
#   json.dump(data,file,indent=2)

foreCast_list=data.get("list")


for i in foreCast_list:
  weather_id=i.get("weather")[0].get("id")
  if(weather_id>700):
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs="jitchowdhuryndp@gmail.com",
      msg="Subject:Rain Alert\n\nIt Might Rain Today Dont Forget To bring Your Umbrella-"
    )
    break



