rows = int(input("Please Enter the total numbers Of Rows  : "))
number = 1
print(" Folyd's Triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end = '')
        number = number + 1
    print()