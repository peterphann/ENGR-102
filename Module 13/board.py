from colorama import Fore, Style
import numpy as np

def color(text : str, color) -> str:
  return color + Style.BRIGHT + text + Fore.RESET + Style.NORMAL

MAIN_COLOR = Fore.MAGENTA
SECONDARY_COLOR = Fore.BLACK
PLAYER1_COLOR = Fore.RED
PLAYER2_COLOR = Fore.GREEN

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
  
  def find_row(self, row : int, column : int, pattern : str):
    cells = []
    row_list = self.board[row]
    row_string = ''.join([str(i) for i in row_list])

    pattern_index = row_string.find(pattern)
    while pattern_index != -1:
      matched_cells = [(row, pattern_index + i) for i in range(len(pattern))]
      cells.extend(matched_cells)
      pattern_index = row_string.find(pattern, pattern_index + 1)
    return cells

  def find_column(self, row : int, column : int, pattern : str):
    cells = []
    column_list = self.board[:,column]
    column_string = ''.join([str(i) for i in column_list])

    pattern_index = column_string.find(pattern)
    while pattern_index != -1:
      matched_cells = [(pattern_index + i, column) for i in range(len(pattern))]
      cells.extend(matched_cells)
      pattern_index = column_string.find(pattern, pattern_index + 1)
    return cells

  def find_diagonal(self, row : int, column : int, pattern : str):
    cells = []

    offset = min(8 - row, column)
    start_row, start_column = row + offset, column - offset
    steps = min(start_row, 8 - start_column) + 1

    diagonal = [self.board[start_row - i, start_column + i] for i in range(steps)]
    diagonal_string = ''.join([str(i) for i in diagonal])

    pattern_index = diagonal_string.find(pattern)
    while pattern_index != -1:
      matched_cells = [(start_row - pattern_index - i, start_column + pattern_index + i) for i in range(len(pattern))]
      cells.extend(matched_cells)
      pattern_index = diagonal_string.find(pattern, pattern_index + 1)
    return cells

  def find_antidiagonal(self, row : int, column : int, pattern : str):
    cells = []
    
    offset = min(row, column)
    start_row, start_column = row - offset, column - offset
    steps = min(8 - start_row, 8 - start_column) + 1

    diagonal = [self.board[start_row + i, start_column + i] for i in range(steps)]
    diagonal_string = ''.join([str(i) for i in diagonal])

    pattern_index = diagonal_string.find(pattern)
    while pattern_index != -1:
      matched_cells = [(start_row + pattern_index + i, start_column + pattern_index + i) for i in range(len(pattern))]
      cells.extend(matched_cells)
      pattern_index = diagonal_string.find(pattern, pattern_index + 1)
    return cells
  
  def check_five(self, row : int, column : int) -> bool:
    pattern = str(self.player) * 5
    matches = []

    matches.extend(self.find_row(row, column, pattern))
    matches.extend(self.find_column(row, column, pattern))
    matches.extend(self.find_diagonal(row, column, pattern))
    matches.extend(self.find_antidiagonal(row, column, pattern))

    if len(matches) > 0:
      self.place_winner(matches)
      return True
    return False
  
  def check_capture(self, row : int, column : int) -> None:
    opponent = 2 if self.board[row, column] == 1 else 1
    pattern = str(self.player) + (str(opponent) * 2) + str(self.player)
    matches = []

    matches.extend(self.find_row(row, column, pattern))
    matches.extend(self.find_column(row, column, pattern))
    matches.extend(self.find_diagonal(row, column, pattern))
    matches.extend(self.find_antidiagonal(row, column, pattern))

    captures_found = len(matches) // 4
    for i in range(captures_found):
      if (row, column) not in matches[4 * i : 4 * i + 4]: continue
      captured1, captured2 = matches[4 * i + 1], matches[4 * i + 2]
      self.remove(captured1[0], captured1[1])
      self.remove(captured2[0], captured2[1])
      if self.player == 1:
        self.p1_captures += 1
      else:
        self.p2_captures += 1

  def place_winner(self, matches : set) -> None:
    for match in matches:
      self.board[match[0]][match[1]] = self.player + 2

  def display(self) -> None:
    EMPTY = color('.', Fore.BLACK)
    PLAYER1 = color(chr(9679), PLAYER1_COLOR)
    PLAYER2 = color(chr(9679), PLAYER2_COLOR)
    WINNER1 = color(chr(9733), PLAYER1_COLOR)
    WINNER2 = color(chr(9733), PLAYER2_COLOR)

    top_edge = '┏' + ('━' * 42) + '┓'
    bottom_edge = '┗' + ('━' * 42) + '┛'
    print(color(top_edge, MAIN_COLOR))

    column_names = color('A B C D E F G H I J K L M N O P Q R S', Fore.WHITE)
    print(f'{color("┃", MAIN_COLOR)}{column_names:>60} {color("┃", MAIN_COLOR)}')
    for index, row in enumerate(self.board):
      row = [PLAYER1 if tile == 1 else PLAYER2 if tile == 2 else WINNER1 if tile == 3 else WINNER2 if tile == 4 else EMPTY for tile in row]
      print(f'{color("┃", MAIN_COLOR)} {color(str(index + 1), Fore.WHITE):>21} {" ".join(row)} {color("┃", MAIN_COLOR)}')
    print(color(bottom_edge, MAIN_COLOR))