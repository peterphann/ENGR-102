# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 13
# Date: 1 December 2023

from board import *
from game_drawing import show_win

def parse_cell(cell : str):
  '''Converts the user input to a tuple representing the row and column'''
  cell = cell.upper()
  letters = 'ABCDEFGHIJKLMNOPQRS'
  column = letters.index(cell[0].upper())
  row = int(cell[1:]) - 1
  return row, column

def print_scoreboard(board : Board, user_input : str, message : str):
  '''Prints the scoreboard with the provided message and the last user input'''
  score_display = color('Score: ', SECONDARY_COLOR) + color(str(board.p1_captures), PLAYER1_COLOR) + ' ' + color(str(board.p2_captures), PLAYER2_COLOR)
  player_display = color("P2", PLAYER2_COLOR) if board.player == 1 else color("P1", PLAYER1_COLOR)
  bar_display = color("|", MAIN_COLOR)
  tile_display = color('→ ' + user_input.upper(), SECONDARY_COLOR)
  message_display = color(message, SECONDARY_COLOR)
  print(f'{score_display} {bar_display} {player_display} {tile_display} {bar_display} {message_display}')

def main():
  # Initialize board from separate module
  board = Board()
  
  # Initialize default values for game
  user_input = ''
  last_valid_input = '?'
  message = 'Welcome to Pente!'
  player1_name = color('[Player 1]', PLAYER1_COLOR)
  player2_name = color('[Player 2]', PLAYER2_COLOR)

  # Main game loop
  while user_input != 'stop':
    board.display()   
    print_scoreboard(board, last_valid_input, message)
    user_input = input(f'{player1_name if board.player == 1 else player2_name}{SECONDARY_COLOR + Style.BRIGHT} Enter tile: ')
    
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

    # Check if tiles were captured or if a player got 5 in a row``
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
  show_win()

def menu():
    '''Displays menu options'''
    print(color("[I] Instructions", MAIN_COLOR))
    print(color("[R] Rules", MAIN_COLOR))
    print(color("[P] Play", MAIN_COLOR))
    print(color("[Q] Quit", MAIN_COLOR))

playing = True

while playing:
    # Display menu and take user input to choose an option
    menu()
    option = input(Style.BRIGHT + '> ').upper()

    print(color("━" * 40, SECONDARY_COLOR))
    print(Style.BRIGHT, end='')

    if option == 'I':
        with open("pente_rules_and_instructions.txt", "r") as file:
            lines = file.read().split('\n')
            instructions = '\n'.join(lines[:5])
            print(instructions)
    elif option == 'R':
        with open("pente_rules_and_instructions.txt", "r") as file:
            lines = file.read().split('\n')
            rules = '\n'.join(lines[7:12])
            print(rules)
    elif option == 'P':
        # Start game
        print("Starting the game...")
        main()
    elif option == 'Q':
        playing = False
        print(":(")
    else:
        print("Invalid option. Please choose a valid option.")

    print(Fore.WHITE, Style.NORMAL)