# Add function
def add(x,y):
    return x + y

#Subtract function
def subtract(x,y):
    return x - y

#Multiply Function
def multiply(x, y):
    return x * y

#Divide Function
def divide(x,y):
    return x / y

#Main Function
def main():
    print("Welcome to the Basic Calculator!")
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))

    computation = input("Do you want to Add, Multiply, Subtract, or Divide the numbers?: ")


    if computation.lower() == "add":
        print(add(x,y))
    elif computation.lower() == "multiply":
        print(multiply(x,y))
    elif computation.lower() == "divide":
        print(divide(x,y))
    else:
        print(subtract(x,y))

main()
