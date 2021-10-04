test = input("Enter your word: ")

length = len(test)

middle = test[len(test)//2]

if length % 2 > 0:
  print(middle)
else:
  print("")
