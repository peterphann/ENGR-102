# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 4.16
# Date:         5 September 2023

num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
num3 = float(input('Enter number 3: '))

# Compare numbers
if num2 > num1: num1 = num2
if num3 > num1: num1 = num3

print(f'The largest number is {num1}')