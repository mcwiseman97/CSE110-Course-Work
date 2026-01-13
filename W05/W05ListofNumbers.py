import math

num_choice = 2
num_list = []

print("Enter a list of numbers, type 0 when finished.")
i = 0
while num_choice != 0:
    num_choice = int(input("Enter number: "))
    if num_choice != 0:
        num_list.append(num_choice)
        i = i + 1
    else:
        continue
print()

print(f"The sum is: {sum(num_list)}")

average_list = sum(num_list) / len(num_list)

print(f"The average is: {average_list}")
print(f"The largest number is: {max(num_list)}")