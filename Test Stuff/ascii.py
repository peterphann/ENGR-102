conversion = {
  " ": [' ',' ',' ',' ',' '],
  "A": ['███','█ █','███','█ █','█ █'],
  "B": ['██ ','█ █','██ ','█ █','██ '],
  "C": ['███','█  ','█  ','█  ','███'],
  "D": ['██ ','█ █','█ █','█ █','██ '],
  "E": ['███','█  ','██ ','█  ','███'],
  "F": ['███','█  ','██ ','█  ','█  '],
  "G": ['███','█  ','█ █','█ █','███']
}

string = input('Enter string: ')

for row in range(5):
  for character in string:
    current_row = conversion[character][row]
    print(current_row, end=" ")
  print()