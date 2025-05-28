import random
number = str(random.randint(1,10))
print("I will generate a number from 1 to 10, and you have to guess the digit, for the first time i BEING nice, so dont disturb me >:(")
print("The game ends when you guess it, click play agian if you'd like.")
while True:
    guess = input("Give me a GUESS NOWWW\n" )
    if number == guess:
     print("YA WIN! Fun fact: This is the 19th class!")
     print("The number was", number)
     break
    else:
     print("TRY AGIAN! I KNOW YOU CANT READ MINDS BUT DO IT!!!")