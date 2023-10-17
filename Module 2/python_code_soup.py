# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 2.11
# Date:         23 August 2023

# 1
x = 1
z = 0
z += x
print(z)

# 27
y = 10
x += 1
x += 1
y += x
z += y
z += y
print(z)

# 102
y = 10
x = y
z = 0
y *= x
x = 1
x += 1
z += y
z += x
print(z)

# 1000000000000
y = 10
x = y
y *= x
y *= x
x = y
y *= x
x = y
y *= x
z = 0
z += y
print(z)

# 8675
y = 10
x = y
z = 0
y += x
x = y
y *= x
y *= x
z += y

y = 10
y *= x
z += y
z += y
z += y
z += x
z += x
z += x
y = 10
z += y
x = 1
x += 1
x += 1
x += 1
x += 1
z += x
print(z)

