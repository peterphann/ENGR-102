# creat a dictionary containing each drawing of a digit or letter to display later on the clock
dictionary = {
  '0' : ['000','0 0','0 0','0 0','000'],
  '1' : [' 1 ','11 ',' 1 ',' 1 ','111'],
  '2' : ['222','  2','222','2  ','222'],
  '3' : ['333','  3','333','  3','333'],
  '4' : ['4 4','4 4','444','  4','  4'],
  '5' : ['555','5  ','555','  5','555'],
  '6' : ['666','6  ','666','6 6','666'],
  '7' : ['777','  7','  7','  7','  7'],
  '8' : ['888','8 8','888','8 8','888'],
  '9' : ['999','9 9','999','  9','999'],
  ':' : [' ',':',' ',':',' '],
  'A' : [' A ','A A','AAA','A A','A A'],
  'P' : ['PPP','P P','PPP','P  ','P  '],
  'M' : ['M   M','MM MM','M M M','M   M','M   M']
}

time = str(input("Enter the time: "))
clock_type = str(input("Choose the clock type (12 or 24): "))
character = str(input("Enter your preferred character: "))

# check if the user inputted an allowed character
permitted = 'abcdeghkmnopqrsuvwxyz@$&*='
# if the charactered is not allowed, do not continue, otherwise, go on
while character not in permitted:
   character = input("Character not permitted! Try again: ")