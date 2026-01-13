"""
Author: Michael Wiseman
Assignment:
date: 1/9/26
"""

# Part 1 and 2

favorite_letter = input("What is your favorite letter in the word 'Commitment'? ").upper()
word = "commitment"
print()

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(favorite_letter, end="")
    else:
        print(letter, end="")
print()






# Part 3

favorite_letter = input("What is your favorite letter in the word 'Commitment'? ").upper()
word = "commitment"
blank = "_"
print()

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(blank, end="")
    else:
        print(letter, end="")
print()
