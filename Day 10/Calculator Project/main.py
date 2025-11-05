from  art import  logo
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return  n1-n2

def multiply(n1,n2):
    return  n1*n2

def divide ( n1,n2):
    return  n1/n2






operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}





def calculator():
    print(logo)
    previous_result = 0
    should_run=True
    n1 = float(input("What's the first number: \n"))

    while should_run:
        for key in operations:
            print(key)

        sign = input("What's the operation: \n")
        n2 = float(input("What's the second number: \n"))

        for key in operations:
            if sign == key:
                previous_result = operations[key](n1=n1,n2=n2)
                print(f"Result {previous_result}")

        option = input(f"Type 'y' to continue with calculating with {previous_result} or type 'n' to start a new calculation: \n").lower()

        if (option == "y"):
            n1 = previous_result
        elif (option == "n"):
            n1 = 0
            print("\n" * 20)
            calculator()


calculator()










