# import csv

# with open("Day-25/weather_data.csv") as data_file:
#   data=csv.reader(data_file)
#   next(data)
#   temperatures=[]
#   for row in data:
#     temp=int(row[1].strip())
#     temperatures.append(temp)

# print(temperatures)

# import pandas

# data = pandas.read_csv("Day-25/weather_data.csv")
# print(data)
# print(type(data))
# temp= data.temp.to_list()
# print(temp)

# maxTemp=data.temp.max()
# print(maxTemp)


# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# def celToF(num):
#   return ((num*1.8)+32)

# print(celToF(data[data.day=="Monday"].temp))


# #create dataFrame from scratch
# data_dict = {
#   "students":["Amy","James","Angela"],
#   "scores":[76,56,65]
# }

# scoreData=pandas.DataFrame(data_dict)
# print(scoreData)
# scoreData.to_csv("Day-25/score.csv")


# print(pd.__version__)
# data=[902,903,904,109,70]
# room_series=pd.Series(data,index=["Room1","Room2","Room3","Room4","Room5"])
# room_series.loc["Room1"]=9902
# room_series.iloc[1]=2909
# # print(room_series)


# calories = { "Day 1":1750,"Day 2":2025,"Day 3":1500}
# calorie_series=pd.Series(calories)
# print(calorie_series)

# # print(calorie_series[calorie_series<2000])

# data={
#   "Name":["SpongeBob","Patrick","Squidward"]
# }

import pandas as pd
data = pd.read_csv("Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
greySqu=len((data[data["Primary Fur Color"]=="Gray"]))
redSqu=len((data[data["Primary Fur Color"]=="Cinnamon"]))
blackSqu=len((data[data["Primary Fur Color"]=="Black"]))

data_dict={
  "Fur Color" : ["Gray","Cinnamon","Black"],
  "Count" :[greySqu,redSqu,blackSqu]

}

pd_dataframe = pd.DataFrame(data_dict)
print(pd_dataframe)
pd_dataframe.to_csv("Day-25/SquCount.csv")

