# A number is called a PPDI of power n if the sum of its digits to the power n equals the number itself.
# ------------------------------
# For example, 8208 is a PPDI of power 4 because
# 8^4 + 2^4 + 0^4 + 8^4 = 8208
# ------------------------------
# Given a number and a power, print whether or not the number is a PPDI
# Assume the number is a 4-digit number.
# ------------------------------
# Sample inputs:

# Enter a number: 1634
# Enter a power: 4
# 1634 is a PPDI of power 4!

# Enter a number: 9132
# Enter a power: 6
# 9132 is NOT a PPDI of power 6!

number = int(input('Enter a number: '))
power = int(input('Enter a power: '))

digit_1 = number // 1000
digit_2 = (number % 1000) // 100
digit_3 = (number % 100) // 10
digit_4 = number % 10
sum = (digit_1 ** power) + (digit_2 ** power) + (digit_3 ** power) + (digit_4 ** power)

if sum == number:
  print(f'{number} is a PPDI of power {power}!')
else:
  print(f'{number} is NOT a PPDI of power {power}!')



  