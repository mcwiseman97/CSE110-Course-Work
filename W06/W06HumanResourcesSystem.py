"""
Author: Michael Wiseman
Assignment:
Date:1/12/26
"""

with open("CSE110/W06/hr_system.txt") as hr_system:
    next(hr_system) #Looked up a way to skip the header of a file next() jumps current line
    for emp in hr_system:
        emp_info = emp.split()
        emp_name = emp_info[0]
        emp_id = emp_info[1]
        emp_title = emp_info[2]
        emp_salary = float(emp_info[3]) # change salary to float

        paycheck = emp_salary / 24 # paycheck calculation

        if emp_title == "Engineer":
            paycheck += 1000 # add $1000 bonus to check

        print(f"{emp_name} (ID: {emp_id}), {emp_title} - ${paycheck:.2f}") # Formatting


