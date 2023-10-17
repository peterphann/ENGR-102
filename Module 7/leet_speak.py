# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 7.26
# Date:         25 September 2023

# Create conversion map
conversion = {
  'a': '4',
  'e': '3',
  'o': '0',
  's': '5',
  't': '7'
}

text = input('Enter some text: ')
new_text = ''

for i in range(len(text)):
  if text[i] in conversion:
    new_text += conversion[text[i]]
  else:
    new_text += text[i]

print(f'In leet speak, "{text}" is:')
print(new_text)