print("Select your PUR-FECT Ride: ")
print("1. Bike")
print("2. Car")
choice = int( input ("Enter you PUR-FECTO Choice: ")  )
if(  choice ==1):
    print("What type of bike ya want?!")
    print("1. scooty")
    print("2. scooter(cheaper)")
    choice2=int(input("Enter your choice 2:"))
    if choice2==1:
        print("You have selected Scooty(thanks for making me rich)")
    else:
        print("you have selected Scooter(good choice)")
elif(  choice == 2):
    print("What type of PUR-FECTO car type you want?")
    print("1.Sedan(Oh its nice)")
    print("2. XUV (idk what is this)")
    choice3=int(input("Enter your Choice 3:"))
    if choice3==1:
     print("You have selected sedan(yay!)")
    else:
     print("You Have Selected XUV(did you listen?)")
else:
 print("Wrong Choice!")