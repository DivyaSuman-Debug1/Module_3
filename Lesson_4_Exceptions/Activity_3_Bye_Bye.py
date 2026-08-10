valid = False
while not valid:
    try:
        n = int(input("Write the number the Loop starts from : "))
        while (n % 2 == 0):
            print("Bye")
            valid = True 
    except ValueError:
        print("The Number should be an Integer")