# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 7.29
# Date:         25 September 2023

# Define function to convert list of digits to an integer
def combine_list(digits):
  return int(''.join(digits))

sum = 0
for i in range(10000):
  number = i
  iterations = 0

  while number != 6174 and number != 0:
    iterations += 1

    # Determine big and lower integers, pad with 0s as necessary
    lower = list(str(number))
    lower += ['0'] * (4 - len(lower))
    lower.sort()
    upper = lower[::-1]
    
    number = combine_list(upper) - combine_list(lower)

  # Print output
  sum += iterations

print(f'Kaprekar\'s routine takes {sum} total iterations for all four-digit numbers')