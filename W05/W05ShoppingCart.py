"""
Author: Michael
Assignment: Shopping cart
Date: 1/11/26
"""

# A menu needs to be added with options to a
# 1. Add new items
# 2. Display content in cart
# 3. Remove items
# 4. Calculate the total
# 5. Quit

import math

item = ""
item_cost = ""

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
        continue
    elif choice == 2:
        print("Here is the list of all items in the cart and thier totals.")
        print()
        i = 0
        counter = 1
        for items in cart:
            print(f"{counter}. ", end="")
            print(f"{items} -", end=" ")
            print(f"${cart_costs[i]:.2f}")
            i += 1
            counter += 1
        print()
        continue
    elif choice == 3:
        print()
        print("Which item would you like to remove from the cart? ")
        change_num = int(input("Select the the number you would like to change: ")) - 1
        cart.pop(change_num)
        cart_costs.pop(change_num)
        continue
    elif choice == 4:
        print()
        print("Here is the total cost of everything in the cart:")
        i = 0
        counter = 1
        for items in cart:
            print(f"{counter}. ", end="")
            print(f"{items} -", end=" ")
            print(f"${cart_costs[i]:.2f}")
            i += 1
            counter += 1
        continue
    elif choice == 5:
        break
    else: 
        print()
        print("Invalid choice, try again.")
        continue
    