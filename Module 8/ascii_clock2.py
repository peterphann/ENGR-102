conversion = {
  "0": ["000","0 0","0 0","0 0","000"],
  "1": [" 1 ","11 "," 1 "," 1 ","111"],
  "2": ["222","  2","222","2  ","222"],
  "3": ["333","  3","333","  3","333"],
  "4": ["4 4","4 4","444","  4","  4"],
  "5": ["555","5  ","555","  5","555"],
  "6": ["666","6  ","666","6 6","666"],
  "7": ["777","  7","  7","  7","  7"],
  "8": ["888","8 8","888","8 8","888"],
  "9": ["999","9 9","999","  9","999"],
  ":": [" ",":"," ",":"," "],
  "A": ["AAA","A A","AAA","A A","A A"],
  "P": ["PPP","P P","PPP","P  ","P  "],
  "M": ["M   M","MM MM","M M M","M   M","M   M"]
}
time = input('Enter the time: ')
clock_type = input('Choose the clock type (12 or 24): ')
character = input('Enter your preferred character: ')
while character not in "abcdeghkmnopqrsuvwxyz@$█&*= ":
  character = input('Character not permitted! Try again: ')

if clock_type == "12":
  hours_minutes = time.split(":")
  hour = int(hours_minutes[0])

  period = 'AM' if hour < 12 else 'PM'
  if hour == 0:
    hour = 12
  elif hour > 12:
    hour -= 12

  time = str(hour) + ":" + hours_minutes[1] + period

for row in range(5):
  for digit in time:
    digit_row = conversion[digit][row]
    if True:#digit != " " and digit not in ":APM":
      digit_row = digit_row.replace(digit, character)
    print(digit_row, end=" ")
  print()