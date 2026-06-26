response=requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
response.raise_for_status()
print(response.status_code)