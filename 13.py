print("Half Pyramid Pattern of  Star (*):")
n = int(input("Enter the amount of rows:  "))
for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()