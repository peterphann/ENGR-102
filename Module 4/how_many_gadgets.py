# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 4.18
# Date:         5 September 2023

def calculate_gadgets(num):
  gadgets = min(num, 10) * 10
  if (num > 10):
    ramp = min(num - 10, 40)
    gadgets += int(ramp * (ramp + 21) / 2)
  if (num > 50):
    maximum = min(num - 50, 50)
    gadgets += 50 * maximum
  return gadgets

# Prompt for input
day = int(input('Please enter a positive value for day: '))
if (day <= 0):
  print('You entered an invalid number!')
else:
  print(f'The sum total number of gadgets produced on day {day} is {calculate_gadgets(day)}')

