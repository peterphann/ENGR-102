# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 7.27
# Date:         25 September 2023

# Convert string list to integer list
strings = input('Enter numbers: ').split(' ')
numbers = [int(i) for i in strings]

# Loop through different splicings and compare sums
possible = False
for i in range(1, len(numbers)):
  list1 = numbers[0:i]
  list2 = numbers[i:]

  sum1 = 0
  sum2 = 0
  for num in list1:
    sum1 += num
  for num in list2:
    sum2 += num

  if sum1 == sum2:
    print(f'Left: {list1}')
    print(f'Right: {list2}')
    print(f'Both sum to {sum1}')
    possible = True
    break

if not possible:
  print('Cannot split evenly')

  