"""
Docstring for W02.W02NumericVariable
Author: Michael Wiseman
Assignment: Cookie Math
Date 1/8/26
"""

#get users age and incrament by 1
age = int(input("How old are you? "))
newAge = age + 1
print(f"On your next Birthday, you will be, {newAge}")

print()# Blank line insert

#Standard egg count is 12, find the egg count by number of cartson
cartonCount = int(input("How many cartons do you have? "))

eggCount = cartonCount * 12

print(f"You have {eggCount} eggs" )

print() # Blank line insert

#Find how many cookies per person
cookieCount = int(input("How many cookies do you have? "))
peopleCount = int(input("How many people are there? "))

dividedCookies = float(peopleCount / cookieCount) #convert two ints into a float

print(f"Each person may have {dividedCookies} cookies")
