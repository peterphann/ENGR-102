colon = [[0],[1],[0],[1],[0]]
a_list = [[0,1,0],[1,0,1],[1,1,1],[1,0,1],[1,0,1]]
p_list = [[1,1,1],[1,0,1],[1,1,1],[1,0,0],[1,0,0]]
m_list = [[1,0,0,0,1],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]]
zero = [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]
one = [[0,1,0],[1,1,0],[0,1,0],[0,1,0],[1,1,1]]
two = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
three = [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]
four = [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]
five = [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]
six = [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]
seven = [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
eight = [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
nine = [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]

conversion = {
  ":": colon,
  "A": a_list,
  "P": p_list,
  "M": m_list,
  "0": zero,
  "1": one,
  "2": two,
  "3": three,
  "4": four,
  "5": five,
  "6": six,
  "7": seven,
  "8": eight,
  "9": nine
}

exceptions = [":", "A", "P", "M"]
permitted_characters = "abcdeghkmnopqrsuvwxyz@$&*="

def military_to_twelve(military_time : str) -> str:
  hours_minutes = military_time.split(":")

  period = 'AM'
  hour = int(hours_minutes[0])

  if hour == 0:
    hour = 12
  elif hour >= 13:
    hour -= 12

  if hour >= 12:
    period = 'PM'
    
  hours_minutes[0] = str(hour)
  return ':'.join(hours_minutes) + period

def print_digits(digit_list : list):
  for row in range(5):
    for digit in digit_list:
      if digit not in exceptions and user_character != "":
        character = user_character
      else:
        character = digit
      current_row = conversion[digit][row]
      converted_row = [character if num == 1 else " " for num in current_row]
      print(''.join(converted_row), end=" ")
    print()

time = input('Enter the time: ')
if input('Choose the clock type (12 or 24): ') == "12":
  time = military_to_twelve(time)

user_character = input('Enter your preferred character: ')
while user_character not in permitted_characters and user_character != "":
  user_character = input('Character not permitted! Try again: ')
digits = list(time)
print_digits(digits)
