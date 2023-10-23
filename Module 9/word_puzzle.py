# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan  
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 9.15
# Date: 23 October 2023

def print_puzzle(puzzle):
  ''' Print puzzle as a long division problem. '''

  # Print puzzle
  puzzle = puzzle.split(',')
  for i in range(len(puzzle)):
    if i == 1:
      print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
    print(f'{puzzle[i]: >16}')
    if i > 1 and i % 2 == 0:
      print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle):
  ''' Get all unique letters in a puzzle '''

  # Loop through each letter and add to list if not already added
  letters = ''
  for letter in puzzle:
    if letter not in letters and letter not in " |,":
      letters += letter
  return letters

def is_valid_guess(letters, guess):
  ''' Returns whether or not a given guess is valid '''

  # Create dictionary to hold occurrences
  occurrences = {}
  for letter in letters:
    occurrences[letter] = 0

  # Loop through each letter and add to dictionary
  for letter in guess:
    if letter in letters:
      occurrences[letter] += 1

  # Get number of total and unique guesses
  unique_guesses = len([word for word, occurrence in occurrences.items() if occurrence > 0])
  valid_guesses = sum(occurrences.values())
  
  return unique_guesses == 10 and valid_guesses == 10

def check_user_guess(dividend, quotient, divisor, remainder):
  ''' Returns whether a user's guess is correct '''

  # Return boolean expression
  return dividend == quotient * divisor + remainder

def make_number(word, guess):
  ''' Forms a number from a guess and a word '''

  #
  guess = list(guess)
  string = ''
  for letter in word:
    string += str(guess.index(letter))
  return int(string)

def make_numbers(puzzle, guess):
  ''' Forms a number from a guess and a puzzle '''

  # Split puzzle into corresponding pieces
  words = puzzle.split(',')
  split = words[1].split(' | ')
  dividend = split[1]
  quotient = words[0]
  divisor = split[0]
  remainder = words[len(words) - 1]

  # Call make_number on each word and return tuple
  return make_number(dividend, guess), make_number(quotient, guess), make_number(divisor, guess), make_number(remainder, guess)

def main():
  puzzle = input('Enter a word arithmetic puzzle: \n')
  print_puzzle(puzzle)
  guess = input('\nEnter your guess, for example ABCDEFGHIJ: ')
  
  valid_letters = get_valid_letters(puzzle)
  valid_guess = is_valid_guess(valid_letters, guess)

  if not valid_guess:
    print('Your guess should contain exactly 10 unique letters used in the puzzle.')
    return
  
  dividend, quotient, divisor, remainder = make_numbers(puzzle, guess)
  correct = check_user_guess(dividend, quotient, divisor, remainder)

  if correct:
    print('Good job!')
  else:
    print('Try again!')


if __name__ == '__main__':
  main()