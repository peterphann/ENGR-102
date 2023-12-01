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
    matches = set()

    matches.update(self.find_row(row, column, pattern))
    matches.update(self.find_column(row, column, pattern))
    matches.update(self.find_diagonal(row, column, pattern))
    matches.update(self.find_antidiagonal(row, column, pattern))

    if len(matches) > 0:
      self.place_winner(matches)
      return True
    return False

  def place_winner(self, matches : set) -> None:
    for match in matches:
      self.board[match[0]][match[1]] = self.player + 2

  def display(self) -> None:
    EMPTY = '.'
    PLAYER1 = Fore.RED + Style.BRIGHT + chr(9679) + Fore.RESET + Style.NORMAL
    PLAYER2 = Fore.GREEN + Style.BRIGHT + chr(9679) + Fore.RESET + Style.NORMAL
    WINNER1 = Fore.RED + Style.BRIGHT + chr(9733) + Fore.RESET + Style.NORMAL
    WINNER2 = Fore.GREEN + Style.BRIGHT + chr(9733) + Fore.RESET + Style.NORMAL
    print(color_text('-' * 40, Fore.YELLOW))
    print(f'{"A B C D E F G H I J K L M N O P Q R S":>40}')
    for index, row in enumerate(self.board):
      row = [PLAYER1 if tile == 1 else PLAYER2 if tile == 2 else WINNER1 if tile == 3 else WINNER2 if tile == 4 else EMPTY for tile in row]
      print(f'{index + 1:>2} {" ".join(row)}')
    print(color_text('-' * 40, Fore.YELLOW))