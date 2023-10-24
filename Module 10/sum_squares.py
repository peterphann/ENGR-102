# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 10.13
# Date:         23 October 2023

from time import time
from math import sqrt

# def list_nums(n):
#     '''chatgpt solution'''
#     for a in range(1, n):
#         for b in range(a, n):
#             for c in range(b, n):
#                 for d in range(c, n):
#                     if a**2 + b**2 + c**2 + d**2 == n:
#                         return [a, b, c, d]

def list_nums(n):
  nums = []
  while n != 0:
    nums += [int(sqrt(n))]
    n -= int(sqrt(n)) ** 2
  return nums

print(list_nums(15))

# # how to measure how long your function takes to run:
# t1 = time() # get start time
# print(list_nums(15)) # run function
# t2 = time() # get end time
# print(f"This took {t2-t1} seconds") # print result