# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 2.8
# Date: 1 September 2023

from math import *

# Part 1 
t1 = 10
t2 = 55
d1 = 2027
d2 = 23027

time = 25
position = ((d2 - d1) / (t2 - t1)) * (time - t1) + d1;
print('Part 1:')
print('For t =', time, 'minutes, the position p =', position, 'kilometers')

# Part 2
print('Part 2:')
radius = 6745
circumference = 2 * pi * radius
time = 300
slope = (d2 - d1) / (t2 - t1)
position = (slope * (time - t1) + d1) % circumference;
print('For t =', time, 'minutes, the position p =', position, 'kilometers')
