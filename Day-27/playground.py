def add(*nums):
  #thats why positional arg coz it matters
  print(nums[2])
  sum=0
  for i in nums:
    sum+=i
  print(sum)

add(1,2,3,4,5,6,7,8,9,10)

class Car:
  def __init__(self,**kwargs):
    self.company=kwargs["company"]
    self.model = kwargs["model"]


newCar=Car(company="NISSAN",model="GT-R")
print(newCar.company)
print(newCar.model)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2)