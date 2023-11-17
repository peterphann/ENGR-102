import numpy as np

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
plaintext = input('Plaintext: ')
key = input('Key: ')
encode = input('Encode or Decode? (E/D): ') == 'E'

# Process file into 100 x 100 array with numpy
with open('module12quizF23.txt', 'r') as file:
  numbers = []
  for line in file:
    numbers.append(int(line))
  numbers = np.array(numbers).reshape(100, 100)

# Turn plaintext and key into array of ints
letters = [alphabet.index(letter) for letter in plaintext]
key = [alphabet.index(letter) for letter in key]

# Loop through each letter and shift according to key
key_index = 0
encode = 1 if encode else -1
for i in range(len(letters)):
  letters[i] += encode * key[key_index]
  key_index = 0 if key_index == len(key) - 1 else key_index + 1

# Convert key and letter arrays to alphabet
letters = [alphabet[letter] for letter in letters]
key = [alphabet[letter] for letter in key]

# Print output
print(f'Message: {"".join(letters)}')
