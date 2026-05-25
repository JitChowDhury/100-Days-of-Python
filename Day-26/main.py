import random


number_list = [1,2,3]
newList=[]
for num in number_list:
  newNum=num+1
  newList.append(newNum)

print(newList)

#new_list=[new_item for item in list]

newList2=[num+1 for num in newList]
print(newList2)

name = "Jit"
nameList = [letter for letter in name]
print(nameList)

doubledNum = [num*2 for num in range(1,6)]
print(doubledNum)

#conditional list comprehension
#new list = [new item for item in list if test]

names=['Alex','Beth','Caroline',"Dave",'Eleanor','Freddie']
short_names=[name for name in names if len(name)<=4]
long_names=[name.upper() for name in names if len(name)>4]
print(short_names)
print(long_names)

#dictionary comprehension
# new_dict = {new key: new value for item in list}
#new dict = {new key:new value for (key,value) in dict.items()}

scoreDict={name:random.randint(1,11) for name in names}
print(scoreDict)

passedStundet = {key:value for (key,value) in scoreDict.items() if value>3}
print(passedStundet)