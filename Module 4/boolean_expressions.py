# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 4.15
# Date: 5 September 2023

############ Part A ############
a = True if input('Enter True or False for a: ') in ['T', 't', 'True'] else False
b = True if input('Enter True or False for b: ') in ['T', 't', 'True'] else False
c = True if input('Enter True or False for c: ') in ['T', 't', 'True'] else False

############ Part B ############
print(f'a and b and c: {a and b and c}')
print(f'a or b or c: {a or b or c}')

############ Part C ############
print(f'XOR: {not a and b or a and not b}')
print(f'Odd number: {int(a + b + c) % 2 == 1}')

############ Part D ############
print(f'Complex 1: {(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)}')
print(f'Complex 2: {(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))}')
print(f'Simple 1: {(not b) or (not a and not c)}')
print(f'Simple 2: {(not b and c) or a}')
