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
  cell = cell.upper()
  letters = 'ABCDEFGHIJKLMNOPQRS'
  column = letters.index(cell[0].upper())
  row = int(cell[1:]) - 1
  return row, column

def print_scoreboard(board : Board, user_input : str, message : str):
  score_display = color('Score: ', SECONDARY_COLOR) + color(str(board.p1_captures), PLAYER1_COLOR) + ' ' + color(str(board.p2_captures), PLAYER2_COLOR)
  player_display = color("P1", PLAYER1_COLOR) if board.player == 1 else color("P2", PLAYER2_COLOR)
  bar_display = color("|", MAIN_COLOR)
  tile_display = color('→ ' + user_input, SECONDARY_COLOR)
  message_display = color(message, SECONDARY_COLOR)
  print(f'{score_display} {bar_display} {player_display} {tile_display} {bar_display} {message_display}')

def main():
  # Initialize board and call initial input
  board = Board()
  
  # Main game loop
  user_input = ''
  last_valid_input = '?'
  message = 'Welcome to Pente!'
  while user_input != 'stop':
    player1_name = color('[Player 1]', PLAYER1_COLOR)
    player2_name = color('[Player 2]', PLAYER2_COLOR)

    board.display()   
    print_scoreboard(board, last_valid_input, message)
    user_input = input(f'{player1_name if board.player == 1 else player2_name}{Fore.BLACK + Style.BRIGHT} Enter tile: ')
    if user_input == 'stop':
      break

    # Parse user input and check for any errors
    try:
      row, column = parse_cell(user_input)
    except:
      message = f'Invalid input "{user_input}". Please enter a valid tile (e.g., A1).'
      continue
    if not (0 <= row <= 18) or not (0 <= column <= 18):
      message = f'The tile {user_input} is outside the board. Please enter a valid tile (ex. A1).'
      continue
    if board.board[row, column] != 0:
      message = f'The tile {user_input} is already taken. Please enter another tile.'
      continue

    # Place piece on specified tile and check for patterns
    last_valid_input = user_input
    board.place(row, column)
    is_finished = board.check_five(row, column)
    print(f'is_finished: {is_finished}')
    # board.check_capture(row, column)
    if is_finished or board.p1_captures == 5 or board.p2_captures == 5:
      break

    # Swap players and continue
    board.next_player()

  board.display()
  if user_input == 'stop':  
    if board.player == 1:
      print(f'{color("Red", PLAYER1_COLOR)} forfeited! {color("Green", PLAYER2_COLOR)} wins!')
    else:
      print(f'{color("Green", PLAYER2_COLOR)} forfeited! {color("Red", PLAYER1_COLOR)} wins')
  else:
    if board.player == 1:
      print(f'{color("Red", PLAYER1_COLOR)} {color("got five in a row!", SECONDARY_COLOR)} {color("Red wins!", PLAYER1_COLOR)}')
    else:
      print(f'{color("Green", PLAYER2_COLOR)} {color("got five in a row!", SECONDARY_COLOR)} {color("Green wins!", PLAYER2_COLOR)}')

if __name__ == '__main__':
  main()