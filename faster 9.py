ch = (input("Please Enter Your Own Magical Character! :"))
if ((ch >= 'a' and ch <= 'z') or (ch <= 'Z')):
    print(" The Given Character " , ch, "is an Alphabet")
elif(ch >= '0' and ch <= '9'):
    print(" The Given Character ", ch, "is a Digit")
else:
    print("The Given Character", ch, "is a Special Character")