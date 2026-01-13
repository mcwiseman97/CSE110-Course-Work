"""
Author: Michael Wiseman
Assignment: While Loops - Negatice/positive - Ask for Candy
date: 1/9/26
"""

# Program that asks for a positive number - Outputs the number if positive, or Asks for a positive number again if its negative
number = -1
while number < 0:
    number = int(input("Please type a positive number: "))
    if number < 0:
        print("Sorry, that is a negative number. Please try again.")
    else:
        print(f"The number is: {number}")
        break






#Asks for cancy until says yes
answer = "no"

while answer == "no":
    answer = input("May I have a piece of candy? ").lower()
    if answer == "yes":
        break
    
print("Thank you!")