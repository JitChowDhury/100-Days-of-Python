print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("What's your age Bigga?"))

    if age<=12:
        print("You should pay 5rs")
    elif age<=18:
        print("Please pay 10rs")
    else:
        print("Please pay 20rs")

else:
    print("Sorry you have to grow taller before you can ride.")
