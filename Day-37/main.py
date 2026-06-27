import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"


USERNAME="helifakx"

TOKEN="ewejr348e9erwieow3"
user_params={

  "token": "ewejr348e9erwieow3",

  "username":"helifakx",

  "agreeTermsOfService":"yes",

  "notMinor":"yes"

}


# response=requests.post(url=pixela_endpoint,json=user_params)

# print(response.text)


graph_endPoint=f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {

  "id":"graph1",

  "name":"Cycling Graph",

  "unit":"Km",

  "type":"float",

  "color":"ajisai"

}

headers={

  "X-USER-TOKEN":TOKEN
}


# response=requests.post(url=graph_endPoint,json=graph_config,headers=headers)

# print(response.text)

theDay=datetime(year=2026,month=6,day=26)


pixel_endPoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"

pixel_config={
  "date":theDay.strftime("%Y%m%d"),

  "quantity":"10",
}

    


# response=requests.post(url=pixel_endPoint,json=pixel_config,headers=headers)

# print(response.text)


update_endPoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{theDay.strftime('%Y%m%d')}"

new_pixel_data={
  "quantity":"4.5"
}
# response=requests.put(url=update_endPoint,json=new_pixel_data,headers=headers)
# print(response.text)


delete_endPoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{theDay.strftime('%Y%m%d')}"

response=requests.delete(url=delete_endPoint,headers=headers)
print(response.text)