# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 3.16
# Date: 1 September 2023

time1 = float(input('Enter time 1: '))
x1 = float(input('Enter the x position of the object at time 1: '))
y1 = float(input('Enter the y position of the object at time 1: '))
z1 = float(input('Enter the z position of the object at time 1: '))
time2 = float(input('Enter time 2: '))
x2 = float(input('Enter the x position of the object at time 2: '))
y2 = float(input('Enter the y position of the object at time 2: '))
z2 = float(input('Enter the z position of the object at time 2: '))

slope_x = (x2 - x1) / (time2 - time1)
slope_y = (y2 - y1) / (time2 - time1)
slope_z = (z2 - z1) / (time2 - time1)

# Interpolate Function
def interpolate(time):
    x = slope_x * (time - time1) + x1
    y = slope_y * (time - time1) + y1
    z = slope_z * (time - time1) + z1
    print(f'At time {time:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})')

interval = (time2 - time1) / 4
interpolate(time1)
interpolate(time1 + interval)
interpolate(time1 + 2 * interval)
interpolate(time1 + 3 * interval)
interpolate(time2)


