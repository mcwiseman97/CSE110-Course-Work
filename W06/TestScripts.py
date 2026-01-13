# if the refrence file is not in the same directory as the python script or the
#  programs main folder, you will need to specify the static location.

with open("CSE110/W06/courses.txt") as courses_file:


    for line in courses_file:
        print(line.strip()) #Stip take the extra white spaces away that are not associate to the variable itself.



# This is practice for the split operator
something = "This is a test to split."

something_list = something.split() # You can split based on a defined marker like a "","" placed in the () after split

print(something_list)