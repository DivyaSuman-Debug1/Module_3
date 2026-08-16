#1.  def and return     →  define 4 functions: add, subtract, multiply, divide
#2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
#3.  float(input())     →  to read numbers from the user
#4.  return values      →  each function must return the correct result

def add(a, b):
    return(a + b) 

def subtract(a , b):
    return(a - b)

def multiply(a, b):
    return(a * b)

def divide(a, b):
    return(a / b)

try:
    operation = input("Choose which way you want to Operate the Calculator.(+, -, *, /): ")
    a = int(input("Enter the First Number: "))
    b = int(input("Enter the Second Number: "))

    if operation == "+":
        result = add (a, b)
    elif operation == "-":
        result = subtract (a, b)
    elif operation == "*":
        result = multiply (a, b)
    elif operation == "/":
        result = divide (a, b)
    else:
        print("Invalid Operation Chosen")
        result = None
    if result is not None:
        print("Result is:", result)
except SyntaxError:
    print("Invalid, Use Numbers instead of Words")