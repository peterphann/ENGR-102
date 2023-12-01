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
  player_display = color("P2", PLAYER2_COLOR) if board.player == 1 else color("P1", PLAYER1_COLOR)
  bar_display = color("|", MAIN_COLOR)
  tile_display = color('→ ' + user_input.upper(), SECONDARY_COLOR)
  message_display = color(message, SECONDARY_COLOR)
  print(f'{score_display} {bar_display} {player_display} {tile_display} {bar_display} {message_display}')

def main():
  # Initialize board and call initial input
  board = Board()
  
  # Main game loop
  user_input = ''
  last_valid_input = '?'
  message = 'Welcome to Pente!'
  player1_name = color('[Player 1]', PLAYER1_COLOR)
  player2_name = color('[Player 2]', PLAYER2_COLOR)

  while user_input != 'stop':
    board.display()   
    print_scoreboard(board, last_valid_input, message)
    user_input = input(f'{player1_name if board.player == 1 else player2_name}{Fore.BLACK + Style.BRIGHT} Enter tile: ')
    
    if user_input == 'stop':
      player_display = color("Player 1", PLAYER1_COLOR) if board.player == 1 else color("Player 2", PLAYER2_COLOR)
      opponent_display = color("Player 1", PLAYER1_COLOR) if board.player == 2 else color("Player 2", PLAYER2_COLOR)
      message = f'\n{player_display} {color("forfeited!", SECONDARY_COLOR)} {opponent_display} {color("wins!", SECONDARY_COLOR)}'
      break

    # Parse user input and check for any errors
    try:
      row, column = parse_cell(user_input)
    except:
      message = f'Invalid input "{user_input}".'
      continue
    if not (0 <= row <= 18) or not (0 <= column <= 18):
      message = f'{user_input.upper()} is outside the board.'
      continue
    if board.board[row, column] != 0:
      message = f'{user_input.upper()} is already taken.'
      continue

    # Place piece on specified tile and check for patterns
    last_valid_input = user_input
    message = ''
    board.place(row, column)
    has_five_in_row = board.check_five(row, column)
    has_captured = board.check_capture(row, column)

    if has_captured:
      player_display = color("P1", PLAYER1_COLOR) if board.player == 1 else color("P2", PLAYER2_COLOR)
      message = f'{player_display} {color("captured some tiles!", SECONDARY_COLOR)}'
    if has_five_in_row:
      player_display = color("Player 1", PLAYER1_COLOR) if board.player == 1 else color("Player 2", PLAYER2_COLOR)
      message = f'\n{player_display} {color("got five in a row!", SECONDARY_COLOR)} {player_display} {color("wins!", SECONDARY_COLOR)}'
      break
    if board.p1_captures == 5 or board.p2_captures == 5:
      player_display = color("Player 1", PLAYER1_COLOR) if board.player == 1 else color("Player 2", PLAYER2_COLOR)
      message = f'\n{player_display} {color("got five captures!", SECONDARY_COLOR)} {player_display} {color("wins!", SECONDARY_COLOR)}'
      break

    # Swap players and continue
    board.next_player()

  board.display()
  print_scoreboard(board, last_valid_input, message)
  
if __name__ == '__main__':
  main()