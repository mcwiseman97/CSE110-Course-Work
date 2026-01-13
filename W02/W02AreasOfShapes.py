"""
Author: Michael Wiseman
Assignment: Area of Shapes
Coursework from https://byui-cse.github.io/cse110-ww-course/week02/code-along.html

Date: 1/8/26
"""
import math #importing math for Pi


# Area of a SQUARE           - Area = Length squared

# Area of a Rectangle        - Area = Length * Width

# Area of a Circle           - Area = Pi * Radius squared


#Square
square_length = float(input("What is the length of one side of the square? "))
square_area = square_length * square_length
print(f"The are of the square is: {square_area:.1f}")

print()

rectangle_length = float(input("What is the length of one side of the rectangle? "))
rectangle_width = float(input("What is the width of one side of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The are of the rectangle is: {rectangle_area:.1f}")

print()

circle_radius = float(input("What is the radius of the circle: "))
circle_area = math.pi * (circle_radius ** 2)
print(f"The are of the circle is: {circle_area:.1f}")