bill = 0
tax = 0
tip = 0
pizzas = ["the standard", "vegetarian", "hawaiian", "yeah buddy"]
descriptions = [
    "The Standards is a chesse pizza with red sauce.",
    "The Vegetarian has onions, mushrooms, and green pepppers.",
    "The Hawaiian has pepperoni and pineapple.",
    "The Yeah Buddy has locally sourced organic ricotta, baby kale, heirloom tomatoes, and exotic mushrooms."
]
prices = [12.99, 14.99, 15.99, 21,99]
addOns = ["pepperoni", "mushrooms", "hot peppers", "ricotta", "spinach", "tomatoes"]
ADDON = 2
TAXRATE = .055
LOWTIP = .15
STANDARDTIP = .20
HIGHTIP = .30
print("Welcome to Pizza Paradise!")
print("We have an amazing list of pizzas: \n")
for pizza in pizzas:
    print(pizza.title())
action = input("How can I help you? \n\tEnter 'o' to place an order.\n Enter 'd' to get a description of our pizzas. \n\t Enter 'l' to list our extra toppings.")
if action == "o":
    ordering = True
    while ordering:
        orderItem = input("What would you like to order? \n\t The Standard (s)\n\t Vegetarian (v) \n\t Hawaiian (h) \n\t Yeah Buddy (yb)")
