prices = []

while True:
    try:
        item = input("enter item price (Q to quit): ")

        if item.upper() == "Q":
            break

        price = float(item)

        if price < 0:
            print("Invalid price!")
        else:
            prices.append(price)
            print("Item added!")

    except ValueError:
        print("Invalid price!")

    finally:
        print("Entry processed.\n")

print(f"Items purchased: {len(prices)}")
print(f"Total: ${sum(prices):.2f}")