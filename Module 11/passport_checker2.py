# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan  
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 11.10
# Date: 1 November 2023

def check_range(value, range):
  '''Returns whether or not a given value is in a range, represented by a tuple'''
  return value >= range[0] and value <= range[1]

def parse_passport(passport):
  passport = passport.replace('\n', ' ')
  pairs = passport.split(' ')
  map = dict(value.split(':') for value in pairs)
  print(map)

def is_valid(passport):
  '''Returns a boolean value representing whether a given passport is valid'''
  
  checks = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
  
  # Clean passport string and isolate keys
  passport = passport.replace('\n', " ")
  pairs = passport.split(' ')
  keys = [pair.split(':')[0] for pair in pairs]
  
  for key in keys:
    if key in checks:
      checks.remove(key)
    else:
      return False
    
  return (checks == [] or checks == ['ecl'])
  
# Open the file provided and get passports
file_name = 'scanned_passports.txt' #input('Enter the name of the file: ')
file = open(file_name)
passports = file.read().split('\n\n')
file.close()

# Loop through each passport and write to valid passports if valid
output_file = open('valid_passports.txt', 'w')
parse_passport(passports[0])

# valid = 0
# for passport in passports:
#   if is_valid(passport):
#     valid += 1
#     output_file.write(passport + "\n\n")
# output_file.close()

# print(f'There are {valid} valid passports')