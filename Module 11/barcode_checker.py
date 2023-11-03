# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 11.11
# Date:         1 November 2023

def valid_barcode(barcode):
  # Turn barcode into list of digits
  digits = [int(i) for i in list(barcode)]
  check_value = digits[-1]

  # Get first and second sums
  first = sum(digits[0:12:2])
  second = sum(digits[1:12:2])

  # Perform calculations to get the comparison number
  value = second * 3 + first
  comparison = 10 - (value % 10)

  # Return boolean
  return comparison == check_value

def main():
  # Read file and split into barcodes
  file_name = input('Enter the name of the file: ')
  with open(file_name) as file:
    barcodes = file.read().splitlines()

  # Initialize counter variable
  valid = 0

# Loop through each barcode and call function
  with open('valid_barcodes.txt', 'w') as valid_file:
    for barcode in barcodes:
      if valid_barcode(barcode):
        valid += 1
        valid_file.write(barcode + "\n")
  print(f'There are {valid} valid barcodes')

if __name__ == '__main__':
  main()




