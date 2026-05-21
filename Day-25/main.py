# import csv

# with open("Day-25/weather_data.csv") as data_file:
#   data=csv.reader(data_file)
#   next(data)
#   temperatures=[]
#   for row in data:
#     temp=int(row[1].strip())
#     temperatures.append(temp)

# print(temperatures)

import pandas

data = pandas.read_csv("Day-25/weather_data.csv")
print(data)

temp = data["temp"].to_list();
print(sum(temp)/len(temp))