# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan  
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 8.10
# Date: 20 October 2023

dictionary = {
  '0' : ['000','0 0','0 0','0 0','000'],
  '1' : [' 1 ','11 ',' 1 ',' 1 ','111'],
  '2' : ['222','  2','222','2  ','222'],
  '3' : ['333','  3','333','  3','333'],
  '4' : ['4 4','4 4','444','  4','  4'],
  '5' : ['555','5  ','555','  5','555'],
  '6' : ['666','6  ','666','6 6','666'],
  '7' : ['777','  7','  7','  7','  7'],
  '8' : ['888','8 8','888','8 8','888'],
  '9' : ['999','9 9','999','  9','999'],
  ':' : [' ',':',' ',':',' '],
  'A' : [' A ','A A','AAA','A A','A A'],
  'P' : ['PPP','P P','PPP','P  ','P  '],
  'M' : ['M   M','MM MM','M M M','M   M','M   M']
}

time = str(input("Enter the time: "))
clock_type = str(input("Choose the clock type (12 or 24): "))
character = str(input("Enter your preferred character: "))

permitted = 'abcdeghkmnopqrsuvwxyz@$&*='
while character not in permitted:
   character = input("Character not permitted! Try again: ")

# Parse input depending on clock type
# If a 12 hour clock is chosen
if clock_type == "12":
    # If the number entered is larger than 12:00
    time = time.split(":")
    if int(time[0]) > 12 and int(time[1]) > 00:
        # Subtract 12 from the hour and display PM
        time[0] = int(time[0]) - 12
        time = str(time[0]) + ":" + str(time[1]) + "PM"
    # Otherwise display an AM
    elif int(time[0]) == 12:
       time = "12" + ":" + str(time[1]) + "PM"
    elif int(time[0]) == 0:
        time = "12" + ":" + str(time[1]) + "AM"
    else:
        time = str(time[0]) + ":" + str(time[1]) + "AM"
# If a 24 hour clock is chosen
elif clock_type == "24":
    # Keep it the same as the input
    time = time

print()
# Loop from row 1 - 5
for row in range(5):
  # Loop through each digit in provided string
  row_output = []
  for digit in time:
    # Determine correct character based on user input
    # If no character is given, use the digit's character
    # Don't change character if :, A, P, M
    if character == "" or digit in ":APM":
      character_used = digit
    else:
      character_used = character
    # Modify corresponding list with correct character
    current_row = dictionary[digit][row]
    current_row = current_row.replace(digit, character_used)
    # Add current row of digit into list
    row_output.append(current_row)
  # Print list, joined by spaces
  print(" ".join(row_output))

