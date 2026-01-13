with open("CSE110/W06/life-expectancy.csv") as census:
    next(census)
    choice_year = int(input("What year are you checking for:\n"))

    overall_max = (-1, "", 0)
    overall_min = (100, "", 0)
    year_max = (-1, "")
    year_min = (100, "")

    for country, _, year, exp in (line.strip().split(",") for line in census):
        year, exp = int(year), float(exp)

        overall_max = max(overall_max, (exp, country, year))
        overall_min = min(overall_min, (exp, country, year))

        if year == choice_year:
            year_max = max(year_max, (exp, country))
            year_min = min(year_min, (exp, country))

    print(f"\nThe overall max life expectancy is {overall_max[0]} from {overall_max[1]} in {overall_max[2]}.")
    print(f"The overall min life expectancy is {overall_min[0]} from {overall_min[1]} in {overall_min[2]}.\n")

    print(f"For the year {choice_year}:")
    print(f"The max life expectancy was in {year_max[1]} with {year_max[0]}.")
    print(f"The min life expectancy was in {year_min[1]} with {year_min[0]}.")
