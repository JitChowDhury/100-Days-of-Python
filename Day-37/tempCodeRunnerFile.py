import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME="helifakx"
TOKEN="ewejr348e9erwieow3"
user_params={
  "token": "ewejr348e9erwieow3",
  "username":"helifakx",
  "agreeTermsOfService":"yes",
  "notMinor":"yes"

}

response=requests.post(url=pixela_endpoint,json=user_params)
print(response.text)

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

response=requests.post(url=graph_endPoint,json=graph_config,headers=headers)
print(response.text)

pixel_endPoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"
pixel_config={
  "date":"202600627",
  "quantity":3,
}

response=requests.post(url=pixela_endpoint,json=pixel_config)
print(response.text)
