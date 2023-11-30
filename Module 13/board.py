import numpy as np

class Board:

  def __init__(self) -> None:
    self.board = np.array([[0 for i in range(19)] for j in range(19)])

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
  
  def check_row(self, row : int, column : int, player : int) -> int:
    

  