"""
Author: Michael Wiseman
Assignment:
date: 1/9/26
"""

import random

# Variable declaration
play_again = "yes"

# If player says yes, the game restarts
while play_again == "yes":

    # Random number resets very time the player want to play again and setsd guess to 0 agiain
    random_number = random.randint(1,10)
    print(random_number)
    guess = 0
    
#Loop until answer is correct
    while guess != random_number:
        guess = int(input("What do you guess the number is? "))
        if guess > random_number:
            print("Lower")
        elif guess < random_number:
            print("Higher")
        else:
            break # Inestead of posting a message, just break the line
    print()
    print(f"Great job! {guess} was the correct number!")
    play_again = input("Would you like to play again? ").lower()

print()
print(f"Thanks for playin!")

