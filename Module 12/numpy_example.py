# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan  
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 12.12
# Date: 6 November 2023

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

import numpy as np

A = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
B = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
C = np.array([[0, 1, 2], [3, 4, 5]])
D = A @ B @ C
D_tranpose = np.transpose(D)
E = np.sqrt(D) / 2

print(f'A = {A}\n')
print(f'B = {B}\n')
print(f'C = {C}\n')
print(f'D = {D}\n')
print(f'D^T = {D_tranpose}\n')
print(f'E = {E}')