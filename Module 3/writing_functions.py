# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 3.18
# Date:         30 August 2023

from math import *

# Define functions for each shape
def triangle_area(side):
    return sqrt(3) * (side ** 2) / 4

def square_area(side):
    return side * side

def pentagon_area(side):
    return (1 / 4) * sqrt(5 * (5 + 2 * sqrt(5))) * (side * side)

def dodecagon_area(side):
    return 3 * (2 + sqrt(3)) * (side * side)

side_length = float(input('Please enter the side length: '))
print(f'A triangle with side {side_length:.2f} has area {triangle_area(side_length):.3f}')
print(f'A square with side {side_length:.2f} has area {square_area(side_length):.3f}')
print(f'A pentagon with side {side_length:.2f} has area {pentagon_area(side_length):.3f}')
print(f'A dodecagon with side {side_length:.2f} has area {dodecagon_area(side_length):.3f}')