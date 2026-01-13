"""
Author: Michael Wiseman
Assignment: Grade Calculator
Date:1/8/26
"""

# Second attempt while following the code along

grade_percent = float(input("What percent do you have? "))
letter_grade = ""
sign = ""

if grade_percent >= 90:
    letter_grade = "A"
elif grade_percent >= 80:
    letter_grade = "B"
elif grade_percent >= 70:
    letter_grade = "C"
elif grade_percent >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"  

ending_number = grade_percent % 10

if ending_number >= 7:
    sign = "+"
elif ending_number <= 3:
    sign = "-"
else:
    sign = ""

print(f"Your letter grade is {letter_grade}{sign}.")
if grade_percent >= 70:
    print("Congradulation! You are doing a fantastic job!")
else:
    print("You got this! Keep studying and make sure to get support when you need it!")



# My orginal code attempt
"""
grade_percent = float(input("What percent do you have? "))
letter_grade = ""

if grade_percent >= 90:
    if grade_percent >= 97:
        letter_grade = "A+"
    elif grade_percent < 97 and grade_percent >= 94:
        letter_grade = "A"
    else:
        letter_grade = "A-"
elif grade_percent >= 80:
    if grade_percent >= 87:
        letter_grade = "B+"
    elif grade_percent < 87 and grade_percent >= 84:
        letter_grade = "B"
    else:
        letter_grade = "B-"      
elif grade_percent >= 70:
    if grade_percent >= 77:
        letter_grade = "c+"
    elif grade_percent < 77 and grade_percent >= 74:
        letter_grade = "c"
    else:
        letter_grade = "c-"        
elif grade_percent >= 60:
    if grade_percent >= 67:
        letter_grade = "D+"
    elif grade_percent < 67 and grade_percent >= 64:
        letter_grade = "D"
    else:
        letter_grade = "D-"          
else:
    letter_grade = "F"       
        
        
print(f"Your letter grade is {letter_grade}.")

"""