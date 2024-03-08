#Sorry for that simple project. i didn't had any idea to create something so i created a simple calculator

result = None
x = input("Enter the x value: ")
y = input("Enter the y value: ")
sign = input("Enter the sign (+,-,/,*,pow,remainder or %): ")

if sign == "+":
    result = x + y
elif sign == "-":
    result = x - y
elif sign == "*":
    result = x * y
elif sign == "/":
    result = x / y
elif sign == "%" or "remainder":
    result = x % y
elif sign == "pow":
    result = x**y
print("The result is: " + str(result))
