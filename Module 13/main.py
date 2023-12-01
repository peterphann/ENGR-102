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
# Date: 1 December 2023

from colorama import Fore, Style
from board import Board

def parse_cell(cell : str):
  letters = 'ABCDEFGHIJKLMNOPQRS'
  column = letters.index(cell[0].upper())
  row = int(cell[1:]) - 1
  return row, column

def color_text(text : str, color) -> str:
  return color + Style.BRIGHT + text + Fore.RESET + Style.NORMAL

def main():
  # Initialize board and call initial input
  board = Board()
  board.display()
  print('Welcome to Pente - Good luck!')
  user_input = ''

  # Main game loop
  while user_input != 'stop':
    player1_name = color_text('[Player 1]', Fore.RED)
    player2_name = color_text('[Player 2]', Fore.GREEN)
    user_input = input(f'{player1_name if board.player == 1 else player2_name} Enter tile: ').upper()
    if user_input == 'stop':
      break

    # Parse user input and check for any errors
    try:
      row, column = parse_cell(user_input)
      if not (0 <= row <= 18) or not (0 <= column <= 18):
        raise ValueError(f'The tile {user_input} is outside the board. Please enter a valid tile (ex. A1).')
      if board.board[row][column] != 0:
        raise ValueError(f'Invalid input "{user_input}". Please enter a valid tile (e.g., A1).')
    except ValueError as e:
      board.display()
      print(e)
      continue
    except IndexError:
      board.display()
      print('Error')
      continue

    # Place piece on specified tile and check for patterns
    board.place(row, column)
    is_finished = board.check_five(row, column)
    print(f'is_finished: {is_finished}')
    # board.check_capture(row, column)
    board.display()
    if is_finished or board.p1_captures == 5 or board.p2_captures == 5:
      break

    # Swap players and continue
    print(f'P1 {board.p1_captures} {board.p2_captures} P2 | {"P1" if board.player == 1 else "P2"} → {user_input}')
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