try:
    number = int(input("Enter The Value : "))
    print("This is not Valid")
    print(number/0)
except ZeroDivisionError:
    print("We cannot divide by Zero")
except ValueError:
    print("Only Integers are Allowed")