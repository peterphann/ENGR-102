# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 4.14
# Date: 5 September 2023

# Prompt for input
a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))

output = ""

if a != 0:
  output += f'{"+" if a > 0 else "-"} {abs(a) if abs(a) != 1 else ""}x^2 '
if b != 0:
  output += f'{"+" if b > 0 else "-"} {abs(b) if abs(b) != 1 else ""}x '
if c != 0:
  output += f'{"+" if c > 0 else "-"} {abs(c)} '
if output[0] == '+':
  output = output[2:]

print(f'The quadratic equation is {output}= 0')


