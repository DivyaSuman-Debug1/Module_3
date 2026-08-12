import random
playing = True
number = str(random.randint(1,9))

print("I will generate one number in between 1 & 9 and You need to guess the number with only one digit at a time")
print("The game ends when you guess one Correct Number")

while playing:
    guess = input("Give me your guess: ")
    if number == guess:
        print("You have Won the Game")
        break
    else:
        print("The guess is Incorrect, Try Again: ")