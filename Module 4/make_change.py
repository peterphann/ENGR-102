# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 4.13
# Date: 5 September 2023

amount_paid = float(input('How much did you pay? '))
amount_cost = float(input('How much did it cost? '))

change = amount_paid - amount_cost
print(f'You received ${change:.2f} in change. That is...')

# Multiply to avoid floating-point weirdness AHHHHH
change = round(change * 100)

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change

if quarters >= 1: print(f'{quarters:.0f} {"quarter" if quarters == 1 else "quarters"}')
if dimes >= 1: print(f'{dimes:.0f} {"dime" if dimes == 1 else "dimes"}')
if nickels >= 1: print(f'{nickels:.0f} {"nickel" if nickels == 1 else "nickels"}')
if pennies >= 1: print(f'{pennies:.0f} {"penny" if pennies == 1 else "pennies"}')