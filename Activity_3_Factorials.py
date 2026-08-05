def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The Factorial of 0", factorial(0))
print("The Factorial of 1", factorial(1))
print("The Factorial of 2", factorial(2))
print("The Factorial of 3", factorial(3))
print("The Factorial of 4", factorial(4))
print("The Factorial of 5", factorial(5))