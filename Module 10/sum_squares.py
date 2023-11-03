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

def list_nums(n):
  # Get maximum number that a term could potentially be
  lim = ceil(sqrt(n) + 1)

  # Create dictionary with squares to avoid repeat computations
  squares = {}
  for i in range(lim):
      squares[i] = i**2
  
  # For each term, loop from 0 to the limit and see if it equals n
  for a in range(0, lim):
      for b in range(a, lim):
          for c in range(b, lim):
              for d in range(c, lim):
                  if squares[a] + squares[b] + squares[c] + squares[d] == n:
                      return [a, b, c, d]
                     
def count_sets(n):
  # Same as list_nums() but count number of valid sets
  lim = ceil(sqrt(n) + 1)

  squares = {}
  for i in range(lim):
      squares[i] = i**2
  
  count = 0
  for a in range(0, lim):
      for b in range(a, lim):
          for c in range(b, lim):
              for d in range(c, lim):
                  if squares[a] + squares[b] + squares[c] + squares[d] == n:
                      count += 1
  return count

# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(15)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result