"""
Author: Michael Wiseman
Assignment:
Date:
"""

with open("CSE110/W06/life-expectancy.csv") as census:
    next(census)
    choice_year = int(input("What year are you checking for: "))
    print()

    #Variabls for total data set
    all_max_expectancy = -1
    all_max_country = ""
    all_max_year = 0
    all_min_expectancy = 100
    all_min_country = ""
    all_min_year = 0

    #Variables for year that was selected.
    max_expectancy = -1
    max_country = ""
    min_expectancy = 100
    min_country = ""

    for data in census:
        data_list = data.split(",")
        country = data_list[0]
        code = data_list[1]
        year = int(data_list[2])
        expectancy = float(data_list[3])

        # If's to find overall min and max
        if expectancy > all_max_expectancy:
            all_max_expectancy = expectancy
            all_max_year= year
            all_max_country = country
        if expectancy < all_min_expectancy:
            all_min_expectancy = expectancy
            all_min_year = year
            all_min_country = country
        
        # If's to find min's and max's from a specific year
        if choice_year == year and expectancy > max_expectancy:
            max_expectancy = expectancy
            max_country = country
        if choice_year == year and expectancy < min_expectancy:
            min_expectancy = expectancy
            min_country = country

    print(f"The overall max life expectancy is : {all_max_expectancy} from {all_max_country} in {all_max_year}.")
    print(f"The overall max life expectancy is : {all_min_expectancy} from {all_min_country} in {all_min_year}.") 
    print()
    print(f"For the year {choice_year}:")
    print(f"The max life expectancy was in {max_country} is {max_expectancy}.")
    print(f"The min life expectancy was in {min_country} is {min_expectancy}.")
    print()