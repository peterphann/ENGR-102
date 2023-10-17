# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 7.28
# Date:         25 September 2023

# Define function to convert list of digits to an integer
def combine_list(digits):
  return int(''.join(digits))

start = int(input('Enter a four-digit integer: '))

print(start, end='')
number = start
iterations = 0

while number != 6174 and number != 0:
  iterations += 1

  # Determine big and lower integers, pad with 0s as necessary
  lower = list(str(number))
  lower += ['0'] * (4 - len(lower))
  lower.sort()
  upper = lower[::-1]
  
  number = combine_list(upper) - combine_list(lower)
  print(f' > {number}', end='')

# Print output
print(f'\n{start} reaches {number} via Kaprekar\'s routine in {iterations} iterations')