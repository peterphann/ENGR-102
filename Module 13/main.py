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
    self.board = np.full((19, 19), 0)
    self.player = 1
    self.p1_captures, self.p2_captures = 0, 0

  def next_player(self) -> None:
    self.player = 2 if self.player == 1 else 1

  def place(self, row : int, column : int) -> None:
    self.board[row][column] = self.player

  def remove(self, row : int, column : int) -> None:
    self.board[row][column] = 0
  
  def get_row(self, row : int, column : int) -> str:
    current_row = [str(i) for i in self.board[row]]
    return ''.join(current_row)
  
  def get_column(self, row : int, column : int) -> str:
    current_column = self.board[:,column]
    current_column = [str(i) for i in current_column]
    return ''.join(current_column)
  
  def get_diagonal(self, row : int, column : int) -> str:
    boundary = min(18 - row, column)
    starting_row, starting_column = row + boundary, column - boundary
    diagonal_steps = min(starting_row, 18 - starting_column)
    current_diagonal = [self.board[starting_row - i][starting_column + i] for i in range(diagonal_steps + 1)]
    current_diagonal = [str(i) for i in current_diagonal]
    return ''.join(current_diagonal)
  
  def get_antidiagonal(self, row : int, column : int) -> str:
    boundary = min(row, column)
    starting_row, starting_column = row - boundary, column - boundary
    antidiagonal_steps = min(18 - row, 18 - column)
    current_antidiagonal = [self.board[starting_row + i][starting_column + i] for i in range(antidiagonal_steps + 1)]
    current_antidiagonal = [str(i) for i in current_antidiagonal]
    return ''.join(current_antidiagonal)

  def check_five(self, row : int, column : int) -> bool:
    match = str(self.player) * 5
    matches = set()

    # Check row
    row_string = self.get_row(row, column)
    row_search = row_string.find(match)
    matches.update([(row, row_search + i) for i in range(5) if row_search != -1])
      

    # Check column
    column_string = self.get_column(row, column)
    column_search = column_string.find(match)
    matches.update([(column_search + i, column) for i in range(5) if column_search != -1])
      

    # Check diagonal
    starting_row, starting_column = row + min(18 - row, column), column - min(18 - row, column)
    diagonal_string = self.get_diagonal(row, column)
    diagonal_search = diagonal_string.find(match)
    matches.update([(starting_row - diagonal_search - i, starting_column + diagonal_search + i) for i in range(5) if diagonal_search != -1])
      

    # Check antidiagonal
    boundary = min(row, column)
    starting_row, starting_column = row - boundary, column - boundary
    antidiagonal_string = self.get_antidiagonal(row, column)
    antidiagonal_search = antidiagonal_string.find(match)
    matches.update([(starting_row + antidiagonal_search + i, starting_column + antidiagonal_search + i) for i in range(5) if antidiagonal_search != -1])
      

    if len(matches) > 0:
      self.place_winner(matches)
      return True
    return False

  def check_capture(self, row : int, column : int):
    opponent = 2 if self.player == 1 else 1
    match = f'{str(self.player)}{str(opponent) * 2}{str(self.player)}'
    captures = 0
    captured = set()

    row_string = self.get_row(row, column)
    row_search = row_string.find(match)
    if row_search != -1:
      captures += 1
      captured.update([(row, row_search + 1), (row, row_search + 2)])

    column_string = self.get_column(row, column)
    column_search = column_string.find(match)
    if column_search != -1:
      captures += 1
      captured.update([(column_search + 1, column), (column_search + 2, column)])

    if self.player == 1:
      self.p1_captures += captures
    else:
      self.p2_captures += captures

    for point in captured:
      self.remove(point[0], point[1])

  def place_winner(self, matches : set) -> None:
    for match in matches:
      self.board[match[0]][match[1]] = self.player + 2

  def display(self) -> None:
    EMPTY = '.'
    PLAYER1 = Fore.RED + Style.BRIGHT + chr(9679) + Fore.RESET + Style.NORMAL
    PLAYER2 = Fore.GREEN + Style.BRIGHT + chr(9679) + Fore.RESET + Style.NORMAL
    WINNER1 = Fore.RED + Style.BRIGHT + chr(9733) + Fore.RESET + Style.NORMAL
    WINNER2 = Fore.GREEN + Style.BRIGHT + chr(9733) + Fore.RESET + Style.NORMAL
    print('-' * 40)
    print(f'{"A B C D E F G H I J K L M N O P Q R S":>40}')
    for index, row in enumerate(self.board):
      row = [PLAYER1 if tile == 1 else PLAYER2 if tile == 2 else WINNER1 if tile == 3 else WINNER2 if tile == 4 else EMPTY for tile in row]
      print(f'{index + 1:>2} {" ".join(row)}')
    print('-' * 40)

def parse_cell(cell : str):
  letters = 'ABCDEFGHIJKLMNOPQRS'
  column = letters.index(cell[0].upper())
  row = int(cell[1:]) - 1
  return row, column

def main():
  # Initialize board and dictionary to convert letters to numbers
  board = Board()

  # Call initial input & display
  board.display()
  print('Welcome to Pente - Good luck!')
  user_input = ''

  # Main game loop
  while user_input != 'stop':  

    user_input = input(f'{"[Red]" if board.player == 1 else "[Green]"} Enter tile: ')
    if user_input == 'stop':
      break

    # Parse user input
    try:
      row, column = parse_cell(user_input)
      if board.board[row][column] != 0:
        board.display()
        print(f'The tile {user_input} is already taken!')
        continue
    except:
      board.display()
      print(f'Your input "{user_input}" is invalid!')
      continue

    # Place piece on specified tile and check for patterns
    board.place(row, column)
    is_finished = board.check_five(row, column)
    board.check_capture(row, column)
    board.display()
    if is_finished or board.p1_captures == 5 or board.p2_captures == 5:
      break

    # Swap players and continue
    print(f'{"R" if board.player == 1 else "G"}>{user_input} | P1 {board.p1_captures} vs. P2 {board.p2_captures}')
    board.next_player()

  if user_input == 'stop':
    print('-' * 40)
    if board.player == 1:
      print('Red forfeited! Green wins!')
    else:
      print('Green forfeited! Red wins')
  else:
    if board.player == 1:
      print('Red won!')
    else:
      print('Green won!')

if __name__ == '__main__':
  main()