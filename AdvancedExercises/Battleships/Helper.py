def prompt_position():

    direction = input("Which direction would you like the boat to tail? "
                      "\nA) North. "
                      "\nB) East. "
                      "\nC) South. "
                      "\nD) West. \n").upper()

    options = {
        "A": "North",
        "B": "East",
        "C": "South",
        "D": "West"
    }

    return options.get(direction)


print(prompt_position())