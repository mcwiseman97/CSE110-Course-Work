"""
Author: Michael Wiseman
Assignment: If Statement Assignement
Date: 1/8/26
"""

first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

# Determin if the first number is greater than the second
# return three statemnts for greater, not greater, or equal
if first_number > second_number:
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
elif first_number < second_number:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")
else:
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")


fav_animal = "monkey"
your_fav_animal = input("What is your favorite animal? ")
your_fav_animal = your_fav_animal.lower()
# Note that you can either add .lower() to the first instance of the variable, 
# or on a new line where you override the variable


if your_fav_animal == fav_animal:
    print("This is my favorite animal too!")
else:
    print("This one is not my favorite.")