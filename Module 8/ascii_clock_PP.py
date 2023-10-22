# Loop from row 1 - 5
for row in range(5):
  # Loop through each digit in provided string
  for digit in time:
    # Determine correct character based on user input
    # If no character is given, use the digit's character
    # Don't change character if :, A, P, M
    if character == " " or digit in ":APM":
      character_used = digit
    else:
      character_used = character