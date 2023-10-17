# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 6.13
# Date:         21 September 2023

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))

for i in range(1, 101):
  # Test if i is divisible by both num1 and num2
  if i % (num1 * num2) == 0:
    print('Howdy Whoop')
  elif i % num1 == 0:
    print('Howdy')
  elif i % num2 == 0:
    print('Whoop')
  else:
    print(i)