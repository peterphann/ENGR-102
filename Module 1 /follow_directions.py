# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 1.13
# Date:         21 August 2023

from math import *

print("This shows the evaluation of sin(x - 1)/(x - 1) evaluated close to x=1.")
print("My guess is 1\n")

# Calculations:
print(sin(1.1 - 1) / (1.1 - 1))
print(sin(1.01 - 1) / (1.01 - 1))
print(sin(1.001 - 1) / (1.001 - 1))
print(sin(1.0001 - 1) / (1.0001 - 1))
print(sin(1.00001 - 1) / (1.00001 - 1))
print(sin(1.000001 - 1) / (1.000001 - 1))
print(sin(1.0000001 - 1) / (1.0000001 - 1))
print(sin(1.00000001 - 1) / (1.00000001 - 1))

print("\nMy guess was correct")


