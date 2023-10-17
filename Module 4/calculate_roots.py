# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 4.19
# Date:         5 September 2023

from math import *

a = float(input('Please enter the coefficient A: '))
b = float(input('Please enter the coefficient B: '))
c = float(input('Please enter the coefficient C: '))
discriminant = b ** 2 - (4 * a * c)
imaginary = discriminant < 0

# Check discriminant to see number of solutions
if (a != 0):
  if (discriminant != 0):
    if not imaginary:
      print(f'The roots are x = {(-b + sqrt(discriminant)) / 2 * a} and x = {(-b - sqrt(discriminant)) / 2 * a}') # Real Solutions
    else:
      print(f'The roots are x = {-b / 2 * a} + {sqrt(abs(discriminant)) / 2 * a}i and x = {-b / 2 * a} - {sqrt(abs(discriminant)) / 2 * a}i') # Imaginary Solutions
  else:
    print(f'The root is x = {-b / 2 * a}') # One Solution
elif (b != 0):
  print(f'The root is x = {-c / b}') # Linear Equation
else:
  print('You entered an invalid combination of coefficients!') # Constant :(
