# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 6.16
# Date:         21 September 2023



# Used algebraic formula to calculate sum up to n - 1
for number in range(10000):
  sum1 = (number ** 2 - number) / 2
  sum2 = 0
  r = 0

  while sum2 < sum1:
    sum2 += (number + 1) + r
    r += 1

  if sum1 == sum2:
    print(f'{number} is a balancing number with r={r}')