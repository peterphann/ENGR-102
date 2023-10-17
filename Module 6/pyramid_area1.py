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
area = 0

for layer in range(1, layers + 1):
  # The side of each layer is made of the same number of squares as there are layers.
  # There are 3 sides, so there are n * 3 squares to account for
  side_area = (layer * 3) * (side_length ** 2)

  # The top of each layer is made of (n ** 2) triangles, each with an area of sqrt(3) / 4 * (l ** 2)
  top_area = (sqrt(3) / 4) * (side_length ** 2) * (layer ** 2)

  # The top surface area of the previous layer obscures the current layer, so subtract
  top_area -= (sqrt(3) / 4) * (side_length ** 2) * ((layer - 1) ** 2)

  area += side_area + top_area

print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')
