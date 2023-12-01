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

from colorama import Fore, Style
import numpy as np

class Board:
  
  def __init__(self) -> None:
    self.board = np.array([['.' for i in range(19)] for j in range(19)])

  def place(self, row : int, column : int, player : int) -> None:
    PLAYER1 = chr(9679)
    PLAYER2 = chr(9675)

    tile = PLAYER1 if player == 1 else PLAYER2
    self.board[row - 1][column - 1] = tile

  def __str__(self) -> str:
    output = ''

    output += f'{"A B C D E F G H I J K L M N O P Q R S":>40}\n'
    for index, list in enumerate(self.board):
      output += f'{index + 1:>2} {" ".join(list)}\n'
    
    return output

conversion = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19
  }

def parse_cell(cell : str):
  column = conversion[cell[0].upper()] - 1
  row = int(cell[1:]) - 1
  return row, column

# Create function to display board with proper formatting
def display_board(board : list):
  print(f'{"A B C D E F G H I J K L M N O P Q R S":>40}')
  for index, list in enumerate(board):
    print(f'{index + 1:>2} {" ".join(list)}')

def clean_slice(slice : list, target : str) -> str:
  '''
  Replaces the pieces in a slice of the board with either 1 or 0 to prevent complications
  with str.find() and the color formatting.'''
  slice = ['1' if item == target else item for item in slice]
  slice = ['0' if item != '1' and item != '□' else item for item in slice]
  return slice

def check_row(board : list, cell : tuple):
  '''
  Function that takes in a board and a cell and checks if the given row has five-in-a-row. If a match if found, 
  return a tuple containing the cells of the match. Otherwise, return an empty tuple.
  '''
  row, column = cell
  player = board[row][column]
  board_row = clean_slice(board[row], player)
  board_row = ''.join(board_row)

  first_match = board_row.find('11111')
  if first_match == -1:
    return ()
  else:
    return ((row, first_match), (row, first_match + 1), (row, first_match + 2), (row, first_match + 3), (row, first_match + 4))

def check_column(board : list, cell : tuple):
  row, column = cell
  player = board[row][column]
  board_column = clean_slice([row[column] for row in board], player)
  board_column = ''.join(board_column)

  first_match = board_column.find('11111')
  if first_match == -1:
    return ()
  else:
    return (first_match, column), (first_match + 1, column), (first_match + 2, column), (first_match + 3, column), (first_match + 4, column)

def check_topleft_diag(board : list, cell : tuple):
  row, column = cell
  player = board[row][column]

  limit = min(row, column)
  row, column = row - limit, column - limit

  limit2 = min(18 - row, 18 - column)
  diagonal = clean_slice([board[row + i][column + i] for i in range(limit2 + 1)], player)
  diagonal = ''.join(diagonal)

  first_match = diagonal.find('11111')

  if first_match == -1:
    return ()
  else:
    match_row, match_col = row + first_match, column + first_match
    return (match_row, match_col), (match_row + 1, match_col + 1), (match_row + 2, match_col + 2), (match_row + 3, match_col + 3), (match_row + 4, match_col + 4)

def check_botleft_diag(board : list, cell : tuple):
  row, column = cell
  player = board[row][column]

  limit = min(18 - row, column)
  row, column = row + limit, column - limit

  limit2 = min(row, 18 - column)
  diagonal = clean_slice([board[row - i][column + i] for i in range(limit2 + 1)], player)
  diagonal = ''.join(diagonal)

  first_match = diagonal.find('11111')
  if first_match == -1:
    return ()
  else:
    match_row, match_col = row - first_match, column + first_match
    return (match_row, match_col), (match_row - 1, match_col + 1), (match_row - 2, match_col + 2), (match_row - 3, match_col + 3), (match_row - 4, match_col + 4)

def check_board(board : list, cell : tuple):
  matches1 = check_row(board, cell)
  matches2 = check_column(board, cell)
  matches3 = check_topleft_diag(board, cell)
  matches4 = check_botleft_diag(board, cell)

  return tuple(set(matches1 + matches2 + matches3 + matches4))

def main():
  # Create variables for tile symbols
  player1_turn = True
  PLAYER1 = Fore.RED + Style.BRIGHT + chr(9679) + Fore.RESET + Style.NORMAL
  PLAYER2 = Fore.GREEN + Style.BRIGHT + chr(9679) + Fore.RESET + Style.NORMAL

  # Initialize board and dictionary to convert letters to numbers
  board = [['.' for i in range(19)] for j in range(19)]

  # Call initial input & display
  display_board(board)
  user_input = input(f'\n{"[Red]" if player1_turn else "[Green]"} Enter tile: ')

  while user_input != 'stop':  
    # Split user input by column and row
    try:
      row, column = parse_cell(user_input)
      if board[row][column] != '.':
        display_board(board)
        print('That tile is already taken!')
        user_input = input(f'{"[Red]" if player1_turn else "[Green]"} Enter tile: ')
        continue
    except:
      display_board(board)
      print('Invalid input!')
      user_input = input(f'{"[Red]" if player1_turn else "[Green]"} Enter tile: ')
      continue

    board[row][column] = PLAYER1 if player1_turn else PLAYER2
    display_board(board)

    check = check_board(board, (row, column))
    if check != ():
      print(check)
      break

    player1_turn = not player1_turn
    user_input = input(f'\n{"[Red]" if player1_turn else "[Green]"} Enter tile: ')

  if

  if player1_turn:
    print('Red won!')
  else:
    print('Green won!')

if __name__ == '__main__':
  main()