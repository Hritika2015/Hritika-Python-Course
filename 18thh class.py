try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma that can didvide:"))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
  print("WRONG! TRY AGIAN CUZ YOU DIDN'T UNDERSTAND" )
#2
except SyntaxError:
  print("WRONG! TRY AGIAN CUZ YOU DIDN'T UNDERSTAND" )
  #3
except:
  print("WRONG! TRY AGIAN CUZ YOU DIDN'T UNDERSTAND" )
  #4
else:
  print("YAY! YOU FINALLY HAVE 1Q+!" )
finally:
  print("This WIll execute no matter WHAT!")