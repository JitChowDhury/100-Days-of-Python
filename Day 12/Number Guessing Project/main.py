import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
ACTUAL_NUMBER=random.choice(range(1,101))

difficulty = input ("Choose A difficulty 'easy' or 'hard':").lower()

turn=0

if difficulty == "easy":
    turn=10
elif difficulty == "hard":
    turn=5

number_found=False

while number_found==False:
    print(f"Turn Left:{turn}")


    if turn==0:
        break
    number=(float)(input("Make a guess: "))
    if number==ACTUAL_NUMBER:
        print(f"You Got it the actual number was {ACTUAL_NUMBER}")
        number_found=True
    elif number > ACTUAL_NUMBER:
        print("Too High\nGuess Again")
    elif number < ACTUAL_NUMBER:
        print("Too Low\nGuess Again")

    turn -= 1
    if turn == 0 and not number_found:
        print(f"You've run out of turns! The number was {ACTUAL_NUMBER}")
        break



