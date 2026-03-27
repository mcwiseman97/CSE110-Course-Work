"""
Author: Michael Wiseman
Assignment:
date: 3/27/26
"""

"""
Used import random
I added to this assignment a list of words and a randomizer so that each time a player starts, they will have to figure out the new word.
With this, i made the program check the length of the word to dynamically show the correct hint length.
"""
import random

word_list = ["computer", "banana", "apple", "orange", "grape"]

random_word = random.choice(word_list)
correct_length = len(random_word)

print("Welcome to the word guessing game!")
print("Your hint is:", end=" ")
for i in range(correct_length):
    print("_ ", end="")

guess = ""
guess_count = 0

while guess != random_word:
    guess = input("\nWhat is your guess? ")
    guess_length = len(guess)
    guess_count = guess_count + 1
    if guess_length != correct_length:
        print(f"Sorry, the guess must have {correct_length} letters.")
        continue #continue indicates that we can now skip current loop and move on to the next loop
    
    #l_list means letter list (For results of the guess)
    l_list = [""] * correct_length

    for i in range(correct_length):
        if guess[i] == random_word[i]:
            l_list[i] = guess[i].upper()
        elif guess[i] in random_word:
            l_list[i] = guess[i].lower()
        else:
            l_list[i] = "_"
    
    for letter in l_list:
        print(letter, end=" ") # using " " instead of "" allows for there to be a space between letters
    print()

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
