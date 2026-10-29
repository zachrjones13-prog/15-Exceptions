animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"]

try:
    index = int(input("Enter an index: "))
    print(animals[index])

except IndexError:
    print("That index does not exist!")

except ValueError:
    print("That is not a valid integer!")