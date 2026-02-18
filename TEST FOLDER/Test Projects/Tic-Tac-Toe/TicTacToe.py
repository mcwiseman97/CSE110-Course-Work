import random

# TODO: Fix the tic tac toe board to display the correctly so the lines dont move when an X or O is placed on the board.
# TODO: Make the console switch between player after each move.
# TODO: Make the console clear after each move.
# TODO: end the game if 3 spots in a row are filled with the same letter.


print("\nWelcome to the game of Tic Tac Toe!\n")
users = ["",""]
users[0] = input("What is the first players name? ").capitalize()
users[1] = input("\nWhat is the second players name? ").capitalize()

print(f"Welcome {users[0]} and {users[1]}! Best of luck!\n")

starter = random.randint(0,1)

aa = ""
ab = ""
ac = ""

ba = ""
bb = ""
bc = ""

ca = ""
cb = ""
cc = ""

gamestatus = True
print(f"{users[starter]}, You will go first.\n")

#while gamestatus:
choice = input("What cell do you want to choose? (EX: a1)")

if choice == "a1":
    aa = "o"

if choice == "a2":
    ab = "o"

if choice == "a3":
    ac = "o"

if choice == "b1":
    ba = "o"

if choice == "b2":
    bb = "o"

if choice == "b3":
    bc = "o"

if choice == "c1":
    ca = "o"

if choice == "c2":
    cb = "o"

if choice == "c3":
    cc = "o"

if choice == "a1":
    aa = "x"

if choice == "a2":
    ab = "x"

if choice == "a3":
    ac = "x"

if choice == "b1":
    ba = "x"

if choice == "b2":
    bb = "x"

if choice == "b3":
    bc = "x"

if choice == "c1":
    ca = "x"

if choice == "c2":
    cb = "x"

if choice == "c3":
    cc = "x"

print("   A       B       C  ")
print("        |       |      ")
print(f"1    {aa}   |   {ba}    |   {ca}  ")
print("  _ _ _ | _ _ _ | _ _ _")
print("        |       |      ")
print(f"2    {ab}   |   {bb}    |   {cb}  ")
print("  _ _ _ | _ _ _ | _ _ _")
print("        |       |      ")
print(f"3    {ac}   |   {bc}    |   {cc}  ")
print("        |       |      ")