item = ""
l_items= []
i = 0
while item != "quit":
    item = input("Enter an item you need at the store (Type quit to finish list): ")
    if item == "quit":
        continue
    else:
         l_items.append(item)
         i = i + 1
print()       

print("The shopping list is: ")
for groceries in l_items:
    print("Items: ", end="")
    print(groceries)

print()
i = 0
print("The shopping list with indexes is: ")
for groceries in l_items:
    print(f"{i}. ", end="")
    print(groceries)
    i += 1
print()

change_item = int(input("Which number would you like to change? "))
new_item = input("What would you like the new item to be? ")
l_items[change_item] = new_item


i = 0
print("The shopping list with indexes is: ")
for groceries in l_items:
    print(f"{i}. ", end="")
    print(groceries)
    i += 1
print()


