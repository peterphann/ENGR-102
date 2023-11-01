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

def check_color(color):
  '''Returns whether a hexadecimal color is valid'''

  valid_characters = '0123456789ABCDEFabcdef'
  if color[0] != '#' or len(color) != 7:
    return False
  color = list(color)[1:]
  
  for character in color:
    if character not in valid_characters:
      return False
  return True

def check_height(height):
  '''Returns whether a given height is valid'''
  if 'cm' in height:
    height = height.strip('cm')
    return check_range(int(height), (150, 193))
  elif 'in' in height:
    height = height.strip('in')
    return check_range(int(height), (59, 76))
  else:
    return False

def check_countryid(id):
  '''Returns whether a given country ID is valid'''
  stripped = id.lstrip('0')
  return stripped.isdigit() and len(stripped) == 3

def check_range(value, range):
  '''Returns whether or not a given value is in a range, represented by a tuple'''
  return value >= range[0] and value <= range[1]

def parse_passport(passport):
  '''Returns a dictionary with key-value pairs representing a given passport'''
  passport = passport.replace('\n', ' ')
  pairs = passport.split(' ')
  keys = dict(value.split(':') for value in pairs)
  return keys

def is_valid(passport):
  '''Returns a boolean value representing whether a given passport is valid'''
  
  checks = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
  passport = parse_passport(passport)
  
  for key in passport:
    if key in checks:
      checks.remove(key)
    else:
      return False
  
  # Run through all the checks :D
  if (checks != [] and checks != ['ecl']): return False
  if not check_range(int(passport['byr']), (1920, 2007)): return False
  if not check_range(int(passport['iyr']), (2013, 2023)): return False
  if not check_range(int(passport['eyr']), (2023, 2033)): return False
  if not check_height(passport['hgt']): return False
  if not check_color(passport['hcl']): return False
  if len(passport['pid']) != 9: return False
  if not check_countryid(passport['cid']): return False

  return True
  
# Open the file provided and get passports
file_name = input('Enter the name of the file: ')
file = open(file_name)
passports = file.read().split('\n\n')
file.close()

# Loop through each passport and write to valid passports if valid
output_file = open('valid_passports2.txt', 'w')

valid = 0
for passport in passports:
  if is_valid(passport):
    valid += 1
    output_file.write(passport + "\n\n")
output_file.close()

print(f'There are {valid} valid passports')