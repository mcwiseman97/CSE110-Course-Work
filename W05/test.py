import os

cart = []
cart_costs = []

choice = 0

print("Welcome to the Shopping Cart Program!")
while choice != 5:
    print()
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = int(input("Please enter an action: "))

    if choice == 1:
        print()
        item = input("What item would you like to add to the cart? ")
        item_cost = float(input("What is the cost of this item? "))
        cart.append(item)
        cart_costs.append(item_cost)

    elif choice == 2:
        print("Here is the list of all items in the cart and their totals.")
        print()
        for counter, (item, cost) in enumerate(zip(cart, cart_costs), start=1):
            print(f"{counter}. {item} - ${cost:.2f}")
        print()

    elif choice == 3:
        if not cart:
            print("\nYour cart is empty!")
        else:
            print()
            print("Here are the items currently in your cart:")
            for counter, (item, cost) in enumerate(zip(cart, cart_costs), start=1):
                print(f"{counter}. {item} - ${cost:.2f}")
            print()
            change_num = int(input("Select the number of the item you would like to remove: ")) - 1
            if 0 <= change_num < len(cart):
                cart.pop(change_num)
                cart_costs.pop(change_num)
            else:
                print("Invalid item number.")

    elif choice == 4:
        print()
        print("Here is the total cost of everything in the cart:")
        for counter, (item, cost) in enumerate(zip(cart, cart_costs), start=1):
            print(f"{counter}. {item} - ${cost:.2f}")
        print(f"Total: ${sum(cart_costs):.2f}")

    elif choice == 5:
        break

    else:
        print("\nInvalid choice, try again.")

    input("\nPress Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')