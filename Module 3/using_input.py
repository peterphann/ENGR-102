# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 3.17
# Date:         30 August 2023

from math import *

# Newton's Second Law (F = ma)
print('This program calculates the applied force given mass and acceleration')
mass = float(input('Please enter the mass (kg): '))
acceleration = float(input('Please enter the acceleration (m/s^2): '))
force = mass * acceleration
print(f'Force is {force:.1f} N\n')

# Bragg's Law (nλ = 2dsin(θ))
print('This program calculates the wavelength given distance and angle')
distance = float(input('Please enter the distance (nm): '))
angle = float(input('Please enter the angle (degrees): '))
wavelength = 2 * distance * sin(angle * pi/180)
print(f'Wavelength is {wavelength:.4f} nm\n')

# Radioactive Decay (N(t) = N₀ * 2^(-t / t_half))
print('This program calculates how much Radon-222 is left given time and initial amount')
time = float(input('Please enter the time (days): '))
initial_amount = float(input('Please enter the initial amount (g): '))
half_life = 3.8
remaining_radon = initial_amount * 2 ** (-(time / half_life))
print(f'Radon-222 left is {remaining_radon:.2f} g\n')

# Ideal Gas Law (PV = nRT)
print('This program calculates the pressure given moles, volume, and temperature')
moles = float(input('Please enter the number of moles: '))
volume = float(input('Please enter the volume (m^3): '))
temperature = float(input('Please enter the temperature (K): '))
gas_constant = 8.314
pressure = (moles * gas_constant * temperature) / volume
pressure /= 1000 # Convert to kPa
print(f'Pressure is {pressure:.0f} kPa')
