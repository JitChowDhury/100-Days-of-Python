import random
from random import randint

import  my_module

randomNumber = random.randint(1,10)
print(f"Random INT Number is: {randomNumber}")
print(f"Random Number is: {my_module.my_fav_number}")

random_number_0_to_1 = random.random()*10
print(f"Random FLOAT Number is: {random_number_0_to_1}")


random_float = random.uniform(1,10)
print(f"Random FLOAT Number is: {random_float}")

choice = random.randint(0,1)
if choice==1:
    print("HEAD")
elif choice == 0:
    print("TAIL")

