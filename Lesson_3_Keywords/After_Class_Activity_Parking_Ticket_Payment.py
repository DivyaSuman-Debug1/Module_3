def calculate_change(paid, price):
    change = paid - price 
    return change
snack = ("Chips")
price = int(input("What is the Price of Chips: "))
print("The Machine can only take coins of Value 1, 5, 10 and 25")
while True:
    paid = int(input("How much are you Paying for the Snacks: "))
    if paid not in (1, 5, 10, 25):
        print("You gave the Machine a Non Acceptable Coin")
        continue
    else:
        result = calculate_change(paid, price)
        if result==0:
            print("Nothing needs to be returned as Change")
            break
        else:
            print("Collect your Snack & Cash, The return amount is:", result)
            break