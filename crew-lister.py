crewbies = []
running = True
while running:
    action = input("What would you like to do? \n Add a crewbie(a), delete a crewbie(d), or list the crewbies(l)? ")
    if action == "a":
        crewbie = input("Enter crewbie to add: ")
        crewbies.append(crewbie)
        print(f"Crewbie {crewbie} has been added to the crew!")
    elif action == "d":
        if len(crewbies) == 0:
            print("There are no crewbies to list.")
        else:
            crewbie = input("Enter the name of the crewbie to remove: ")
            crewbie = crewbies.remove(crewbie)
            print(f"{crewbie} has been removed from the crew.")
    elif action == "l":
        order = input("How would you like to list the crew: alphabetically(a) or reverse alphabetically(r)?")
        if len(crewbies) == 0:
            print("Sorry, there are no crewbies in the crew yet.")
        else:
            if order == "a":
                crewbies.sort()
                print(crewbies)
            else:
                crewbies.sort(reverse=True)
                print(crewbies)
    else:
        running = False
        print("Thanks for working with the crew.")
