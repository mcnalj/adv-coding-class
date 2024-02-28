favoriteColor = "red"
guessing = True
while guessing:
    guess = input("Guess my favorite color: ")
    if guess == "q":
        guessing = False
    elif guess.lower() != favoriteColor:
        print(f"Sorry, it's not {guess}, try again.")
    else:
        print(f"You got it! {guess.title()} is my favorite color!")
        guessing = False
print("Thanks for playing!")
    