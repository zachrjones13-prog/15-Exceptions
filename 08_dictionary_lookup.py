prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2}

try:
    item = input("What food do you want:  ")
    print(f"This costs {prices[item]} dollars")

except KeyError:
    print("Sorry, that item is not on the menu.")