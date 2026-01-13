"""
Author: Michael Wiseman
Assignmnet: Creating Lists
Date: 1/11/26
"""

friend_name = ""
names = []
i = 0
while friend_name != "end":
    friend_name = input("Type a friends name: ")
    if friend_name == "end":
        continue
    else:
         names.append(friend_name)
         i = i + 1
print()     
print("Thank you for providing your friends names.")
print("Your friends are: ")
for friend in names:
    print(friend)