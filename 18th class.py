try:
    number = int(input("Enter a GOOD,NICE HAPPY RARE SUPER NUMBER:"))
    print("The number entered was HORRIBLE!! WHY DID YOU ENTER", number)
except ValueError as ex:
      print("Exception:", ex)