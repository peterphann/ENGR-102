import matplotlib.pyplot as plt
import numpy as np
from math import *
import matplotlib as mpl

xy = np.linspace(-10, 10, 100, endpoint=True)
x_vals = []
y_vals = []
z_vals = []

for x in xy:
  for y in xy:
    x_vals += [x]
    y_vals += [y]
    try:
      #z_vals += [x**2 + y**2 - 9]
      z_vals += [sin(cos(x**2 * y))]
    except ValueError:
      z_vals += [0]
    

plt.scatter(x_vals, y_vals, c=z_vals, marker='s')
plt.colorbar()
plt.show()