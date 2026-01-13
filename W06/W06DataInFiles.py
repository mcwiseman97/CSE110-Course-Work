"""
Author: Michael Wiseman
Assignment: Find youngest persons name and age
Date: 12
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

lowest_age = 120
i = 0
for person in people:
    personal_info = person.split()
    name = personal_info[0]
    age = int(personal_info[1])

    if age < lowest_age:
        lowest_age = age
        youngest_person = name
    i += 1   

print(f"{youngest_person} has the lowest age at {lowest_age} years old.")