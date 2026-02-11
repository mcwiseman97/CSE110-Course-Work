import random

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