# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 7.25
# Date:         25 September 2023

sentence = input('Enter word(s) to convert to Pig Latin: ')
split = sentence.split(' ')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

new_sentence = ''
# Split sentence by spaces
for word in split:
  if word[0] in vowels:
    new_sentence += word + 'yay '
  else:
    index = 0
    while word[index] not in vowels: # Find first letter that isn't a vowel
      index += 1
    new_sentence += word[index:] + word[0:index] + 'ay '

print(f'In Pig Latin, "{sentence}" is: {new_sentence}')