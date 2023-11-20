# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 12.14
# Date:         17 November 2023

import numpy as np
import matplotlib.pyplot as plt

points = []
point = np.array([1, 0])
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])

points.append(point)
for i in range(250):
  new_point = points[-1] @ matrix
  points.append(new_point)

x = [point[0] for point in points]
y = [point[1] for point in points]

fig, ax = plt.subplots()
ax.set_title('Spiral traced out with matrix multiplication')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
ax.grid()
plt.show()