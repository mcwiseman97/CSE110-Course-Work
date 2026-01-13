"""
Author: Michael Wiseman
Assignement: Computing area
Date: 1/12/26
"""
import math

def compute_area_square(length):
    square_area = length * length
    return square_area
def compute_area_rectangle(length, width):
   rectangle_area = length * width
   return rectangle_area
def compute_area_circle(radius):
   circle_area = math.pi * (radius ** 2)
   return circle_area
   
shape = ""


while shape != "quit":
    print()
    shape = input("What shape do you have? ").lower()
    if shape == "square":
      print()
      square_length = float(input("What is the length of one side of the square? "))
      square_area = compute_area_square(square_length) 
      print(f"The area of this square is: {square_area}")
      break 
    elif shape == "rectangle":
       print()
       rectangle_length = float(input("What is the length of one side of the rectangle? "))
       rectangle_width = float(input("What is the width of one side of the rectangle? "))
       rectangle_area = compute_area_rectangle(rectangle_length, rectangle_width)
       print(f"The area of this rectangle is: {rectangle_area}")
       break
    elif shape == "circle":
       print()
       circle_radius = float(input("What is the radius of the circle: "))
       circle_area = compute_area_circle(circle_radius)
       print(f"The area of this circle is: {circle_area}")
       break
    else:
       continue
if shape == "quit":
    print()
    print("Have a great day!")
else:  
    print()
    print(f"Your computed the area of a {shape}!")
    print()

