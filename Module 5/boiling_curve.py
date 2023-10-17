# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 5.4
# Date:         21 September 2023

# Import math module
from math import *

# Define function to calculate flux based on points and temperature given
def calculate_flux(temp, x0, y0, x1, y1):
  slope = log10(y1 / y0) / log10(x1 / x0) # Calculates slope using given formula
  return y0 * ((temp / x0) ** slope)      # Returns heat flux at temperature 'temp' using points given

# Get excess temperature from user, convert to float
excess_temp = float(input('Enter the excess temperature: '))

# Check excess_temp and use corresponding linear interpolation
# If the temperature is out of the range, print an error messahe
if excess_temp < 1.3 or excess_temp > 1200:
  print('Surface heat flux is not available')
# Else, if the temp. is less than or equal to 5, calculate using points 1 and 2
elif excess_temp <= 5:
  heat_flux = calculate_flux(excess_temp, 1.3, 1000, 5, 7000)
  print(f'The surface heat flux is approximately {heat_flux:.0f} W/m^2')
# Else, if the temp. is less than or equal to 5, calculate using points 2 and 3
elif excess_temp <= 30:
  heat_flux = calculate_flux(excess_temp, 5, 7000, 30, 1.5E6)
  print(f'The surface heat flux is approximately {heat_flux:.0f} W/m^2')
# Else, if the temp. is less than or equal to 5, calculate using points 3 and 4
elif excess_temp <= 120:
  heat_flux = calculate_flux(excess_temp, 30, 1.5E6, 120, 2.5E4)
  print(f'The surface heat flux is approximately {heat_flux:.0f} W/m^2')
# Else, if the temp. is less than or equal to 5, calculate using points 4 and 5
elif excess_temp <= 1200:
  heat_flux = calculate_flux(excess_temp, 120, 2.5E4, 1200, 1.5E6)
  print(f'The surface heat flux is approximately {heat_flux:.0f} W/m^2')
