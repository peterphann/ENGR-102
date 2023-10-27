# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 10.13
# Date:         23 October 2023

from time import time
from math import sqrt, ceil

def limit(n):
  # Get limit of number
  if n < 0:
    return 0
  else:
    return ceil(sqrt(n)) + 1

def list_nums(n):
  # Get maximum number that the term could potentially be
  lim = limit(n)
  # For each term, loop from 0 to the limit and see if it equals n
  for a in range(0, lim):
      for b in range(a, limit(n - a**2)):
          for c in range(b, limit(n - a**2 - b**2)):
              for d in range(c, limit(n - a**2 - b**2 - c**2)):
                  if a**2 + b**2 + c**2 + d**2 == n:
                      return [a, b, c, d]
                     
def count_sets(n):
  # Same process as list_nums but keep track of valid numbers
  count = 0
  limit = ceil(sqrt(n)) + 1
  for a in range(0, limit):
      for b in range(a, limit):
          for c in range(b, limit):
              for d in range(c, limit):
                  if a**2 + b**2 + c**2 + d**2 == n:
                      count += 1
  return count

# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(15)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result