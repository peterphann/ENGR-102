# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 11.12
# Date:         30 October 2023

# Prompt user for input
filename = input('Enter the filename: ')
character = input('Enter a character: ')

# Read file and create contents variable
with open(filename) as file: 
  contents = file.read().split('\n')
  contents = [line.split(',') for line in contents]

# Open output file and write lines
output_file = open(filename[0:-4] + '.txt', 'w')

# Loop through each line and print spaces and characters accordingly
for line in contents:
  space = True
  output = []
  # Get used character and switch
  for value in line:
    used = " " if space else character
    output.append(used * int(value))
    space = not space
  output_file.write(''.join(output) + "\n")
output_file.close()

print(f'{filename[0:-4]}.txt created!')

  