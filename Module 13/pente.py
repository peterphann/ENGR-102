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

from board import *

def parse_cell(cell : str):
  letters = 'ABCDEFGHIJKLMNOPQRS'
  column = letters.index(cell[0].upper())
  row = int(cell[1:]) - 1
  return row, column

def main():
  # Initialize board and call initial input
  board = Board()
  board.display()
  print(color('Welcome to Pente - Good luck!', MAIN_COLOR))
  
  # Main game loop
  user_input = ''
  while user_input != 'STOP':
    player1_name = color('[Player 1]', PLAYER1_COLOR)
    player2_name = color('[Player 2]', PLAYER2_COLOR)
    user_input = input(f'{player1_name if board.player == 1 else player2_name} {color("Enter tile: ", Fore.BLACK)}').upper()
    if user_input == 'STOP':
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
    score_display = color('Score: ', MAIN_COLOR) + color(str(board.p1_captures), PLAYER1_COLOR) + ' ' + color(str(board.p2_captures), PLAYER2_COLOR)
    player_display = color("P1", PLAYER1_COLOR) if board.player == 1 else color("P2", PLAYER2_COLOR)
    tile_display = color('→ ' + user_input, Fore.BLACK)
    print(f'{score_display} {color("|", Fore.BLACK)} {player_display} {tile_display}')
    board.next_player()

  if user_input == 'STOP':  
    print(DIVIDER_LINE)
    if board.player == 1:
      print(f'{color("Red", PLAYER1_COLOR)} forfeited! {color("Green", PLAYER2_COLOR)} wins!')
    else:
      print(f'{color("Green", PLAYER2_COLOR)} forfeited! {color("Red", PLAYER1_COLOR)} wins')
  else:
    if board.player == 1:
      print(f'{color("Red", PLAYER1_COLOR)} got five in a row! {color("Red", PLAYER1_COLOR)} wins!')
    else:
      print(f'{color("Green", PLAYER2_COLOR)} got five in a row! {color("Green", PLAYER2_COLOR)} wins!')

if __name__ == '__main__':
  main()