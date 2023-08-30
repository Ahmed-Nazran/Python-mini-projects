import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

print("Calculator")
print("Operations: +, -, *, /, ^, sqrt, sin, cos, tan")

while True:
    operation = input("Enter operation: ")

    if operation in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operation == '+':
            print("Result:", add(num1, num2))
        elif operation == '-':
            print("Result:", subtract(num1, num2))
        elif operation == '*':
            print("Result:", multiply(num1, num2))
        elif operation == '/':
            print("Result:", divide(num1, num2))
    elif operation == '^':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print("Result:", power(base, exponent))
    elif operation == 'sqrt':
        num = float(input("Enter number: "))
        print("Result:", square_root(num))
    elif operation in ('sin', 'cos', 'tan'):
        angle = float(input("Enter angle in degrees: "))
        if operation == 'sin':
            print("Result:", sin(angle))
        elif operation == 'cos':
            print("Result:", cos(angle))
        elif operation == 'tan':
            print("Result:", tan(angle))
    else:
        print("Invalid operation. Please enter a valid operation.")
    
    play_again = input("Do you want to perform another calculation? (y/n): ")
    if play_again.lower() != 'y':
        print("!")
        break
