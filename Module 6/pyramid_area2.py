# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 6.11
# Date: 21 September 2023

from math import *

side_length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))

# All of the summations can be rewritten as the sum of numbers 1 - n or sum of squares of the numbers from 1 - n
# Just take out the constants and rewrite

sum_layers = ((layers * (layers + 1)) / 2)
sum_layers_squared = ((layers * (layers + 1) * (2 * layers + 1)) / 6)
sum_layers_squared1 = ((layers - 1) * layers * (2 * layers - 1) / 6)

side_area = 3 * (side_length ** 2) * sum_layers
top_area = (sqrt(3) / 4) * (side_length ** 2) * sum_layers_squared
obscured_area = (sqrt(3) / 4) * (side_length ** 2) * sum_layers_squared1

area = side_area + top_area - obscured_area
print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')
