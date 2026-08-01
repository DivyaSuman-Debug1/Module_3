def greet_customer():
    print("Welcome to the Lemon Stand")
    print("We sell freshly squeezed Lemonade just for You")
def calculate_price(price, ask):
    total = price * ask
    return total
def calculate_change(total):
    amount = int(input("How much did the Customer Pay: "))
    return amount - total
def thanks_messages():
    print("Thank you for using our services")
greet_customer()
price = int(input("Enter the Price per Cup: "))
ask = int(input("How much cups would you like to take: "))
total = calculate_price(price, ask)
remaining = calculate_change(total)
print("Remaining change is equal to", remaining)
thanks_messages()