def inputNumber(number1, number2):
  number1_2 = int(number1)
  number2_2 = int(number2)

  if number1_2 is not number1 or number2_2 is not number2:
    return(False)
  else:
    return(True)


print(inputNumber(10.0, 21))
