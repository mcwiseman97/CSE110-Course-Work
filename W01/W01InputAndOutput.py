"""" 
Author: Michael Wiseman
Assignment: Formatting Strings
Date 1/8/26
"""
# Notes are created by typing the pound symbol


firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
print(f"Your name is {lastName}, {firstName} {lastName}.")

# Test of string methods
print(f"Your name is {lastName.lower()}, {firstName.upper()} {lastName.capitalize()}.")