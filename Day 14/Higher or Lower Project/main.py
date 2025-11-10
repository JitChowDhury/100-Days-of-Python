import random

import art
from game_data import data
score = 0
is_wrong=False
print(art.logo)
value1 = random.choice(data)
data.remove(value1)
value2 = random.choice(data)
data.remove(value2)


while not is_wrong:
    print(f"Compare A:{value1["name"]}, a {value1["description"]}, from {value1["country"]}")
    print(art.vs)
    print(f"Against B:{value2["name"]}, a {value2["description"]}, from {value2["country"]}")
    choice=input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice=="A":
        if value1["follower_count"] > value2["follower_count"]:
            score+=1
            value2 = random.choice(data)
            data.remove(value2)
            print(f"You're Right current score: {score}")
        else:
            is_wrong=True
            print(f"Sorry , that's wrong. Final Score {score}")
    elif choice=="B":
        if value2["follower_count"] > value1["follower_count"]:
            score+=1
            value1 = random.choice(data)
            data.remove(value1)
            print(f"You're Right current score: {score}")
        else:
            is_wrong=True
            print(f"Sorry , that's wrong. Final Score {score}")