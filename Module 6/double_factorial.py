# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 6.14
# Date:         21 September 2023

def doublefactorial(num):
  if num == 0: return 1

  current = num
  result = 1

  # Decrement by 2 on each passing
  while (current > 0):
    result *= current
    current -= 2
  
  return result