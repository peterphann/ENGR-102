# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Claudia Phan
#               Olivia Goralski
#               Peter Phan
#               Benjamin Sandefur
# Section:      521
# Assignment:   LAB: Matplotlib Example
# Date:         17 November 2023

import numpy as np
import matplotlib.pyplot as plt

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

# Plot 1
x1 = np.linspace(-2, 2, 100)
def func(f, x):
    return (1 / (4*f)) * (x**2)
z1 = func(2, x1)
z2 = func(6, x1)

fig, ax = plt.subplots()
ax.plot(x1, z1, color='red', linewidth=2, label='f=2')
ax.plot(x1, z2, color='blue', linewidth=6, label='f=6')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Parabola plots with varying focal length")
ax.legend()
plt.show()


# Plot 2
x2 = np.linspace(-4, 4, 25)
y2 = 2*x2**3 + 3*x2**2 - 11*x2 -6
fig, ax = plt.subplots()
ax.scatter(x2, y2, marker = "*", color = "yellow", edgecolors = "black", s = 100)
ax.set_ylabel("y values")
ax.set_xlabel("x values")
ax.set_title("Plot of cubic polynomial")
plt.show()

# Plot 3
x3 = np.linspace(-2*np.pi, 2*np.pi)
fig, axs = plt.subplots(2)
plt.setp(axs, yticks=[-1,0,1])
axs[0].tick_params(labelbottom = False)
axs[0].plot(x3, np.cos(x3), color = 'red', label='cos(x)')
axs[1].plot(x3, np.sin(x3), color = 'gray', label='sin(x)')
axs[0].set_title("Plot of cos(x) and sin(x)")
axs[0].set_ylabel("y=cos(x)")
axs[1].set_ylabel("y=sin(x)")
axs[1].set_xlabel("x")
axs[0].grid()
axs[1].grid()
axs[0].legend(loc='lower right')
axs[1].legend(loc='upper right')
plt.show() 