"""
Author: Michael Wiseman
Assignment: Meal Calculator + Tax
Date: 1/8/26
"""

# Gather meal cost
kid_cost = float(input("What is the cost of a child's meal? "))
adult_cost = float(input("What is the cost of an adults meal? "))

# Gather person count
num_kids = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

#calculate total pretax cost
subtotal = (num_adults * adult_cost) + (num_kids * kid_cost)

print(f"Subtotal: ${subtotal:.2f}")

print()

# Gather tax
tax_rate = int(input("What is the sales tax rate? "))
applied_taxes = subtotal * (tax_rate / 100) #convert int into percentage
print(f"Sales Tax: ${applied_taxes}")
total_cost = subtotal + applied_taxes
print(f"Total: ${total_cost:.2f}")

print()

# Calculate amount paid and provide change amount
paid_amount = float(input("What is the payement amount? "))
change = paid_amount - total_cost
print(f"Change: ${change:.2f}")