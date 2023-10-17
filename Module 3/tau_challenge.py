# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 3.19
# Date:         30 August 2023

from math import pi # Only imports the pi variable from math

tau = 2 * pi
precision = int(input('Please enter the number of digits of precision for tau: '))
print(f'The value of tau to {precision} digits is: {tau:.{precision}f}')
