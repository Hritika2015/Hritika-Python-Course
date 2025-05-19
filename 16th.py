for x in range(10):
    if x % 20 == 0:
     print("twist")
    #2     
    elif x % 15 == 0:
      pass
    #3
    elif x % 5 == 0:
      print("fizz")
    #4
    elif x % 3 == 0:
      print("buzz")
    else:
      print(x)