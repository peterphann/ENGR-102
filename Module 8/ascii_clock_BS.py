# Modify corresponding list with correct character
current_row = dictionary[digit][row]
current_row = current_row.replace(digit, character_used)
# Print row n of each digit in one line
print(current_row, end=' ')
# Go to the next line on each iteration
print()
