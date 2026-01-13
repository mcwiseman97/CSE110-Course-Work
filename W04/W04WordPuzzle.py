"""
Author: Michael Wiseman
Assignment:
date: 1/10/26
"""

# Wordle Style Game

"""
Criteria
An underscore _ indicates that the letter was not present in the secret word.

A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)


MIDWEEK EXPECTATIONS
1. Have a secret word stored in the program.

2. Prompt the user for a guess.

3. Continue looping as long as that guess is not correct.

4. Calculate the number of guesses and display it at the end.

"""

correct_word = "computer"
correct_length = len(correct_word)


print("Welcome to the word guessing game!")
print()
print("Your hint is: _ _ _ _ _ _ _ _")

guess = ""
guess_count = 0

while guess != correct_word:
    guess = input("What is your guess? ")
    guess_length = len(guess)
    guess_count = guess_count + 1
    if guess_length != correct_length:
        print(f"Sorry, the guess must have {correct_length} letters.")
        continue #continue indicates that we can now skip current loop and move on to the next loop
    
    #l_list means letter list (For results of the guess)
    l_list = [""] * correct_length

    for i in range(correct_length):
        if guess[i] == correct_word[i]:
            l_list[i] = guess[i].upper()
        elif guess[i] in correct_word:
            l_list[i] = guess[i].lower()
        else:
            l_list[i] = "_"
    
    for letter in l_list:
        print(letter, end=" ") # using " " instead of "" allows for there to be a space between letters
    print()

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")






"""
ORIGINAL ATTEMPT
print("Welcome to the word guessing game!")
print()

correct_word = "computer"
correct_word_length = len(correct_word)

trigger = True

guess = ""
guess_count = 0

guess = input("What is your guess? ").lower()

guess_length = len(guess)


if guess_length != correct_word_length:
    print("Your word is not the right legth. Try again")
else:
    
    i = 0
    # Lines up the index to the corrisponding appleletter in correct word
    for index in range(correct_word_length):
        print(index, end="")
        print(correct_word[i], end="")
        print(guess[i])
        i = i + 1


    print()

    # Verifying matches - Displays matches in the correct index
    i = 0
    while i < 8:
        if correct_word[i] == guess[i]:
            print(f"{correct_word[i].upper()} ", end="")
            i = i +1
        else:
            print("_ ", end="")
            i = i + 1
    print()


# return index of matching letters in wrong locations

"""
