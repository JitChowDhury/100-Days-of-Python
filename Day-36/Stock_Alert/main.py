import requests
import os
import smtplib
import json


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key= os.environ.get("STOCK_API_KEY")
news_api_key= os.environ.get("NEWS_API_KEY")

news_parameters={
  "q":COMPANY_NAME,
  "apiKey":news_api_key,
}

stock_parameters={
  "function":"TIME_SERIES_DAILY",
  "symbol":STOCK,
  "datatype":"json",
  "apikey":stock_api_key
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_response=requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
stock_response.raise_for_status()

daily_data=stock_response.json().get("Time Series (Daily)")
daily_data_list=[value for (key,value) in daily_data.items()]

yesterdayPrice=float(daily_data_list[1].get("4. close"))
dayBeforeYesterdayPrice=float(daily_data_list[2].get("4. close"))

price_diff=abs(dayBeforeYesterdayPrice-yesterdayPrice)


percentage_diff=(price_diff/dayBeforeYesterdayPrice)*100


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_list=[]
if percentage_diff>1:
  response=requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
  response.raise_for_status()
  data=response.json().get("articles")
  

  


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
news_list = [
    f"Headline: {article['title']}\nBrief: {article['description']}"
    for article in data[:3]
]
with open("news.txt","w",encoding="utf-8") as file:
  for news in news_list:
    file.write(news + "\n\n")

