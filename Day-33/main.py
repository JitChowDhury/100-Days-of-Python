# import requests

# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data=response.json()["iss_position"]
# longitude=data["longitude"]
# latitude=data["latitude"]

# position=(longitude,latitude)
# print(position)

MY_LAT=22.57
MY_LONG=88.36
parameters = {
  "lat":MY_LAT,
  "lng":MY_LONG,
  "formatted":0
}


import requests
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
print(response.json()["results"]["sunset"].split("T"))
