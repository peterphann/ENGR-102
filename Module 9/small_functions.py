# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 9.16
# Date:         22 October 2023

from math import *

def parta(sphere_radius, hole_radius):
  sphere_volume = (4 / 3) * pi * sphere_radius**3

  cylinder_height = sqrt(sphere_radius**2 - hole_radius**2)
  cap_height = sphere_radius - cylinder_height

  # Cylinder and caps heights represent half of the overall volume
  cylinder_volume = pi * hole_radius**2 * cylinder_height
  cap_volume = (pi * cap_height**2) / 3 * (3 * sphere_radius - cap_height)

  # Multiply volume by 2
  parta_volume = 2 * (cylinder_volume + cap_volume)

  return sphere_volume - parta_volume

def partb(n):
  # Loop through all possible strating integers
  for i in range(1, int(n / 2), 2):
    sum = 0
    num = i
    values = []

    # Sum adjacent odd numbers until value is greater than or equal to n
    while sum < n:
      values += [num]
      sum += num
      num += 2
    
    if sum == n:
      return values
  return False

    

def partc(character, name, school, email):
  # Find max length of arguments
  max_length = max(len(name), len(school), len(email))

  result = character * (max_length + 6) + f'\n{character}  {name:^{max_length}}  {character}' + f'\n{character}  {school:^{max_length}}  {character}' + f'\n{character}  {email:^{max_length}}  {character}\n' + character * (max_length + 6)
  return result

def partd(list):
  minimum = min(list)
  maximum = max(list)

  # Get median of list depending on length
  list = sorted(list)
  if len(list) % 2 == 1:
    median = list[int(len(list) / 2)]
  else:
    median = (list[int(len(list) / 2 - 1)] + list[int(len(list) / 2)]) / 2

  return minimum, median, maximum

def parte(times, distances):
  # Initialzie empty list
  velocities = []

  # Loop from index 0 to n - 1
  for i in range(len(times) - 1):
    # Calculate differences in adjacent times and distances
    delta_time = times[i + 1] - times[i]
    delta_distance = distances[i + 1] - distances[i]
    
    # Calculate velocity and add to list
    velocities += [delta_distance / delta_time]
  return velocities

def partf(list):
  # Loop through possible combinations of numbers and see if they add to 2027
  for i in range(0, len(list) - 1):
    for j in range(i + 1, len(list)):
      if list[i] + list[j] == 2027:
        return list[i] * list[j]
  return False

def partg(x, tolerance):
  term = tolerance
  sum = 0
  n = 1
  
  # Calculate term at n and add to sum. If below tolerance, exit loop and return
  term = (2 / (2 * n - 1)) * (x ** (2 * n - 1))
  while abs(term) >= tolerance:
    sum += term
    n += 1
    term = (2 / (2 * n - 1)) * (x ** (2 * n - 1))
  return sum

if __name__ == '__main__':
  main()