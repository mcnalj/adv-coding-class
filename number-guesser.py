import random

targetNumber = random.randint(1, 100)
guessing = True
while guessing:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < targetNumber:
        print("Sorry, too low.")
    elif guess > targetNumber:
        print("Nope, the magic number is lower")
    else:
        print("You win! You guessed the magic number.")
        guessing = False

        