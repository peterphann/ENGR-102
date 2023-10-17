# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 2.9
# Date:         23 August 2023

from math import *

# Newton's Second Law (F = ma)
mass = 27
acceleration = 1.5
force = mass * acceleration
print("Force is", force, "N")

# Bragg's Law (nλ = 2dsin(θ))
distance = 0.025
angle = 35
wavelength = 2 * distance * sin(angle * pi/180)
print("Wavelength is", wavelength, "nm")

# Radioactive Decay (N(t) = N₀ * 2^(-t / t_half))
time = 5
initial_amount = 27
half_life = 3.8
remaining_radon = initial_amount * 2 ** (-(time / half_life))
print("Radon-222 left is", remaining_radon, "g")

# Ideal Gas Law (PV = nRT)
volume = 0.27
temperature = 415
gas_constant = 8.314
moles = 5
pressure = (moles * gas_constant * temperature) / volume
pressure /= 1000 # Convert to kPa
print("Pressure is", pressure, "kPa")