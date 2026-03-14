"""
Author: Michael Wiseman
Assignment: Meal Calculator + Tax
Date: 3/14/26
"""
# I have added a terminal receipt at the end of the program
# That encourages a user to add a tip and sign after payment

# Gather meal cost
kid_cost = float(input("What is the cost of a child's meal? "))
adult_cost = float(input("What is the cost of an adults meal? "))

# Gather person count
num_kids = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

#calculate total pretax cost
subtotal = (num_adults * adult_cost) + (num_kids * kid_cost)

print(f"\nSubtotal: ${subtotal:.2f}\n")

# Gather tax
tax_rate = int(input("What is the sales tax rate? "))
applied_taxes = subtotal * (tax_rate / 100) #convert int into percentage
print(f"Sales Tax: ${applied_taxes:.2f}")
total_cost = subtotal + applied_taxes
print(f"Total: ${total_cost:.2f}\n")

# Calculate amount paid and provide change amount
paid_amount = float(input("What is the payment amount? "))
change = paid_amount - total_cost
print(f"Change: ${change:.2f}")

print("-------------------------------")
print("|          Thank You!         |")
print("|       Come back soon!       |")
print("|                             |")
print(f"|   {num_kids} x Kid Meal       ${kid_cost:.2f}  |")
print(f"|   {num_adults} x Adult meal     ${adult_cost:.2f}  |")
print("|                             |")
print("|                             |")
print(f"|   Subtotal:         ${subtotal:.2f}  |")
print("|                             |")
print(f"|   Sales Tax:        ${tax_rate:.2f}   |")
print(f"|   Total:            ${total_cost:.2f}  |")
print("|                             |")
print(f"|   Payment:          ${paid_amount:.2f}  |")
print(f"|   Change:           ${change:.2f}   |")
print("|                             |")
print("|    Tip:   ________________  |")
print("|    Total: ________________  |")
print("|                             |")
print("|    Sign  X________________  |")
print("-------------------------------")
