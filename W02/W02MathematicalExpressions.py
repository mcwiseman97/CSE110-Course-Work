"""
Author: Michael Wiseman
Assignment: Converting Fehrenheit to Celcius
Date 1/8/26
"""
import math

fahrenheit = int(input("What is the temprature in Fahrenheit? ")) #Fahrenheit is always a full number

celcius = (fahrenheit - 32) * 5 / 9 # Celcius is -32 from Fahrenheit and * 5/9

print(f"The temperature in Celcius is {celcius:.1f} degrees.") # :.1f allows for one decimal point to be shown



 