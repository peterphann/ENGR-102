import numpy as np

alphabet = 'abcdefghijklmnopqrstuvwxyz'
plaintext = 'lbclllsnllnwoisu'

# Process file into 100 x 100 array with numpy
with open('module12quizF23.txt', 'r') as file:
  numbers = []
  for line in file:
    numbers.append(int(line))
  numbers = np.array(numbers).reshape(100, 100)

# Find key using array
key1 = sum(numbers[:,85][:5])
key2 = int(sum(numbers[4]) / len(numbers[4]))
key3 = sum(numbers[62][-5:])
key4 = min(numbers[0])
key5 = max(numbers[29])

# Turn plaintext and key into array of ints
letters = [alphabet.index(letter) for letter in plaintext]
key = [key1, key2, key3, key4, key5]

# Loop through each letter and shift according to key
key_index = 0
for i in range(len(letters)):
  letters[i] -= key[key_index]
  key_index = 0 if key_index == len(key) - 1 else key_index + 1

# Convert key and letter arrays to alphabet
letters = [alphabet[letter] for letter in letters]
key = [alphabet[letter] for letter in key]

# Print output
print(f'Plaintext: {plaintext}')
print(f'Key: {"".join(key)}')
print(f'Message: {"".join(letters)}')
