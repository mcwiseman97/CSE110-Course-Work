"""
Author: Michael Wiseman
Assignment:
Date: 1/12/26
"""

with open("CSE110/W06/books.txt") as books:
    for line in books:
        print(line.strip())