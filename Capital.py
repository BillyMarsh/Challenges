def capitalLetter(letter_string):
  for letter in letter_string:
      t = letter.isupper()
      print(letter, "=", t)

test = input("Enter Word To Find Capitals: ")
capitalLetter(test)
