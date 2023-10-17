# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: go_moves lab
# Date: 2 October 2023

# Initialize board and dictionary to convert letters to numbers
board = [["." for i in range(9)] for j in range(9)]
conversion = {
  'A': 1,
  'B': 2,
  'C': 3,
  'D': 4,
  'E': 5,
  'F': 6,
  'G': 7,
  'H': 8,
  'I': 9
}

# Create variables for tile symbols
black_turn = True
black_tile = chr(9679)
white_tile = chr(9675)

# Create function to display board with proper formatting
def display_board():
  print(f'{"A B C D E F G H I":>19}')
  for index, list in enumerate(board):
    print(f'{index + 1} {" ".join(list)}')

# Call initial input & display
display_board()
user_input = input(f'{"[Black]" if black_turn else "[White]"} Enter tile: ')
while user_input != 'stop':  
  # Split user input by column and row
  column = conversion[user_input[0].upper()] - 1
  row = int(user_input[1]) - 1

  # If the tile is taken, don't switch turns and retry input
  if board[row][column] != '.':
    print('That tile is already taken!')
  else:
    board[row][column] = black_tile if black_turn else white_tile
    black_turn = not black_turn
  display_board()
  user_input = input(f'{"[Black]" if black_turn else "[White]"} Enter tile: ')
  
