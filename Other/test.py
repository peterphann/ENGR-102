nums = [-1]

maximum = sum(nums)

for i in range(len(nums)):
  for j in range(i + 1, len(nums)):
    print(i, j)
    if sum(nums[i:j]) > maximum:
      maximum = sum(nums[i:j])
print(maximum)