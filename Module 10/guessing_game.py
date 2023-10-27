# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 10.14 
# Date:         27 October 2023

def check_guess(guess, answer):
  # Use conditionals to see if the guess is too high or too low
  if guess > answer:
    print('Too high!')
  elif guess < answer:
    print('Too low!')
  else:
    return True
  return False

def prompt_input():
  # Keep prompting input until it is valid using try catch block
  guess = input('What is your guess? ')
  valid = False
  while not valid:
    try:
      guess = int(guess)
      valid = True
    except:
      guess = input('Bad input! Try again: ')
  return guess 

def main():
  # Initialize variables, secret number
  secret_number = 27
  print('Guess the secret number! Hint: it\'s an integer between 1 and 100...')
  won = False
  guesses = 0
  
  # Loop until guess is correct, keep track of number of guesses
  while not won:
    guess = prompt_input()
    guesses += 1
    won = check_guess(guess, secret_number)
  print(f'You guessed it! It took you {guesses} guesses.')

if __name__ == "__main__":
  main()