# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 6.15
# Date:         21 September 2023

from math import *

number = int(input('Enter a positive integer: '))
iterations = 0

# Loop through and calculate number until it equals 1
print(f'The Juggler sequence starting at {number} is:')
while number != 1:
  iterations += 1
  print(f'{number}, ', end='')
  if number % 2 == 0:
    number = floor(sqrt(number))
  else:
    number = floor(number ** (3/2))

# Print the last 1
print('1')
print(f'It took {iterations} iterations to reach {number}')
  