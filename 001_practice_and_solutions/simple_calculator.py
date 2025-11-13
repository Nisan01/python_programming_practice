
a=[12,"nisan",15,"a","c",45.67,True,None]

for i in a:
    print(i)
    print(type(i))


print("Enter an operation (+, -, *, /):") 
operation = input()

operators = ['+', '-', '*', '/']
if operation not in operators:
    print("Invalid operation. Please enter one of +, -, *, /.")
    exit()  

   

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")   
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")



